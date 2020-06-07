from django.db import models


# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    date = models.DateTimeField(verbose_name='Published Date')

    def __str__(self):
        return self.title
