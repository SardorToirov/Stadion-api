from django.db import models
from users.models import User
# Create your models here.
class Stadium(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    price = models.IntegerField()

    def __str__(self):
        return self.name
    
   


