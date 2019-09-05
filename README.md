# Django Alexa Template


This is a [Alexa](https://developer.amazon.com/it/alexa) skill boilerplate using [Django](https://docs.djangoproject.com) project as local web service and [ngrok](https://ngrok.com/) to expose the local server behind NATs and firewalls to the public internet over secure tunnels.

## Documentation
  - [Basic requirements](#basic-requirements)
  - [Initialization](#initialization)
  - [Usage](#usage)


## Basic requirements

**[ngrok](https://ngrok.com/)** and **[ask-cli](https://developer.amazon.com/es/docs/smapi/quick-start-alexa-skills-kit-command-line-interface.html)** must be installed before initializing the project.

**[cookiecutter](https://github.com/cookiecutter/cookiecutter)** is required to clone this boilerplate.


## Initialization

Use cookiecutter to clone the boilerplate:

```shell
$ cookiecutter https://github.com/20tab/django-alexa-template
```

## Usage

Only one command to deploy and test your skill using your local web server.

To run without deploy your skill:

```shell
$ make run
```

If skill changes you need to deploy it. To simplify this process you can use:

```shell
$ make run d=--deploy
```

In every case the terminal will show django runserver logs:

```shell
Performing system checks...

System check identified no issues (0 silenced).
September 05, 2019 - 11:15:11
Django version 2.2.5, using settings 'myskill.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
```

