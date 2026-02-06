# Maswali ya Mitihani

Maswali haya ni ya kabla na baada ya mihadhara kwa mtaala wa AI unaopatikana kwenye https://aka.ms/ai-beginners

## Kuongeza seti ya maswali iliyotafsiriwa

Ongeza tafsiri ya maswali kwa kuunda miundo inayolingana ya maswali katika folda za `assets/translations`. Maswali ya msingi yapo kwenye `assets/translations/en`. Maswali yamegawanywa katika makundi kadhaa kulingana na somo. Hakikisha unalinganisha namba na sehemu sahihi ya maswali. Kuna jumla ya maswali 40 katika mtaala huu, na hesabu inaanzia 0.

Baada ya kuhariri tafsiri, hariri faili ya `index.js` katika folda ya tafsiri ili kuingiza faili zote ukifuata kanuni za `en`.

Hariri faili ya `index.js` katika `assets/translations` ili kuingiza faili mpya zilizotafsiriwa.

Kisha, hariri menyu kunjuzi katika `App.vue` kwenye programu hii ili kuongeza lugha yako. Linganisha kifupi cha lugha kilichotafsiriwa na jina la folda ya lugha yako.

Mwishowe, hariri viungo vyote vya maswali katika masomo yaliyotafsiriwa, ikiwa yapo, ili kujumuisha utafsiri huu kama kigezo cha swali: `?loc=fr` kwa mfano.

## Usanidi wa Mradi

```
npm install
```

### Inakamilisha na kupakia tena kwa maendeleo

```
npm run serve
```

### Inakamilisha na kupunguza kwa uzalishaji

```
npm run build
```

### Inakagua na kurekebisha faili

```
npm run lint
```

### Kubadilisha usanidi

Tazama [Marejeleo ya Usanidi](https://cli.vuejs.org/config/).

Shukrani: Asante kwa toleo la awali la programu hii ya maswali: https://github.com/arpan45/simple-quiz-vue

## Kuweka kwenye Azure

Hapa kuna mwongozo wa hatua kwa hatua wa kukusaidia kuanza:

1. Nakili Hifadhi ya GitHub  
Hakikisha msimbo wa programu yako ya wavuti tuli uko kwenye hifadhi yako ya GitHub. Nakili hifadhi hii.

2. Unda Azure Static Web App  
- Unda [akaunti ya Azure](http://azure.microsoft.com)  
- Nenda kwenye [Azure portal](https://portal.azure.com)  
- Bonyeza “Create a resource” na utafute “Static Web App”.  
- Bonyeza “Create”.  

3. Sanidi Azure Static Web App  
- Msingi:  
  - Usajili: Chagua usajili wako wa Azure.  
  - Kikundi cha Rasilimali: Unda kikundi kipya cha rasilimali au tumia kilichopo.  
  - Jina: Toa jina kwa programu yako ya wavuti tuli.  
  - Eneo: Chagua eneo lililo karibu zaidi na watumiaji wako.  

- #### Maelezo ya Uwekaji:  
  - Chanzo: Chagua “GitHub”.  
  - Akaunti ya GitHub: Ruhusu Azure kufikia akaunti yako ya GitHub.  
  - Shirika: Chagua shirika lako la GitHub.  
  - Hifadhi: Chagua hifadhi yenye msimbo wa programu yako ya wavuti tuli.  
  - Tawi: Chagua tawi unalotaka kuweka kutoka.  

- #### Maelezo ya Ujenzi:  
  - Vigezo vya Ujenzi: Chagua mfumo ambao programu yako imejengwa nao (mfano, React, Angular, Vue, n.k.).  
  - Eneo la Programu: Eleza folda yenye msimbo wa programu yako (mfano, / ikiwa iko kwenye mzizi).  
  - Eneo la API: Ikiwa una API, eleza eneo lake (hiari).  
  - Eneo la Matokeo: Eleza folda ambapo matokeo ya ujenzi yanazalishwa (mfano, build au dist).  

4. Kagua na Unda  
Kagua mipangilio yako na bonyeza “Create”. Azure itaweka rasilimali zinazohitajika na kuunda faili ya GitHub Actions katika hifadhi yako.  

5. Faili ya GitHub Actions Workflow  
Azure itaunda moja kwa moja faili ya GitHub Actions workflow katika hifadhi yako (.github/workflows/azure-static-web-apps-<name>.yml). Faili hii itashughulikia mchakato wa ujenzi na uwekaji.  

6. Fuata Uwekaji  
Nenda kwenye kichupo cha “Actions” katika hifadhi yako ya GitHub.  
Unapaswa kuona mchakato wa workflow ukiendelea. Mchakato huu utajenga na kuweka programu yako ya wavuti tuli kwenye Azure.  
Baada ya workflow kukamilika, programu yako itakuwa hewani kwenye URL iliyotolewa na Azure.  

### Mfano wa Faili ya Workflow  

Hapa kuna mfano wa jinsi faili ya GitHub Actions workflow inaweza kuonekana:  
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

### Rasilimali za Ziada  
- [Nyaraka za Azure Static Web Apps](https://learn.microsoft.com/azure/static-web-apps/getting-started)  
- [Nyaraka za GitHub Actions](https://docs.github.com/actions/use-cases-and-examples/deploying/deploying-to-azure-static-web-app)  

**Kanusho**:  
Hati hii imetafsiriwa kwa kutumia huduma ya kutafsiri ya AI [Co-op Translator](https://github.com/Azure/co-op-translator). Ingawa tunajitahidi kuhakikisha usahihi, tafadhali fahamu kuwa tafsiri za kiotomatiki zinaweza kuwa na makosa au kutokuwa sahihi. Hati ya asili katika lugha yake ya awali inapaswa kuzingatiwa kama chanzo cha mamlaka. Kwa taarifa muhimu, tafsiri ya kitaalamu ya binadamu inapendekezwa. Hatutawajibika kwa kutoelewana au tafsiri zisizo sahihi zinazotokana na matumizi ya tafsiri hii.