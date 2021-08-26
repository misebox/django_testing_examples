.PHONY: all
all:

requirements.txt: requirements.in
	$(MAKE) req

.PHONY: requirements
req:
	docker run --rm -it -v "$(CURDIR):/src" misebox/pip-tools
