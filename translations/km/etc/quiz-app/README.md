# ការប្រលង

ការប្រលង​ទាំងនេះ​គឺជាការប្រលងមុននិងបន្ទាប់ពីមេរៀនសម្រាប់មុខវិជ្ជា AI នៅ https://aka.ms/ai-beginners

## ការបន្ថែមសំណុំការប្រលងបកប្រែ

បន្ថែមការបកប្រែការប្រលងដោយបង្កើតរចនាសម្ព័ន្ធការប្រលងដែលត្រូវគ្នានៅក្នុងថត `assets/translations`។ ការប្រលងតែមួយគត់មាននៅក្នុង `assets/translations/en`។ ការប្រលងត្រូវបានបំបែកជាក្រុមជាច្រើនតាមមេរៀន។ ពិនិត្យឲ្យប្រាកដថាជួរលេខត្រូវតាមផ្នែកការប្រលងត្រឹមត្រូវ។ មានការប្រលងសរុប ៤០ ក្នុងមុខវិជ្ជានេះ ហើយការរាប់ចាប់ផ្តើមពី ០។

បន្ទាប់ពីកែសម្រួលការបកប្រែ សូមកែសម្រួលឯកសារ index.js នៅក្នុងថតការបកប្រែ ដើម្បីនាំចូលឯកសារទាំងអស់តាមបទបញ្ជានៅក្នុង `en`។

កែសម្រួលឯកសារ `index.js` នៅក្នុង `assets/translations` ដើម្បីនាំចូលឯកសារបកប្រែថ្មី។

បន្ទាប់ពីនេះ កែសម្រួលចុចជ្រើសរើសភាសា(dropdown) នៅក្នុង `App.vue` ក្នុងកម្មវិធីនេះ ដើម្បីបន្ថែមភាសារបស់អ្នក។ ត្រូវផ្គូផ្គងអក្សររួមតំណាងភាសានេះជាមួយឈ្មោះថតសម្រាប់ភាសារបស់អ្នក។

ចុងក្រោយ កែសម្រួលតំណភ្ជាប់ការប្រលងទាំងអស់នៅក្នុងមេរៀនបកប្រែ ប្រសិនបើវាមាន ដើម្បីបញ្ចូលការបកប្រែទីនេះជាពណ៌នាការស្នើសុំនៅ query parameter: `?loc=fr` ជាឧទាហរណ៍។

## ការតំឡើងគម្រោង

```
npm install
```

### ការបញ្ចូលនិងផ្ទុកឡើងឡើងវិញសម្រាប់ការអភិវឌ្ឍន៍

```
npm run serve
```

### ការបញ្ចូលនិងកាត់បន្ថយសម្រាប់ការផលិត

```
npm run build
```

### ការត្រួតពិនិត្យនិងជួសជុលឯកសារ

```
npm run lint
```

### ការប្តូរតំរូវការផ្ទាល់ខ្លួន

