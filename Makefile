buildkit:
	DOCKER_BUILDKIT=1 docker build -t whatsappMessanger .

build:
	docker build -t whatsappMessanger .

clean_docker:
	docker rm --force whatsappMessanger
