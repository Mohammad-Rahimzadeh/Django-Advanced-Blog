from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.

User = get_user_model()

class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=250)
    category = models.ForeignKey('Category', null=True, on_delete=models.SET_NULL)
    content = models.TextField()
    image = models.ImageField(upload_to='post-image', blank=True, null=True)
    status = models.BooleanField()
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    published_date = models.DateTimeField()

    def __str__(self):
        return '{}'.format(self.title)
    

class Category(models.Model):
    title = models.CharField(max_length=250)

    def __str__(self):
        return '{}'.format(self.title)