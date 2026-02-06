# கேள்விகள்

இந்த கேள்விகள் AI பாடத்திட்டத்திற்கான முன் மற்றும் பின்-வகுப்பு கேள்விகள் ஆகும். https://aka.ms/ai-beginners

## மொழிபெயர்க்கப்பட்ட கேள்வி தொகுப்பை சேர்க்க

மொழிபெயர்க்கப்பட்ட கேள்விகளை `assets/translations` கோப்பகங்களில் பொருந்தும் கேள்வி அமைப்புகளை உருவாக்குவதன் மூலம் சேர்க்கவும். மூல கேள்விகள் `assets/translations/en` இல் உள்ளன. கேள்விகள் பாடத்திட்டத்தின் பாடங்களின் அடிப்படையில் பல பிரிவுகளாக பிரிக்கப்பட்டுள்ளன. சரியான கேள்வி பிரிவுடன் எண் ஒழுங்கை சரிசெய்யவும். இந்த பாடத்திட்டத்தில் மொத்தம் 40 கேள்விகள் உள்ளன, எண்ணிக்கை 0-இல் தொடங்குகிறது.

மொழிபெயர்ப்புகளை திருத்திய பிறகு, `en` இல் உள்ள வழிமுறைகளை பின்பற்றி மொழிபெயர்ப்பு கோப்பகத்தில் உள்ள `index.js` கோப்பை திருத்தி அனைத்து கோப்புகளையும் இறக்குமதி செய்யவும்.

பின்னர், `assets/translations` இல் உள்ள `index.js` கோப்பை திருத்தி புதிய மொழிபெயர்க்கப்பட்ட கோப்புகளை இறக்குமதி செய்யவும்.

அதன் பிறகு, இந்த பயன்பாட்டில் உள்ள `App.vue` இல் உள்ள dropdown ஐ திருத்தி உங்கள் மொழியைச் சேர்க்கவும். உங்கள் மொழிக்கான கோப்பகத்தின் பெயருடன் உள்ளூர் சுருக்கத்தை பொருத்தவும்.

இறுதியாக, மொழிபெயர்க்கப்பட்ட பாடங்களில் உள்ள அனைத்து கேள்வி இணைப்புகளையும், அவை இருந்தால், இந்த உள்ளூர்மயமாக்கலை ஒரு கேள்வி அளவுருவாக சேர்க்க திருத்தவும்: உதாரணமாக `?loc=fr`.

## திட்ட அமைப்பு

```
npm install
```

### மேம்பாட்டிற்காக தொகுத்து மற்றும் தானாக மீண்டும் ஏற்றுகிறது

```
npm run serve
```

### உற்பத்திக்காக தொகுத்து மற்றும் சுருக்குகிறது

```
npm run build
```

### கோப்புகளை சீரமைக்கிறது மற்றும் திருத்துகிறது

```
npm run lint
```

### கட்டமைப்பை தனிப்பயனாக்கவும்

