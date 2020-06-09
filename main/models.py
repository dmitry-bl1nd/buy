from django.db import models

class Building(models.Model):
    type = models.CharField("Категория", max_length=100)
    price = models.PositiveIntegerField("Цена")

    class Meta:
        verbose_name = 'Объявление'
        verbose_name_plural = 'Объявления'