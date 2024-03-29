# Django Alexa Template


This is a [Alexa](https://developer.amazon.com/it/alexa) skill boilerplate using [Django](https://docs.djangoproject.com) project as local web service and [ngrok](https://ngrok.com/) to expose the local server behind NATs and firewalls to the public internet over secure tunnels.

## Documentation
  - [Basic requirements](#basic-requirements)
  - [Initialization](#initialization)
  - [Usage](#usage)


### Basic requirements

- **[ngrok](https://ngrok.com/)** and **[ask-cli](https://developer.amazon.com/es/docs/smapi/quick-start-alexa-skills-kit-command-line-interface.html)** must be installed before initializing the project.

- **[cookiecutter](https://github.com/cookiecutter/cookiecutter)** is required to clone this boilerplate.

- also **[virtualenv](https://virtualenv.pypa.io/en/latest/installation/)** is required, to prepare the virtual environment used by Django 


### Initialization

Use cookiecutter to clone the boilerplate:

```shell
$ cookiecutter https://github.com/20tab/django-alexa-template
```

### Usage

First of all you have to expose your local web server to a public url, using ngrok:

```shell
$ ngrok http 8000
```

Then

```shell
$ cd <skill_dirname>
```

After this run command to deploy and test your skill using your local web server.

To run without deploy your skill:

```shell
$ make run
```

If skill changes you need to deploy it. To simplify this process you can use:

```shell
$ make run d=--deploy
```

> **NOTE**: "make run" command is simply a wrapper using python and ask-cli commands.


In every case the terminal will show django runserver logs:

```shell
Performing system checks...

System check identified no issues (0 silenced).
September 05, 2019 - 11:15:11
Django version 2.2.5, using settings 'myskill.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
```

To run test on your web service, just launch the following command:
```shell
$ make test
```

