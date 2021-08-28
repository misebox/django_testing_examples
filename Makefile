.PHONY: all
all:

libs:
	@pip install -r requirements.txt

requirements.txt: requirements.in
	@$(MAKE) req

.PHONY: requirements
req:
	@docker run --rm -it -v "$(CURDIR):/src" misebox/pip-tools

.PHONY: test
test: mypy unittest

.PHONY: mypy
mypy:
	@mypy .

.PHONY: unittest
unittest:
	@python manage.py test
