# Eventex

Sistema de Eventos encomendado pela Morena

[![Build Status](https://travis-ci.org/mayckxavier/eventex-2020.svg?branch=master)](https://travis-ci.org/mayckxavier/eventex-2020)

## Como desenvolver?

1. Clone o repositório.
2. Crie um virtualenv com Python 3.6.3
3. Ative o virtualenv
4. instale as dependencias
5. Configure a instancia com o .env
6. Execute os testes

```console
$ git glone git@github.com:mayckxavier/eventex-2020.git
$ cd eventex-2020
$ python -m venv .wttd
$ source .wttd/bin/activate
$ pip install -r requirements.txt
$ cp contrib/env-sample .env
$ python manage.py test
```

## Como fazer deploy?

1. Crie uma instancia no heroku
2. Envie as configuracoes para o heroku
3. Defina uma SECRET_KEY segura para a instancia
4. Defina DEBUG=False
5. Configure o servico de email
6. envie o codigo para o heroku

```console
$ heroku create minhainstancia
$ heroku config:push
$ heroku config:set SECRET_KEY=`python contrib/secret_gen.py`
$ heroku config:set DEBUG=False
#configuro o email
$ git push heroku master --force
```
