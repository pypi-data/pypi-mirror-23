version = $(shell python setup.py --version | tail -1)

all:
	python setup.py sdist

clean:
	rm -f itm_wrap.c* itm.cpp itm*.so
	rm -rf build __pycache__

sdist:
	python setup.py sdist

release:
	python setup.py sdist
	python setup.py bdist_wheel
	twine upload dist/itm-$(version).tar.gz
	twine upload dist/itm-$(version)*.whl

fresh: clean all

.PHONY: all clean fresh sdist
