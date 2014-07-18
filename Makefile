## pynames Makefile
## Copyright (C) 2014 Petri Heinilä, LGPL 2.1

include INFO

RMALL = rm -rf
PIP3 = pip3
PEP8 = pep8 --first --show-source --show-pep8
PYLINT = pylint  --rcfile=setup.cfg

cache = ./build
pycaches = $(shell find . -name __pycache__) 

##############################################################################

.PHONY: install develop test clean public_html ghpages

help::
	@echo Targets:
	@echo "  install     - install files into $(prefix)"
	@echo "  develop     - install as development mode (symlinks)"
	@echo "  clean       - clean generated build files"
	@echo "  pep8        - check PEP8 python code style"
	@echo "  lint        - check pytcon code style and correcteness"
	@echo "  style       - python code checks"

install:
	$(PIP3) install -r requirements.txt .

develop:
	$(PIP3) install -r requirements-dev.txt -r requirements.txt -e .
	
clean::
	$(RMALL) build
	$(RMALL) dist
	$(RMALL) $(name).egg-info
	$(RMALL) $(pycaches)

pep8::
	$(PEP8) $(name)
	
lint::
	$(PYLINT) $(name)

style:: pep8 lint
