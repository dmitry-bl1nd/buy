from django.db import models

class Building(models.Model):
    type = models.CharField("Категория", max_length=100)
    price = models.PositiveIntegerField("Цена")
    img = models.CharField("Картинка", max_length=250, default="1.jpeg")
    class Meta:
        verbose_name = 'Объявление'
        verbose_name_plural = 'Объявления'