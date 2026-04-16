# မေးခွန်းများ

ဒီမေးခွန်းများဟာ AI သင်ခန်းစာများအတွက် [!NOTE] သင်ခန်းစာမတိုင်မီနှင့်ပြီးနောက် မေးခွန်းများဖြစ်ပါတယ်။ https://aka.ms/ai-beginners မှာတွေ့နိုင်ပါတယ်။

## ဘာသာပြန်ထားသော မေးခွန်းများထည့်သွင်းခြင်း

ဘာသာပြန်ထားသော မေးခွန်းများကို `assets/translations` ဖိုလ်ဒါတွင် သက်ဆိုင်ရာ မေးခွန်းဖွဲ့စည်းမှုများကို ဖန်တီးခြင်းဖြင့် ထည့်သွင်းပါ။ အခြေခံမေးခွန်းများကို `assets/translations/en` တွင်ရှိပါတယ်။ မေးခွန်းများကို သင်ခန်းစာအလိုက် အုပ်စုများအဖြစ် ခွဲထားပြီး အမှတ်အသားများကို သက်ဆိုင်ရာ မေးခွန်းပိုင်းနှင့် ကိုက်ညီအောင် လိုက်လျောညီထွေစွာထားပါ။ ဒီသင်ခန်းစာမှာ စုစုပေါင်း 40 ခုရှိပြီး အရေအတွက်ကို 0 မှ စတင်ပါတယ်။

ဘာသာပြန်ထားသော မေးခွန်းများကို ပြင်ဆင်ပြီးနောက် `assets/translations` ဖိုလ်ဒါထဲမှာရှိတဲ့ `index.js` ဖိုင်ကို ပြင်ဆင်ပြီး `en` မှာရှိတဲ့ စံနည်းများအတိုင်း ဖိုင်များကို import လုပ်ပါ။

ထို့နောက် ဒီ app ရဲ့ `App.vue` ထဲမှာ dropdown ကို ပြင်ဆင်ပြီး သင့်ဘာသာစကားကို ထည့်သွင်းပါ။ ဘာသာပြန်ထားသော အတိုကောက်ကို သင့်ဘာသာစကားဖိုလ်ဒါနာမည်နှင့် ကိုက်ညီအောင်လုပ်ပါ။

နောက်ဆုံးမှာ ဘာသာပြန်ထားသော သင်ခန်းစာများရှိလျှင် မေးခွန်းလင့်ခ်များကို ပြင်ဆင်ပြီး localization ကို query parameter အနေနဲ့ ထည့်သွင်းပါ။ ဥပမာ `?loc=fr`။

## Project setup

```
npm install
```

### Development အတွက် Compiles နှင့် hot-reloads

```
npm run serve
```

### Production အတွက် Compiles နှင့် minifies

```
npm run build
```

### ဖိုင်များကို Lints နှင့် ပြင်ဆင်ခြင်း

```
npm run lint
```

### Configuration ကို Customize လုပ်ခြင်း

