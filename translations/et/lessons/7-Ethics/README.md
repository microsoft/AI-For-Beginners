# Eetiline ja vastutustundlik tehisintellekt

Oled peaaegu lõpetanud selle kursuse, ja loodetavasti näed nüüd selgelt, et tehisintellekt põhineb mitmetel formaalsetel matemaatilistel meetoditel, mis võimaldavad meil leida seoseid andmetes ja treenida mudeleid, et jäljendada mõningaid inimkäitumise aspekte. Praegusel ajal peame tehisintellekti väga võimsaks tööriistaks, mis aitab andmetest mustreid välja tuua ja neid mustreid uute probleemide lahendamiseks rakendada.

## [Eelloengu viktoriin](https://white-water-09ec41f0f.azurestaticapps.net/quiz/5/)

Siiski näeme ulmekirjanduses tihti lugusid, kus tehisintellekt kujutab endast ohtu inimkonnale. Tavaliselt keskenduvad need lood mingisugusele tehisintellekti mässule, kus AI otsustab inimestele vastu astuda. See eeldab, et tehisintellektil on mingisugused emotsioonid või et ta suudab teha otsuseid, mida tema arendajad ei osanud ette näha.

Selle kursuse raames õpitud tehisintellekt ei ole midagi muud kui suur maatriksarvutus. See on väga võimas tööriist, mis aitab meil probleeme lahendada, ja nagu iga teine võimas tööriist - seda saab kasutada nii heaks kui ka halbadeks eesmärkideks. Oluline on, et seda saab ka *valesti kasutada*.

## Vastutustundliku tehisintellekti põhimõtted

Et vältida tehisintellekti juhuslikku või tahtlikku väärkasutust, on Microsoft välja toonud olulised [Vastutustundliku tehisintellekti põhimõtted](https://www.microsoft.com/ai/responsible-ai?WT.mc_id=academic-77998-cacaste). Järgnevad mõisted toetavad neid põhimõtteid:

* **Õiglus** on seotud olulise probleemiga, milleks on *mudeli kallutatus*, mis võib tekkida kallutatud andmete kasutamisel mudeli treenimiseks. Näiteks, kui püüame ennustada inimese tõenäosust saada tarkvaraarendaja töökoht, võib mudel eelistada mehi - lihtsalt seetõttu, et treeningandmestik oli tõenäoliselt kallutatud meeste suunas. Peame hoolikalt tasakaalustama treeningandmeid ja uurima mudelit, et vältida kallutatust ning tagada, et mudel arvestab olulisemaid tunnuseid.
* **Usaldusväärsus ja turvalisus**. Oma olemuselt võivad tehisintellekti mudelid teha vigu. Neuraalvõrk tagastab tõenäosusi, ja me peame seda otsuste tegemisel arvesse võtma. Igal mudelil on teatud täpsus ja tagasikutsumine, ning me peame seda mõistma, et vältida kahju, mida valed soovitused võivad põhjustada.
* **Privaatsus ja turvalisus** omavad tehisintellekti spetsiifilisi mõjusid. Näiteks, kui kasutame treeningmudeli jaoks mõningaid andmeid, muutuvad need andmed mingil määral mudelisse "integreerituks". Ühelt poolt suurendab see turvalisust ja privaatsust, teisalt peame meeles pidama, milliste andmetega mudel treeniti.
* **Kaasatus** tähendab, et me ei loo tehisintellekti selleks, et inimesi asendada, vaid pigem selleks, et inimesi täiendada ja muuta meie töö loovamaks. See on seotud ka õiglusega, sest kui tegeleme alahinnatud kogukondadega, on enamik kogutud andmestikest tõenäoliselt kallutatud, ja peame tagama, et need kogukonnad on kaasatud ja tehisintellekt käsitleb neid õigesti.
* **Läbipaistvus**. See hõlmab tagamist, et oleme alati selged tehisintellekti kasutamise osas. Samuti, kus võimalik, tahame kasutada tehisintellekti süsteeme, mis on *tõlgendatavad*.
* **Vastutus**. Kui tehisintellekti mudelid teevad otsuseid, ei ole alati selge, kes nende otsuste eest vastutab. Peame tagama, et mõistame, kus tehisintellekti otsuste vastutus lasub. Enamasti tahaksime kaasata inimesi oluliste otsuste tegemise protsessi, et tegelikud inimesed oleksid vastutavad.

## Vastutustundliku tehisintellekti tööriistad

Microsoft on välja töötanud [Vastutustundliku tehisintellekti tööriistakasti](https://github.com/microsoft/responsible-ai-toolbox), mis sisaldab mitmeid tööriistu:

* Tõlgendatavuse armatuurlaud (InterpretML)
* Õigluse armatuurlaud (FairLearn)
* Vigade analüüsi armatuurlaud
* Vastutustundliku tehisintellekti armatuurlaud, mis sisaldab:

   - EconML - põhjusliku analüüsi tööriist, mis keskendub "mis siis kui" küsimustele
   - DiCE - vastandlike analüüside tööriist, mis võimaldab näha, milliseid tunnuseid tuleb muuta, et mõjutada mudeli otsust

Lisateabe saamiseks tehisintellekti eetika kohta külastage [seda õppetundi](https://github.com/microsoft/ML-For-Beginners/tree/main/1-Introduction/3-fairness?WT.mc_id=academic-77998-cacaste) masinõppe õppekavas, mis sisaldab ülesandeid.

## Ülevaade ja iseseisev õpe

Läbige see [õppejuhis](https://docs.microsoft.com/learn/modules/responsible-ai-principles/?WT.mc_id=academic-77998-cacaste), et õppida rohkem vastutustundliku tehisintellekti kohta.

## [Järelloengu viktoriin](https://white-water-09ec41f0f.azurestaticapps.net/quiz/6/)

---

**Lahtiütlus**:  
See dokument on tõlgitud AI tõlketeenuse [Co-op Translator](https://github.com/Azure/co-op-translator) abil. Kuigi püüame tagada täpsust, palume arvestada, et automaatsed tõlked võivad sisaldada vigu või ebatäpsusi. Algne dokument selle algses keeles tuleks pidada autoriteetseks allikaks. Olulise teabe puhul soovitame kasutada professionaalset inimtõlget. Me ei vastuta selle tõlke kasutamisest tulenevate arusaamatuste või valesti tõlgenduste eest.