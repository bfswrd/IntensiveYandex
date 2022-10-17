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

Windows/Mac OS

```bash
git clone https://github.com/bfswrd/IntensiveYandex
cd IntensiveYandex
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
``` 

Linux

```bash
git clone https://github.com/bfswrd/IntensiveYandex
cd IntensiveYandex
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
``` 

##### Или запустите

Windows/Mac OS

```bash
git clone https://github.com/bfswrd/IntensiveYandex|cd IntensiveYandex|python -m venv venv|source venv/bin/activate|pip install -r requirements.txt
```

Linux

```bash
git clone https://github.com/bfswrd/IntensiveYandex|cd IntensiveYandex|python3 -m venv venv|source venv/bin/activate|pip install -r requirements.txt
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
```

#### Можно запускать ↓

---

### Старт

Windows/Mac OS

```bash
python manage.py runserver 127.0.0.1:8000
```

Linux

```bash
python3 manage.py runserver 127.0.0.1:8000
```

---
