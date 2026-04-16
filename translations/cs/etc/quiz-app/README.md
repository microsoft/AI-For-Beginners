# Kvízy

Tyto kvízy slouží jako přednáškové a popřednáškové kvízy pro AI kurikulum na https://aka.ms/ai-beginners

## Přidání přeložené sady kvízů

Přidejte překlad kvízu vytvořením odpovídajících struktur kvízů ve složkách `assets/translations`. Kanonické kvízy se nacházejí v `assets/translations/en`. Kvízy jsou rozděleny do několika skupin podle lekcí. Ujistěte se, že číslování odpovídá správné sekci kvízu. Celkem je v tomto kurikulu 40 kvízů, přičemž číslování začíná od 0.

Po úpravě překladů upravte soubor index.js ve složce s překlady tak, aby importoval všechny soubory podle konvencí v `en`.

Upravte soubor `index.js` v `assets/translations`, aby importoval nově přeložené soubory.

Poté upravte rozbalovací nabídku v `App.vue` v této aplikaci, abyste přidali svůj jazyk. Odpovídající lokalizovanou zkratku přizpůsobte názvu složky pro váš jazyk.

Nakonec upravte všechny odkazy na kvízy v přeložených lekcích, pokud existují, aby obsahovaly tuto lokalizaci jako parametr dotazu: například `?loc=fr`.

## Nastavení projektu

```
npm install
```

### Kompilace a automatické načítání pro vývoj

```
npm run serve
```

### Kompilace a minimalizace pro produkci

```
npm run build
```

### Kontrola a oprava souborů

```
npm run lint
```

### Přizpůsobení konfigurace

Viz [Konfigurační reference](https://cli.vuejs.org/config/).

Poděkování: Díky původní verzi této aplikace pro kvízy: https://github.com/arpan45/simple-quiz-vue

## Nasazení na Azure

Zde je podrobný průvodce, který vám pomůže začít:

1. Vytvořte fork GitHub repozitáře  
Ujistěte se, že váš kód statické webové aplikace je ve vašem GitHub repozitáři. Vytvořte fork tohoto repozitáře.

2. Vytvořte statickou webovou aplikaci na Azure  
- Vytvořte si [Azure účet](http://azure.microsoft.com)  
- Přejděte na [Azure portál](https://portal.azure.com)  
- Klikněte na „Vytvořit prostředek“ a vyhledejte „Static Web App“.  
- Klikněte na „Vytvořit“.  

3. Konfigurace statické webové aplikace  
- Základy:  
  - Předplatné: Vyberte své předplatné Azure.  
  - Skupina prostředků: Vytvořte novou skupinu prostředků nebo použijte existující.  
  - Název: Zadejte název pro svou statickou webovou aplikaci.  
  - Region: Vyberte region nejbližší vašim uživatelům.  

- #### Podrobnosti nasazení:  
  - Zdroj: Vyberte „GitHub“.  
  - GitHub účet: Autorizujte Azure k přístupu k vašemu GitHub účtu.  
  - Organizace: Vyberte svou GitHub organizaci.  
  - Repozitář: Vyberte repozitář obsahující vaši statickou webovou aplikaci.  
  - Větev: Vyberte větev, ze které chcete nasazovat.  

- #### Podrobnosti sestavení:  
  - Předvolby sestavení: Vyberte framework, na kterém je vaše aplikace postavena (např. React, Angular, Vue, atd.).  
  - Umístění aplikace: Zadejte složku obsahující kód vaší aplikace (např. / pokud je v kořenovém adresáři).  
  - Umístění API: Pokud máte API, zadejte jeho umístění (volitelné).  
  - Umístění výstupu: Zadejte složku, kde je generován výstup sestavení (např. build nebo dist).  

4. Kontrola a vytvoření  
Zkontrolujte své nastavení a klikněte na „Vytvořit“. Azure nastaví potřebné prostředky a vytvoří GitHub Actions workflow ve vašem repozitáři.

5. GitHub Actions workflow  
Azure automaticky vytvoří soubor GitHub Actions workflow ve vašem repozitáři (.github/workflows/azure-static-web-apps-<name>.yml). Tento workflow bude zajišťovat proces sestavení a nasazení.

6. Sledování nasazení  
Přejděte na kartu „Actions“ ve vašem GitHub repozitáři.  
Měli byste vidět běžící workflow. Tento workflow sestaví a nasadí vaši statickou webovou aplikaci na Azure.  
Jakmile workflow dokončí, vaše aplikace bude dostupná na poskytnuté URL Azure.

### Příklad souboru workflow

Zde je příklad, jak může vypadat soubor GitHub Actions workflow:  
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

### Další zdroje  
- [Dokumentace Azure Static Web Apps](https://learn.microsoft.com/azure/static-web-apps/getting-started)  
- [Dokumentace GitHub Actions](https://docs.github.com/actions/use-cases-and-examples/deploying/deploying-to-azure-static-web-app)  

**Prohlášení:**  
Tento dokument byl přeložen pomocí služby pro automatický překlad [Co-op Translator](https://github.com/Azure/co-op-translator). Ačkoli se snažíme o přesnost, mějte prosím na paměti, že automatické překlady mohou obsahovat chyby nebo nepřesnosti. Původní dokument v jeho původním jazyce by měl být považován za autoritativní zdroj. Pro důležité informace se doporučuje profesionální lidský překlad. Neodpovídáme za žádná nedorozumění nebo nesprávné interpretace vyplývající z použití tohoto překladu.