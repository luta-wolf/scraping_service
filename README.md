# Сервис по сбору и рассылки вакансий

<details>
<summary>Описание проекта</summary>

### Научимся
- как скрапить данные с сайтов
- как работает Django и как работают его компонеты между собой
- запускать процессы вне Django
- пользоваться бибилиотеками `requests` и `beautiful soup`
- для оформления интерфейса воспользуемся [Bootstrap](https://getbootstrap.com/) и [здесь на русском](https://bootstrap-4.ru/)
- разместим наш сайт на сервисе [heroku](https://www.heroku.com/) чтобы он был виден всем

### IDE
- Vs code (Python от Microsofft и Djaneiro - Django Snippets)
- Pycharm

### Полезное
- [Обучающий видеокурс на Udemy.com](https://www.udemy.com/course/site-on-django-3/)
- [Код](https://github.com/olegJF/scraping_service)
</details>

<details>
<summary>Определения</summary>

- `QuerySet` - список объектов заданной модели. QuerySet позволяет читать данные из базы данных, фильтровать и изменять их порядок.
- `ORM` (англ. Object-Relational Mapping, рус. объектно-реляционное отображение, или преобразование) — технология программирования, которая связывает базы данных с концепциями объектно-ориентированных языков программирования, создавая «виртуальную объектную базу данных»... т.е. ORM — прослойка между базой данных и кодом который пишет программист, которая позволяет созданые в программе объекты складывать/получать в/из бд.
- `Bootstrap` — это открытый и бесплатный фреймворк, который используется веб-разработчиками для быстрой вёрстки адаптивных дизайнов сайтов и веб-приложений. Включает в себя HTML- и CSS шаблоны оформления для типографики, веб форм, кнопок, меток, блоков навигации и прочих компонентов веб-интерфейса, включая JavaScript расширения.
- `Requests` — это HTTP-библиотека для языка программирования Python. Цель проекта — сделать HTTP-запросы более простыми и удобными для человека. Документация на [английском](https://requests.readthedocs.io/en/latest/).
- `Beautiful Soup` - представляет собой пакет Python для анализа документов HTML и XML (включая наличие неправильной разметки, то есть незакрытых тегов, названных так в честь супа тегов). Он создает дерево синтаксического анализа для проанализированных страниц, которое можно использовать для извлечения данных из HTML, что полезно для парсинга веб-страниц. Подробнее [здесь](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) и [здесь](https://www.crummy.com/software/BeautifulSoup/bs4/doc.ru/bs4ru.html#)
- `Selenium` - это инструмент для автоматизации действий веб-браузера. В большинстве случаев используется для тестирования Web-приложений, но этим не ограничивается. В частности, он может быть использован для решения рутинных задач администрирования сайта или регулярного получения данных из различных источников (сайтов). Используется редко, однако несет важный характер. Подробнее [здесь](https://www.selenium.dev/) и [здесь](https://www.crummy.com/software/BeautifulSoup/bs4/doc.ru/bs4ru.html#id8).
- `User agent` - идентификационная строка клиентского приложения; обычно используется для приложений, осуществляющих доступ к веб-сайтам — браузеров, поисковых роботов и «пауков», мобильных телефонов и других устройств со встроенным доступом к веб-ресурсам. [Подробнее ...](https://ru.wikipedia.org/wiki/User_agent)


</details>

<details>
<summary>Команды</summary>

### Виртульное окружение
- `python3.10 -m venv venv` - установка venv
- `source venv/bin/activate` - запуск venv
- `pip install --upgrade pip` - обновляем pip
- `pip freeze` - просмотр установеленных бибилиотек в venv
- `deactivate` - выход из venv
- `pip freeze > requirements.txt` - запись установленных библиотек из venv в txt файл
- `pip install -r requirements.txt`- установка всех требуемыех библиотек в venv
### Команды git
- `git reset HEAD` - отменить последний `add`
- `git reset --hard` - сбросить все изменения до последнего комита (может привести к потере результатов работы)
### Установка Django и библиотек
- `pip install django` - установка последней версии django (в качестве бибилиотеки)
- `pip install requests` - установка библиотеки `requests`
- `pip install bs4` - установка библиотеки `beautiful soup`
- `pip install django-jsonfield-backport` - установка библиотеки для сохранения `json`полей в бд `sqlite3`
- `pip install ipython` - установка ipython (прокаченный интерпретатора), который работает с внутренней структурой django и базой данных
### Запуск и работа с проектом
- `django-admin startproject <name_project> .` - создание проекта django
- `python manage.py startapp <name_project> .` - создание приложения в самом django (их может быть много)
- `python manage.py makemigrations` - создаем миргации (будущие таблицы в БД)
- `python manage.py migrate` - запуск миграций (базовые настройки для БД)
- `python manage.py createsuperuser` - создание суперюзера
- `python manage.py runserver` - запуск проекта в браузере `http://127.0.0.1:8000/`
- `python manage.py shell` - запуск интерпретатора, который работает с внутренней структурой django и базой данных
- `python manage.py dumpdata scraping  > <file_name>.json` - сохранение базы даннх в `json` формат (в одну строку)
- `python manage.py dumpdata --indent 2 scraping  > <file_name>.json` - сохранение базы даннх в более удобный для чтения `json` формат
- `python manage.py loaddata <file_name>.json` - загрузка бд из `json` файла
</details>
<details>
<summary>Полезные ссылки</summary>

## Полезные ссылки
- [gitignore.io](https://www.toptal.com/developers/gitignore/) - генерирует удобные `.gitignore` файлы для нашего проекта
- [Django](https://www.djangoproject.com/) - официальная документация
- [Django fun](https://django.fun/) - документация на русском
- [bootstrap color](https://getbootstrap.com/docs/5.2/customize/color/#theme-colors) - цветовая палитра bootstrap
- [MATERIAL DESIGN color](https://m2.material.io/design/color/the-color-system.html#tools-for-picking-colors) - цветовая палитра MD
- [MATERIAL DESIGN 3](https://m3.material.io/styles/color/overview) - цветовая палитра MD3
- [mailgun](https://www.mailgun.com/) и [sendgrid](https://sendgrid.com/)- сервисы по отправке писем
- [freenom](https://www.freenom.com/) - бесплатные домены

</details>

### Пошаговое выполнение проекта
<details>
<summary>Часть 2 - Django. Старт проекта и создание приложений</summary>

- `001` Схема работы джанга и его компонентов
<img width="1615" alt="image" src="https://user-images.githubusercontent.com/58044383/206925171-dbd04e9f-4456-4301-b852-f20cc8bc8925.png">

- `003` Перевел админку на русский
<img width="1262" alt="image" src="https://user-images.githubusercontent.com/58044383/206928854-10938b5d-58b6-42bb-86b6-99957e4205c8.png">

- `004` Подключил страницу `/home`
<img width="338" alt="image" src="https://user-images.githubusercontent.com/58044383/207385563-3a193cd2-e2ff-4754-99c8-cb15f3a5aaca.png">

- `005` Добавил текущую дату на страницу `/home`
<img width="400" alt="image" src="https://user-images.githubusercontent.com/58044383/207696337-bfdc0b17-a5bc-4994-b9e5-0a17aad106e9.png">

- `008` Создание миграций - таблички `City` в БД
<img width="708" alt="image" src="https://user-images.githubusercontent.com/58044383/207704015-c049f59e-7913-43de-9d0d-29ea812be8e1.png">

- `008` Вывел таблицу `City` `/admin` + название городов выглядят как они есть
<img width="1208" alt="image" src="https://user-images.githubusercontent.com/58044383/207709105-53b5ac51-0fa6-42bd-b684-223d53e22f95.png">

- `010` - Создал в БД таблицу `Language` (подключаются через миграции)
<img width="860" alt="image" src="https://user-images.githubusercontent.com/58044383/207958323-64aabf8a-70e0-4a24-b39b-ee96e5effe6f.png">
<img width="1143" alt="image" src="https://user-images.githubusercontent.com/58044383/207958624-7997aea5-b180-4fff-9b6c-6f930dc73508.png">

- `013` - Создал в БД таблицу `Vacancy` (подключаются через миграции)
<img width="706" alt="image" src="https://user-images.githubusercontent.com/58044383/208195341-cb7df05b-bde3-44d5-a2ba-0104ac81b25b.png">
<img width="1167" alt="image" src="https://user-images.githubusercontent.com/58044383/208195443-0061f077-9b71-4a0a-803f-808a7e852c76.png">

- `014` - Создание записей в БД через внутренний интерпретатор - кварисет
<img width="1305" alt="image" src="https://user-images.githubusercontent.com/58044383/208277153-06f5f299-0c15-457b-a298-9829aefb1b42.png">
<img width="1130" alt="image" src="https://user-images.githubusercontent.com/58044383/208276215-8d831e52-af52-49f1-bb54-0ce9ce019502.png">

- `015` - Объясняет QuerySet
- `018` - Подключил bootstrap, на стр `home` вывел из БД назване вакансии, url и ее описание
<img width="1057" alt="image" src="https://user-images.githubusercontent.com/58044383/208319970-abd5df50-c3ca-4481-a9c8-b6ae8ab6783d.png">

- `020` - Сделал шапку, вложил вакансии в красивые формочки, середина вложена в контейнер, т.е. расположена строго по центру.
<img width="1046" alt="image" src="https://user-images.githubusercontent.com/58044383/208492639-405ac281-bf78-4e16-95d6-9a37d1eba99e.png">

- `021` - Работа с `Live Tebplates` в `PyCharm`
- `021` - Добавил к описанию город, язык и дату появления объявления.
<img width="1197" alt="image" src="https://user-images.githubusercontent.com/58044383/208549969-3993c778-4875-417e-bc6c-8f017bf57bab.png">
</details>

<details>
<summary>Часть 3 - Форма. Какие формы бывают и как с ними работать</summary>

- `001` - Разместил окошки ввода города и языка
- В командной строке происходит поиск по введеным параметрам
<img width="620" alt="image" src="https://user-images.githubusercontent.com/58044383/208749889-94657010-6260-43e2-be28-cfc0bfd3f517.png">

- `003` - С помощью форм Django поменял окошки
<img width="419" alt="image" src="https://user-images.githubusercontent.com/58044383/208787427-f9a66e54-9026-4e84-ac09-0e5d6be95678.png">

- `004` - Наведение красоты - поменял окошки и кнопку
<img width="691" alt="image" src="https://user-images.githubusercontent.com/58044383/208990727-68fe767f-19a2-4219-8f34-3f5d28d07ebe.png">

- `005` - Выравнивание кнопок по центру
<img width="862" alt="image" src="https://user-images.githubusercontent.com/58044383/208997138-6181a255-309e-4955-a77c-9d878c35f074.png">
</details>

<details>
<summary>Часть 4 - Приложение accounts</summary>

- `001` - Лекция об юзераз и абстрактных юзерах
- `002` - Создали новое приложение `accounts` для авторизиции и переопределения [юзеров](https://docs.djangoproject.com/en/3.0/topics/auth/customizing/#a-full-example)
- `003` - Сохранили базу данный в `json` формат
- `004` - Удаление старой базы `db.sqlite3`, удаление файлов и папки `scraping/migrations`, кроме файла `__init__.py`, создание новой бд и новых миграций
<img width="820" alt="image" src="https://user-images.githubusercontent.com/58044383/209208852-77da0140-fa95-4e10-b269-1691e65a6b14.png">
<img width="1357" alt="image" src="https://user-images.githubusercontent.com/58044383/209210717-18158b07-417f-4a32-95ef-be9e094f14b4.png">
</details>

<details>
<summary>Часть 5 - Получение данных с сайтов с вакансиями (скрапинг)</summary>

- `001` - Несколько слов о том, как получать данные с сайтов.
- `002` - Получение html-страницы с сайта `https://hh.ru/`
<img width="862" alt="image" src="https://user-images.githubusercontent.com/58044383/209395485-4dae3cc0-4a25-42dd-8743-1f92d28318b6.png">

- `003` - Принципы поиска данных внутри html-текста
	Блок со всеми вакансиями `<div class="bloko-columns-wrapper">`
<img width="1199" alt="image" src="https://user-images.githubusercontent.com/58044383/209450248-78bbdb21-d769-4d30-b66a-952be7ecbc8d.png">

	Блок с одной вакансией `<div class="vacancy-serp-item__layout">`
<img width="772" alt="image" src="https://user-images.githubusercontent.com/58044383/209450259-2d8b77c6-c357-4288-86ef-f7e7e401d0b2.png">

	Блок с названием вакансии и ссылкой на нее `<a class="serp-item__title" `
<img width="770" alt="image" src="https://user-images.githubusercontent.com/58044383/209450270-d3b41d28-6406-4f3c-a0cb-b28592351836.png">

	Блок с Названием компании и ссылкой на нее `<div class="vacancy-serp-item__meta-info-company">`
<img width="768" alt="image" src="https://user-images.githubusercontent.com/58044383/209450283-f4c174d4-3ee0-4525-b59b-4c48fcd60d07.png">

	Блок с описанием вакансии `<div class="g-user-content">`
<img width="763" alt="image" src="https://user-images.githubusercontent.com/58044383/209450308-7217f852-5c6e-4885-890d-386ba62324b4.png">

- `004` Сбор (скрапинг) данных с сайта `hh.ru`
- `005` Финализируем функционал для `hh.ru`
<img width="1112" alt="image" src="https://user-images.githubusercontent.com/58044383/209480231-62d6a4ca-80df-40dd-9c26-2b90f7140a6e.png">

- `006 - 009` Сбор данных и финализировние с сайтов `habr.com`, `career.habr.com` и `superjob.ru`
- `010` - Сбор данных со всех трех сайтов
<img width="1288" alt="image" src="https://user-images.githubusercontent.com/58044383/209632443-d2141eda-875f-4289-8a6f-0ad24236906a.png">

- `011` Запуск Django вне самого проекта.
- `012` Сохранение полученных вакансий в БД
<img width="1465" alt="image" src="https://user-images.githubusercontent.com/58044383/209659708-dfc9ef6c-460e-40f7-bfab-225b87111886.png">

- `013` Модель `Error` для сохранения ошибок
<img width="802" alt="image" src="https://user-images.githubusercontent.com/58044383/209666430-81ab2ec0-ae29-47bb-892c-70e5322a5680.png">

- `014` Несоответствие библиотеки jsonfield для Django 3.1.+
- `015` Как и где хранить адреса для парсеров.
- `016` Модель `Url` для парсинга по разным наборам Город-Язык
<img width="809" alt="image" src="https://user-images.githubusercontent.com/58044383/209675177-398de9da-7614-41e7-bc5e-3b063b4307b6.png">

- `017` Получение уникальных наборов пар город-ЯП, из таблицы с пользователями
<img width="1352" alt="image" src="https://user-images.githubusercontent.com/58044383/209679929-c926f976-4bce-4d56-a658-c66e86599fd6.png">

- `018` Получения набора урлов, согласно данных от пользователей.
- `019` Запуск функций скрапинга с полученными из БД данными
<img width="1293" alt="image" src="https://user-images.githubusercontent.com/58044383/209764927-8c9bbdea-f5b6-42bc-8e1b-2ae2b4a16c4a.png">

- `019` Несколько слов об асинхронном запуске функций
- `020` Несколько слов об асинхронном запуске функций
</details>

<details>
<summary>Часть 6 - Внесение изменений в отображения</summary>

- `001` - Реорганизация функций отображения.
<img width="1120" alt="image" src="https://user-images.githubusercontent.com/58044383/210198125-2ce8d63e-a158-458b-8b5f-de5d8b446b00.png">

- `002` - Пагинация (постраничное отображение). Подключение к функции отображения.
<img width="1291" alt="image" src="https://user-images.githubusercontent.com/58044383/210199642-5763a138-f205-41b9-b537-f282b2be1e0a.png">

- `003` - Пагинация. Улучшение отображения с помощью Bootstrap.
<img width="1261" alt="image" src="https://user-images.githubusercontent.com/58044383/210205322-a926aca7-092b-4bad-9f69-3ef2c024bff2.png">
</details>

<details>
<summary>Часть 7 - Кабинет пользователя</summary>

- `001` - Форма для входа пользователя.
- `002` - Функции входа\выхода пользователя.
<img width="1022" alt="image" src="https://user-images.githubusercontent.com/58044383/210251919-fe626c3a-cc84-46db-8bd8-586a644dd896.png">

- `003` - Регистрация нового пользователя. Форма.
- `004` - Функция для регистрации нового пользователя.
<img width="974" alt="image" src="https://user-images.githubusercontent.com/58044383/210389629-ef3f9af1-a2bd-4242-b9c7-90108afd6d91.png">

- `005` - Форма для изменения настроек пользователя.
<img width="1087" alt="image" src="https://user-images.githubusercontent.com/58044383/210401686-fceb27b7-fc96-4b42-b8cb-5f4b39f028dd.png">

- `006` - Изменение данных. Удаление пользователя.
<img width="1426" alt="image" src="https://user-images.githubusercontent.com/58044383/210713491-6b190ffa-d0fb-4653-91eb-3c0feede308c.png">
<img width="1437" alt="image" src="https://user-images.githubusercontent.com/58044383/210713436-46353927-bd30-49a1-93a1-3624cc7baf7d.png">

- `007` - Система информирования messages.
<img width="1438" alt="image" src="https://user-images.githubusercontent.com/58044383/210752119-cfca16b2-a625-4604-ada7-f4c778198daa.png">
<img width="1431" alt="image" src="https://user-images.githubusercontent.com/58044383/210753529-66f2c8b7-4d0f-41eb-a658-f1c661ffc60a.png">

</details>

<details>
<summary>Часть 8 - Кабинет пользователя</summary>

- `001` - Рассылка писем. Какие есть варианты.
	1. использовать службы по рассылки писем (`mailgun` или `sendgrid`) и быть готовым кому-то что то доказыать, создавать белые списки
	2. использовать возможности django (`send_mail()`) и вместе с тем для этого нужно иметь свой почтовый сервер
</details>
