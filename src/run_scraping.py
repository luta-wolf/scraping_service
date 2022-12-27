from  scraping.parsers import *
import codecs

parsers = ((pars_hh, 'https://kazan.hh.ru/search/vacancy?area=113&search_field=name&salary=455000&text=Python+developer&ored_clusters=true&enable_snippets=true'),
			(pars_habr, 'https://career.habr.com/vacancies?q=python%20developer&s[]=2&s[]=82&s[]=4&type=all'),
			(pars_job, 'https://russia.superjob.ru/vacancy/search/?keywords=Python%20developer')
			)

jobs, errors = [], []
for func, url in parsers:
	j, e = func(url)
	jobs += j
	errors += e


h = codecs.open('hh2.txt', 'w', 'utf-8')
for job in jobs:
	h.write(str(job) + '\n')
h.close()
