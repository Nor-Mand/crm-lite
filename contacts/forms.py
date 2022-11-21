from django.forms import ModelForm, TextInput, Select
from .models import Partner, Companies

custom_field = "appearance-none block w-full bg-gray-200 text-gray-700 border border-gray-200 rounded py-3 px-4 mt-10 lg:mt-0 leading-tight focus:outline-none focus:bg-white focus:border-gray-500"

class ContactModelForm(ModelForm):
    class Meta:
        model = Partner
        fields = ['full_name', 'street', 'phone', 'email', 'company_id', 'country', 'image_person']
        widgets = {
            'full_name': TextInput(attrs={"class": f"{custom_field}"}),
            'street': TextInput(attrs={"class": f"{custom_field}"}),
            'phone': TextInput(attrs={"class": f"{custom_field}"}),
            'email': TextInput(attrs={"class": f"{custom_field}"}),
            'company_id': Select(attrs={"class": f"{custom_field}"}),
            'country': Select(attrs={"class": f"{custom_field}"}),

        }


class CompanyModelForm(ModelForm):
    class Meta:
        model = Companies
        fields = ['name', 'website', 'tax_id', 'industry_id', 'logo_company']
        widgets ={
            'name': TextInput(attrs={"class": f"{custom_field}"}),
            'website': TextInput(attrs={"class": f"{custom_field}"}),
            'tax_id': TextInput(attrs={"class": f"{custom_field}"}),
            'industry_id': Select(attrs={"class": f"{custom_field}"}),
        }