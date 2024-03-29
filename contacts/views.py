from django.shortcuts import redirect, render
from django.views.generic import DetailView
from .models import Partner, Companies
from crm.models import Menus
from .forms import ContactModelForm, CompanyModelForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required


@login_required
def contact_list_view(request):
    contacts = Partner.objects.all()
    if request.method == 'POST':
        formContacts = ContactModelForm(request.POST)
        if formContacts.is_valid():
            formContacts.save()
            return redirect('contacts:contact-list')
    else:
        formContacts = ContactModelForm()
    menus = Menus.objects.all().order_by('position')
    context = {
        'contacts': contacts,
        'formContacts': formContacts,
        'menus': menus
    }
    return render(request, 'contact-list.html', context=context)


# class ContactDetailView(LoginRequiredMixin, DetailView):
#     template_name = 'contact-detail.html'
#     queryset = Partner.objects.all()
#     context_object_name = 'partners'

@login_required
def contact_detail_view(request, pk):
    partners = Partner.objects.get(id=pk)
    menus = Menus.objects.all().order_by('position')
    context = {
        'partners': partners,
        'menus': menus
    }
    return render(request,'contact-detail.html',context)


@login_required
def contact_updated_view(request, pk):
    contacts = Partner.objects.get(id=pk)
    if request.method == 'POST':
        formContacts = ContactModelForm(request.POST, request.FILES, instance=contacts)
        if formContacts.is_valid():
            formContacts.save()
        return redirect('contacts:contact-list')
    else:
        formContacts = ContactModelForm(instance=contacts)
    context = {
        'contacts': contacts,
        'formContacts': formContacts

    }
    return render(request, 'contact-update.html', context)


@login_required
def contact_delete(request, pk):
    contact = Partner.objects.get(id=pk)
    contact.delete()
    return redirect('/contacts')


@login_required
def company_list_view(request):
    company = Companies.objects.all()
    if request.method == 'POST':
        formCompany = CompanyModelForm(request.POST, request.FILES)
        if formCompany.is_valid():
            formCompany.save()
            return redirect('company:company-list')
    else:
        formCompany = CompanyModelForm()
    menus = Menus.objects.all().order_by('position')
    context = {
        'company': company,
        'formCompany': formCompany,
        'menus': menus
    }
    return render(request, 'company-list.html', context=context)


# class CompanyDetailView(LoginRequiredMixin, DetailView):
#     template_name = 'company_detail.html'
#     queryset = Companies.objects.all()
#     context_object_name = 'companies'
#     print("################")

@login_required
def company_detail_view(request, pk):
    companies = Companies.objects.get(id=pk)
    menus = Menus.objects.all().order_by('position')
    context={
        'companies': companies,
        'menus':menus
    }
    return render(request, 'company_detail.html', context)

@login_required
def company_updated_view(request, pk):
    company = Companies.objects.get(id=pk)
    if request.method == 'POST':
        formCompany = CompanyModelForm(request.POST, request.FILES, instance=company)
        if formCompany.is_valid():
            formCompany.save()
        return redirect('contacts:company-list')
    else:
        formCompany = CompanyModelForm(instance=company)
    context = {
        'company': company,
        'formCompany': formCompany

    }
    return render(request, 'company_update.html', context)


@login_required
def company_delete_view(request,pk):
    company = Companies.objects.get(id=pk)
    company.delete()
    return redirect('contacts:company-list')