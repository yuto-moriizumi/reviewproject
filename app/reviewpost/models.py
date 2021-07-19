from django.db import models

# Create your models here.
from django.contrib.auth.models import User

EVALUATION_CHOICES = [("良い", "良い"), ("悪い", "悪い")]


class ReviewModel(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    images = models.ImageField(upload_to="")
    useful_review = models.IntegerField(default=0, null=True, blank=True)
    useful_review_record = models.TextField()
    evaluation = models.CharField(max_length=10, choices=EVALUATION_CHOICES)