[Configuration Reference](https://cli.vuejs.org/config/) ကိုကြည့်ပါ။

Credit: ဒီ quiz app ရဲ့ မူရင်းဗားရှင်းကို ဖန်တီးသူ https://github.com/arpan45/simple-quiz-vue

## Azure တွင် Deploy လုပ်ခြင်း

ဒီအဆင့်ဆင့်လမ်းညွှန်ကို အသုံးပြုပြီး စတင်နိုင်ပါသည်-

1. GitHub Repository ကို Fork လုပ်ပါ  
သင့် static web app code ကို သင့် GitHub repository ထဲမှာရှိအောင်လုပ်ပါ။ ဒီ repository ကို Fork လုပ်ပါ။

2. Azure Static Web App တစ်ခုဖန်တီးပါ  
- [Azure account](http://azure.microsoft.com) တစ်ခုဖန်တီးပါ  
- [Azure portal](https://portal.azure.com) ကိုသွားပါ  
- “Create a resource” ကိုနှိပ်ပြီး “Static Web App” ကို ရှာပါ။  
- “Create” ကိုနှိပ်ပါ။

3. Static Web App ကို Configure လုပ်ပါ  
- Basics: Subscription: သင့် Azure subscription ကို ရွေးပါ။  
- Resource Group: အသစ် resource group တစ်ခုဖန်တီးပါ သို့မဟုတ် ရှိပြီးသားကို အသုံးပြုပါ။  
- Name: သင့် static web app အတွက် နာမည်ပေးပါ။  
- Region: သင့်အသုံးပြုသူများနီးစပ်ရာဒေသကို ရွေးပါ။

- #### Deployment Details:
- Source: “GitHub” ကို ရွေးပါ။  
- GitHub Account: Azure ကို သင့် GitHub account ကို access လုပ်ခွင့်ပေးပါ။  
- Organization: သင့် GitHub organization ကို ရွေးပါ။  
- Repository: သင့် static web app ပါဝင်တဲ့ repository ကို ရွေးပါ။  
- Branch: Deploy လုပ်ချင်တဲ့ branch ကို ရွေးပါ။

- #### Build Details:
- Build Presets: သင့် app ဖန်တီးထားတဲ့ framework ကို ရွေးပါ (ဥပမာ React, Angular, Vue, စသည်တို့)။  
- App Location: သင့် app code ပါဝင်တဲ့ folder ကို ဖော်ပြပါ (ဥပမာ / သင့် root မှာရှိလျှင်)။  
- API Location: API ရှိလျှင် location ကို ဖော်ပြပါ (optional)။  
- Output Location: build output ဖိုင်များ ဖန်တီးထားတဲ့ folder ကို ဖော်ပြပါ (ဥပမာ build သို့မဟုတ် dist)။

4. Review နှင့် Create  
သင့် settings ကို ပြန်လည်သုံးသပ်ပြီး “Create” ကိုနှိပ်ပါ။ Azure သက်ဆိုင်ရာ resources များကို ဖန်တီးပြီး သင့် repository ထဲမှာ GitHub Actions workflow တစ်ခု ဖန်တီးပါမည်။

5. GitHub Actions Workflow  
Azure သင့် repository ထဲမှာ GitHub Actions workflow ဖိုင် (.github/workflows/azure-static-web-apps-<name>.yml) ကို အလိုအလျောက် ဖန်တီးပါမည်။ ဒီ workflow က build နှင့် deployment လုပ်ငန်းစဉ်ကို စီမံပါမည်။

6. Deployment ကို Monitor လုပ်ပါ  
သင့် GitHub repository ရဲ့ “Actions” tab ကိုသွားပါ။  
Workflow တစ်ခု run ဖြစ်နေသည်ကို တွေ့ရပါမည်။ ဒီ workflow က သင့် static web app ကို Azure တွင် build နှင့် deploy လုပ်ပါမည်။  
Workflow ပြီးဆုံးပြီးနောက် သင့် app ကို Azure URL မှာ live ဖြစ်နေပါမည်။

### Workflow ဖိုင် ဥပမာ

GitHub Actions workflow ဖိုင်ရဲ့ ဥပမာကို အောက်မှာကြည့်ပါ:  
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

### အပိုဆောင်း Resources  
- [Azure Static Web Apps Documentation](https://learn.microsoft.com/azure/static-web-apps/getting-started)  
- [GitHub Actions Documentation](https://docs.github.com/actions/use-cases-and-examples/deploying/deploying-to-azure-static-web-app)  

**အကြောင်းကြားချက်**:  
ဤစာရွက်စာတမ်းကို AI ဘာသာပြန်ဝန်ဆောင်မှု [Co-op Translator](https://github.com/Azure/co-op-translator) ကို အသုံးပြု၍ ဘာသာပြန်ထားပါသည်။ ကျွန်ုပ်တို့သည် တိကျမှုအတွက် ကြိုးစားနေသော်လည်း၊ အလိုအလျောက် ဘာသာပြန်မှုများတွင် အမှားများ သို့မဟုတ် မမှန်ကန်မှုများ ပါဝင်နိုင်သည်ကို သတိပြုပါ။ မူရင်းဘာသာစကားဖြင့် ရေးသားထားသော စာရွက်စာတမ်းကို အာဏာတရ အရင်းအမြစ်အဖြစ် သတ်မှတ်သင့်ပါသည်။ အရေးကြီးသော အချက်အလက်များအတွက် လူက ဘာသာပြန်မှုကို အသုံးပြုရန် အကြံပြုပါသည်။ ဤဘာသာပြန်မှုကို အသုံးပြုခြင်းမှ ဖြစ်ပေါ်လာသော အလွဲအလွတ်များ သို့မဟုတ် အနားယူမှားမှုများအတွက် ကျွန်ုပ်တို့သည် တာဝန်မယူပါ။