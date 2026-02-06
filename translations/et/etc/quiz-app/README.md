# Viktoriinid

Need viktoriinid on tehisintellekti õppekava eel- ja järeltestid aadressil https://aka.ms/ai-beginners

## Tõlgitud viktoriinide komplekti lisamine

Lisa viktoriini tõlge, luues vastavad viktoriinistruktuurid kaustadesse `assets/translations`. Algupärased viktoriinid asuvad kaustas `assets/translations/en`. Viktoriinid on jaotatud mitmeks rühmaks vastavalt õppetundidele. Veendu, et numbrid vastaksid õigetele viktoriini osadele. Selles õppekavas on kokku 40 viktoriini, alustades numbrist 0.

Pärast tõlgete redigeerimist muuda tõlke kaustas faili `index.js`, et importida kõik failid vastavalt `en` kaustas kehtivatele konventsioonidele.

Muuda faili `index.js` kaustas `assets/translations`, et importida uued tõlgitud failid.

Seejärel muuda selle rakenduse failis `App.vue` rippmenüüd, et lisada oma keel. Sobita lokaliseeritud lühend oma keele kausta nimega.

Lõpuks muuda kõiki tõlgitud õppetundides olevaid viktoriinilinke, kui need eksisteerivad, lisades lokaliseerimise päringuparameetrina: näiteks `?loc=fr`.

## Projekti seadistamine

```
npm install
```

### Kompileerib ja laadib arendamiseks dünaamiliselt

```
npm run serve
```

### Kompileerib ja minimeerib tootmiseks

```
npm run build
```

### Kontrollib ja parandab faile

```
npm run lint
```

### Kohanda konfiguratsiooni

Vaata [Konfiguratsiooni viidet](https://cli.vuejs.org/config/).

Tunnustus: Tänud selle viktoriinirakenduse algversiooni eest: https://github.com/arpan45/simple-quiz-vue

## Azure'i juurutamine

Siin on samm-sammuline juhend, mis aitab sul alustada:

1. Forki GitHubi hoidla
Veendu, et sinu staatilise veebirakenduse kood on sinu GitHubi hoidlasse salvestatud. Forki see hoidla.

2. Loo Azure'i staatiline veebirakendus
- Loo [Azure'i konto](http://azure.microsoft.com)
- Mine [Azure'i portaali](https://portal.azure.com) 
- Klõpsa “Create a resource” ja otsi “Static Web App”.
- Klõpsa “Create”.

3. Konfigureeri staatiline veebirakendus
- Põhiseaded: Tellimus: Vali oma Azure'i tellimus.
- Ressursigrupp: Loo uus ressursigrupp või kasuta olemasolevat.
- Nimi: Anna oma staatilisele veebirakendusele nimi.
- Piirkond: Vali piirkond, mis on sinu kasutajatele kõige lähemal.

- #### Juurutamise üksikasjad:
- Allikas: Vali “GitHub”.
- GitHubi konto: Autoriseeri Azure'il juurdepääs sinu GitHubi kontole.
- Organisatsioon: Vali oma GitHubi organisatsioon.
- Hoidla: Vali hoidla, mis sisaldab sinu staatilist veebirakendust.
- Haru: Vali haru, millest soovid juurutada.

- #### Ehituse üksikasjad:
- Ehituse eelseaded: Vali raamistik, millele sinu rakendus on ehitatud (nt React, Angular, Vue jne).
- Rakenduse asukoht: Määra kaust, mis sisaldab sinu rakenduse koodi (nt /, kui see on juurkaustas).
- API asukoht: Kui sul on API, määra selle asukoht (valikuline).
- Väljundi asukoht: Määra kaust, kuhu ehituse väljund salvestatakse (nt build või dist).

4. Ülevaatus ja loomine
Vaata oma seaded üle ja klõpsa “Create”. Azure seadistab vajalikud ressursid ja loob GitHub Actions töövoo sinu hoidlasse.

5. GitHub Actions töövoog
Azure loob automaatselt GitHub Actions töövoo faili sinu hoidlasse (.github/workflows/azure-static-web-apps-<name>.yml). See töövoog haldab ehituse ja juurutamise protsessi.

6. Juurutamise jälgimine
Mine oma GitHubi hoidla vahekaardile “Actions”.
Sa peaksid nägema töövoogu töötamas. See töövoog ehitab ja juurutab sinu staatilise veebirakenduse Azure'i.
Kui töövoog on lõpule jõudnud, on sinu rakendus reaalajas kättesaadav määratud Azure'i URL-i kaudu.

### Näide töövoo failist

Siin on näide, milline GitHub Actions töövoo fail võib välja näha:
name: Azure Static Web Apps CI/CD
```
on:
  push:
    branches:
      - main
  pull_request:
    types: [opened, synchronize, reopened, closed]
    branches:
      - main

jobs:
  build_and_deploy_job:
    runs-on: ubuntu-latest
    name: Build and Deploy Job
    steps:
      - uses: actions/checkout@v2
      - name: Build And Deploy
        id: builddeploy
        uses: Azure/static-web-apps-deploy@v1
        with:
          azure_static_web_apps_api_token: ${{ secrets.AZURE_STATIC_WEB_APPS_API_TOKEN }}
          repo_token: ${{ secrets.GITHUB_TOKEN }}
          action: "upload"
          app_location: "etc/quiz-app # App source code path"
          api_location: ""API source code path optional
          output_location: "dist" #Built app content directory - optional
```

### Lisamaterjalid
- [Azure'i staatiliste veebirakenduste dokumentatsioon](https://learn.microsoft.com/azure/static-web-apps/getting-started)
- [GitHub Actions dokumentatsioon](https://docs.github.com/actions/use-cases-and-examples/deploying/deploying-to-azure-static-web-app)

---

**Lahtiütlus**:  
See dokument on tõlgitud AI tõlketeenuse [Co-op Translator](https://github.com/Azure/co-op-translator) abil. Kuigi püüame tagada täpsust, palume arvestada, et automaatsed tõlked võivad sisaldada vigu või ebatäpsusi. Algne dokument selle algses keeles tuleks pidada autoriteetseks allikaks. Olulise teabe puhul soovitame kasutada professionaalset inimtõlget. Me ei vastuta selle tõlke kasutamisest tulenevate arusaamatuste või valesti tõlgenduste eest.