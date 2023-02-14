from django.urls import path
from .views import kanban, list_view, reports, update_view, delete_view, LeadDetailView

app_name = 'crm'

urlpatterns = [
    path('kanban/', kanban, name='kanban-view'),
    path('list/', list_view, name='list-view'),
    path('reports/', reports, name='reports-view'),
    path('detail/<int:pk>/', LeadDetailView.as_view(), name='lead-detail'),
    path('update/<int:pk>/', update_view, name='lead-update'),
    path('delete/<int:pk>/', delete_view, name='lead-delete'),
]