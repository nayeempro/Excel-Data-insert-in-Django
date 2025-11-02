from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('upload/', views.upload, name='upload_files'),
    path('showTable/', views.showTable, name='show_table'),
    path('analytics/', views.analytics, name='analytics'),
]