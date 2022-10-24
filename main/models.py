from django.db import models
from django.contrib.auth.models import User


class Biletlar(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    
class Questions(models.Model):
    bilet = models.ForeignKey(Biletlar, on_delete=models.CASCADE, related_name='quest_bilet')
    number = models.PositiveIntegerField()
    question = models.CharField(max_length=255)
    image = models.ImageField(upload_to='image', null=True, blank=True)
    optionA = models.CharField(max_length=255)
    optionB = models.CharField(max_length=255)
    optionC = models.CharField(max_length=255, null=True, blank=True)
    optionD = models.CharField(max_length=255, null=True, blank=True)
    optionE = models.CharField(max_length=255, null=True, blank=True)
    correct = models.CharField(max_length=255)

    def __str__(self):
        return str(self.bilet.name) + "." + str(self.number) + "." + self.question


