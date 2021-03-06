from django.db import models
from django.utils import timezone
class Building(models.Model):
    type = models.CharField('Категория', max_length=100)
    price = models.PositiveIntegerField('Цена', default='10')
    img = models.ImageField('Картинка', upload_to='img', default='img/noimg.jpg')
    area = models.PositiveIntegerField('Площадь', default='10')
    location = models.CharField('Место', max_length=25)
    date = models.DateTimeField('Дата публикации', default=timezone.now())
    class Meta:
        verbose_name = 'Объявление'
        verbose_name_plural = 'Объявления'

