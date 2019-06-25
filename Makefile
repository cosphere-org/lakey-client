# Makefile

include .lily/lily_assistant.makefile


deploy_to_pypi:
	python setup.py sdist && \
	twine upload dist/*
