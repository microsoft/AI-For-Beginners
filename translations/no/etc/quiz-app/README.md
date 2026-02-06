# Quizzer

Disse quizene er forhånds- og etterforelesningsquizene for AI-pensumet på https://aka.ms/ai-beginners

## Legge til et oversatt quizsett

Legg til en oversettelse av quizene ved å opprette tilsvarende quizstrukturer i mappen `assets/translations`. De originale quizene finnes i `assets/translations/en`. Quizene er delt inn i flere grupper etter leksjon. Sørg for å justere nummereringen slik at den samsvarer med riktig quizseksjon. Det er totalt 40 quizzer i dette pensumet, og nummereringen starter på 0.

Etter at du har redigert oversettelsene, rediger `index.js`-filen i oversettelsesmappen for å importere alle filene i henhold til konvensjonene i `en`.

Rediger `index.js`-filen i `assets/translations` for å importere de nye oversatte filene.

Deretter redigerer du nedtrekksmenyen i `App.vue` i denne appen for å legge til språket ditt. Sørg for at den lokaliserte forkortelsen samsvarer med mappenavnet for språket ditt.

Til slutt, rediger alle quizlenkene i de oversatte leksjonene, hvis de finnes, for å inkludere denne lokaliseringen som en spørringsparameter: `?loc=fr` for eksempel.

## Prosjektoppsett

```
npm install
```

### Kompilerer og oppdaterer automatisk for utvikling

```
npm run serve
```

### Kompilerer og minimerer for produksjon

```
npm run build
```

### Linter og fikser filer

```
npm run lint
```

### Tilpass konfigurasjonen

Se [Konfigurasjonsreferanse](https://cli.vuejs.org/config/).

Kreditering: Takk til den originale versjonen av denne quiz-appen: https://github.com/arpan45/simple-quiz-vue

## Distribuere til Azure

Her er en trinnvis veiledning for å komme i gang:

1. Fork en GitHub-repositorium
Sørg for at koden til din statiske webapp ligger i ditt GitHub-repositorium. Fork dette repositoriet.

2. Opprett en Azure Static Web App
- Opprett en [Azure-konto](http://azure.microsoft.com)
- Gå til [Azure-portalen](https://portal.azure.com) 
- Klikk på "Opprett en ressurs" og søk etter "Static Web App".
- Klikk "Opprett".

3. Konfigurer den statiske webappen
- Grunnleggende: Abonnement: Velg ditt Azure-abonnement.
- Ressursgruppe: Opprett en ny ressursgruppe eller bruk en eksisterende.
- Navn: Gi et navn til din statiske webapp.
- Region: Velg regionen nærmest brukerne dine.

- #### Distribusjonsdetaljer:
- Kilde: Velg "GitHub".
- GitHub-konto: Autoriser Azure til å få tilgang til din GitHub-konto.
- Organisasjon: Velg din GitHub-organisasjon.
- Repositorium: Velg repositoriet som inneholder din statiske webapp.
- Gren: Velg grenen du vil distribuere fra.

- #### Byggdetaljer:
- Byggforhåndsinnstillinger: Velg rammeverket appen din er bygget med (f.eks. React, Angular, Vue, osv.).
- App-plassering: Angi mappen som inneholder appkoden din (f.eks. / hvis den er i roten).
- API-plassering: Hvis du har en API, angi plasseringen (valgfritt).
- Utdata-plassering: Angi mappen der byggeutdataene genereres (f.eks. build eller dist).

4. Gjennomgå og opprett
Gjennomgå innstillingene dine og klikk "Opprett". Azure vil sette opp de nødvendige ressursene og opprette en GitHub Actions-arbeidsflyt i repositoriet ditt.

5. GitHub Actions-arbeidsflyt
Azure vil automatisk opprette en GitHub Actions-arbeidsflytfil i repositoriet ditt (.github/workflows/azure-static-web-apps-<name>.yml). Denne arbeidsflyten vil håndtere bygge- og distribusjonsprosessen.

6. Overvåk distribusjonen
Gå til "Actions"-fanen i GitHub-repositoriet ditt.
Du bør se en arbeidsflyt som kjører. Denne arbeidsflyten vil bygge og distribuere din statiske webapp til Azure.
Når arbeidsflyten er fullført, vil appen din være live på den oppgitte Azure-URL-en.

### Eksempel på arbeidsflytfil

Her er et eksempel på hvordan GitHub Actions-arbeidsflytfilen kan se ut:
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

### Ytterligere ressurser
- [Azure Static Web Apps-dokumentasjon](https://learn.microsoft.com/azure/static-web-apps/getting-started)
- [GitHub Actions-dokumentasjon](https://docs.github.com/actions/use-cases-and-examples/deploying/deploying-to-azure-static-web-app)

---

**Ansvarsfraskrivelse**:  
Dette dokumentet er oversatt ved hjelp av AI-oversettelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selv om vi streber etter nøyaktighet, vær oppmerksom på at automatiserte oversettelser kan inneholde feil eller unøyaktigheter. Det originale dokumentet på sitt opprinnelige språk bør anses som den autoritative kilden. For kritisk informasjon anbefales profesjonell menneskelig oversettelse. Vi er ikke ansvarlige for misforståelser eller feiltolkninger som oppstår ved bruk av denne oversettelsen.