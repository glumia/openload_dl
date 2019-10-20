clean:
	@ find . -type d -name '__pycache__' -exec rm -rf {} +
	@ rm -rf build dist *.egg-info .egg
	@ rm -f *.log *.mp4


lint:
	@ black .
	@ flake8 --config=.flake8


publish:
	python setup.py sdist bdist_wheel
	twine upload dist/*
	rm -fr build dist .egg *.egg-info
