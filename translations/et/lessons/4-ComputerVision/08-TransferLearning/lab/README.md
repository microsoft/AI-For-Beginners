# Oxfordi lemmikloomade klassifitseerimine ülekandeõppe abil

Laboriülesanne [AI for Beginners Curriculum](https://github.com/microsoft/ai-for-beginners) programmist.

## Ülesanne

Kujutle, et pead looma rakenduse lemmikloomade päevahoiu jaoks, et kataloogida kõik lemmikloomad. Üks sellise rakenduse suurepäraseid funktsioone oleks tõu automaatne tuvastamine fotolt. Selles ülesandes kasutame ülekandeõpet, et klassifitseerida päriselu lemmikloomade pilte [Oxford-IIIT](https://www.robots.ox.ac.uk/~vgg/data/pets/) lemmikloomade andmestikust.

## Andmestik

Kasutame algset [Oxford-IIIT](https://www.robots.ox.ac.uk/~vgg/data/pets/) lemmikloomade andmestikku, mis sisaldab 35 erinevat koera- ja kassitõugu.

Andmestiku allalaadimiseks kasuta järgmist koodilõiku:

```python
!wget https://www.robots.ox.ac.uk/~vgg/data/pets/data/images.tar.gz
!tar xfz images.tar.gz
!rm images.tar.gz
```

## Märkmiku avamine

Alusta laborit, avades [OxfordPets.ipynb](OxfordPets.ipynb)

## Õppetunnid

Ülekandeõpe ja eelnevalt treenitud võrgud võimaldavad meil lahendada päriselu pildiklassifikatsiooni probleeme suhteliselt lihtsalt. Siiski töötavad eelnevalt treenitud võrgud hästi sarnaste piltide puhul, ja kui hakkame klassifitseerima väga erinevaid pilte (nt meditsiinilised pildid), on tõenäoline, et tulemused on palju kehvemad.

---

**Lahtiütlus**:  
See dokument on tõlgitud AI tõlketeenuse [Co-op Translator](https://github.com/Azure/co-op-translator) abil. Kuigi püüame tagada täpsust, palume arvestada, et automaatsed tõlked võivad sisaldada vigu või ebatäpsusi. Algne dokument selle algses keeles tuleks pidada autoriteetseks allikaks. Olulise teabe puhul soovitame kasutada professionaalset inimtõlget. Me ei vastuta selle tõlke kasutamisest tulenevate arusaamatuste või valesti tõlgenduste eest.