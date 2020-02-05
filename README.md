# Jumpahead Online
Online platform for JumpAhead program

## Local Development Setup:

### Set up a virutal environment (Optional, but recommended)
Using a virtual environment is beneficial for a variety of reasons, but primarily, it will create a separate python installation for you to use just for this project. This way, the requirements you install won't affect your OS's default python installation.

1. Install [virtualenvwrapper](https://virtualenvwrapper.readthedocs.io/en/latest/install.html): `pip install virutalenvwrapper`
2. Add the following to your shell startup file:
```
export WORKON_HOME=$HOME/.virtualenvs
export PROJECT_HOME=$HOME/Devel
source /usr/local/bin/virtualenvwrapper.sh
```
3. Create a python 3.7 virtualenv: `mkvirtualenv jumpahead --python=python3`
Use `workon jumpahead` to activate your virtual environment, `deactivate` to deactivate

### Clone the repo and install requirements
1. `git clone git@github.com:DersJ/jumpahead.git`
2. `cd jumpahead && pip install -r requirements.txt`

### Set up environment variables
In order to keep the database url and secret key secure, we abstract those values into environment variables. Locally, these will be stored in a file called `.env`. On heroku, they are stored in the `config vars` setting.

1. Create env file: `touch .env`
2. In `.env`, add the `SECRET_KEY` and `DATABASE_URL` from heroku -> jumpahead -> settings -> config vars -> reveal config vars. Also, set `DEBUG=True`
```
SECRET_KEY= ...
DEBUG=True
DATABASE_URL= ...
```

### Run the local dev server
1. In the root of this repo with your virtual environment active, run `python manage.py runserver` 
2. Navigate to [127.0.0.1:8000]() in the browser
