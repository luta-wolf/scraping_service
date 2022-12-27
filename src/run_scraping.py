import codecs
import os, sys
from django.db import DatabaseError

proj = os.path.dirname(os.path.abspath('manage.py'))
sys.path.append(proj)
os.environ["DJANGO_SETTINGS_MODULE"] = "scraping_service.settings"

import django
django.setup()

from scraping.parsers import *
from scraping.models import Vacancy, City, Language

parsers = ((pars_hh, 'https://kazan.hh.ru/search/vacancy?area=113&search_field=name&salary=455000&text=Python+developer&ored_clusters=true&enable_snippets=true'),
			(pars_habr, 'https://career.habr.com/vacancies?q=python%20developer&s[]=2&s[]=82&s[]=4&type=all'),
			(pars_job, 'https://russia.superjob.ru/vacancy/search/?keywords=Python%20developer')
		)

city = City.objects.filter(slug='moskva').first()
language = Language.objects.filter(slug = 'python').first()

jobs, errors = [], []
for func, url in parsers:
	j, e = func(url)
	jobs += j
	errors += e

for job in jobs:
	v = Vacancy(**job, city=city, language=language)
	try:
		v.save()
	except DatabaseError:
		pass

# file = codecs.open('hh.txt', 'w', 'utf-8')
# for job in jobs:
# 	file.write(str(job) + '\n')
# file.close()
