from django.db import models
from django.urls import reverse



class Restaurant(models.Model):

    name = models.CharField(max_length=255)
    rank = models.DecimalField(decimal_places=1, max_digits=10)
    average_bill = models.IntegerField()
    menu = models.ManyToManyField('Products', related_name='menu')

    def __str__(self):
        return "%s" % self.name

    class Meta:
        verbose_name = 'Ресторан'
        verbose_name_plural = 'Ресторани'

class Products(models.Model):

    title = models.CharField(max_length=255)

    def __str__(self):
        return "{}".format(self.title)

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукти'
