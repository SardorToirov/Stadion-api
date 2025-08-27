from django.db import models
from users.models import User
# Create your models here.
class Stadium(models.Model):
    CHOICES = (
        ('yangi', 'New'),
        ('o\'rta', 'Middle'),
        ('eski', 'old'),
    )


    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    price = models.IntegerField()
    weight = models.IntegerField()
    height = models.IntegerField()
    stadions_status = models.CharField(max_length=10, choices=CHOICES, default='o\'rta')
    


    def __str__(self):
        return self.name
    

class StadionsImage(models.Model):
    stadium = models.ForeignKey(Stadium, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='stadiums/')

    def __str__(self):
        return f"Image for {self.stadium.name}"


