# Viktorinos

Šios viktorinos yra prieš ir po paskaitų skirtos AI mokymo programai, esančiai https://aka.ms/ai-beginners

## Kaip pridėti išverstą viktorinų rinkinį

Pridėkite viktorinų vertimą, sukurdami atitinkamas viktorinų struktūras aplanke `assets/translations`. Pagrindinės viktorinos yra aplanke `assets/translations/en`. Viktorinų rinkiniai yra suskirstyti pagal pamokas. Įsitikinkite, kad numeracija atitinka tinkamą viktorinų skyrių. Šioje mokymo programoje iš viso yra 40 viktorinų, numeracija prasideda nuo 0.

Po vertimo redagavimo, redaguokite failą `index.js` vertimo aplanke, kad importuotumėte visus failus pagal `en` aplanko konvencijas.

Redaguokite failą `index.js` aplanke `assets/translations`, kad importuotumėte naujus išverstus failus.

Tada redaguokite išskleidžiamąjį meniu faile `App.vue` šiame projekte, kad pridėtumėte savo kalbą. Suderinkite lokalizuotą santrumpą su savo kalbos aplanko pavadinimu.

Galiausiai, redaguokite visus viktorinų nuorodas išverstose pamokose, jei jos egzistuoja, kad įtrauktumėte šią lokalizaciją kaip užklausos parametrą: pavyzdžiui, `?loc=fr`.

## Projekto nustatymas

```
npm install
```

### Kompiliavimas ir greitas perkrovimas kūrimui

```
npm run serve
```

### Kompiliavimas ir minimizavimas gamybai

```
npm run build
```

### Failų tikrinimas ir taisymas

```
npm run lint
```

### Konfigūracijos pritaikymas

Žiūrėkite [Konfigūracijos nuorodą](https://cli.vuejs.org/config/).

Kreditas: Dėkojame originalios šios viktorinų programėlės versijos autoriui: https://github.com/arpan45/simple-quiz-vue

## Diegimas į Azure

Štai žingsnis po žingsnio vadovas, kaip pradėti:

1. Fork'inkite GitHub saugyklą  
Įsitikinkite, kad jūsų statinės žiniatinklio programos kodas yra jūsų GitHub saugykloje. Fork'inkite šią saugyklą.

2. Sukurkite Azure Static Web App  
- Susikurkite [Azure paskyrą](http://azure.microsoft.com)  
- Eikite į [Azure portalą](https://portal.azure.com)  
- Spustelėkite „Create a resource“ ir ieškokite „Static Web App“.  
- Spustelėkite „Create“.  

3. Konfigūruokite Static Web App  
- Pagrindai: Prenumerata: Pasirinkite savo Azure prenumeratą.  
- Išteklių grupė: Sukurkite naują išteklių grupę arba naudokite esamą.  
- Pavadinimas: Nurodykite savo statinės žiniatinklio programos pavadinimą.  
- Regionas: Pasirinkite regioną, artimiausią jūsų vartotojams.  

- #### Diegimo detalės:  
- Šaltinis: Pasirinkite „GitHub“.  
- GitHub paskyra: Suteikite Azure prieigą prie savo GitHub paskyros.  
- Organizacija: Pasirinkite savo GitHub organizaciją.  
- Saugykla: Pasirinkite saugyklą, kurioje yra jūsų statinė žiniatinklio programa.  
- Šaka: Pasirinkite šaką, iš kurios norite diegti.  

- #### Kūrimo detalės:  
- Kūrimo šablonai: Pasirinkite sistemą, su kuria sukurta jūsų programa (pvz., React, Angular, Vue ir kt.).  
- Programos vieta: Nurodykite aplanką, kuriame yra jūsų programos kodas (pvz., / jei jis yra šakniniame aplanke).  
- API vieta: Jei turite API, nurodykite jos vietą (neprivaloma).  
- Išvesties vieta: Nurodykite aplanką, kuriame sugeneruojama kūrimo išvestis (pvz., build arba dist).  

4. Peržiūrėkite ir sukurkite  
Peržiūrėkite savo nustatymus ir spustelėkite „Create“. Azure sukurs reikalingus išteklius ir sukurs GitHub Actions darbo eigą jūsų saugykloje.

5. GitHub Actions darbo eiga  
Azure automatiškai sukurs GitHub Actions darbo eigos failą jūsų saugykloje (.github/workflows/azure-static-web-apps-<name>.yml). Ši darbo eiga tvarkys kūrimo ir diegimo procesą.

6. Stebėkite diegimą  
Eikite į „Actions“ skirtuką savo GitHub saugykloje.  
Turėtumėte matyti veikiančią darbo eigą. Ši darbo eiga sukurs ir įdiegs jūsų statinę žiniatinklio programą į Azure.  
Kai darbo eiga bus baigta, jūsų programa bus pasiekiama nurodytu Azure URL adresu.

### Pavyzdinis darbo eigos failas

Štai pavyzdys, kaip gali atrodyti GitHub Actions darbo eigos failas:  
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

### Papildomi ištekliai  
- [Azure Static Web Apps dokumentacija](https://learn.microsoft.com/azure/static-web-apps/getting-started)  
- [GitHub Actions dokumentacija](https://docs.github.com/actions/use-cases-and-examples/deploying/deploying-to-azure-static-web-app)  

---

**Atsakomybės apribojimas**:  
Šis dokumentas buvo išverstas naudojant AI vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors siekiame tikslumo, prašome atkreipti dėmesį, kad automatiniai vertimai gali turėti klaidų ar netikslumų. Originalus dokumentas jo gimtąja kalba turėtų būti laikomas autoritetingu šaltiniu. Kritinei informacijai rekomenduojama naudoti profesionalų žmogaus vertimą. Mes neprisiimame atsakomybės už nesusipratimus ar klaidingus interpretavimus, atsiradusius dėl šio vertimo naudojimo.