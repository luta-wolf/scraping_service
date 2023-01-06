import os, sys
import django
from django.core.mail import EmailMultiAlternatives

from django.contrib.auth import get_user_model

proj = os.path.dirname(os.path.abspath('manage.py'))
sys.path.append(proj)
os.environ["DJANGO_SETTINGS_MODULE"] = "scraping_service.settings"

django.setup()
from scraping.models import Vacancy


User = get_user_model()
qs = User.objects.filter(send_email=True).values('city', 'language', 'email')
user_dct = {}
for i in qs:
	user_dct.setdefault((i['city'], i['language']), [])
	user_dct[(i['city'], i['language'])].append(i['email'])
if user_dct:
	params = {'city_id__in': [], 'language_id__in': []}
	for pair in user_dct.keys():
		params['city_id__in'].append(pair[0])
		params['language_id__in'].append(pair[1])
	qs = Vacancy.objects.filter(**params)[:10]


# Отправка писем подписчикам. Начальный функционал.
subject, from_email, to = 'hello', 'from@example.com', 'to@example.com'
text_content = 'This is an important message.'
html_content = '<p>This is an <strong>important</strong> message.</p>'
msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
msg.attach_alternative(html_content, "text/html")
msg.send()
