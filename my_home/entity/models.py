from django.contrib.auth.models import User
from django.db import models


class Entity(models.Model):
    modified_by = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name='Изменил')
    value = models.IntegerField('Значение')
    properties = models.ManyToManyField('Property')

    class Meta:
        verbose_name = 'Элемент'
        verbose_name_plural = 'Элементы'

    def __str__(self):
        return f'{self.value}'


class Property(models.Model):
    key = models.CharField('Ключ', max_length=150)
    value = models.CharField('Значение', max_length=150)

    class Meta:
        verbose_name = 'Свойство'
        verbose_name_plural = 'Свойства'

    def __str__(self):
        return f'{self.key} : {self.value}'
