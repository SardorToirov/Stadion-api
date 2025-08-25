from django.db import models
from stadiums.models import Stadium
from users.models import User

# Create your models here.
class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    stadium = models.ForeignKey(Stadium, on_delete=models.CASCADE)
    start_time = models.TimeField()
    end_time = models.TimeField()
    status = models.CharField(max_length=20, default='pending')

    def __str__(self):
        return f"{self.user.username} - {self.stadium.name} ({self.start_time} to {self.end_time})"


