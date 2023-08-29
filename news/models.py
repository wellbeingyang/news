from django.db import models

# Create your models here.


class Text(models.Model):
    text = models.TextField()


class news(models.Model):
    id = models.IntegerField(primary_key=True)
    url = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    date = models.CharField(max_length=20)
    category = models.IntegerField()
    image_url = models.CharField(max_length=50)
    editor = models.CharField(max_length=50)
    content = models.ForeignKey(Text, on_delete=models.CASCADE)
