## libs: pip install

all: test

libs:
	@pip install -r requirements.txt

requirements.txt: requirements.in
	@$(MAKE) req

## req:  compile requirements.in into requirements.txt
req:
	@docker run --rm -it -v "$(CURDIR):/src" misebox/pip-tools

## test: mypy and unittest
.PHONY: test
test: mypy unittest

.PHONY: mypy
mypy:
	@mypy .

.PHONY: unittest
unittest:
	@python manage.py test  # --parallel

## dev:  run dev server
.PHONY: dev
dev:
	@python manage.py runserver

## help: output this text
help:
	@cat Makefile | egrep '^##'

