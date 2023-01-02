import codecs
import os, sys
from django.contrib.auth import get_user_model
from django.db import DatabaseError
import asyncio

proj = os.path.dirname(os.path.abspath('manage.py'))
sys.path.append(proj)
os.environ["DJANGO_SETTINGS_MODULE"] = "scraping_service.settings"

import django
django.setup()

from scraping.parsers import *
from scraping.models import Vacancy, City, Language, Error, Url

User = get_user_model()

parsers = ((pars_hh, 'hh'),
			(pars_habr, 'habr'),
			(pars_job, 'job')
		)


# parsers = ((pars_hh, 'https://kazan.hh.ru/search/vacancy?area=113&search_field=name&text=Python+developer&ored_clusters=true&enable_snippets=true'),
# 			(pars_habr, 'https://career.habr.com/vacancies?q=python%20developer&s[]=2&s[]=82&s[]=4&type=all'),
# 			(pars_job, 'https://russia.superjob.ru/vacancy/search/?keywords=Python%20developer')
# 		)
jobs, errors = [], []


def get_settings():
	qs = User.objects.filter(send_email=True).values()
	settings_lst = set((q['city_id'], q['language_id']) for q in qs)
	return settings_lst

def get_urls(_settings):
	qs = Url.objects.all().values()
	url_dct = {(q['city_id'], q['language_id']): q['url_data'] for q in qs}
	urls = []
	for pair in _settings:
		tmp = {}
		tmp['city'] = pair[0]
		tmp['language'] = pair[1]
		tmp['url_data'] = url_dct[pair]
		urls.append(tmp)
	return urls

# async def main(value):
# 	func, url, city, language = value
# 	job, err = await loop.run_in_executor(None, func, url, city, language)
# 	errors.append(err)
# 	jobs.append(job)

settings = get_settings()
url_list = get_urls(settings)

# city = City.objects.filter(slug='moskva').first()
# language = Language.objects.filter(slug = 'python').first()
import time
start = time.time()


# loop = asyncio.get_event_loop()
# tmp_tasks = [(func, data.get(key), data['city'], data['language'])
# 			for data in url_list
# 			for func, key in parsers]

# tasks = asyncio.wait([loop.create_task(main(f)) for f in tmp_tasks])


for data in url_list:

	for func, key in parsers:
		url = data['url_data'][key]
		j, e = func(url, city=data['city'], language=data['language'])
		jobs += j
		errors += e
print(time.time() - start)

for job in jobs:
	v = Vacancy(**job)
	try:
		v.save()
	except DatabaseError:
		pass

if errors:
	er = Error(data=errors).save()

# file = codecs.open('hh.txt', 'w', 'utf-8')
# for job in jobs:
# 	file.write(str(job) + '\n')
# file.close()
