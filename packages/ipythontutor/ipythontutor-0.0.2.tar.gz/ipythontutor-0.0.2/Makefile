all: readme

readme: README.md

README.md: README.ipynb
	jupyter nbconvert --to markdown README.ipynb

pypi:
	python setup.py sdist upload

testpypi: 
	./setup.py sdist upload -r testpypi
