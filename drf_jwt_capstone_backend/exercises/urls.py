from django.urls import path
from exercises import views



app_name = "exercises"
urlpatterns = [
    path('', views.add_exercises, name='exercises_list'),
    path('delete/<int:pk>/', views.delete_exercises, name='exercises_delete'),
    path('get/<int:pk>/', views.get_exercise, name='exercises_get_one'),
    path('get/all/', views.get_all_exercises, name='exercises_get_all'),
    path('update/<int:pk>/', views.update_exercise, name='update_exercises'),
]