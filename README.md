#  Django oline shop


## О приложении:
Приложение является полноценным маркетом с товарами , корзиной . Так и со стороны бэка допуступы всевозможные создание
карточек товара 

### Backend
+ API — Django REST
+ База Данных — PostgreSQL
+ Кэширование — Redis
+ Фоновые задачи — Celery
+ Контейнеризация — Docker и Docker Compose
+ Логирование - Centry
+ ORM — DjangoORM
### Frontend
+ HTML , CSS(Bootstrap)
+ JavaScript(JQuery , Next.js)

- Создаём виртуальное окружение Python и активируем его

  ```
  $ python -m venv venv
  $ venv\Scripts\activate.bat - для Windows / source venv/bin/activate - для Linux и MacOS
  ```

- Устанавливаем зависимости проекта

  ```
  $ pip install -r requirements.txt
  ```
 

- Миграции БД

  ```
  $ python manage.py migrate --noinput
  ```
  
- 3апуск

  ```
  $ python manage.py runserver
 
  $ gunicorn config.wsgi:application --bind 0.0.0.0:8000
  ```
  

Docker

- Собрать проект
  ```
  $ docker-compose -f docker-compose.yml up -d --build
  ```


## Админка

```
$ python manage.py createsuperuser --username admin@email.com --email admin@email.com


$ docker-compose -f docker-compose.yml exec web python manage.py createsuperuser --username admin@email.com --email admin@email.com
```



- Запуск Celery 

  ```
    Windows:
  $ celery -A config beat --loglevel=info
  $ celery -A config worker --pool=solo --loglevel=info
  
    Linux:
  $ celery -A config worker --beat --loglevel=info
  ```
  
## REST API

К некоторым ручкам нужна аутентификация . Для доступа к API перейти :
:  ```http://.../swagger``` 

##  Авто-заполнение магазина для быстрого тестирования

POST запрос по адресу ```http://.../api/db_auto_fill``` с содержимым в формате:

```
{
  model: "Categories",
  amount: 7
}
```


