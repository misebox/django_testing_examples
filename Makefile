.PHONY: all
all:

libs:
	@pip install -r requirements.txt

requirements.txt: requirements.in
	@$(MAKE) req

.PHONY: requirements
req:
	@docker run --rm -it -v "$(CURDIR):/src" misebox/pip-tools

.PHONY: mypy
mypy:
	@mypy .

test:
	@python manage.py test
