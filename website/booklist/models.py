from django.db import models

# Create your models here.

class Book(models.Model):
    # This is the model of the books on the bookshelf.
    
    # Basic information of a book
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    isbn = models.CharField(max_length=20, primary_key=True)
    price = models.DecimalField()

    # Additional information of a book
    introduction = models.CharField(max_length=2000, null=True, blank=True)
    url = models.CharField(maxn_length=200, null=True, blank=True)
    image = models.CharField(maxn_length=50, null=True, blank=True)

    # Current status of the book
    
