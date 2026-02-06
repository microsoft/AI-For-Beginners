# Quizzer

Disse quizzer er før- og efterforelæsningsquizzer for AI-læseplanen på https://aka.ms/ai-beginners

## Tilføjelse af et oversat quizsæt

Tilføj en quizoversættelse ved at oprette matchende quizstrukturer i `assets/translations`-mapperne. De originale quizzer findes i `assets/translations/en`. Quizzerne er opdelt i flere grupper efter lektion. Sørg for at tilpasse nummereringen med den korrekte quizsektion. Der er i alt 40 quizzer i denne læseplan, og nummereringen starter ved 0.

Efter at have redigeret oversættelserne, rediger `index.js`-filen i oversættelsesmappen for at importere alle filerne i henhold til konventionerne i `en`.

Rediger `index.js`-filen i `assets/translations` for at importere de nye oversatte filer.

Derefter skal du redigere dropdown-menuen i `App.vue` i denne app for at tilføje dit sprog. Match den lokaliserede forkortelse med mappenavnet for dit sprog.

Til sidst skal du redigere alle quiz-links i de oversatte lektioner, hvis de findes, for at inkludere denne lokalisering som en forespørgselsparameter: `?loc=fr` for eksempel.

## Projektopsætning

```
npm install
```

### Kompilerer og genindlæser til udvikling

```
npm run serve
```

### Kompilerer og minimerer til produktion

```
npm run build
```

### Linter og retter filer

```
npm run lint
```

### Tilpas konfiguration

Se [Konfigurationsreference](https://cli.vuejs.org/config/).

Credits: Tak til den originale version af denne quiz-app: https://github.com/arpan45/simple-quiz-vue

## Udrulning til Azure

Her er en trin-for-trin guide til at hjælpe dig i gang:

1. Fork en GitHub-repository
Sørg for, at din statiske webapp-kode er i din GitHub-repository. Fork denne repository.

2. Opret en Azure Static Web App
- Opret en [Azure-konto](http://azure.microsoft.com)
- Gå til [Azure-portalen](https://portal.azure.com) 
- Klik på “Create a resource” og søg efter “Static Web App”.
- Klik på “Create”.

3. Konfigurer den statiske webapp
- Grundlæggende: Abonnement: Vælg dit Azure-abonnement.
- Ressourcegruppe: Opret en ny ressourcegruppe eller brug en eksisterende.
- Navn: Angiv et navn til din statiske webapp.
- Region: Vælg den region, der er tættest på dine brugere.

- #### Udrulningsdetaljer:
- Kilde: Vælg “GitHub”.
- GitHub-konto: Autoriser Azure til at få adgang til din GitHub-konto.
- Organisation: Vælg din GitHub-organisation.
- Repository: Vælg den repository, der indeholder din statiske webapp.
- Gren: Vælg den gren, du vil udrulle fra.

- #### Bygningsdetaljer:
- Bygningsforudindstillinger: Vælg det framework, din app er bygget med (f.eks. React, Angular, Vue osv.).
- App-placering: Angiv mappen, der indeholder din app-kode (f.eks. / hvis den er i roden).
- API-placering: Hvis du har en API, angiv dens placering (valgfrit).
- Output-placering: Angiv mappen, hvor build-output genereres (f.eks. build eller dist).

4. Gennemse og opret
Gennemse dine indstillinger og klik på “Create”. Azure vil oprette de nødvendige ressourcer og oprette en GitHub Actions workflow i din repository.

5. GitHub Actions Workflow
Azure vil automatisk oprette en GitHub Actions workflow-fil i din repository (.github/workflows/azure-static-web-apps-<name>.yml). Denne workflow vil håndtere bygge- og udrulningsprocessen.

6. Overvåg udrulningen
Gå til fanen “Actions” i din GitHub-repository.
Du bør se en workflow køre. Denne workflow vil bygge og udrulle din statiske webapp til Azure.
Når workflowen er færdig, vil din app være live på den angivne Azure-URL.

### Eksempel på workflow-fil

Her er et eksempel på, hvordan GitHub Actions workflow-filen kan se ud:
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

### Yderligere ressourcer
- [Azure Static Web Apps Dokumentation](https://learn.microsoft.com/azure/static-web-apps/getting-started)
- [GitHub Actions Dokumentation](https://docs.github.com/actions/use-cases-and-examples/deploying/deploying-to-azure-static-web-app)

---

**Ansvarsfraskrivelse**:  
Dette dokument er blevet oversat ved hjælp af AI-oversættelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selvom vi bestræber os på at sikre nøjagtighed, skal det bemærkes, at automatiserede oversættelser kan indeholde fejl eller unøjagtigheder. Det originale dokument på dets oprindelige sprog bør betragtes som den autoritative kilde. For kritisk information anbefales professionel menneskelig oversættelse. Vi påtager os ikke ansvar for eventuelle misforståelser eller fejltolkninger, der måtte opstå som følge af brugen af denne oversættelse.