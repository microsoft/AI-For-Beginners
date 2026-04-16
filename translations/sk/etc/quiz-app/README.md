# Kvízy

Tieto kvízy sú prednáškové a po prednáškové kvízy pre AI učebný plán na https://aka.ms/ai-beginners

## Pridanie preloženého súboru kvízov

Pridajte preklad kvízu vytvorením zodpovedajúcich štruktúr kvízov v priečinkoch `assets/translations`. Kanonické kvízy sa nachádzajú v `assets/translations/en`. Kvízy sú rozdelené do niekoľkých skupín podľa lekcií. Uistite sa, že číslovanie zodpovedá správnej sekcii kvízu. V tomto učebnom pláne je celkovo 40 kvízov, pričom číslovanie začína od 0.

Po úprave prekladov upravte súbor index.js v priečinku prekladov, aby ste importovali všetky súbory podľa konvencií v `en`.

Upravte súbor `index.js` v `assets/translations`, aby ste importovali nové preložené súbory.

Potom upravte rozbaľovací zoznam v `App.vue` v tejto aplikácii, aby ste pridali svoj jazyk. Zlaďte lokalizovanú skratku s názvom priečinka pre váš jazyk.

Nakoniec upravte všetky odkazy na kvízy v preložených lekciách, ak existujú, aby obsahovali túto lokalizáciu ako parameter dotazu: napríklad `?loc=fr`.

## Nastavenie projektu

```
npm install
```

### Kompilácia a automatické načítanie pre vývoj

```
npm run serve
```

### Kompilácia a minimalizácia pre produkciu

```
npm run build
```

### Kontrola a oprava súborov

```
npm run lint
```

### Prispôsobenie konfigurácie

Pozrite si [Referenciu konfigurácie](https://cli.vuejs.org/config/).

Kredity: Vďaka pôvodnej verzii tejto aplikácie na kvízy: https://github.com/arpan45/simple-quiz-vue

## Nasadenie na Azure

Tu je krok za krokom návod, ako začať:

1. Forknite GitHub repozitár  
Uistite sa, že váš kód statickej webovej aplikácie je vo vašom GitHub repozitári. Forknite tento repozitár.

2. Vytvorte Azure Static Web App  
- Vytvorte si [Azure účet](http://azure.microsoft.com)  
- Prejdite na [Azure portál](https://portal.azure.com)  
- Kliknite na „Vytvoriť zdroj“ a vyhľadajte „Static Web App“.  
- Kliknite na „Vytvoriť“.  

3. Konfigurácia Static Web App  
- Základy: Predplatné: Vyberte svoje Azure predplatné.  
- Resource Group: Vytvorte novú skupinu zdrojov alebo použite existujúcu.  
- Názov: Zadajte názov pre vašu statickú webovú aplikáciu.  
- Región: Vyberte región najbližší vašim používateľom.  

- #### Detaily nasadenia:  
- Zdroj: Vyberte „GitHub“.  
- GitHub účet: Autorizujte Azure na prístup k vášmu GitHub účtu.  
- Organizácia: Vyberte svoju GitHub organizáciu.  
- Repozitár: Vyberte repozitár obsahujúci vašu statickú webovú aplikáciu.  
- Branch: Vyberte vetvu, z ktorej chcete nasadzovať.  

- #### Detaily zostavenia:  
- Predvoľby zostavenia: Vyberte framework, s ktorým je vaša aplikácia vytvorená (napr. React, Angular, Vue, atď.).  
- Umiestnenie aplikácie: Špecifikujte priečinok obsahujúci kód vašej aplikácie (napr. / ak je v koreňovom adresári).  
- Umiestnenie API: Ak máte API, špecifikujte jeho umiestnenie (voliteľné).  
- Umiestnenie výstupu: Špecifikujte priečinok, kde sa generuje výstup zostavenia (napr. build alebo dist).  

4. Kontrola a vytvorenie  
Skontrolujte svoje nastavenia a kliknite na „Vytvoriť“. Azure nastaví potrebné zdroje a vytvorí GitHub Actions workflow vo vašom repozitári.

5. GitHub Actions Workflow  
Azure automaticky vytvorí GitHub Actions workflow súbor vo vašom repozitári (.github/workflows/azure-static-web-apps-<name>.yml). Tento workflow bude spracovávať proces zostavenia a nasadenia.

6. Monitorovanie nasadenia  
Prejdite na kartu „Actions“ vo vašom GitHub repozitári.  
Mali by ste vidieť spustený workflow. Tento workflow zostaví a nasadí vašu statickú webovú aplikáciu na Azure.  
Po dokončení workflowu bude vaša aplikácia dostupná na poskytnutej Azure URL.

### Príklad workflow súboru

Tu je príklad, ako môže vyzerať GitHub Actions workflow súbor:  
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

### Ďalšie zdroje
- [Dokumentácia Azure Static Web Apps](https://learn.microsoft.com/azure/static-web-apps/getting-started)  
- [Dokumentácia GitHub Actions](https://docs.github.com/actions/use-cases-and-examples/deploying/deploying-to-azure-static-web-app)  

**Upozornenie**:  
Tento dokument bol preložený pomocou služby AI prekladu [Co-op Translator](https://github.com/Azure/co-op-translator). Hoci sa snažíme o presnosť, prosím, berte na vedomie, že automatizované preklady môžu obsahovať chyby alebo nepresnosti. Pôvodný dokument v jeho rodnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nie sme zodpovední za žiadne nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.