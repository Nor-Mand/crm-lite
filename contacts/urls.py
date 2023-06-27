from django.urls import path
from .views import contact_delete, \
            contact_list_view, \
            contact_detail_view, \
            contact_updated_view,\
            company_list_view,\
            company_delete_view,\
            company_updated_view,\
            company_list_view,\
            company_detail_view

app_name = 'contacts'

urlpatterns = [
    path('', contact_list_view, name='contact-list'),
    path('<int:pk>/', contact_detail_view, name='contact-detail'),
    path('update/<int:pk>/', contact_updated_view, name='contact-update'),
    path('delete/<int:pk>/', contact_delete, name='contact-delete'),
    path('list', company_list_view, name='company-list'),
    path('detail/<int:pk>/', company_detail_view, name='company-detail'),
    path('companies/update/<int:pk>/', company_updated_view, name='company-update'),
    path('companies/delete/<int:pk>/', company_delete_view, name='company-delete'),
]