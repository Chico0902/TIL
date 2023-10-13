from django.db import models


# Create your models here.
class Keyword(models.Model):
    name = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add= True)

class Trend(models.Model):
    Name = models.TextField()
    result = models.IntegerField()
    search_period = models.TextField()
    created_at = models.DateTimeField(auto_now_add= True)