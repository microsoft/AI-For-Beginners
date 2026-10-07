# Quizzes

Yeh quizzes AI curriculum ke pre- aur post-lecture quizzes hain, jo https://aka.ms/ai-beginners par available hai.

## Translated quiz sets add karna

Kisi quiz ka translation add karne ke liye, `assets/translations` folder mein same quiz structures banayein. Original quizzes `assets/translations/en` mein hain. Yeh quizzes lesson ke hisaab se kai groups mein baanti gayi hain. Dhyan rakhein ki numbering sahi quiz section ke saath match ho. Is curriculum mein kul 40 quizzes hain, jinki ginti 0 se shuru hoti hai.

Translations edit karne ke baad, translations folder mein `index.js` file ko edit karein aur saari files ko `en` mein diye gaye conventions ke hisaab se import karein.

`assets/translations` mein `index.js` file ko edit karein aur nayi translated files ko import karein.

Phir, is app mein `App.vue` ke dropdown ko edit karein aur apni language add karein. Localized abbreviation ko apni language ke folder name se match karein.

Aakhir mein, translated lessons mein saare quiz links ko edit karein, agar woh maujood hain, taaki is localization ko ek query parameter ke roop mein include kiya ja sake: jaise `?loc=fr`.

## Project Setup

```
npm install
```

### Development ke liye compile aur hot-reloads

```
npm run serve
```

### Production ke liye compile aur minify

```
npm run build
```

### Files ko lint aur fix karein

```
npm run lint
```

### Configuration ko customize karein

[Configuration Reference](https://cli.vuejs.org/config/) dekhein.

Credits: Is quiz app ke original version ke liye shukriya: https://github.com/arpan45/simple-quiz-vue

## Azure par Deploy karna

Yahan ek step-by-step guide hai jo aapko shuru karne mein madad karegi:

1. GitHub Repository ko Fork karein  
Dhyan rakhein ki aapka static web app code aapki GitHub repository mein ho. Is repository ko fork karein.

2. Ek Azure Static Web App banayein  
- Ek [Azure account](http://azure.microsoft.com) banayein.  
- [Azure portal](https://portal.azure.com) par jaayein.  
- “Create a resource” par click karein aur “Static Web App” search karein.  
- “Create” par click karein.  

3. Static Web App ko Configure karein  
- #### Basics:  
  - Subscription: Apni Azure subscription chunein.  
  - Resource Group: Ek naya resource group banayein ya maujooda wala use karein.  
  - Name: Apne static web app ke liye ek naam dein.  
  - Region: Apne users ke sabse nazdeeki region ko chunein.  

- #### Deployment Details:  
  - Source: “GitHub” chunein.  
  - GitHub Account: Azure ko apne GitHub account tak access dene ki permission dein.  
  - Organization: Apni GitHub organization chunein.  
  - Repository: Woh repository chunein jisme aapka static web app hai.  
  - Branch: Woh branch chunein jisse aap deploy karna chahte hain.  

- #### Build Details:  
  - Build Presets: Woh framework chunein jisse aapka app bana hai (jaise React, Angular, Vue, etc.).  
  - App Location: Woh folder specify karein jisme aapka app code hai (jaise, / agar woh root mein hai).  
  - API Location: Agar aapke paas API hai, toh uski location specify karein (optional).  
  - Output Location: Woh folder specify karein jahan build output generate hota hai (jaise, build ya dist).  

4. Review aur Create  
Apni settings review karein aur “Create” par click karein. Azure zaroori resources set up karega aur aapki repository mein ek GitHub Actions workflow banayega.  

5. GitHub Actions Workflow  
Azure automatically aapki repository mein ek GitHub Actions workflow file banayega (.github/workflows/azure-static-web-apps-<name>.yml). Yeh workflow build aur deployment process ko handle karega.  

6. Deployment ko Monitor karein  
Apni GitHub repository mein “Actions” tab par jaayein.  
Aapko ek workflow chalta hua dikhega. Yeh workflow aapke static web app ko build karke Azure par deploy karega.  
Jaise hi workflow complete hota hai, aapka app diye gaye Azure URL par live ho jaayega.  

### Example Workflow File

Yahan GitHub Actions workflow file ka ek example hai:  
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

### Additional Resources  
- [Azure Static Web Apps Documentation](https://learn.microsoft.com/azure/static-web-apps/getting-started)  
- [GitHub Actions Documentation](https://docs.github.com/actions/use-cases-and-examples/deploying/deploying-to-azure-static-web-app)  

---

<!-- HINGLISH NOTE START -->
**Note**:
Yeh document Hindi translation ko Hinglish (Roman script) mein convert karke banaya gaya hai, taaki padhna aur samajhna aasaan ho.
Isme kuch galtiyan ya anuvaad ki kamiyan ho sakti hain. Sabse sahi jaankari ke liye original English document ko hi authoritative source maanein.
<!-- HINGLISH NOTE END -->
