PROJ=mrslight
IPA=174
IPB=27
SERV_IPD=20
BR_IPD=21
MOB_IPD=4
.generalClean:
	-rm hostExtras
.hostExtras:
	echo "$(IPA).$(IPB).0.$(SERV_IPD)	$(PROJ)_server" > hostExtras
	echo "$(IPA).$(IPB).0.$(BR_IPD)	$(PROJ)_br" >> hostExtras
	echo "$(IPA).$(IPB).0.$(MOB_IPD)	$(PROJ)_mob" >> hostExtras

