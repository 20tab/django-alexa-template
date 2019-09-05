import os


def create_virtualenv():
    os.system("cp .env.tpl .env")
    os.mkdir(".venv")
    os.system("virtualenv .venv/skill_env")
    os.system(".venv/skill_env/bin/pip install -r requirements.txt")


def initialize():
    os.system(".venv/skill_env/bin/python manage.py migrate")


create_virtualenv()
initialize()
