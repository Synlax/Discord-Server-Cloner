.PHONY: build run logs clean

IMAGE_NAME = dexu-cloner

build:
	docker build -t $(IMAGE_NAME) .

run:
	docker run -it --rm --name $(IMAGE_NAME)_container $(IMAGE_NAME)

logs:
	docker logs $(IMAGE_NAME)_container

clean:
	docker stop $(IMAGE_NAME)_container || true
	docker rm -f $(IMAGE_NAME)_container || true
	docker rmi -f $(IMAGE_NAME) || true    