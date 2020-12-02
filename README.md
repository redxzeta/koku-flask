# koku-flask

1. Install poetry https://python-poetry.org/docs/

1. `poetry install` to install dependencies

1. simple backend for one of my projects to handle data 

1. `pip install python python-dotenv`

1. create `.env` 
    ```
    MONGOUSER = SOMEUSERNAME
    PASS = SOMEDANKPASSWORD
    DB_NAME = SOMEDBNAME
   ```

1.  alternative in Pycharm edit config -> env variables

1. Set up procfile, replace $1 w/ the name of your main flask app

`$ echo "web: gunicorn app:$1" >> Procfile`

1. create `requirements.txt`

`poetry export -f requirements.txt --output requirements.txt`

1. heroku deployment
```
heroku login
heroku create
git push heroku master
```