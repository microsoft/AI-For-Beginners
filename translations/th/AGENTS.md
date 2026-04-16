# AGENTS.md

## ภาพรวมโครงการ

AI for Beginners เป็นหลักสูตรครอบคลุมระยะเวลา 12 สัปดาห์ ประกอบด้วย 24 บทเรียนที่ครอบคลุมพื้นฐานของปัญญาประดิษฐ์ (AI) โครงการนี้มีบทเรียนเชิงปฏิบัติที่ใช้ Jupyter Notebooks แบบฝึกหัด และห้องปฏิบัติการจริง หลักสูตรครอบคลุมหัวข้อดังนี้:

- AI เชิงสัญลักษณ์ด้วยการแทนความรู้และระบบผู้เชี่ยวชาญ
- เครือข่ายประสาทและการเรียนรู้เชิงลึกด้วย TensorFlow และ PyTorch
- เทคนิคและสถาปัตยกรรมการมองเห็นด้วยคอมพิวเตอร์
- การประมวลผลภาษาธรรมชาติ (NLP) รวมถึง transformers และ BERT
- หัวข้อเฉพาะทาง: อัลกอริทึมทางพันธุกรรม, การเรียนรู้แบบเสริมกำลัง, ระบบหลายตัวแทน
- จริยธรรม AI และหลักการ AI ที่รับผิดชอบ

**เทคโนโลยีหลัก:** Python 3, Jupyter Notebooks, TensorFlow, PyTorch, Keras, OpenCV, Vue.js (สำหรับแอปแบบทดสอบ)

**สถาปัตยกรรม:** คลังเนื้อหาการศึกษา พร้อม Jupyter Notebooks ที่จัดระเบียบตามหัวข้อ และแอปแบบทดสอบที่พัฒนาด้วย Vue.js พร้อมการสนับสนุนหลายภาษาอย่างกว้างขวาง

## คำสั่งการตั้งค่า

### สภาพแวดล้อมการพัฒนาหลัก (Python/Jupyter)

หลักสูตรนี้ออกแบบมาให้ทำงานร่วมกับ Python และ Jupyter Notebooks วิธีที่แนะนำคือการใช้ miniconda:

```bash
# Clone the repository
git clone https://github.com/microsoft/ai-for-beginners
cd ai-for-beginners

# Create and activate conda environment
conda env create --name ai4beg --file environment.yml
conda activate ai4beg

# Start Jupyter Notebook
jupyter notebook
# OR
jupyter lab
```

### ทางเลือก: ใช้ devcontainer

```bash
# Open in VS Code and select "Reopen in Container" when prompted
# The devcontainer will automatically set up the environment
```

### การตั้งค่าแอปแบบทดสอบ

แอปแบบทดสอบเป็นแอป Vue.js แยกต่างหากที่อยู่ใน `etc/quiz-app/`:

```bash
cd etc/quiz-app
npm install
npm run serve  # Development server
npm run build  # Production build
npm run lint   # Lint and fix files
```

## เวิร์กโฟลว์การพัฒนา

### การทำงานกับ Jupyter Notebooks

1. **การพัฒนาในเครื่อง:**
   - เปิดใช้งานสภาพแวดล้อม conda: `conda activate ai4beg`
   - เริ่ม Jupyter: `jupyter notebook` หรือ `jupyter lab`
   - ไปที่โฟลเดอร์บทเรียนและเปิดไฟล์ `.ipynb`
   - รันเซลล์แบบโต้ตอบเพื่อทำตามบทเรียน

2. **VS Code พร้อมส่วนขยาย Python:**
   - เปิดคลังใน VS Code
   - ติดตั้งส่วนขยาย Python
   - VS Code จะตรวจจับและใช้สภาพแวดล้อม conda โดยอัตโนมัติ
   - เปิดไฟล์ `.ipynb` โดยตรงใน VS Code

3. **การพัฒนาในคลาวด์:**
   - **GitHub Codespaces:** คลิก "Code" → "Codespaces" → "Create codespace on main"
   - **Binder:** ใช้ป้าย Binder บน README เพื่อเปิดในเบราว์เซอร์
   - หมายเหตุ: Binder มีทรัพยากรจำกัดและข้อจำกัดการเข้าถึงเว็บบางประการ

