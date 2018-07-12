# Flask API

This is the Flask micro-framework API for Department and Employee details. Operations includes HTTP methods are `GET` `PUT` `DELETE` and `POST`<br/>

**Database:** Mysql<br/>
**Database ORM:** SQLAlchemy

The detail information about database found in [Database dump](/dump)

**Installation**

The installation is very straightforward and make sure you are using at least python 3.6.x and later.
Make sure *pip* setuptool is installed with python package.

Create virtual environment using following commands.

```
$ cd flask-crud-api
$ pip install virtualenv
$ virtualenv env
```

Activate virtual environment.

*Linux or Mac*

```
$ source env/bin/activate
```

OR

*Windows*

```
$ env\Scripts\activate
```

Install dependencies/packages.

```
(env) $ pip install -r requirements.txt
```

**Running**

When all dependencies are installed, run the flask application on your local instance.

```
(env) $ python runserver.py
```

Access application by entering *http://127.0.0.1:5000/* or *http://localhost:5000/* url on browser.

**Testing**

Run the tests.

```
(env) $ py.test tests/ --cov src --cov-report term-missing
```

*Note: Test cases are pending for this application.*

**For style guide enforcement (flake8)**

```
(env) $ flake8 src/ tests/
```

**Swagger**

[Swagger specification](/spec)

**References**

* [Python](https://www.python.org)
* [Flask](http://flask.pocoo.org)
* [SQLAlchemy](https://www.sqlalchemy.org)
* [Flake8](http://flake8.pycqa.org)
