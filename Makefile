SHELL := /bin/zsh
.SHELLFLAGS := -c
up:
	source ~/.zshr && \
	workon erb7
	python manage.py runserver

static:
	python manage.py collectstatic
