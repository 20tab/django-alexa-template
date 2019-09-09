"""Define invoke tasks."""

import getpass
import os
import sys
import json
from pathlib import Path
from {{ cookiecutter.project_slug }}.settings import DEBUG

# import dj_database_url
# from django.core.management.utils import get_random_secret_key
# from dotenv import find_dotenv, load_dotenv
from invoke import task
import requests
from requests.exceptions import ConnectionError
import pprint


@task
def run(c, deploy=False):
    set_skill_json()
    if deploy:
        c.run("ask deploy")
    if DEBUG:
        c.run("python manage.py runserver")


def get_public_urls():
    try:
        res = {}
        ngrok_data = requests.get("http://127.0.0.1:4040/api/tunnels").json()
        for t in ngrok_data['tunnels']:
            res[t['proto']] = t['public_url']
        return res
    except ConnectionError:
        print("Please run ngrok first of all")
        exit(0)


def set_skill_json():
    """
    Read ngrok apis to check public url and change it in endpoint key in skill.json file.
    Return True if endpoint is changed else False.
    """
    if DEBUG:
        endpoint = {
            "uri": f"{get_public_urls()['https']}/alexa/",
            "sslCertificateType": "Wildcard"
        }
    else:
        endpoint = {
            "sourceDir": "alexa/lambda_upload",
            "uri": "ask-custom-{{ cookiecutter.project_slug }}"
        }
    if DEBUG:
        config = None
        with open(".ask/config", "r") as f:
            config = json.loads(f.read())
            try:
                config["deploy_settings"]["default"]["resources"].pop("lambda", None)
            except KeyError:
                config = None
        if config:
            with open(".ask/config", "w") as f:
                f.write(json.dumps(config, indent=2))
    else:
        config = None
        with open(".ask/config", "r") as f:
            config = json.loads(f.read())
            try:
                lambda_ref = [
                    {
                        "functionName": "",
                        "alexaUsage": [
                            "custom/default"
                        ],
                        "runtime": "python3.6",
                        "handler": "skill.handler"
                    }
                ]
                config["deploy_settings"]["default"]["resources"]["lambda"] = lambda_ref
            except KeyError:
                config = None
        if config:
            with open(".ask/config", "w") as f:
                f.write(json.dumps(config, indent=2))
    with open("skill.json", "r") as f:
        skill_json = json.loads(f.read())

    if skill_json["manifest"]["apis"]["custom"]["endpoint"] != endpoint:
        skill_json["manifest"]["apis"]["custom"]["endpoint"] = endpoint
        with open("skill.json", "w") as f:
            f.write(json.dumps(skill_json, indent=2))
            return True
    return False


# NOTE: originally cribbed from fab 1's contrib.console.confirm
def confirm(question, assume_yes=True):
    """
    Ask user a yes/no question and return their response as a boolean.

    ``question`` should be a simple, grammatically complete question such as
    "Do you wish to continue?", and will have a string similar to ``" [Y/n] "``
    appended automatically. This function will *not* append a question mark for
    you.

    By default, when the user presses Enter without typing anything, "yes" is
    assumed. This can be changed by specifying ``affirmative=False``.

    .. note::
        If the user does not supplies input that is (case-insensitively) equal
        to "y", "yes", "n" or "no", they will be re-prompted until they do.

    :param str question: The question part of the input.
    :param bool assume_yes:
        Whether to assume the affirmative answer by default. Default value:
        ``True``.

    :returns: A `bool`.
    """
    # Set up suffix
    if assume_yes:
        suffix = "Y/n"
    else:
        suffix = "y/N"
    # Loop till we get something we like
    # TODO: maybe don't do this? It can be annoying. Turn into 'q'-for-quit?
    while True:
        # TODO: ensure that this is Ctrl-C friendly, ISTR issues with
        # raw_input/input on some Python versions blocking KeyboardInterrupt.
        response = input("{0} [{1}] ".format(question, suffix))
        response = response.lower().strip()  # Normalize
        # Default
        if not response:
            return assume_yes
        # Yes
        if response in ["y", "yes"]:
            return True
        # No
        if response in ["n", "no"]:
            return False
        # Didn't get empty, yes or no, so complain and loop
        err = "I didn't understand you. Please specify '(y)es' or '(n)o'."
        print(err, file=sys.stderr)
