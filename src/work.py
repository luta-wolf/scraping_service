import requests
import codecs
from bs4 import BeautifulSoup as BS

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
# url2 = 'https://career.habr.com/vacancies?q=python+developer&l=1&type=all'
resp = requests.get(url, headers=headers)
jobs = []
errors = []
if resp.status_code == 200:
	soup = BS(resp.content, 'html.parser')
	div_lst = soup.find_all('div', attrs={'class': "vacancy-serp-item__layout"})
	if div_lst:
		for div in div_lst:
			title = div.find('a', attrs={'class': 'serp-item__title'})
			href = title.get('href')
			vacancy = title.text
			company = div.find('a').text
			content = div.find( attrs={'data-qa': 'vacancy-serp__vacancy_snippet_requirement'}).text
			jobs.append({'title': vacancy, 'url': href, 'description': content, 'company': company,})
	else:
		errors.append({'url': url, 'title': 'Div does not exists'})
else:
	errors.append({'url': url, 'title': 'Page do not response'})

# for job in jobs:
# 	print()
# 	print(*jobs, sep='\n')

h = codecs.open('hh2.txt', 'w', 'utf-8')
h.write(str(jobs))
h.close()


