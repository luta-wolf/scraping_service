from django.db import models

# Create your models here.

# Создаем таблицы БД
'''
в файле models.py создаются классы, которые являются полным отражением
тех таблиц, которые в дальнейшем будут находится в БД


Таблицы сбор вакансий c определенных сайтов, где они размещаются
Вакансии разделяем специальностям и городам
Отдельно табличка по
- вакансиям
- специальностям
- городам
'''

class City(models.Model): # переводит питоновскмй класс в таблицу
	name = models.CharField(max_length=50, verbose_name='Название населенного пункта')
	slug = models.CharField(max_length=50, blank=True)

	class Meta:
		verbose_name = 'Название населенного пункта'
		verbose_name_plural = 'Название населенных пунктов'

	def __str__(self) -> str:
		return self.name