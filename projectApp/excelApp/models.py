from django.db import models

# Create your models here.
class CourseInfo(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    email = models.EmailField()
    course_name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=4, decimal_places=2)
    city = models.CharField(max_length=50)
    enrolled_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20)