### การสนับสนุน GPU สำหรับบทเรียนขั้นสูง

บทเรียนในภายหลังจะได้รับประโยชน์อย่างมากจากการเร่งความเร็วด้วย GPU:

- **Azure Data Science VM:** ใช้ VM ซีรีส์ NC ที่รองรับ GPU
- **Azure Machine Learning:** ใช้ฟีเจอร์โน้ตบุ๊กพร้อมการประมวลผล GPU
- **Google Colab:** อัปโหลดโน้ตบุ๊กทีละตัว (มีการสนับสนุน GPU ฟรี)

### การพัฒนาแอปแบบทดสอบ

```bash
cd etc/quiz-app
npm run serve  # Hot-reload development server at http://localhost:8080
```

## คำแนะนำการทดสอบ

คลังนี้มุ่งเน้นไปที่เนื้อหาการเรียนรู้มากกว่าการทดสอบซอฟต์แวร์ ไม่มีชุดการทดสอบแบบดั้งเดิม

### วิธีการตรวจสอบ:

1. **Jupyter Notebooks:** รันเซลล์ตามลำดับเพื่อยืนยันว่าโค้ดตัวอย่างทำงานได้
2. **การทดสอบแอปแบบทดสอบ:** ทดสอบด้วยตนเองผ่านเซิร์ฟเวอร์พัฒนา
3. **การตรวจสอบการแปล:** ตรวจสอบเนื้อหาที่แปลในโฟลเดอร์ `translations/`
4. **การตรวจสอบ linting แอปแบบทดสอบ:** `npm run lint` ใน `etc/quiz-app/`

### การรันโค้ดตัวอย่าง:

```bash
# Activate environment first
conda activate ai4beg

# Run Python scripts directly
python lessons/4-ComputerVision/07-ConvNets/pytorchcv.py

# Or execute notebooks
jupyter notebook lessons/3-NeuralNetworks/03-Perceptron/Perceptron.ipynb
```

## รูปแบบโค้ด

### รูปแบบโค้ด Python

- ใช้รูปแบบมาตรฐาน Python สำหรับโค้ดการศึกษา
- โค้ดที่ชัดเจนและอ่านง่าย โดยเน้นการเรียนรู้มากกว่าการปรับแต่ง
- มีคอมเมนต์อธิบายแนวคิดสำคัญ
- เป็นมิตรกับ Jupyter Notebook: เซลล์ควรเป็นแบบแยกตัวเองได้มากที่สุด
- ไม่มีข้อกำหนด linting ที่เข้มงวดสำหรับเนื้อหาบทเรียน

### JavaScript/Vue.js (แอปแบบทดสอบ)

- การตั้งค่า ESLint ใน `etc/quiz-app/package.json`
- รัน `npm run lint` เพื่อตรวจสอบและแก้ไขปัญหาอัตโนมัติ
- ใช้รูปแบบ Vue 2.x
- สถาปัตยกรรมแบบคอมโพเนนต์

### การจัดระเบียบไฟล์

```
lessons/
  ├── 0-course-setup/          # Setup instructions
  ├── 1-Intro/                 # Introduction to AI
  ├── 2-Symbolic/              # Symbolic AI
  ├── 3-NeuralNetworks/        # Neural Networks basics
  ├── 4-ComputerVision/        # Computer Vision
  ├── 5-NLP/                   # Natural Language Processing
  ├── 6-Other/                 # Other AI techniques
  ├── 7-Ethics/                # AI Ethics
  └── X-Extras/                # Additional content

etc/
  ├── quiz-app/                # Vue.js quiz application
  └── quiz-src/                # Quiz source files

translations/                  # Multi-language translations
```

## การสร้างและการปรับใช้

### เนื้อหา Jupyter

ไม่จำเป็นต้องมีขั้นตอนการสร้าง - Jupyter Notebooks ถูกใช้งานโดยตรง

### แอปแบบทดสอบ

```bash
cd etc/quiz-app

# Development
npm run serve

# Production build
npm run build  # Outputs to etc/quiz-app/dist/

# Deploy to Azure Static Web Apps
# Azure automatically creates GitHub Actions workflow
# See etc/quiz-app/README.md for detailed deployment instructions
```

### เว็บไซต์เอกสาร

