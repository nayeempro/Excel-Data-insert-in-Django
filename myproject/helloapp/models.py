from django.db import models

class Customer1(models.Model):
    name = models.CharField(max_length=100) 
    email = models.EmailField(unique=True)  
    phone = models.CharField(max_length=15, null=True, blank=True)  
    created_at = models.DateTimeField(auto_now_add=True)  
 

class Customers1(models.Model):
    customer_id = models.CharField(max_length=50)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    age = models.IntegerField()
    city = models.CharField(max_length=100)


class Customers2(models.Model):
    customer_id = models.CharField(max_length=50)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    age = models.IntegerField()
    city = models.CharField(max_length=100)


class Customers3(models.Model):
    customer_id = models.CharField(max_length=50)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    age = models.IntegerField()
    city = models.CharField(max_length=100)

class Customers_all(models.Model):
    customer_id = models.CharField(max_length=50)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    age = models.IntegerField()
    city = models.CharField(max_length=100)


class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    description = models.TextField()
    pic = models.ImageField(upload_to='book_pics/', blank=True, null=True)  # New pic field
    

