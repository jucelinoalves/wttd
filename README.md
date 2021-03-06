# Eventex

[![Build Status](https://travis-ci.org/jucelinoalves/wttd.svg?branch=master)](https://travis-ci.org/jucelinoalves/wttd)
[![Maintainability](https://api.codeclimate.com/v1/badges/e20baeaa07578d353f7f/maintainability)](https://codeclimate.com/github/jucelinoalves/wttd/maintainability)

## Como desenvolver?

1. Clone o repositório.
2. Crie um virtualenv com Python 3.5
3. Ative o virtualenv.
4. Instale as dependências.
5. Configure a instância com o .env
6. Execute os testes.

```console
            
git clone https://github.com/jucelinoalves/wttd.git
cd wttd
python -m venv .wttd
source .wttd/Scripts/activate
pip install -r requirements-dev.txt
cp contrib/env-sample .env
python manage.py test
```

## Como fazer o deploy
 
 1. Crie uma instância no heroku.
 2. Envie as configurações para o heroku.
 3. Defina uma SECRET_KEY segura para instância.
 4. Defina DEBUG=False
 5. Configure o serviço de email.
 6. Envie o código para o heroku.
 
```console
heroku create minhainstancia
heroku config:push
heroku config:set SECRET_KEY=python contrib/secret_gen.py
heroku config:set DEBUG=False
# configuro o email
git push heroku master --force

``` 
 
 