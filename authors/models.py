from django.db import models

# Create your models here.
class Authors(models.Model):
    first_name = models.CharField(max_length=120)
    last_name = models.CharField(max_length=120)
    imageURL = models.CharField(max_length=400)

    def __str__(self):
        return self.first_name + " " + self.last_name

class Books(models.Model):
    RED= 'RED'
    BLUE = 'BLUE'
    GREEN = 'GREEN'
    colors = [
        (RED, ('RED')),
        (BLUE, ('BLUE')),
        (GREEN, ('GREEN')),
    ]
    title = models.CharField(max_length=120)
    available = models.BooleanField(default=True)
    color=  models.CharField(max_length=120, choices=colors, default=RED)
    author= models.ForeignKey(Authors, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
