from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
# Create your models here.


class Puzzle(models.Model):
    title = models.CharField(max_length=200, null=False, blank=False)
    size = models.IntegerField(
        validators=[MinValueValidator(2), MaxValueValidator(10)])
    created_at = models.DateTimeField()
    update_at = models.DateTimeField()
    picture_url = models.TextField(max_length=2000)
    user_id = models.CharField(max_length=200)
