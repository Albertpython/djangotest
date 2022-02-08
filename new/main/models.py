from django.db import models

class Type(models.Model):
    name = models.CharField('Type name', max_length=30)


class Car(models.Model):
    type_car = models.ForeignKey('Type', on_delete=models.CASCADE)
    name = models.CharField('Car name', max_length=30)
    
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Car'
        verbose_name_plural = 'Cars'
