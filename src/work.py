import requests
import codecs

'''
Парсим
https://hh.ru/
https://career.habr.com/
https://www.superjob.ru/
https://djinni.co
'''

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 5.1; rv:47.0) Gecko/20100101 Firefox/47.0',
			'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'
			}

url = 'https://hh.ru/search/vacancy?search_field=name&search_field=company_name&search_field=description&text=Python+developer'
url2 = 'https://career.habr.com/vacancies?q=python+developer&l=1&type=all'
resp = requests.get(url, headers=headers)
h = codecs.open('hh2.html', 'w', 'utf-8')
h.write(str(resp.text))
h.close()

'''
Блок со всеми вакансиями
<div class="bloko-columns-wrapper">

Блок с одной вакансией
<div class="vacancy-serp-item__layout">

Блок с названием вакансии и ссылкой на нее
<a class="serp-item__title" data-qa="serp-item__title" target="_blank" href="https://kazan.hh.ru/vacancy/72814312?from=vacancy_search_catalog&amp;query=Python+developer">Python Developer Trainee</a>

Блок с Названием компании и ссылкой на нее
<div class="vacancy-serp-item__meta-info-company">
	<a data-qa="vacancy-serp__vacancy-employer" class="bloko-link bloko-link_kind-tertiary" href="/employer/6093775?hhtmFrom=vacancy_search_catalog">Aston</a>
</div>

Блок с описанием вакансии
<div class="g-user-content">
'''
