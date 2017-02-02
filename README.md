# creadr api
python 2.7 on Flask

## dev environment setup (Mac & Linux)

**prerequisite**
- virtualenv
- pip

**steps**
- clone the repo
```sh
git clone git@github.com:creadr/creadr-api.git
cd creadr-api
```

- set up virtual env
```sh
virtualenv ~/.venv/creadr-api
. ~/.venv/creadr-api/bin/activate
```

- install dependencies
```sh
pip install -r requirements.txt
```

- run test
```sh
python manage.py test
```

- run server locally
```sh
python manage.py runserver
```

- test server
```sh
$ curl localhost:8080
Hello World!
```
