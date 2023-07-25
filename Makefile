PHONY: \
	__build_test_image \
	clean \
	format-code \
	lint \
	test \
	update-and-lock-requirements

__build_test_image:
	docker build -f .docker/test.Dockerfile -t cracking-coding-test .

clean:
	rm -rf .pytest_cache
	rm -rf .mypy_cache
	find . -name '__pycache__' -exec rm -rf {} +
	find . -name '*.pyc' -delete

format-code: __build_test_image
	docker run \
		-v $(shell pwd):/src \
		-u $$(stat -c "%u:%g" $(shell pwd)) \
		cracking-coding-test \
		black .

lint: __build_test_image
	docker run \
		-v $(shell pwd):/src \
		-u $$(stat -c "%u:%g" $(shell pwd)) \
		cracking-coding-test \
		black --check .
	docker run \
		-v $(shell pwd):/src \
		-u $$(stat -c "%u:%g" $(shell pwd)) \
		cracking-coding-test \
		flake8

test: __build_test_image
	docker run \
		-v $(shell pwd):/src \
		-u $$(stat -c "%u:%g" $(shell pwd)) \
		cracking-coding-test \
    pytest --cov-report term-missing --cov=solutions

update-and-lock-requirements: __build_test_image
	rm requirements-lock.txt
	cp requirements.txt requirements-lock.txt
	docker run \
		-v $(shell pwd):/src \
		-u $$(stat -c "%u:%g" $(shell pwd)) \
		cracking-codgin-test \
		lock requirements-lock.txt
