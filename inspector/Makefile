NAME=inspector
include ../settings.mk
ALL: Dockerfile 
	make .hostExtras
	docker build -t $(PROJ)/$(NAME) .

run_mobile:
	docker run  --net container:$(PROJ)_mlapp -it --privileged=true --ip $(IPA).$(IPB).0.$(MOB_IPD)  --name $(PROJ)_$(NAME)   $(PROJ)/$(NAME)

run_server:
	docker run  --net container:$(PROJ)_mlserver -it --privileged=true --ip $(IPA).$(IPB).0.$(SERV_IPD)  --name $(PROJ)_$(NAME)   $(PROJ)/$(NAME)

run_bridge:
	docker run  --net container:$(PROJ)_mlbridge -it --privileged=true --ip $(IPA).$(IPB).0.$(BR_IPD)  --name $(PROJ)_$(NAME)   $(PROJ)/$(NAME)

clean:
	-docker kill $(PROJ)_$(NAME)
	-docker rm $(PROJ)_$(NAME)
	-make .generalClean
