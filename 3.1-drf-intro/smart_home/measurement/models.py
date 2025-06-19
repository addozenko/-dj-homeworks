from django.db import models

# TODO: опишите модели датчика (Sensor) и измерения (Measurement)


class Measurement(models.Model):
    temperature = models.CharField(max_length=10)  
    created_at = models.DateTimeField(auto_now_add=True) 

class Sensor(models.Model):
    name = models.CharField('Название', max_length=64)
    description = models.CharField('Описание', max_length=64)
    measurements = models.ManyToManyField(Measurement, related_name='sensors')
