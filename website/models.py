from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class blog(models.Model):
    choice =(
    ("1", "Draft"), 
    ("2", "Published"),
    )
    
    title = models.CharField(max_length=300)
    content = models.TextField()
    meta = models.CharField(max_length=100)
    MetaTitle = models.CharField(max_length=200)
    date = models.DateField(auto_now=False, auto_now_add=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(choices=choice,default=1,max_length=1)
    slug = models.CharField(max_length=50)
    

    
