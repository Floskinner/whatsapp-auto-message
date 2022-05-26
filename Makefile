buildkit:
	DOCKER_BUILDKIT=1 docker build -t whatsapp-messanger .

build:
	docker build -t whatsapp-messanger .

clean_docker:
	docker rm --force whatsapp-messanger