คลังนี้ใช้ Docsify สำหรับเอกสาร:
- `index.html` เป็นจุดเริ่มต้น
- ไม่จำเป็นต้องสร้าง - ให้บริการโดยตรงผ่าน GitHub Pages
- เข้าถึงได้ที่: https://microsoft.github.io/AI-For-Beginners/

## แนวทางการมีส่วนร่วม

### กระบวนการ Pull Request

1. **รูปแบบชื่อเรื่อง:** ชื่อเรื่องที่ชัดเจนและอธิบายการเปลี่ยนแปลง
2. **ข้อกำหนด CLA:** ต้องลงนาม Microsoft CLA (ตรวจสอบอัตโนมัติ)
3. **แนวทางเนื้อหา:**
   - รักษาโฟกัสการศึกษาและแนวทางที่เป็นมิตรกับผู้เริ่มต้น
   - ทดสอบโค้ดตัวอย่างทั้งหมดในโน้ตบุ๊ก
   - ตรวจสอบให้แน่ใจว่าโน้ตบุ๊กรันได้ตั้งแต่ต้นจนจบ
   - อัปเดตการแปลหากมีการแก้ไขเนื้อหาภาษาอังกฤษ
4. **การเปลี่ยนแปลงแอปแบบทดสอบ:** รัน `npm run lint` ก่อน commit

### การมีส่วนร่วมในการแปล

- การแปลเป็นไปโดยอัตโนมัติผ่าน GitHub Actions โดยใช้ co-op-translator
- การแปลด้วยตนเองอยู่ใน `translations/<language-code>/`
- การแปลแบบทดสอบอยู่ใน `etc/quiz-app/src/assets/translations/`
- รองรับภาษา: มากกว่า 40 ภาษา (ดู README สำหรับรายการเต็ม)

### พื้นที่การมีส่วนร่วมที่ใช้งานอยู่

ดู `etc/CONTRIBUTING.md` สำหรับความต้องการปัจจุบัน:
- ส่วนการเรียนรู้แบบเสริมกำลังเชิงลึก
- การปรับปรุงการตรวจจับวัตถุ
- ตัวอย่างการจดจำเอนทิตีที่มีชื่อ
- ตัวอย่างการฝึกฝังแบบกำหนดเอง

## การตั้งค่าสภาพแวดล้อม

### การพึ่งพาที่จำเป็น

```bash
# Core Python packages (from requirements.txt)
tensorflow==2.17.0
torch (via conda)
torchvision (via conda)
keras==3.5.0
opencv (via conda)
scikit-learn
numpy==1.26
pandas==2.2.2
matplotlib==3.9
jupyter
```

### ตัวแปรสภาพแวดล้อม

ไม่จำเป็นต้องมีตัวแปรสภาพแวดล้อมพิเศษสำหรับการใช้งานพื้นฐาน

สำหรับการปรับใช้ Azure (แอปแบบทดสอบ):
- `AZURE_STATIC_WEB_APPS_API_TOKEN` (ตั้งค่าโดยอัตโนมัติโดย Azure)

## การแก้ไขข้อบกพร่องและการแก้ปัญหา

### ปัญหาทั่วไป

**ปัญหา:** การสร้างสภาพแวดล้อม conda ล้มเหลว
- **วิธีแก้ไข:** อัปเดต conda ก่อน: `conda update conda -y`
- ตรวจสอบให้แน่ใจว่ามีพื้นที่ดิสก์เพียงพอ (แนะนำ 50GB)

**ปัญหา:** ไม่พบ kernel ของ Jupyter
- **วิธีแก้ไข:** 
  ```bash
  conda activate ai4beg
  python -m ipykernel install --user --name ai4beg
  ```

**ปัญหา:** ไม่พบ GPU ในโน้ตบุ๊ก
- **วิธีแก้ไข:** 
  - ตรวจสอบการติดตั้ง CUDA: `nvidia-smi`
  - ตรวจสอบ GPU ของ PyTorch: `python -c "import torch; print(torch.cuda.is_available())"`
  - ตรวจสอบ GPU ของ TensorFlow: `python -c "import tensorflow as tf; print(tf.config.list_physical_devices('GPU'))"`

**ปัญหา:** แอปแบบทดสอบไม่เริ่มต้น
- **วิธีแก้ไข:**
  ```bash
  cd etc/quiz-app
  rm -rf node_modules package-lock.json
  npm install
  npm run serve
  ```

