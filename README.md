# AgriTjet
a start up focused on using the possibilities of technology to enhance the production and distribution of raw, processed and finished agro products to consumers, companies etc via a dedicated delivery channel


## Project setup

* clone this repo and `cd` into it
* create a virtual environment `python -m venv venv`
* activate it
if you are on linux or mac `source venv/bin/activate`
if you are on windows `./sripts/activate`

``` python
pip install -r requirements.txt

```

### Compile for development

there are two ways to setup the server locally

1. if you have python 3+ installed in your computer

``` python
python manage.py migrate

python manage runserver [port]
```

2. if you have docker installed on your computer

``` bash
./scripts/docker_biuld
 
./scripts/docker_run
```

### Compile for production

``` python
DJANGO_SETTINGS_MODULE=tjet.settings.production python manage.py migrate
DJANGO_SETTINGS_MODULE=tjet.settings.production python manage.py runserver [port]
```

**you will need to have your postgres database configurations in your .env file**

## CONTRIBUTING

Everyone is welcomed to trow-in his/her own idea to help make this project a success. To contribute to this Open Source Project, please read through [CONTRIBUTING.md](CONTRIBUTING.md).

## CODE OF CONDUCT

To ensure that the project continues in peace, the project will follow a set of code of conduct as listed in [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md).
