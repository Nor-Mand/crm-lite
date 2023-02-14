from django.forms import ModelForm, TextInput, NumberInput, Select, Textarea
from .models import Lead

custom_field = "appearance-none block w-full bg-gray-200 text-gray-700 border border-gray-200 rounded py-3 px-4 mt-2 lg:mt-0 leading-tight focus:outline-none focus:bg-white focus:border-gray-500"


class OpportunityModelForm(ModelForm):
    class Meta:
        model = Lead
        fields = ['name', 'expect_revenue', 'date_deadline', 'partner_id', 'stage_id', 'company_id', 'description']
        widgets = {
            'name': TextInput(attrs={"class": f"{custom_field}"}),
            'expect_revenue': NumberInput(attrs={"class": f"{custom_field}", "min": 0}),
            'date_deadline': NumberInput(attrs={'type': 'date',
                                                "class": f"{custom_field}"}),
            'partner_id': Select(attrs={"class": f"{custom_field}"}),
            'stage_id': Select(attrs={"class": f"{custom_field}"}),
            'company_id': Select(attrs={"class": f"{custom_field}"}),
            'description': Textarea(attrs={"class": f"{custom_field}", "rows": 9}),
        }
