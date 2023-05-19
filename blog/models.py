from django.db import models

# Create your models here.


class Post(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    body = models.TextField()
    signature = models.CharField(max_length=100, default='Sydney White')
    date = models.DateField()

    def __str__(self):
        return self.title
