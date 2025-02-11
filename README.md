<a href="https://www.breatheco.de"><img height="250" align="right" margin-top="90" src="https://github.com/4GeeksAcademy/fastapi-rest-hello/blob/main/docs/assets/fastapi.jpg?raw=true"></a>

# FastAPI Template for Junior Developers

Create APIs with FastAPI in minutes, [📹 watch the video tutorial](https://youtu.be/ORxQ-K3BzQA).

- [Extensive documentation here](https://fastapi.tiangolo.com/).
- Integrated with Pipenv for package management.
- Quick deployment to Render.com with `$ pipenv run deploy`.
- Use of the `.env` file for configuration.
- Integration of SQLAlchemy for database abstraction.

## 1) Installation

> Important: The template is made for Python 3.10, but you can change the version in the `Pipfile`.

The following steps are automatically executed if you use Codespaces. If you are doing a local installation, you must run them manually:

```sh
pipenv install
psql -U root -c 'CREATE DATABASE example;'
pipenv run init
pipenv run migrate
pipenv run upgrade
```

## 2) How to start coding

There is a sample API running with a sample database. All your application code should be written inside the `./src/` folder.

- `src/app.py` (this is where you should code your endpoints with FastAPI)  
- `src/models.py` (your database tables and serialization logic using SQLAlchemy)  
- `src/utils.py` (some reusable classes and functions)  
- `src/admin.py` (FastAPI Admin configuration to easily manage data)  

For a more detailed explanation, look for the tutorial inside the `docs` folder.

## Remember to migrate every time you change your models

You must migrate and update the migrations for each update you make to your models:

```bash
$ pipenv run migrate # (to create the migrations)
$ pipenv run upgrade  # (to update your database with the migrations)
```

## Check your API live

Once you run the command `pipenv run start`, your API will start running live and you can open it in your browser. 
FastAPI automatically generates interactive documentation at `/docs` and `/redoc`.

## Publish/Deploy your API!

This template is 100% ready to be deployed with Render.com in a matter of minutes.  
Please read the [official documentation about it](https://fastapi.tiangolo.com/deployment/).

## Contributors

This template was built as part of the [Coding Bootcamp](https://4geeksacademy.com/us/coding-bootcamp) at 4Geeks Academy by [Alejandro Sanchez](https://twitter.com/alesanchezr) and many other contributors. Learn more about our [Full Stack Developer Course](https://4geeksacademy.com/us/coding-bootcamps/part-time-full-stack-developer) and [Data Science Bootcamp](https://4geeksacademy.com/us/coding-bootcamps/datascience-machine-learning). You can find other templates and resources like this on the [school's GitHub page](https://github.com/4geeksacademy/).
