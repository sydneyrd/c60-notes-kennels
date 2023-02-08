from django.db import models


class Walker(models.Model):
    name = models.CharField(max_length=155)
    email = models.CharField(max_length=155)
    city = models.ForeignKey('City', on_delete=models.CASCADE, related_name='walkers')

