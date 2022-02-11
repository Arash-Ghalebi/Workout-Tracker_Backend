from django.urls import path
from bodyweights import views



app_name = "bodyweights"
urlpatterns = [
    path('add/', views.add_bodyweight, name='add_bodyweight'),
    path('<int:fk>/', views.get_bodyweight, name='get_bodyweight'),
    path('delete/<int:pk>/', views.delete_bodyweight, name='delete_bodyweight'),
    path('get/<int:pk>/', views.get_one_bodyweight, name='get_one_bodyweight'),
    path('update/<int:pk>/', views.update_bodyweight, name='update_bodyweight'),
]