from django.db import models
from scraping.utils import from_cyrillic_to_eng

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
	name = models.CharField(max_length=50,
							verbose_name='Название населенного пункта',
							unique=True) # повторов городов не будет
	slug = models.CharField(max_length=50, blank=True, unique=True)

	class Meta:
		verbose_name = 'Название населенного пункта'
		verbose_name_plural = 'Название населенных пунктов'

	def __str__(self) -> str:
		return self.name

	def save(self, *args, **kwargs):
		if not self.slug:
			self.slug = from_cyrillic_to_eng(str(self.name))
		super().save(*args, **kwargs)

class Language(models.Model):
	name = models.CharField(max_length=50,
							verbose_name='Язык программирования',
							unique=True) # повторов языков не будет
	slug = models.CharField(max_length=50, blank=True, unique=True)

	class Meta:
		verbose_name = 'Язык программирования'
		verbose_name_plural = 'Языки программирования'

	def __str__(self) -> str:
		return self.name

	def save(self, *args, **kwargs):
		if not self.slug:
			self.slug = from_cyrillic_to_eng(str(self.name))
		super().save(*args, **kwargs)


class Vacancy(models.Model):
	url = models.URLField(unique=True)
	title = models.CharField(max_length=250, verbose_name='Заголовок вакансии')
	company = models.CharField(max_length=250, verbose_name='Компания')
	description = models.TextField(verbose_name='Описание вакансии')
	city = models.ForeignKey('City', on_delete=models.CASCADE, verbose_name='Город')
	language = models.ForeignKey('Language', on_delete=models.CASCADE, verbose_name='Язык программирования')
	timestamp = models.DateField(auto_now_add=True)

	class Meta:
		verbose_name = 'Вакансия'
		verbose_name_plural = 'Вакансии'

	def __str__(self) -> str:
		return self.title
