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
<summary>Оределения</summary>

- `QuerySet` - список объектов заданной модели. QuerySet позволяет читать данные из базы данных, фильтровать и изменять их порядок.
- `ORM` (англ. Object-Relational Mapping, рус. объектно-реляционное отображение, или преобразование) — технология программирования, которая связывает базы данных с концепциями объектно-ориентированных языков программирования, создавая «виртуальную объектную базу данных»... т.е. ORM — прослойка между базой данных и кодом который пишет программист, которая позволяет созданые в программе объекты складывать/получать в/из бд.
- `Bootstrap` — это открытый и бесплатный фреймворк, который используется веб-разработчиками для быстрой вёрстки адаптивных дизайнов сайтов и веб-приложений. Включает в себя HTML- и CSS шаблоны оформления для типографики, веб форм, кнопок, меток, блоков навигации и прочих компонентов веб-интерфейса, включая JavaScript расширения.


</details>

<details>
<summary>Команды</summary>

### Виртульное окружение
- `python3.10 -m venv venv` - установка venv
- `source venv/bin/activate` - запуск venv
- `pip install --upgrade pip` - обновляем pip
- `pip freeze` - просмотр установеленных бибилиотек в venv
- `deactivate` - выход из venv
- `pip3 freeze > requirements.txt` - запись установленных библиотек из venv в txt файл
- `pip install -r requirements.txt`- установка всех требуемыех библиотек в venv
### Команды git
- `git reset HEAD` - отменить последний `add`
- `git reset --hard` - сбросить все изменения до последнего комита (может привести к потере результатов работы)
### Установка и запуск Django
- `pip install django` - установка последней версии django (в качестве бибилиотеки)
- `pip install requests` - установка библиотеки requests
- `python manage.py makemigrations` - создаем миргации (будущие таблицы в БД)
- `python manage.py migrate` - запуск миграций (базовые настройки для БД)
- `django-admin startproject <name_project> .` - установка django (в качестве приложения)
- `python manage.py startapp <name_project> .` - установка django (в качестве приложения)
- `python manage.py createsuperuser` - создание суперюзера
- `python manage.py runserver` - запуск проекта в браузере `http://127.0.0.1:8000/`
- `python manage.py shell` - запуск интерпретатора, который работает с внутренней структоурой django и базой данных
- `python manage.py dumpdata scraping  > <file_name>.json` - сохранение базы даннх в `json` формат (в одну строку)
- `manage.py dumpdata --indent 2 scraping  > <file_name>.json` - сохранение базы даннх в более удобный для чтения `json` формат
- `python manage.py loaddata <file_name>.json` - загрузка бд из `json` файла
- `pip install ipython` - установка ipython (прокаченный интерпретатора), который работает с внутренней структоурой django и базой данных
</details>
<details>
<summary>Полезные ссылки</summary>

## Полезные ссылки
- [gitignore.io](https://www.toptal.com/developers/gitignore/) - генерирует удобные `.gitignore` файлы для нашего проекта
- [Django](https://www.djangoproject.com/) - официальная документация
- [Django fun](https://django.fun/) - документация на русском
- [bootstrap color](https://getbootstrap.com/docs/5.2/customize/color/#theme-colors) - цветовая палитра bootstrap
- [MATERIAL DESIGN color](https://m2.material.io/design/color/the-color-system.html#tools-for-picking-colors) - цветовая палитра MD

</details>
<details>
<summary>Пошаговое выполнение проекта часть 2</summary>

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
<summary>Пошаговое выполнение проекта часть 3</summary>

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
<summary>Пошаговое выполнение проекта часть 4</summary>

- `001` - Лекция об юзераз и абстрактных юзерах
- `002` - Создали новое приложение `accounts` для авторизиции и переопределения [юзеров](https://docs.djangoproject.com/en/3.0/topics/auth/customizing/#a-full-example)
- `003` - Сохранили базу данный в `json` формат
- `004` - Удаление старой базы `db.sqlite3`, удаление файлов и папки `scraping/migrations`, кроме файла `__init__.py`, создание новой бд и новых миграций
<img width="820" alt="image" src="https://user-images.githubusercontent.com/58044383/209208852-77da0140-fa95-4e10-b269-1691e65a6b14.png">
<img width="1357" alt="image" src="https://user-images.githubusercontent.com/58044383/209210717-18158b07-417f-4a32-95ef-be9e094f14b4.png">
</details>

<details>
<summary>Часть 5 - Получение данный с сайтов с вакансиями (скрапинг)</summary>
- `001` - Несколько слов о том, как получать данные с сайтов.
</details>
