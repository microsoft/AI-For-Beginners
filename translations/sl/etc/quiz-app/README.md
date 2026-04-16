# Kvizi

Ti kvizi so pred- in po-predavanji kvizi za učni načrt umetne inteligence na https://aka.ms/ai-beginners

## Dodajanje prevedenega nabora kvizov

Prevod kviza dodate tako, da ustvarite ustrezne strukture kvizov v mapah `assets/translations`. Izvirni kvizi so v `assets/translations/en`. Kvizi so razdeljeni v več skupin po lekcijah. Poskrbite, da bo številčenje usklajeno s pravilnim razdelkom kviza. V tem učnem načrtu je skupaj 40 kvizov, številčenje pa se začne pri 0.

Po urejanju prevodov uredite datoteko index.js v mapi za prevode, da uvozite vse datoteke v skladu s konvencijami v `en`.

Uredite datoteko `index.js` v `assets/translations`, da uvozite nove prevedene datoteke.

Nato uredite spustni meni v `App.vue` v tej aplikaciji, da dodate svoj jezik. Ujemajte lokalizirano okrajšavo z imenom mape za vaš jezik.

Na koncu uredite vse povezave do kvizov v prevedenih lekcijah, če obstajajo, tako da vključite to lokalizacijo kot parameter poizvedbe: `?loc=fr` na primer.

## Nastavitev projekta

```
npm install
```

### Prevajanje in samodejno osveževanje za razvoj

```
npm run serve
```

### Prevajanje in minimiziranje za produkcijo

```
npm run build
```

### Preverjanje kode in odpravljanje napak

```
npm run lint
```

### Prilagoditev konfiguracije

Glejte [Referenca konfiguracije](https://cli.vuejs.org/config/).

Zasluge: Zahvala za izvirno različico te aplikacije za kvize: https://github.com/arpan45/simple-quiz-vue

## Uvajanje na Azure

Tukaj je korak za korakom vodnik, ki vam bo pomagal začeti:

1. Fork GitHub repozitorija  
Poskrbite, da je koda vaše statične spletne aplikacije v vašem GitHub repozitoriju. Forkajte ta repozitorij.

2. Ustvarite Azure Static Web App  
- Ustvarite [Azure račun](http://azure.microsoft.com)  
- Pojdite na [Azure portal](https://portal.azure.com)  
- Kliknite na “Create a resource” in poiščite “Static Web App”.  
- Kliknite “Create”.

3. Konfigurirajte Static Web App  
- Osnovno: Naročnina: Izberite svojo Azure naročnino.  
- Skupina virov: Ustvarite novo skupino virov ali uporabite obstoječo.  
- Ime: Določite ime za svojo statično spletno aplikacijo.  
- Regija: Izberite regijo, ki je najbližje vašim uporabnikom.

- #### Podrobnosti uvajanja:  
- Vir: Izberite “GitHub”.  
- GitHub račun: Pooblastite Azure za dostop do vašega GitHub računa.  
- Organizacija: Izberite svojo GitHub organizacijo.  
- Repozitorij: Izberite repozitorij, ki vsebuje vašo statično spletno aplikacijo.  
- Branch: Izberite vejo, iz katere želite uvajati.

- #### Podrobnosti gradnje:  
- Prednastavitve gradnje: Izberite ogrodje, s katerim je vaša aplikacija zgrajena (npr. React, Angular, Vue itd.).  
- Lokacija aplikacije: Določite mapo, ki vsebuje kodo vaše aplikacije (npr. /, če je v korenu).  
- Lokacija API-ja: Če imate API, določite njegovo lokacijo (neobvezno).  
- Lokacija izhoda: Določite mapo, kjer je ustvarjen izhod gradnje (npr. build ali dist).

4. Pregled in ustvarjanje  
Preglejte svoje nastavitve in kliknite “Create”. Azure bo nastavil potrebne vire in ustvaril GitHub Actions delovni tok v vašem repozitoriju.

5. GitHub Actions delovni tok  
Azure bo samodejno ustvaril GitHub Actions delovni tok datoteko v vašem repozitoriju (.github/workflows/azure-static-web-apps-<ime>.yml). Ta delovni tok bo upravljal proces gradnje in uvajanja.

6. Spremljanje uvajanja  
Pojdite na zavihek “Actions” v vašem GitHub repozitoriju.  
Videti bi morali, da delovni tok teče. Ta delovni tok bo zgradil in uvedel vašo statično spletno aplikacijo na Azure.  
Ko se delovni tok zaključi, bo vaša aplikacija na voljo na dodeljenem Azure URL-ju.

### Primer datoteke delovnega toka

Tukaj je primer, kako bi lahko izgledala datoteka GitHub Actions delovnega toka:  
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

### Dodatni viri  
- [Dokumentacija za Azure Static Web Apps](https://learn.microsoft.com/azure/static-web-apps/getting-started)  
- [Dokumentacija za GitHub Actions](https://docs.github.com/actions/use-cases-and-examples/deploying/deploying-to-azure-static-web-app)  

**Omejitev odgovornosti**:  
Ta dokument je bil preveden z uporabo storitve AI za prevajanje [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas prosimo, da upoštevate, da lahko avtomatizirani prevodi vsebujejo napake ali netočnosti. Izvirni dokument v njegovem maternem jeziku je treba obravnavati kot avtoritativni vir. Za ključne informacije priporočamo profesionalni človeški prevod. Ne prevzemamo odgovornosti za morebitna nesporazumevanja ali napačne razlage, ki izhajajo iz uporabe tega prevoda.