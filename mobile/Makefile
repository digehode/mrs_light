#Mobile App
NAME=mlapp
include ../settings.mk
ALL: Dockerfile
	make .hostExtras
	docker build -t $(PROJ)/$(NAME) .
run:
	docker run -i -t --net $(PROJ)_net --ip $(IPA).$(IPB).0.$(MOB_IPD) --privileged=true --name $(PROJ)_$(NAME) $(PROJ)/$(NAME) 

clean:
	-docker kill $(PROJ)_$(NAME)
	-docker rm $(PROJ)_$(NAME)
	-make .generalClean