[Configuration Reference](https://cli.vuejs.org/config/) ஐப் பார்க்கவும்.

Credits: இந்த கேள்வி பயன்பாட்டின் மூல பதிப்புக்கு நன்றி: https://github.com/arpan45/simple-quiz-vue

## Azure-க்கு வெளியிடுதல்

இங்கே நீங்கள் தொடங்க உதவும் படிப்படியாக வழிகாட்டுதல் உள்ளது:

1. GitHub Repository ஐ Fork செய்யவும்
உங்கள் நிலையான வலை பயன்பாட்டு குறியீடு உங்கள் GitHub repository இல் இருக்க வேண்டும். இந்த repository ஐ Fork செய்யவும்.

2. Azure Static Web App ஐ உருவாக்கவும்
- [Azure account](http://azure.microsoft.com) ஐ உருவாக்கவும்
- [Azure portal](https://portal.azure.com) க்கு செல்லவும் 
- “Create a resource” ஐ கிளிக் செய்து “Static Web App” ஐ தேடவும்.
- “Create” ஐ கிளிக் செய்யவும்.

3. Static Web App ஐ அமைக்கவும்
- அடிப்படைகள்: Subscription: உங்கள் Azure subscription ஐத் தேர்ந்தெடுக்கவும்.
- Resource Group: புதிய resource group ஐ உருவாக்கவும் அல்லது ஏற்கனவே உள்ள ஒன்றை பயன்படுத்தவும்.
- Name: உங்கள் static web app க்கு ஒரு பெயரை வழங்கவும்.
- Region: உங்கள் பயனர்களுக்கு அருகிலுள்ள பகுதியைத் தேர்ந்தெடுக்கவும்.

- #### Deployment Details:
- Source: “GitHub” ஐத் தேர்ந்தெடுக்கவும்.
- GitHub Account: Azure உங்கள் GitHub கணக்கை அணுக அனுமதிக்கவும்.
- Organization: உங்கள் GitHub அமைப்பைத் தேர்ந்தெடுக்கவும்.
- Repository: உங்கள் static web app உள்ள repository ஐத் தேர்ந்தெடுக்கவும்.
- Branch: நீங்கள் வெளியிட விரும்பும் branch ஐத் தேர்ந்தெடுக்கவும்.

- #### Build Details:
- Build Presets: உங்கள் பயன்பாடு உருவாக்கப்பட்ட framework ஐத் தேர்ந்தெடுக்கவும் (எ.கா., React, Angular, Vue, போன்றவை).
- App Location: உங்கள் பயன்பாட்டு குறியீடு உள்ள கோப்பகத்தை குறிப்பிடவும் (எ.கா., / இது root இல் இருந்தால்).
- API Location: உங்கள் API இருந்தால், அதன் இடத்தை குறிப்பிடவும் (விருப்பம்).
- Output Location: build output உருவாக்கப்படும் கோப்பகத்தை குறிப்பிடவும் (எ.கா., build அல்லது dist).

4. Review and Create
உங்கள் அமைப்புகளை மதிப்பாய்வு செய்து “Create” ஐ கிளிக் செய்யவும். Azure தேவையான வளங்களை அமைத்து உங்கள் repository இல் GitHub Actions workflow ஐ உருவாக்கும்.

5. GitHub Actions Workflow
Azure உங்கள் repository இல் (.github/workflows/azure-static-web-apps-<name>.yml) GitHub Actions workflow கோப்பை தானாக உருவாக்கும். இந்த workflow build மற்றும் deployment செயல்முறையை நிர்வகிக்கும்.

6. Deployment ஐ கண்காணிக்கவும்
உங்கள் GitHub repository இல் “Actions” tab க்கு செல்லவும்.
ஒரு workflow இயங்குவதை நீங்கள் காணலாம். இந்த workflow உங்கள் static web app ஐ Azure-க்கு build செய்து வெளியிடும்.
Workflow முடிந்தவுடன், உங்கள் பயன்பாடு வழங்கப்பட்ட Azure URL இல் நேரலை ஆக இருக்கும்.

### உதாரண Workflow கோப்பு

GitHub Actions workflow கோப்பு எப்படி இருக்கும் என்பதற்கான உதாரணம்:
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

### கூடுதல் வளங்கள்
- [Azure Static Web Apps Documentation](https://learn.microsoft.com/azure/static-web-apps/getting-started)
- [GitHub Actions Documentation](https://docs.github.com/actions/use-cases-and-examples/deploying/deploying-to-azure-static-web-app)

---

**குறிப்பு**:  
இந்த ஆவணம் [Co-op Translator](https://github.com/Azure/co-op-translator) என்ற AI மொழிபெயர்ப்பு சேவையைப் பயன்படுத்தி மொழிபெயர்க்கப்பட்டுள்ளது. நாங்கள் துல்லியத்திற்காக முயற்சிக்கின்றோம், ஆனால் தானியங்கி மொழிபெயர்ப்புகளில் பிழைகள் அல்லது தவறான தகவல்கள் இருக்கக்கூடும் என்பதை கவனத்தில் கொள்ளவும். அதன் தாய்மொழியில் உள்ள மூல ஆவணம் அதிகாரப்பூர்வ ஆதாரமாக கருதப்பட வேண்டும். முக்கியமான தகவல்களுக்கு, தொழில்முறை மனித மொழிபெயர்ப்பு பரிந்துரைக்கப்படுகிறது. இந்த மொழிபெயர்ப்பைப் பயன்படுத்துவதால் ஏற்படும் எந்த தவறான புரிதல்கள் அல்லது தவறான விளக்கங்களுக்கு நாங்கள் பொறுப்பல்ல.