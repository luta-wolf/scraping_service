import requests
import codecs
from bs4 import BeautifulSoup as BS
from random import randint

__all__ = ('pars_hh', 'pars_habr', 'pars_job')

headers = [
	{'User-Agent': 'Mozilla/5.0 (Windows NT 5.1; rv:47.0) Gecko/20100101 Firefox/47.0',
		'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'},
	{'User-Agent': 'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.112 Safari/537.36',
		'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'},
	{'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; rv:53.0) Gecko/20100101 Firefox/53.0',
		'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'}
	]

def pars_hh(url):
	jobs = []
	errors = []
	# url = 'https://hh.ru/search/vacancy?search_field=name&search_field=company_name&search_field=description&text=Python+developer'
	resp = requests.get(url, headers=headers[randint(0, 2)])
	if resp.status_code == 200:
		soup = BS(resp.content, 'html.parser')
		div_lst = soup.find_all('div', attrs={'class': "vacancy-serp-item__layout"})
		if div_lst:
			for div in div_lst:
				title = div.find('a', attrs={'class': 'serp-item__title'})
				href = title.get('href')
				vacancy = title.text
				company = div.find(attrs={'data-qa': "vacancy-serp__vacancy-employer"}).text
				content = div.find( attrs={'data-qa': 'vacancy-serp__vacancy_snippet_requirement'}).text
				jobs.append({'title': vacancy, 'url': href, 'description': content, 'company': company,})
		else:
			errors.append({'url': url, 'title': 'Div does not exists'})
	else:
		errors.append({'url': url, 'title': 'Page do not response'})
	return jobs, errors

def pars_habr(url):
	jobs = []
	errors = []
	# url = 'https://career.habr.com/vacancies?q=python+developer&l=1&type=all'
	domain = 'https://career.habr.com/'
	resp = requests.get(url, headers=headers[randint(0, 2)])
	if resp.status_code == 200:
		soup = BS(resp.content, 'html.parser')
		div_lst = soup.find_all('div', attrs={'class': 'vacancy-card__inner'})
		if div_lst:
			for div in div_lst:
				title = div.find(attrs={'class': 'vacancy-card__title'})
				href = title.a['href']
				vacancy = title.text
				company = div.find(attrs={'class': 'vacancy-card__company-title'}).text
				content = div.find(attrs={'class': 'vacancy-card__skills'}).text
				jobs.append({'title': vacancy, 'url': domain + href, 'description': content, 'company': company,})
		else:
			errors.append({'url': url, 'title': 'Div does not exists'})
	else:
		errors.append({'url': url, 'title': 'Page do not response'})
	return jobs, errors

def pars_job(url):
	jobs = []
	errors = []
	# url = 'https://russia.superjob.ru/vacancy/search/?keywords=Python%20developer'
	domain = 'https://russia.superjob.ru'
	resp = requests.get(url, headers=headers[randint(0, 2)])
	if resp.status_code == 200:
		soup = BS(resp.content, 'html.parser')
		div_lst = soup.find_all('div', attrs={'class': '_1nGB_'})
		if div_lst:
			for div in div_lst:
				href = div.find('a').get('href')
				vacancy = div.find('a').text
				if not div.find(attrs={'class': '_2zPWM C-ReH _2icK1 _2DxkW'}):
					company = 'No name'
				else:
					company = div.find(attrs={'class': '_2zPWM C-ReH _2icK1 _2DxkW'}).text
				content = div.find(attrs={'class': '_1G5lt _3EXZS _3pAka _3GChV _2GgYH'}).text
				jobs.append({'title': vacancy, 'url': domain + href, 'description': content, 'company': company,})
		else:
			errors.append({'url': url, 'title': 'Div does not exists'})
	else:
		errors.append({'url': url, 'title': 'Page do not response'})
	return jobs, errors

# print(*jobs, sep='\n')

if __name__ == '__main__':
	url = 'https://hh.ru/search/vacancy?search_field=name&search_field=company_name&search_field=description&text=Python+developer'
	jobs, errors = pars_hh(url)
	# url2 = 'https://career.habr.com/vacancies?q=python+developer&l=1&type=all'
	# jobs, errors =  pars_habr(url2)
	# url3 = 'https://russia.superjob.ru/vacancy/search/?keywords=Python%20developer'
	# jobs, errors =  pars_job(url3)
	h = codecs.open('hh2.txt', 'w', 'utf-8')
	for job in jobs:
		h.write(str(job) + '\n')
	h.close()
