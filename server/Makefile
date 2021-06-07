#SERVER
NAME=mlserver
include ../settings.mk
ALL: Dockerfile
	make .hostExtras
	docker build -t $(PROJ)/$(NAME) .
run:
	docker network create --subnet=$(IPA).$(IPB).0.0/16 $(PROJ)_net
	docker run -t --net $(PROJ)_net --ip $(IPA).$(IPB).0.$(SERV_IPD) --privileged=true --name $(PROJ)_$(NAME) $(PROJ)/$(NAME) 

clean:
	-docker kill $(PROJ)_$(NAME)
	-docker kill $(PROJ)_mlbridge
	-docker rm $(PROJ)_$(NAME)
	-docker network rm $(PROJ)_net
	-make .generalClean
