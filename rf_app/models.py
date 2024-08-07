from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
User = get_user_model()

class Post(models.Model):
    title=models.CharField(max_length=250)
    description=models.TextField()
    time=models.DateTimeField(auto_now_add=True)
    verified =models.BooleanField()
    owner=models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title