from django.urls import path
from .views import opportunities_kanban_list_view, opportunity_list_view, crm_reports, LeadDetailView, opportunity_edit_view, opportunity_delete_view

app_name = 'leads'

urlpatterns = [
    path('opportunities/kanban/', opportunities_kanban_list_view, name='kanban-opportunity'),
    path('opportunities/list/', opportunity_list_view, name='list-opportunity'),
    path('reports/', crm_reports, name='crm-reports'),
    path('detail/<int:pk>/', LeadDetailView.as_view(), name='lead-detail'),
    path('update/<int:pk>/', opportunity_edit_view, name='lead-update'),
    path('delete/<int:pk>/', opportunity_delete_view, name='lead-delete'),
]