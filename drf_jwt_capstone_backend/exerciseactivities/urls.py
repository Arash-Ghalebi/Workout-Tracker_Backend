from django.urls import path
from exerciseactivities import views



app_name = "exerciseactivities"
urlpatterns = [
    path('lifting-records/add/', views.add_weight, name='add_weight_record'),
    path('lifting-records/all/<int:fk>/', views.get_weight, name='get_weight_records'),
    path('lifting-records/delete/<int:pk>/', views.delete_weight, name='delete_weight_record'),
    path('lifting-records/get_one_record/<int:pk>/', views.get_one_weight, name='get_all_weight_records'),
    path('lifting-records/update/<int:pk>/', views.update_weight, name='update_weight_record'),
]