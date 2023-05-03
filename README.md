# API проекта WiseJournal

## Описание

API для WiseJournal предоставляет для работоспособности социальной сети. 
Реализованы следующие функции: публикация записей, комментирование записи, подписка на авторов, просмотр сообществ.

## Технологический стек

* [Python 3.11](https://www.python.org)
* [Django 4.2](https://www.djangoproject.com)
* [DRF 3.14](https://www.django-rest-framework.org)
* JWT + Djoser

## Запуск проекта в dev-режиме

**Необходимо клонировать репозиторий**

```bash
git clone https://github.com/HETPAHHEP/api_final_wisejournal
```

**Создать виртуальное окружение и активировать его**

```bash
python -m venv venv
```
```bash
source venv/Scripts/activate
```

**Установить необходимые зависимости**

```bash
cd wisejournal_api
```
```bash
pip install -r requirements.txt
```

**Зафиксировать миграции**

```bash
./manage.py migrate
```

**Создать суперпользователя и запустить проект**

```bash
./manage.py createsuperuser
```

```bash
./manage.py runserver
```

## Документация

Подробная документация по ссылке: http://127.0.0.1:8000/redoc/