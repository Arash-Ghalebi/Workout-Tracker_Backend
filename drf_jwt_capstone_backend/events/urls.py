from django.urls import path
from events import views



app_name = "events"
urlpatterns = [
    path('add/', views.add_entry, name='add_entry'),
    path('all/<int:fk>/', views.get_all_entries, name='get_all_entries'),
    path('delete/<int:pk>/', views.delete_entry, name='delete_entry'),
    
]