មើល [យោងការកំណត់](https://cli.vuejs.org/config/)។

ឥណទាន៖ អរគុណចំពោះមួយនៃកំណែដើមនៃកម្មវិធីការប្រលងនេះ៖ https://github.com/arpan45/simple-quiz-vue

## ការបង្ហោះទៅកាន់ Azure

នេះជាមគ្គុទេសក៍ជាគន្លឹះជំហាន-ដោយ-ជំហានដើម្បីជួយអ្នកចាប់ផ្តើម៖

1. Fork ប្រភព GitHub មួយ
ធានាថាកូដកម្មវិធីវេបស្ថិតស្ថិតរបស់អ្នកមាននៅក្នុងកន្លែងបញ្ជារ GitHub របស់អ្នក។ Fork ប្រភពនេះ។

2. បង្កើត Azure Static Web App
- បង្កើត និង [គណនី Azure](http://azure.microsoft.com)
- ចូលទៅកាន់ [portal Azure](https://portal.azure.com) 
- ចុចលើ “Create a resource” ហើយស្វែងរក “Static Web App”។
- ចុច “Create”។

3. កំណត់រចនាសម្ព័ន្ធ Static Web App
- មូលដ្ឋាន៖ Subscription: ជ្រើសរើសការជាវ Azure របស់អ្នក។
- Resource Group: បង្កើតក្រុមធនធានថ្មីឬប្រើក្រុមដែលមានរួចហើយ។
- Name: ផ្ដល់ឈ្មោះសម្រាប់កម្មវិធីវេបស្ថិតរបស់អ្នក។
- តំបន់៖ ជ្រើសរើសតំបន់ដែលនៅជិតអ្នកប្រើប្រាស់របស់អ្នកបំផុត។

- #### ព័ត៌មានការបង្ហោះ:
- ប្រភព: ជ្រើសរើស “GitHub”។
- គណនី GitHub: អនុញ្ញាតអោយ Azure ទទួលបានការចូលទៅគណនី GitHub របស់អ្នក។
- សហគមន៍: ជ្រើសរើសសហគមន៍ GitHub របស់អ្នក។
- ឃ្លាំងកូដ: ជ្រើសឃ្លាំងកូដដែលមានកម្មវិធីវេបស្ថិតរបស់អ្នក។
- សាខា៖ ជ្រើសរើសសាខាដែលអ្នកចង់បង្ហោះពី។

- #### ព័ត៌មានសំណង់:
- ការកំណត់សំណង់៖ ជ្រើសរើសបណ្ដុំអាវផេកដែលកម្មវិធីរបស់អ្នកបានសង់ជាមួយ (ឧ. React, Angular, Vue, ល។)។
- ទីតាំងកម្មវិធី៖ បញ្ជាក់ថតឯកសារដែលមានកូដកម្មវិធីរបស់អ្នក (ឧ. / ប្រសិនបើវានៅក្នុងជម្រុះ)។
- ទីតាំង API៖ ប្រសិនបើអ្នកមាន API បញ្ជាក់ទីតាំងរបស់វា (ជាជម្រើស)។
- ទីតាំងលទ្ធផល៖ បញ្ជាក់ថតឯកសារដែលផលលទ្ធផលសំណង់ត្រូវបង្កើត (ឧ. build ឬ dist)។

4. ពិនិត្យហើយបង្កើត
ពិនិត្យការកំណត់របស់អ្នកហើយចុច "Create"។ Azure នឹងរៀបចំធនធានចាំបាច់ និងបង្កើតកម្មវិធី GitHub Actions ក្នុងឃ្លាំងកូដរបស់អ្នក។

5. កម្មវិធី GitHub Actions
Azure នឹងបង្កើតឯកសារកម្មវិធី GitHub Actions ដោយស្វ័យប្រវត្តិនៅក្នុងឃ្លាំងកូដរបស់អ្នក (.github/workflows/azure-static-web-apps-<name>.yml)។ កម្មវិធីនេះនឹងរៀបចំដំណើរការសំណង់និងការបង្ហោះ។

6. តាមដានការបង្ហោះ
ចូលទៅកាន់ផ្ទាំង “Actions” ក្នុងឃ្លាំងកូដ GitHub របស់អ្នក។
អ្នកគួរមើលឃើញកម្មវិធីកំពុងដំណើរការ។ កម្មវិធីនេះនឹងសង់និងបង្ហោះកម្មវិធីវេបស្ថិតរបស់អ្នកទៅ Azure។
ពេលដែលកម្មវិធីបញ្ចប់ កម្មវិធីរបស់អ្នកនឹងមាននៅលើ URL Azure ដែលបានផ្ដល់។

### ឧទាហរណ៍ឯកសារ Workflow

នេះជាឧទាហរណ៍ឯកសារកម្មវិធី GitHub Actions ដែលអាចមានរូបរាងដូចខាងក្រោម៖
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

### ឧបករណ៍បន្ថែម
- [ឯកសារអំពី Azure Static Web Apps](https://learn.microsoft.com/azure/static-web-apps/getting-started)
- [ឯកសារអំពី GitHub Actions](https://docs.github.com/actions/use-cases-and-examples/deploying/deploying-to-azure-static-web-app)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ការបដិសេធ**៖  
ឯកសារនេះត្រូវបានបកប្រែដោយប្រើសេវាបកប្រែ AI [Co-op Translator](https://github.com/Azure/co-op-translator)។ ខណៈពួកយើងខិតខំទទួលប្រាកដភាព ពPleaseរយៈពេលដឹងថាការបកប្រែដោយស្វ័យប្រវត្តិអាចមានកំហុសឬការខុសឡើង។ ឯកសារដើមក្នុងភាសាតែមួយគួរត្រូវបានចាត់ទុកជាឯកសារដែលមានអំណាចច្បាស់លាស់។ សម្រាប់ព័ត៌មានសំខាន់ៗ សូមណែនាំឱ្យប្រើការបកប្រែដោយមនុស្សជំនាញវិជ្ជាជីវៈ។ យើងមិនទទួលខុសត្រូវចំពោះការយល់ច្រឡំនូវកំហុស ឬការបកប្រែខុស ណាដែលកើតឡើងពីការប្រើប្រាស់ការបកប្រែនេះទេ។
<!-- CO-OP TRANSLATOR DISCLAIMER END -->