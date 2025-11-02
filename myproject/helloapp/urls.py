from django.urls import  path
from . import views

urlpatterns = [
    path('', views.hello_world, name='hello_world'),
    path('home/', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('test/', views.test, name='test'),
    path('loadingAll/', views.loading, name='loading'),
    path('insert1/', views.insert_customer_Data_1, name='insert1'),
    path('insert2/', views.insert_customer_Data_2, name='insert2'),
    path('bulk/', views.bulk_insert, name='bulk_insert'),
    path('show/', views.show_data, name='show'),
    path('bookList/', views.bookList, name='book_list'),
    path('createBook/', views.create_book, name='create_book'),
    path('book_details/<int:id>/', views.book_details, name='book_details'),
    path('book_details/<int:id>/delete/', views.book_delete, name='book_delete'),
    path('book_details/<int:id>/edit/', views.book_edit, name='book_edit'),
]
