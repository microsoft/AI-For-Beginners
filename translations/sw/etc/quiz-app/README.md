# Quizzes

Dessa quizzar är för- och efterföljande quizzar för AI-läroplanen på https://aka.ms/ai-beginners

## Lägga till en översatt quizuppsättning

Lägg till en quizöversättning genom att skapa matchande quizstrukturer i `assets/translations` mapparna. De kanoniska quizzarna finns i `assets/translations/en`. Quizzarna är uppdelade i flera grupper efter lektion. Se till att numreringen stämmer överens med den rätta quizsektionen. Det finns totalt 40 quizzar i denna läroplan, med räkningen som börjar på 0.

Efter att ha redigerat översättningarna, redigera index.js-filen i översättningsmappen för att importera alla filer enligt konventionerna i `en`.

Redigera `index.js`-filen i `assets/translations` för att importera de nya översatta filerna.

Därefter, redigera rullgardinsmenyn i `App.vue` i denna app för att lägga till ditt språk. Matcha den lokaliserade förkortningen med mappnamnet för ditt språk.

Slutligen, redigera alla quizlänkar i de översatta lektionerna, om de finns, för att inkludera denna lokalisering som en frågeparameter: `?loc=fr` till exempel.

## Projektuppsättning

```
npm install
```

### Kompilerar och hot-reloader för utveckling

```
npm run serve
```

### Kompilerar och minifierar för produktion

```
npm run build
```

### Lintar och fixar filer

```
npm run lint
```

### Anpassa konfiguration

Se [Konfigurationsreferens](https://cli.vuejs.org/config/).

Krediter: Tack till den ursprungliga versionen av denna quizapp: https://github.com/arpan45/simple-quiz-vue

## Distribuera till Azure

Här är en steg-för-steg-guide för att hjälpa dig komma igång:

1. Forka ett GitHub-repo
Se till att din statiska webbapps kod finns i ditt GitHub-repo. Forka detta repo.

2. Skapa en Azure Static Web App
- Skapa ett [Azure-konto](http://azure.microsoft.com)
- Gå till [Azure-portalen](https://portal.azure.com) 
- Klicka på "Skapa en resurs" och sök efter "Static Web App".
- Klicka på "Skapa".

3. Konfigurera den statiska webbappen
- Grundläggande: Prenumeration: Välj din Azure-prenumeration.
- Resursgrupp: Skapa en ny resursgrupp eller använd en befintlig.
- Namn: Ange ett namn för din statiska webbapp.
- Region: Välj den region som ligger närmast dina användare.

- #### Distribueringsdetaljer:
- Källa: Välj "GitHub".
- GitHub-konto: Auktorisera Azure att få tillgång till ditt GitHub-konto.
- Organisation: Välj din GitHub-organisation.
- Repository: Välj det repo som innehåller din statiska webbapp.
- Gren: Välj den gren du vill distribuera från.

- #### Byggdetaljer:
- Byggförinställningar: Välj det ramverk din app är byggd med (t.ex. React, Angular, Vue, etc.).
- App-läge: Specificera mappen som innehåller din appkod (t.ex. / om den ligger i roten).
- API-läge: Om du har ett API, specificera dess plats (valfritt).
- Utmatningsläge: Specificera mappen där byggutmatningen genereras (t.ex. build eller dist).

4. Granska och skapa
Granska dina inställningar och klicka på "Skapa". Azure kommer att ställa in de nödvändiga resurserna och skapa en GitHub Actions-arbetsflöde i ditt repo.

5. GitHub Actions-arbetsflöde
Azure kommer automatiskt att skapa en GitHub Actions-arbetsflödesfil i ditt repo (.github/workflows/azure-static-web-apps-<name>.yml). Detta arbetsflöde kommer att hantera bygg- och distributionsprocessen.

6. Övervaka distributionen
Gå till fliken "Actions" i ditt GitHub-repo.
Du bör se ett arbetsflöde som körs. Detta arbetsflöde kommer att bygga och distribuera din statiska webbapp till Azure.
När arbetsflödet är klart kommer din app att vara live på den angivna Azure-URL:en.

### Exempel på arbetsflödesfil

Här är ett exempel på hur GitHub Actions-arbetsflödesfilen kan se ut:
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

### Ytterligare resurser
- [Dokumentation för Azure Static Web Apps](https://learn.microsoft.com/azure/static-web-apps/getting-started)
- [Dokumentation för GitHub Actions](https://docs.github.com/actions/use-cases-and-examples/deploying/deploying-to-azure-static-web-app)

**Varning**:  
Detta dokument har översatts med hjälp av maskinbaserade AI-översättningstjänster. Även om vi strävar efter noggrannhet, bör du vara medveten om att automatiska översättningar kan innehålla fel eller brister. Det ursprungliga dokumentet på sitt modersmål bör betraktas som den auktoritativa källan. För kritisk information rekommenderas professionell mänsklig översättning. Vi ansvarar inte för eventuella missförstånd eller feltolkningar som uppstår vid användning av denna översättning.