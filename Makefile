PY=python
PELICAN=pelican
PELICANOPTS=

BASEDIR=$(CURDIR)
INPUTDIR=$(BASEDIR)/content
OUTPUTDIR=$(BASEDIR)/../sets-output
CONFFILE=$(BASEDIR)/pelicanconf.py
PUBLISHCONF=$(BASEDIR)/publish.py

GITHUB_PAGES_BRANCH=gh-pages

DEBUG ?= 0
ifeq ($(DEBUG), 1)
	PELICANOPTS += -D
endif

help:
	@echo 'Makefile for a pelican Web site                                        			'
	@echo '                                                                       			'
	@echo 'Usage:                                                                 			'
	@echo '   make html                        (re)generate the web site (localhost)		'
	@echo '   make publish                     generate whole page using production settings (github) && push it to gh-branch'
	@echo '   make serve [PORT=8000]           serve site at http://localhost:8000			'
	@echo '   make devserver [PORT=8000]       start/restart develop_server.sh    			'
	@echo '   make stopserver                  stop local server                  			'
	@echo '                                                                       			'
	@echo 'Set the DEBUG variable to 1 to enable debugging, e.g. make DEBUG=1 html			'
	@echo '                                                                       			'

html:
	$(PELICAN) $(INPUTDIR) -o $(OUTPUTDIR) -s $(CONFFILE) $(PELICANOPTS)

publish:
	$(PELICAN) $(INPUTDIR) -o $(OUTPUTDIR) -s $(PUBLISHCONF) $(PELICANOPTS)
	cd $(OUTPUTDIR) && git add . -A && git commit -m "site update from master branch" && git push origin gh-pages && cd $(BASEDIR)

serve:
ifdef PORT
	cd $(OUTPUTDIR) && $(PY) -m pelican.server $(PORT)
else
	cd $(OUTPUTDIR) && $(PY) -m pelican.server
endif

devserver:
ifdef PORT
	$(BASEDIR)/develop_server.sh restart $(PORT)
else
	$(BASEDIR)/develop_server.sh restart
endif

stopserver:
	kill -9 `cat pelican.pid`
	kill -9 `cat srv.pid`
	@echo 'Stopped Pelican and SimpleHTTPServer processes running in background.'

.PHONY: help publish html serve devserver
