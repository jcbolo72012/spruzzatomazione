from django.urls import path
from . import views

app_name='watering'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:watering_id>/delete', views.delete, name='delete'),
    path('<int:watering_id>/update', views.update, name='update'),
    path('add/', views.add, name='add')
]