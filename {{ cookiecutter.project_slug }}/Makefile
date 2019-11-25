include .env

run:
	( \
		source .venv/skill_env/bin/activate; \
		python -m invoke -p run $(d); \
	)


test:
	( \
		source .venv/skill_env/bin/activate; \
		python manage.py test; \
	)
