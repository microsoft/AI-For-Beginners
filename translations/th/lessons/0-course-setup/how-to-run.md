<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "7df19702b8d2d3f7c4238c51bec2c8fc",
  "translation_date": "2025-08-29T08:42:54+00:00",
  "source_file": "lessons/0-course-setup/how-to-run.md",
  "language_code": "th"
}
-->
# วิธีการรันโค้ด

หลักสูตรนี้มีตัวอย่างโค้ดที่สามารถรันได้และแลปที่คุณอาจต้องการทดลองรัน เพื่อทำสิ่งนี้ คุณจำเป็นต้องมีความสามารถในการรันโค้ด Python ใน Jupyter Notebooks ซึ่งเป็นส่วนหนึ่งของหลักสูตรนี้ คุณมีตัวเลือกหลายวิธีในการรันโค้ดดังนี้:

## รันบนคอมพิวเตอร์ของคุณเอง

หากต้องการรันโค้ดบนคอมพิวเตอร์ของคุณเอง คุณจำเป็นต้องติดตั้ง Python เวอร์ชันใดเวอร์ชันหนึ่งไว้ก่อน ฉันขอแนะนำให้ติดตั้ง **[miniconda](https://conda.io/en/latest/miniconda.html)** ซึ่งเป็นการติดตั้งที่มีน้ำหนักเบาและรองรับตัวจัดการแพ็กเกจ `conda` สำหรับ **virtual environments** ของ Python

หลังจากติดตั้ง miniconda คุณต้องโคลน repository และสร้าง virtual environment สำหรับใช้ในหลักสูตรนี้:

```bash
git clone http://github.com/microsoft/ai-for-beginners
cd ai-for-beginners
conda env create --name ai4beg --file .devcontainer/environment.yml
conda activate ai4beg
```

### การใช้ Visual Studio Code พร้อมส่วนขยาย Python

วิธีที่ดีที่สุดในการใช้หลักสูตรนี้คือการเปิดใน [Visual Studio Code](http://code.visualstudio.com/?WT.mc_id=academic-77998-cacaste) พร้อม [Python Extension](https://marketplace.visualstudio.com/items?itemName=ms-python.python&WT.mc_id=academic-77998-cacaste)

> **หมายเหตุ**: เมื่อคุณโคลนและเปิดไดเรกทอรีใน VS Code มันจะแนะนำให้คุณติดตั้งส่วนขยาย Python โดยอัตโนมัติ คุณยังต้องติดตั้ง miniconda ตามที่อธิบายไว้ข้างต้นด้วย

> **หมายเหตุ**: หาก VS Code แนะนำให้คุณเปิด repository ใน container คุณควรปฏิเสธเพื่อใช้การติดตั้ง Python บนเครื่องของคุณเอง

### การใช้ Jupyter ในเบราว์เซอร์

คุณยังสามารถใช้ Jupyter environment ผ่านเบราว์เซอร์บนคอมพิวเตอร์ของคุณเองได้ ทั้ง Jupyter แบบคลาสสิกและ Jupyter Hub นั้นให้สภาพแวดล้อมการพัฒนาที่สะดวกสบาย เช่น การเติมโค้ดอัตโนมัติ การไฮไลต์โค้ด เป็นต้น

หากต้องการเริ่ม Jupyter บนเครื่องของคุณ ให้ไปที่ไดเรกทอรีของหลักสูตรและรันคำสั่ง:

```bash
jupyter notebook
```
หรือ
```bash
jupyterhub
```
จากนั้นคุณสามารถนำทางไปยังไฟล์ `.ipynb` ใดๆ เปิดไฟล์และเริ่มทำงานได้เลย

### การรันใน container

อีกทางเลือกหนึ่งแทนการติดตั้ง Python คือการรันโค้ดใน container เนื่องจาก repository ของเรามีโฟลเดอร์ `.devcontainer` ที่ระบุวิธีการสร้าง container สำหรับ repo นี้ VS Code จะเสนอให้คุณเปิดโค้ดใน container วิธีนี้ต้องการการติดตั้ง Docker และมีความซับซ้อนมากขึ้น ดังนั้นเราขอแนะนำสำหรับผู้ใช้ที่มีประสบการณ์มากกว่า

## การรันในคลาวด์

หากคุณไม่ต้องการติดตั้ง Python บนเครื่องของคุณ และมีทรัพยากรคลาวด์ให้ใช้งาน ทางเลือกที่ดีคือการรันโค้ดในคลาวด์ มีหลายวิธีที่คุณสามารถทำได้:

* ใช้ **[GitHub Codespaces](https://github.com/features/codespaces)** ซึ่งเป็นสภาพแวดล้อมเสมือนที่สร้างขึ้นบน GitHub และเข้าถึงได้ผ่านอินเทอร์เฟซเบราว์เซอร์ของ VS Code หากคุณมีสิทธิ์เข้าถึง Codespaces คุณสามารถคลิกปุ่ม **Code** ใน repo เริ่ม Codespace และเริ่มใช้งานได้ทันที
* ใช้ **[Binder](https://mybinder.org/v2/gh/microsoft/ai-for-beginners/HEAD)** [Binder](https://mybinder.org) เป็นทรัพยากรคอมพิวเตอร์ฟรีในคลาวด์ที่ให้คุณทดลองโค้ดบน GitHub มีปุ่มที่หน้าแรกเพื่อเปิด repository ใน Binder ซึ่งจะนำคุณไปยังเว็บไซต์ Binder ที่จะสร้าง container และเริ่มอินเทอร์เฟซ Jupyter บนเว็บให้คุณโดยอัตโนมัติ

> **หมายเหตุ**: เพื่อป้องกันการใช้งานในทางที่ผิด Binder มีการบล็อกการเข้าถึงทรัพยากรเว็บบางอย่าง ซึ่งอาจทำให้โค้ดบางส่วนที่ดึงโมเดลหรือชุดข้อมูลจากอินเทอร์เน็ตสาธารณะไม่สามารถทำงานได้ คุณอาจต้องหาวิธีแก้ไขปัญหา นอกจากนี้ ทรัพยากรคอมพิวเตอร์ที่ Binder ให้มานั้นค่อนข้างพื้นฐาน ดังนั้นการฝึกโมเดลจะช้า โดยเฉพาะในบทเรียนที่ซับซ้อนในภายหลัง

## การรันในคลาวด์พร้อม GPU

บทเรียนบางส่วนในหลักสูตรนี้จะได้รับประโยชน์อย่างมากจากการรองรับ GPU เพราะไม่เช่นนั้นการฝึกโมเดลจะช้ามาก คุณมีตัวเลือกบางอย่าง โดยเฉพาะหากคุณสามารถเข้าถึงคลาวด์ผ่าน [Azure for Students](https://azure.microsoft.com/free/students/?WT.mc_id=academic-77998-cacaste) หรือผ่านสถาบันของคุณ:

* สร้าง [Data Science Virtual Machine](https://docs.microsoft.com/learn/modules/intro-to-azure-data-science-virtual-machine/?WT.mc_id=academic-77998-cacaste) และเชื่อมต่อกับมันผ่าน Jupyter จากนั้นคุณสามารถโคลน repo ลงในเครื่องและเริ่มเรียนรู้ได้ VM ตระกูล NC มีการรองรับ GPU

> **หมายเหตุ**: การสมัครสมาชิกบางประเภท รวมถึง Azure for Students อาจไม่มีการรองรับ GPU โดยค่าเริ่มต้น คุณอาจต้องส่งคำขอสนับสนุนทางเทคนิคเพื่อขอเพิ่ม GPU cores

* สร้าง [Azure Machine Learning Workspace](https://azure.microsoft.com/services/machine-learning/?WT.mc_id=academic-77998-cacaste) และใช้ฟีเจอร์ Notebook ที่นั่น [วิดีโอนี้](https://azure-for-academics.github.io/quickstart/azureml-papers/) แสดงวิธีโคลน repository ลงใน Azure ML notebook และเริ่มใช้งาน

คุณยังสามารถใช้ Google Colab ซึ่งมีการรองรับ GPU ฟรีบางส่วน และอัปโหลด Jupyter Notebooks ไปที่นั่นเพื่อรันทีละไฟล์ได้

---

**ข้อจำกัดความรับผิดชอบ**:  
เอกสารนี้ได้รับการแปลโดยใช้บริการแปลภาษา AI [Co-op Translator](https://github.com/Azure/co-op-translator) แม้ว่าเราจะพยายามให้การแปลมีความถูกต้อง แต่โปรดทราบว่าการแปลอัตโนมัติอาจมีข้อผิดพลาดหรือความไม่แม่นยำ เอกสารต้นฉบับในภาษาต้นทางควรถือเป็นแหล่งข้อมูลที่เชื่อถือได้ สำหรับข้อมูลที่สำคัญ ขอแนะนำให้ใช้บริการแปลภาษามนุษย์ที่เป็นมืออาชีพ เราจะไม่รับผิดชอบต่อความเข้าใจผิดหรือการตีความที่ผิดพลาดซึ่งเกิดจากการใช้การแปลนี้