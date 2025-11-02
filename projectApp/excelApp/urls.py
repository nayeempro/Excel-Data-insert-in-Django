from django.urls import include, path
from . import views
urlpatterns = [
   path('', views.home, name='home'),
   path('published', views.published, name='published_data'),
   path('viewInfo/<int:id>/', views.viewInfo, name='stu_info'),
   path('editInfo/<int:id>/', views.edit_stu_info, name='edit_stu_info'),
   path('deleteInfo/<int:id>/', views.delete_stu, name='delete_stu_info'),
   path('confirmInfo/<int:id>/', views.confirm_student, name='confirm_stu_info'),
   path('statistics/', views.courseStatistics, name='course_statistics'),
]
