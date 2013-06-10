PYTHON=`which python`
NAME=`python setup.py --name`
NAME_UNDERSCORE=`python setup.py --name | tr '-' '_'`
VERSION=`python setup.py --version`

all: egg
dist: build deb egg

init:
		@echo "Installing requirements..."
		@pip install -r requirements.txt --use-mirrors

build:
		@echo "Making a source tarball..."
		@$(PYTHON) setup.py sdist

deb:
		@echo "Making a deb package..."
		@$(PYTHON) setup.py --command-packages=stdeb.command bdist_deb

egg:
		@echo "Making an egg..."
		@$(PYTHON) setup.py bdist_egg

install:
		@echo "Installing..."
		@$(PYTHON) setup.py install --install-layout=deb

.PHONY: clean

clean:
		@$(PYTHON) setup.py clean
		@rm -rf build dist $(NAME_UNDERSCORE).egg-info
		@find . -name '*.pyc' -delete