**ปัญหา:** Binder หมดเวลาหรือบล็อกการดาวน์โหลด
- **วิธีแก้ไข:** ใช้ GitHub Codespaces หรือการตั้งค่าในเครื่องเพื่อการเข้าถึงทรัพยากรที่ดีกว่า

### ปัญหาหน่วยความจำ

บทเรียนบางส่วนต้องการ RAM จำนวนมาก (แนะนำ 8GB+):
- ใช้ VM คลาวด์สำหรับบทเรียนที่ใช้ทรัพยากรมาก
- ปิดแอปพลิเคชันอื่นเมื่อฝึกโมเดล
- ลดขนาด batch ในโน้ตบุ๊กหากหน่วยความจำไม่เพียงพอ

## หมายเหตุเพิ่มเติม

### สำหรับผู้สอนหลักสูตร

- ดู `lessons/0-course-setup/for-teachers.md` สำหรับคำแนะนำการสอน
- บทเรียนเป็นแบบแยกตัวเองและสามารถสอนได้ตามลำดับหรือเลือกเฉพาะบางบท
- เวลาที่ประมาณการ: 12 สัปดาห์ที่ 2 บทเรียนต่อสัปดาห์

### ทรัพยากรคลาวด์

- **Azure for Students:** เครดิตฟรีสำหรับนักเรียน
- **Microsoft Learn:** เส้นทางการเรียนรู้เสริมที่เชื่อมโยงตลอดหลักสูตร
- **Binder:** ฟรีแต่มีทรัพยากรจำกัดและข้อจำกัดเครือข่ายบางประการ

### ตัวเลือกการรันโค้ด

1. **ในเครื่อง (แนะนำ):** ควบคุมได้เต็มที่ ประสิทธิภาพดีที่สุด รองรับ GPU
2. **GitHub Codespaces:** VS Code บนคลาวด์ เข้าถึงได้รวดเร็ว
3. **Binder:** Jupyter บนเบราว์เซอร์ ฟรีแต่จำกัด
4. **Azure ML Notebooks:** ตัวเลือกองค์กรพร้อมการสนับสนุน GPU
5. **Google Colab:** อัปโหลดโน้ตบุ๊กทีละตัว มี GPU ฟรีให้บริการ

### การทำงานกับโน้ตบุ๊ก

- โน้ตบุ๊กออกแบบมาให้รันทีละเซลล์เพื่อการเรียนรู้
- โน้ตบุ๊กหลายตัวดาวน์โหลดชุดข้อมูลในการรันครั้งแรก (อาจใช้เวลา)
- โมเดลบางตัวต้องการ GPU เพื่อเวลาฝึกที่เหมาะสม
- ใช้โมเดลที่ฝึกไว้ล่วงหน้าเพื่อลดความต้องการการประมวลผล

### การพิจารณาด้านประสิทธิภาพ

- บทเรียนการมองเห็นด้วยคอมพิวเตอร์ในภายหลัง (CNNs, GANs) ได้รับประโยชน์จาก GPU
- บทเรียน NLP transformer อาจต้องการ RAM จำนวนมาก
- การฝึกจากศูนย์มีประโยชน์ทางการศึกษาแต่ใช้เวลานาน
- ตัวอย่างการเรียนรู้แบบถ่ายโอนช่วยลดเวลาในการฝึก

---

**ข้อจำกัดความรับผิดชอบ**:  
เอกสารนี้ได้รับการแปลโดยใช้บริการแปลภาษา AI [Co-op Translator](https://github.com/Azure/co-op-translator) แม้ว่าเราจะพยายามให้การแปลมีความถูกต้อง แต่โปรดทราบว่าการแปลอัตโนมัติอาจมีข้อผิดพลาดหรือความไม่ถูกต้อง เอกสารต้นฉบับในภาษาดั้งเดิมควรถือเป็นแหล่งข้อมูลที่เชื่อถือได้ สำหรับข้อมูลที่สำคัญ ขอแนะนำให้ใช้บริการแปลภาษามนุษย์ที่มีความเชี่ยวชาญ เราไม่รับผิดชอบต่อความเข้าใจผิดหรือการตีความผิดที่เกิดจากการใช้การแปลนี้