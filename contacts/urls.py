from django.urls import path
from .views import contact_delete, \
            contact_list_view, \
            ContactDetailView, \
            contact_updated_view,\
            company_list_view,\
            company_delete_view,\
            company_updated_view,\
            CompanyDetailView

app_name = 'contacts'

urlpatterns = [
    path('', contact_list_view, name='contact-list'),
    path('<int:pk>/', ContactDetailView.as_view(), name='contact-detail'),
    path('update/<int:pk>/', contact_updated_view, name='contact-update'),
    path('delete/<int:pk>/', contact_delete, name='contact-delete'),
    path('companies/', company_list_view, name='company-list'),
    path('companies/detail/<int:pk>/', CompanyDetailView.as_view(), name='company-detail'),
    path('companies/update/<int:pk>/', company_updated_view, name='company-update'),
    path('companies/delete/<int:pk>/', company_delete_view, name='company-delete'),
]