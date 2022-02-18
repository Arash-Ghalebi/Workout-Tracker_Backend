from django.urls import path
from exerciseactivities import views



app_name = "exerciseactivities"
urlpatterns = [
    path('lifting-records/add/', views.add_weight, name='add_weight_record'),
    path('lifting-records/all-squat/<int:fk>/', views.get_all_squat, name='get_squat_records'),
    path('lifting-records/all-bench/<int:fk>/', views.get_all_bench, name='get_bench_records'),
    path('lifting-records/all-bent/<int:fk>/', views.get_all_bent, name='get_bent_records'),
    path('lifting-records/all-overhead/<int:fk>/', views.get_all_overhead, name='get_overhead_records'),
    path('lifting-records/delete/<int:pk>/', views.delete_weight, name='delete_weight_record'),
    path('lifting-records/get_squat_record/<int:pk>/', views.get_squat_max, name='get_squat'),
    path('lifting-records/get_bench_record/<int:pk>/', views.get_bench_max, name='get_bench'),
    path('lifting-records/get_bent_record/<int:pk>/', views.get_bent_max, name='get_bent'),
    path('lifting-records/get_overhead_record/<int:pk>/', views.get_overhead_max, name='get_overhead'),
    path('lifting-records/update/<int:pk>/', views.update_weight, name='update_weight_record'),
]