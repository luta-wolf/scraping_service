# Сервис по сбору и рассылки вакансий

<details>
<summary>Описание проекта</summary>

### Научимся
- как скрапить данные с сайтов
- как работает Django и как работают его компонеты между собой
- запускать процессы вне Django
- пользоваться бибилиотеками `requests` и `beautiful soup`
- для оформления интерфейса воспользуемся [Bootstrap](https://getbootstrap.com/)
- разместим наш сайт на сервисе [heroku](https://www.heroku.com/) чтобы он был виден всем

### IDE
- Vs code (Python от Microsofft и Djaneiro - Django Snippets)
- Pycharm

### Полезное
- [Обучающий видеокурс на Udemy.com](https://www.udemy.com/course/site-on-django-3/)
- [Код](https://github.com/olegJF/scraping_service)
</details>

<details>
<summary>Команды</summary>

### Виртульное окружение
- `python3.10 -m venv venv` - устанавливаем venv
- `source venv/bin/activate` - запускаем venv
- `pip install --upgrade pip` - обновляем pip
- `pip freeze` - проверка установеленных бибилиотек в venv
- `deactivate` - выходим из venv
- `pip3 freeze > requirements.txt` - запись установеленных билилотек из venv в txt файл
- `pip install -r requirements.txt`- установить все требуемые библиотеки python в новом окружении
### Немного полезных команд git
- `git reset HEAD` - отменить последний `add`
- `git reset --hard` - сбросить все изменеия до последнего комита (может привести к потере результатов работы)
### Установка и запуск Django
- `pip install django` - устанавливаем последнюю версию django (в качестве бибилиотеки)
- `pip install requests` - установка библиотеки requests
- `python manage.py makemigrations` - создаем миргации
- `python manage.py migrate` - запуск миграций (базовые настройки для БД)
- `django-admin startproject <name_project> .` - установка django (в качестве приложения)
- `python manage.py startapp <name_project> .` - установка django (в качестве приложения)
- `python manage.py createsuperuser` - создание суперюзера
- `python manage.py runserver` - запуск проекта в браузере `http://127.0.0.1:8000/`
- `python manage.py shell` - запуск интерактивной консоли
- `pip install ipython` - установка ipython (прокаченный терминал)
</details>

## Полезные ссылки
- [gitignore.io](https://www.toptal.com/developers/gitignore/) - генерирует удобные `.gitignore` файлы для нашего проекта
- [Django](https://www.djangoproject.com/) - официальная документация
- [Django fun](https://django.fun/) - документация на русском


<details>
<summary>Пошаговое выполнение проекта</summary>

- `part1-2, 001` Схема работы джанга и его компонентов
<img width="1615" alt="image" src="https://user-images.githubusercontent.com/58044383/206925171-dbd04e9f-4456-4301-b852-f20cc8bc8925.png">

- `part1-2, 003` Перевел админку на русский
<img width="1262" alt="image" src="https://user-images.githubusercontent.com/58044383/206928854-10938b5d-58b6-42bb-86b6-99957e4205c8.png">

- `part1-2, 004` Подключил страницу `/home`
<img width="338" alt="image" src="https://user-images.githubusercontent.com/58044383/207385563-3a193cd2-e2ff-4754-99c8-cb15f3a5aaca.png">

- `part1-2, 005` Добавил текущую дату на страницу `/home`
<img width="400" alt="image" src="https://user-images.githubusercontent.com/58044383/207696337-bfdc0b17-a5bc-4994-b9e5-0a17aad106e9.png">

- `part1-2, 008` Создание миграций - таблички `City` в БД
<img width="708" alt="image" src="https://user-images.githubusercontent.com/58044383/207704015-c049f59e-7913-43de-9d0d-29ea812be8e1.png">

`part1-2, 008` Вывел таблицу `City` `/admin` + название городов выглядят как они есть
<img width="1208" alt="image" src="https://user-images.githubusercontent.com/58044383/207709105-53b5ac51-0fa6-42bd-b684-223d53e22f95.png">

`part1-2, 010` - Создал в БД таблицу `Language` (подключаются через миграции)
<img width="860" alt="image" src="https://user-images.githubusercontent.com/58044383/207958323-64aabf8a-70e0-4a24-b39b-ee96e5effe6f.png">
<img width="1143" alt="image" src="https://user-images.githubusercontent.com/58044383/207958624-7997aea5-b180-4fff-9b6c-6f930dc73508.png">

`part1-2, 013` - Создал в БД таблицу `Vacancy` (подключаются через миграции)
<img width="706" alt="image" src="https://user-images.githubusercontent.com/58044383/208195341-cb7df05b-bde3-44d5-a2ba-0104ac81b25b.png">
<img width="1167" alt="image" src="https://user-images.githubusercontent.com/58044383/208195443-0061f077-9b71-4a0a-803f-808a7e852c76.png">
</details>
