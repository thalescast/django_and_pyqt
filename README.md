# Aplicação Web com Django

A primeira parte da aplicação foi feita utilizando o Django, framework em Python. Dessa forma é necessário que algumas coisas sejam feitas para que rode adequadamente.

## Instação

É necessário que uma ambiente virtual seja criado para que, quando ativado, seja realizado o seguinte comando dentro da pasta que contém o arquivo requirements:
```
pip install -r requirements.txt
```
O arquivo .txt contem as dependências do projeto e com esse comando, todas elas serão instaladas.

## Banco de dados:

O banco de dados utilizado por este projeto foi o MySql. Desse modo, é necessário que se vá no settings.py da aplicação e configure o seguinte trecho:

```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'db_creative_drive',
        'USER': 'nome_do_usuário_mysql',
        'PASSWORD': 'senha_do_usuário_mysql',
        'HOST': 'localhost',   # Or an IP Address that your DB is hosted on
        'PORT': '3306',
    }
}
```

## Autenticação junto ao servidor Web

Para que seja possível criar um usuário para que se possa fazer Login. Deve-se ir até o local onde o arquivo "manage.py" se encontra e executar o seguinte comando:
```
python manage.py createsuperuser

```

## Rodar aplicação Web

Com o seguinte comando é possível levantar o servidor local e ver a página funcionando:

```

python manage.py runserver

```

