# creadr-api

## dev environment setup (Mac & Linux)

**prerequisite**
- virtualenv
- pip

**steps**
- clone the repo
`git clone git@github.com:creadr/creadr-api.git`
`cd creadr-api`

- set up virtual env
```
virtualenv ~/.venv/creadr-api
. ~/.venv/creadr-api/bin/activate
```

- install dependencies
```
pip install -r requirements.txt
```

- run test
```
python main_test.py
```

- run server locally
```
python main.py
```

- test server
```
$ curl localhost:8080
Hello World!
```
