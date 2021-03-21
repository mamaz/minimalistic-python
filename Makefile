TEST_PATH=$(shell pwd)/example/tests/*.py

test:
	pytest ${TEST_PATH}
