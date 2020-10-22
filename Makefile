
.PHONY: clean-pyc clean-build docs

help:
	@echo "clean-build - remove build artifacts"
	@echo "clean-pyc - remove Python file artifacts"
	@echo "lint - check style with flake8"
	@echo "test - run tests quickly with the default Python"
	@echo "testall - run tests on every Python version with tox"
	@echo "coverage - check code coverage quickly with the default Python"
	@echo "docs - generate Sphinx HTML documentation, including API docs"
	@echo "release - package and upload a release"
	@echo "sdist - package"

clean: clean-build clean-pyc

clean-build:
	rm -fr build/
	rm -fr dist/
	rm -fr *.egg-info

clean-pyc:
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +

clean-docs:
	rm -rf docs/_build/

lint:
	flake8 wrdrd tests

test:
	python setup.py test

test-all:
	tox

coverage:
	coverage run --source wrdrd setup.py test
	coverage report -m
	coverage html
	open htmlcov/index.html

install:
	pip install -r requirements-dev.txt -r requirements.txt -r requirements-docs.txt


BUILDDIR:=docs/_build
BUILDDIRHTML:=${BUILDDIR}/html
BUILDDIRSINGLEHTML:=${BUILDDIR}/singlehtml
STATIC:=docs/_static
LOCALJS=$(STATIC)/js/local.js

localjs:
	echo '' > $(LOCALJS)
	cat $(STATIC)/js/ga.js >> $(LOCALJS)
	cat $(STATIC)/js/newtab.js >> $(LOCALJS)
	cat $(STATIC)/js/sidenav-affix.js >> $(LOCALJS)
	cat $(STATIC)/js/jquery.scrollTo.js >> $(LOCALJS)
	cat $(STATIC)/js/jquery.isonscreen.js >> $(LOCALJS)
	cat $(STATIC)/js/sidenav-scrollto.js >> $(LOCALJS)

LOCALCSS=$(STATIC)/css/local.css
localcss:
	echo '' > $(LOCALCSS)
	cat $(STATIC)/css/custom.css >> $(LOCALCSS)
	cat $(STATIC)/css/sidenav-scrollto.css >> $(LOCALCSS)
	cat $(STATIC)/css/leftnavbar.css >> $(LOCALCSS)

localjs-live:
	$(MAKE) localjs
	cp -v ${LOCALJS} ${BUILDDIRHTML}/_static/js/local.js  || true;
	cp -v ${LOCALJS} ${BUILDDIRSINGLEHTML}/_static/js/local.js  || true;


localcss-live:
	$(MAKE) localcss
	cp -v ${LOCALCSS} ${BUILDDIRHTML}/_static/css/local.css || true;
	cp -v ${LOCALCSS} ${BUILDDIRSINGLEHTML}/_static/css/local.css || true;

local-live:
	$(MAKE) localjs-live
	$(MAKE) localcss-live

docs-api:
	rm -f docs/wrdrd/wrdrd.rst
	rm -f docs/wrdrd/wrdrd.*.rst
	sphinx-apidoc -T -M -o docs/wrdrd/ wrdrd

docs: clean-docs docs-api localjs localcss
	SPHINX_HTML_LINK_SUFFIX='' $(MAKE) -C docs html singlehtml
	#$(MAKE) -C docs singlehtml
	$(MAKE) docs-notify

docs-notify:
	$(shell (hash notify-send \
		&& notify-send -t 30000 "docs build complete." "${PWD}/${BUILDDIRHTML}") || true)

docs_tools_submodule:
	git -C docs/tools/ pull origin master

docs_tools_submodule_upgrade: docs_tools_submodule
	git commit docs/tools -m "DOC: docs/tools: pull latest: $(shell git -C docs/tools rev-parse --short HEAD)"

docs-tools: docs_tools_submodule_upgrade docs

docs-tools-clone:
	test -d ./docs/tools && rmdir ./docs/tools || true
	git clone https://github.com/westurner/tools ./docs/tools

docs-open: docs open


open:
	@#pip install websh.py
	web './${BUILDDIRHTML}/index.html'
	#web ./${BUILDDIRSINGLEHTML}/index.html

PGS_PORT:=8082
open-pgs:
	web 'http://localhost:${PGS_PORT}'

release: clean
	python setup.py sdist upload

sdist: clean
	python setup.py sdist
	ls -l dist

docs-singlehtml:
	$(MAKE) -C ./docs singlehtml
	$(MAKE) docs-mv-singlehtml

docs-mv-singlehtml:
	test -d '${BUILDDIRSINGLEHTML}' && ( \
		mv '${BUILDDIRSINGLEHTML}' '${BUILDDIRHTML}/singlehtml' && \
		ln -s '${BUILDDIRHTML}/singlehtml' '${BUILDDIRSINGLEHTML}' \
	;)  || echo true

singlehtml: ${BUILDDIRHTML}/singlehtml

gh-pages: docs-mv-singlehtml
	# Push docs to gh-pages branch with a .nojekyll file
	ghp-import -n -p '${BUILDDIRHTML}'
	#ghp-import -n -p ./${BUILDDIRSINGLEHTML}

pull:
	git pull

push:
	git push

setup-docs:
	pip install pgs
	pip install -r ./requirements-docs.txt

setup-dev:
	# sudo dnf install gcc python-devel
	# sudo apt-get install gcc python-dev
	pip install -r ./requirements-dev.txt

pgs:
	# Serve locally built HTML over HTTP (with try_files $1.html)
	pgs -p '${BUILDDIRHTML}' -P '${PGS_PORT}'

pgs-gh-pages:
	# Serve gh-pages branch over HTTP (with try_files $1.html)
	pgs -g '${PWD}' -r gh-pages -P '${PGS_PORT}'

serve: serve-fs

serve-fs:
	$(MAKE) pgs PGS_PORT=8082

serve-gh-pages:
	$(MAKE) pgs-gh-pages

serve:
	$(MAKE) pgs PGS_PORT=8082
	$(MAKE) pgs-gh-pages PGS_PORT=8083
