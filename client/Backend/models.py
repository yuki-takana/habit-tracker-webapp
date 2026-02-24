from django.db import models
from django.contrib.auth.models import User

class Habit(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    frequency = models.IntegerField(default=1)  # times per week/day

    def __str__(self):
        return f"{self.user.username} - {self.name}"

class Completion(models.Model):
    habit = models.ForeignKey(Habit, on_delete=models.CASCADE)
    date = models.DateField()

    class Meta:
        unique_together = ('habit', 'date')  # prevent duplicate completions

    def __str__(self):
        return f"{self.habit.name} - {self.date}"