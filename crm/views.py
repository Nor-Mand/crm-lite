from django.db.models import Sum
from django.db.models.functions import ExtractMonth
from django.db.models import Q
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from .models import Lead, Stage, Months
from .forms import OpportunityModelForm
from django.core.mail import send_mail
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin


@login_required
def opportunities_kanban_list_view( request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    stage_filter = Lead.objects.filter(
        Q(stage_id__name__icontains=q)
    )
    total_opportunities = Lead.objects.all().aggregate(total_opportunities=Sum('expect_revenue'))['total_opportunities'] or 0
    opportunities = Lead.objects.all()
    stages = Stage.objects.all()
    if request.method == 'POST':
        formLead = OpportunityModelForm(request.POST)
        if formLead.is_valid():
            formLead.save()
            return redirect('leads:kanban-opportunity')
    else:
        formOpportunity = OpportunityModelForm()
    context = {
        'opportunities': opportunities,
        'stages': stages,
        'stage_filter': stage_filter,
        'formOpportunity': formOpportunity,
        'total_opportunities': total_opportunities
    }
    return render(request, 'kanban_opportunity.html', context=context)


@receiver(pre_save, sender=Lead)
def form_valid(sender, instance, **kwargs):
    send_mail(
        subject=f'the lead {instance.name} has been created',
        message="Go to the site see the new lead"
                f"Name: {instance.name}"
                f"Expect Value: {instance.expect_revenue}"
        f"Date Deadline: {instance.date_deadline}",
        from_email="test@test.com",
        recipient_list=["test2@test.com"]
    )
    return form_valid


class OpportunitiesListView(LoginRequiredMixin, ListView):
    template_name = 'list_opportunity.html'
    queryset = Lead.objects.all()
    context_object_name = 'opportunities'


@login_required
def crm_reports(request):
    new = Lead.objects.filter(stage_id=1).count()
    total_stage_new = Lead.objects.filter(stage_id=1).aggregate(total_credit=Sum('expect_revenue'))['total_credit'] or 0
    total_stage_qualified = Lead.objects.filter(stage_id=2).aggregate(total_credit=Sum('expect_revenue'))['total_credit'] or 0
    total_stage_preposition = Lead.objects.filter(stage_id=3).aggregate(total_credit=Sum('expect_revenue'))['total_credit'] or 0
    total_stage_won = Lead.objects.filter(stage_id=4).aggregate(total_credit=Sum('expect_revenue'))['total_credit'] or 0
    total_stage_lost = Lead.objects.filter(stage_id=5).aggregate(total_credit=Sum('expect_revenue'))['total_credit'] or 0
    leads = Lead.objects.all()
    stages = Lead.objects.raw('SELECT * FROM crm_lead group by stage_id_id, id ORDER BY stage_id_id ASC')
    months = Months.objects.all()
    total_months = Lead.objects.annotate(month=ExtractMonth('date_deadline')).values('month').annotate(total=Sum('expect_revenue')).values('month', 'total','stage_id')
    context = {
        'months': months,
        'stages': stages,
        'leads': leads,
        'new': new,
        'total_stage_new': total_stage_new,
        'total_stage_qualified': total_stage_qualified,
        'total_stage_preposition': total_stage_preposition,
        'total_stage_won': total_stage_won,
        'total_stage_lost': total_stage_lost,
        'total_months': total_months,
    }
    return render(request, 'reports.html', context)


@login_required
def opportunity_list_view(request):
    total_leads = Lead.objects.all().aggregate(total_leads=Sum('expect_revenue'))['total_leads'] or 0
    leads = Lead.objects.all()
    stages = Stage.objects.all()
    if request.method == 'POST':
        formOpportunity = OpportunityModelForm(request.POST)
        if formOpportunity.is_valid():
            formOpportunity.save()
            return redirect('crm:list-opportunity')
    else:
        formOpportunity = OpportunityModelForm()
    context = {
        'leads': leads,
        'stages': stages,
        'formOpportunity': formOpportunity,
        'total_leads': total_leads
    }
    return render(request, 'list_opportunity.html', context=context)

class LeadDetailView(LoginRequiredMixin, DetailView):
    template_name = 'detail_opportunity.html'
    queryset = Lead.objects.all()
    context_object_name = 'leads'


@login_required
def  opportunity_edit_view(request,pk):
    # return HttpResponse('ok')
    leads = Lead.objects.get(id=pk)
    if request.method == 'POST':
        formOpportunity = OpportunityModelForm(request.POST, instance=leads)
        if formOpportunity.is_valid():
            formOpportunity.save()
            return redirect('leads:kanban-opportunity')
    else:
        formOpportunity = OpportunityModelForm(instance=leads)
    context = {
        'formOpportunity': formOpportunity,
        'leads': leads
    }
    return render(request,'update_opportunity.html', context)


@login_required
def opportunity_delete_view(request, pk):
    lead = Lead.objects.get(id=pk)
    lead.delete()
    return redirect("leads:kanban-opportunity")