from django.db import models

class StudentCourse(models.Model):
    id = models.AutoField(primary_key=True)
    StudentName = models.CharField(max_length=100)
    CourseName = models.CharField(max_length=100)
    Email = models.EmailField()
    Price = models.DecimalField(max_digits=10, decimal_places=2)


