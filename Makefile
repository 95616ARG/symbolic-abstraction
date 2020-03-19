.PHONY: docker-test docker-bash docker-image

IMAGE_NAME=symbolic_abstraction

docker-test: docker-image
	docker run --rm -w /app $(IMAGE_NAME) python3 -m pytest tests

docker-bash:
	docker run -it $(IMAGE_NAME) /bin/bash

docker-image:
	docker build --force-rm -t $(IMAGE_NAME) .
