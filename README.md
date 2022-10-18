![project workflow](https://github.com/bfswrd/IntensiveYandex/actions/workflows/python-package.yml/badge.svg)

# Оглавление

* [Запуск](#Запуск)
    * [Установка](#Установка)
    * [Создание .env](#Env)
    * [Старт](#Старт)

python 3.9.6  
Django 3.2.16

---

## Запуск

Последовательно выполните руководство ниже

---

### Установка

Последовательно выполните команды

Windows

```bash
git clone git@github.com:bfswrd/IntensiveYandex
cd IntensiveYandex
python -m venv venv
source venv/Scripts/activate
pip install -r requirements.txt
``` 

Linux/Mac OS

```bash
git clone git@github.com:bfswrd/IntensiveYandex
cd IntensiveYandex
python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt
``` 

##### Или запустите

Windows

```bash
git clone git@github.com:bfswrd/IntensiveYandex;cd IntensiveYandex;python -m venv venv;source venv/Scripts/activate;pip install -r requirements.txt
```

Linux/Mac OS

```bash
git clone git@github.com:bfswrd/IntensiveYandex;cd IntensiveYandex;python3 -m venv venv;source venv/bin/activate;pip3 install -r requirements.txt
```

#### Создайте Env ↓

---

### Env

Необходимо создать файл ".env" и поместить его в корень проекта.

```bash
touch .env
```

В него записать:

```text
SECRET_KEY=<Вами сгенерированный ключ>
DEBUG=<Одно из True/False>
ALLOWED_HOSTS=<ip, разделенные запятой (",")>
```

#### Можно запускать ↓

---

### Старт

Windows

```bash
python manage.py runserver 127.0.0.1:8000
```

Linux/Mac OS

```bash
python3 manage.py runserver 127.0.0.1:8000
```

---
