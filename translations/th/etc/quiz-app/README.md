# แบบทดสอบ

แบบทดสอบเหล่านี้เป็นแบบทดสอบก่อนและหลังการบรรยายสำหรับหลักสูตร AI ที่ https://aka.ms/ai-beginners

## การเพิ่มชุดแบบทดสอบที่แปลแล้ว

เพิ่มการแปลแบบทดสอบโดยการสร้างโครงสร้างแบบทดสอบที่ตรงกันในโฟลเดอร์ `assets/translations` แบบทดสอบต้นฉบับอยู่ใน `assets/translations/en` แบบทดสอบถูกแบ่งออกเป็นกลุ่มตามบทเรียน ตรวจสอบให้แน่ใจว่าการจัดลำดับหมายเลขตรงกับส่วนแบบทดสอบที่เหมาะสม หลักสูตรนี้มีแบบทดสอบทั้งหมด 40 ชุด โดยเริ่มนับจาก 0

หลังจากแก้ไขการแปลแล้ว ให้แก้ไขไฟล์ index.js ในโฟลเดอร์การแปลเพื่อ import ไฟล์ทั้งหมดตามรูปแบบใน `en`

แก้ไขไฟล์ `index.js` ใน `assets/translations` เพื่อ import ไฟล์แปลใหม่

จากนั้นแก้ไข dropdown ใน `App.vue` ในแอปนี้เพื่อเพิ่มภาษาของคุณ ตรวจสอบให้แน่ใจว่าตัวย่อภาษาตรงกับชื่อโฟลเดอร์ของภาษาของคุณ

สุดท้าย แก้ไขลิงก์แบบทดสอบทั้งหมดในบทเรียนที่แปลแล้ว (ถ้ามี) เพื่อเพิ่ม localization เป็น query parameter เช่น `?loc=fr`

## การตั้งค่าโปรเจกต์

```
npm install
```

### คอมไพล์และรีโหลดอัตโนมัติสำหรับการพัฒนา

```
npm run serve
```

### คอมไพล์และย่อขนาดสำหรับการใช้งานจริง

```
npm run build
```

### ตรวจสอบและแก้ไขไฟล์

```
npm run lint
```

### ปรับแต่งการตั้งค่า

ดู [Configuration Reference](https://cli.vuejs.org/config/)

เครดิต: ขอบคุณเวอร์ชันต้นฉบับของแอปแบบทดสอบนี้: https://github.com/arpan45/simple-quiz-vue

## การปรับใช้บน Azure

นี่คือคำแนะนำทีละขั้นตอนเพื่อช่วยให้คุณเริ่มต้นได้:

1. Fork GitHub Repository  
ตรวจสอบให้แน่ใจว่าโค้ดแอปเว็บแบบสถิตของคุณอยู่ใน GitHub repository ของคุณ Fork repository นี้

2. สร้าง Azure Static Web App  
- สร้าง [บัญชี Azure](http://azure.microsoft.com)  
- ไปที่ [Azure portal](https://portal.azure.com)  
- คลิก “Create a resource” และค้นหา “Static Web App”  
- คลิก “Create”  

3. ตั้งค่า Static Web App  
- พื้นฐาน:  
  - Subscription: เลือกการสมัครใช้งาน Azure ของคุณ  
  - Resource Group: สร้าง resource group ใหม่หรือใช้ที่มีอยู่  
  - Name: ตั้งชื่อให้กับแอปเว็บแบบสถิตของคุณ  
  - Region: เลือกภูมิภาคที่ใกล้กับผู้ใช้ของคุณ  

- #### รายละเอียดการปรับใช้:  
  - Source: เลือก “GitHub”  
  - GitHub Account: อนุญาตให้ Azure เข้าถึงบัญชี GitHub ของคุณ  
  - Organization: เลือกองค์กร GitHub ของคุณ  
  - Repository: เลือก repository ที่มีโค้ดแอปเว็บแบบสถิตของคุณ  
  - Branch: เลือก branch ที่คุณต้องการปรับใช้  

- #### รายละเอียดการสร้าง:  
  - Build Presets: เลือก framework ที่แอปของคุณสร้างขึ้น (เช่น React, Angular, Vue เป็นต้น)  
  - App Location: ระบุโฟลเดอร์ที่มีโค้ดแอปของคุณ (เช่น / หากอยู่ใน root)  
  - API Location: หากคุณมี API ให้ระบุตำแหน่ง (ไม่บังคับ)  
  - Output Location: ระบุโฟลเดอร์ที่สร้างผลลัพธ์การ build (เช่น build หรือ dist)  

4. ตรวจสอบและสร้าง  
ตรวจสอบการตั้งค่าของคุณและคลิก “Create” Azure จะตั้งค่าทรัพยากรที่จำเป็นและสร้าง GitHub Actions workflow ใน repository ของคุณ  

5. GitHub Actions Workflow  
Azure จะสร้างไฟล์ GitHub Actions workflow ใน repository ของคุณโดยอัตโนมัติ (.github/workflows/azure-static-web-apps-<name>.yml) ไฟล์ workflow นี้จะจัดการกระบวนการ build และปรับใช้  

6. ติดตามการปรับใช้  
ไปที่แท็บ “Actions” ใน GitHub repository ของคุณ  
คุณควรเห็น workflow กำลังทำงาน Workflow นี้จะ build และปรับใช้แอปเว็บแบบสถิตของคุณไปยัง Azure  
เมื่อ workflow เสร็จสิ้น แอปของคุณจะออนไลน์บน URL ที่ Azure ให้มา  

### ตัวอย่างไฟล์ Workflow  

นี่คือตัวอย่างไฟล์ GitHub Actions workflow:  
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

### แหล่งข้อมูลเพิ่มเติม  
- [Azure Static Web Apps Documentation](https://learn.microsoft.com/azure/static-web-apps/getting-started)  
- [GitHub Actions Documentation](https://docs.github.com/actions/use-cases-and-examples/deploying/deploying-to-azure-static-web-app)  

---

**ข้อจำกัดความรับผิดชอบ**:  
เอกสารนี้ได้รับการแปลโดยใช้บริการแปลภาษา AI [Co-op Translator](https://github.com/Azure/co-op-translator) แม้ว่าเราจะพยายามให้การแปลมีความถูกต้องมากที่สุด แต่โปรดทราบว่าการแปลโดยอัตโนมัติอาจมีข้อผิดพลาดหรือความไม่ถูกต้อง เอกสารต้นฉบับในภาษาดั้งเดิมควรถือเป็นแหล่งข้อมูลที่เชื่อถือได้ สำหรับข้อมูลที่สำคัญ ขอแนะนำให้ใช้บริการแปลภาษามืออาชีพ เราไม่รับผิดชอบต่อความเข้าใจผิดหรือการตีความผิดที่เกิดจากการใช้การแปลนี้