# Сервис по сбору и рассылки вакансий

### Научимся
- как скрапить данные с сайтов
- как работает Django и как работают его компонеты между собой
- запускать процессы вне Django
- для оформления интерфейса воспользуемся [Bootstrap](https://getbootstrap.com/)
- разместим наш сайт на сервисе [heroku](https://www.heroku.com/) чтобы он был виден всем

### Инструменты
- Python
- Django

### Для скрапинга будут использоваться 2 бибилиотеки
- requests
- beautiful soup

### Оформление сайта
- Bootstrap

### IDE
- Vs code (Python от Microsofft и Djaneiro - Django Snippets)
- Pycharm
### Виртульное окружение
- `python3.10 -m venv venv` - устанавливаем venv
- `source venv/bin/activate` - запускаем venv
- `pip install --upgrade pip` - обновляем pip
- `pip freeze` - проверка установеленных бибилиотек в venv
- `deactivate` - выходим из venv
- `pip3 freeze > requirements.txt` - запись усановленных билилотек из venv в txt файл
- `git reset HEAD` - отменить последний `add`
### Установка и запуск Django
- `pip install django` - устанавливаем последнюю версию django (в качестве бибилиотеки)
- `django-admin startproject <name_project> .` - установка django (в качестве приложения)
- `python manage.py runserver` - запуск проекта в браузере `http://127.0.0.1:8000/`
- `python3 manage.py startapp <name_project> ` - установка нашего приложения
- `python3 manage.py migrate` - выполняем миграции
- `python3 manage.py createsuperuser` - создание суперюзера

## Полезные ссылки
- [gitignore.io](https://www.toptal.com/developers/gitignore/) - Генерируйте удобные `.gitignore` файлы для вашего проекта
- [css bootstap](https://www.bootstrapcdn.com/)
