# Eettinen ja vastuullinen tekoäly

Olet melkein suorittanut tämän kurssin, ja toivon, että tähän mennessä näet selvästi, että tekoäly perustuu useisiin muodollisiin matemaattisiin menetelmiin, jotka mahdollistavat suhteiden löytämisen datasta ja mallien kouluttamisen jäljittelemään joitakin ihmisen käyttäytymisen piirteitä. Tässä historian vaiheessa pidämme tekoälyä erittäin voimakkaana työkaluna, joka auttaa meitä löytämään kaavoja datasta ja soveltamaan niitä uusien ongelmien ratkaisemiseen.

## [Pre-lecture quiz](https://white-water-09ec41f0f.azurestaticapps.net/quiz/5/)

Tieteiskirjallisuudessa näemme kuitenkin usein tarinoita, joissa tekoäly muodostaa uhkan ihmiskunnalle. Yleensä nämä tarinat keskittyvät jonkinlaiseen tekoälyn kapinaan, jossa tekoäly päättää vastustaa ihmisiä. Tämä viittaa siihen, että tekoälyllä olisi tunteita tai kyky tehdä päätöksiä, joita sen kehittäjät eivät ole ennakoineet.

Tekoäly, josta olemme oppineet tällä kurssilla, ei ole mitään muuta kuin suurta matriisilaskentaa. Se on erittäin tehokas työkalu, joka auttaa meitä ratkaisemaan ongelmiamme, ja kuten mikä tahansa muu voimakas työkalu - sitä voidaan käyttää sekä hyviin että huonoihin tarkoituksiin. Tärkeää on, että sitä voidaan myös *väärinkäyttää*.

## Vastuullisen tekoälyn periaatteet

Jotta voisimme välttää tekoälyn tahattoman tai tarkoituksellisen väärinkäytön, Microsoft on määritellyt tärkeät [Vastuullisen tekoälyn periaatteet](https://www.microsoft.com/ai/responsible-ai?WT.mc_id=academic-77998-cacaste). Näitä periaatteita tukevat seuraavat käsitteet:

* **Reiluus** liittyy tärkeään ongelmaan, joka koskee *mallin vinoumia*, joita voi syntyä, kun koulutuksessa käytetään vinoutunutta dataa. Esimerkiksi, kun yritämme ennustaa henkilön mahdollisuutta saada ohjelmistokehittäjän työpaikka, malli saattaa suosia miehiä enemmän - vain siksi, että koulutusdata on todennäköisesti ollut vinoutunut miespuolisen yleisön suuntaan. Meidän täytyy huolellisesti tasapainottaa koulutusdataa ja tutkia mallia vinoumien välttämiseksi sekä varmistaa, että malli ottaa huomioon olennaisemmat ominaisuudet.
* **Luotettavuus ja turvallisuus**. Luonteensa vuoksi tekoälymallit voivat tehdä virheitä. Neuroverkko palauttaa todennäköisyyksiä, ja meidän täytyy ottaa tämä huomioon päätöksiä tehdessämme. Jokaisella mallilla on tietty tarkkuus ja palautuskyky, ja meidän täytyy ymmärtää tämä estääksemme haitat, joita väärät neuvot voivat aiheuttaa.
* **Yksityisyys ja turvallisuus** sisältävät tekoälyyn liittyviä erityisiä näkökohtia. Esimerkiksi, kun käytämme dataa mallin kouluttamiseen, tämä data tulee jollain tavalla "integroiduksi" malliin. Toisaalta tämä lisää turvallisuutta ja yksityisyyttä, mutta toisaalta meidän täytyy muistaa, millä datalla malli on koulutettu.
* **Osallisuus** tarkoittaa, että emme rakenna tekoälyä korvaamaan ihmisiä, vaan pikemminkin täydentämään ihmisiä ja tekemään työstämme luovempaa. Tämä liittyy myös reiluuteen, koska käsitellessämme aliedustettuja yhteisöjä, suurin osa keräämästämme datasta on todennäköisesti vinoutunutta, ja meidän täytyy varmistaa, että nämä yhteisöt otetaan mukaan ja käsitellään oikein tekoälyn avulla.
* **Läpinäkyvyys**. Tämä sisältää sen varmistamisen, että olemme aina selkeitä tekoälyn käytöstä. Lisäksi, missä tahansa mahdollista, haluamme käyttää tekoälyjärjestelmiä, jotka ovat *tulkittavissa*.
* **Vastuullisuus**. Kun tekoälymallit tekevät päätöksiä, ei aina ole selvää, kuka on vastuussa näistä päätöksistä. Meidän täytyy varmistaa, että ymmärrämme, missä tekoälyn päätösten vastuu sijaitsee. Useimmissa tapauksissa haluamme sisällyttää ihmisiä tärkeiden päätösten tekemiseen, jotta todelliset ihmiset voidaan asettaa vastuuseen.

## Työkalut vastuulliseen tekoälyyn

Microsoft on kehittänyt [Responsible AI Toolbox](https://github.com/microsoft/responsible-ai-toolbox)-työkalupaketin, joka sisältää joukon työkaluja:

* Tulkittavuuden hallintapaneeli (InterpretML)
* Reiluuden hallintapaneeli (FairLearn)
* Virheanalyysin hallintapaneeli
* Vastuullisen tekoälyn hallintapaneeli, joka sisältää

   - EconML - työkalu kausaalianalyysiin, joka keskittyy "mitä jos" -kysymyksiin
   - DiCE - työkalu kontrafaktuaalianalyysiin, joka mahdollistaa sen näkemisen, mitkä ominaisuudet täytyy muuttaa mallin päätöksen vaikuttamiseksi

Lisätietoja tekoälyn etiikasta löydät [tästä oppitunnista](https://github.com/microsoft/ML-For-Beginners/tree/main/1-Introduction/3-fairness?WT.mc_id=academic-77998-cacaste), joka sisältyy koneoppimisen opetussuunnitelmaan ja sisältää tehtäviä.

## Kertaus ja itseopiskelu

Suorita tämä [Learn Path](https://docs.microsoft.com/learn/modules/responsible-ai-principles/?WT.mc_id=academic-77998-cacaste) oppiaksesi lisää vastuullisesta tekoälystä.

## [Post-lecture quiz](https://white-water-09ec41f0f.azurestaticapps.net/quiz/6/)

---

**Vastuuvapauslauseke**:  
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, huomioithan, että automaattiset käännökset voivat sisältää virheitä tai epätarkkuuksia. Alkuperäinen asiakirja sen alkuperäisellä kielellä tulisi pitää ensisijaisena lähteenä. Kriittisen tiedon osalta suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa väärinkäsityksistä tai virhetulkinnoista, jotka johtuvat tämän käännöksen käytöstä.