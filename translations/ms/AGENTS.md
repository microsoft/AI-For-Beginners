# AGENTS.md

## Gambaran Projek

AI for Beginners adalah kurikulum 12 minggu dengan 24 pelajaran yang merangkumi asas Kecerdasan Buatan. Repositori pendidikan ini termasuk pelajaran praktikal menggunakan Jupyter Notebooks, kuiz, dan makmal hands-on. Kurikulum ini merangkumi:

- AI Simbolik dengan Representasi Pengetahuan dan Sistem Pakar
- Rangkaian Neural dan Pembelajaran Mendalam dengan TensorFlow dan PyTorch
- Teknik dan seni bina Penglihatan Komputer
- Pemprosesan Bahasa Semula Jadi (NLP) termasuk transformer dan BERT
- Topik khusus: Algoritma Genetik, Pembelajaran Pengukuhan, Sistem Multi-Ejen
- Etika AI dan prinsip AI Bertanggungjawab

**Teknologi Utama:** Python 3, Jupyter Notebooks, TensorFlow, PyTorch, Keras, OpenCV, Vue.js (untuk aplikasi kuiz)

**Seni Bina:** Repositori kandungan pendidikan dengan Jupyter Notebooks yang diatur mengikut bidang topik, dilengkapi dengan aplikasi kuiz berasaskan Vue.js dan sokongan pelbagai bahasa yang meluas.

## Perintah Persediaan

### Persekitaran Pembangunan Utama (Python/Jupyter)

Kurikulum ini direka untuk dijalankan dengan Python dan Jupyter Notebooks. Pendekatan yang disyorkan adalah menggunakan miniconda:

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

### Alternatif: Menggunakan devcontainer

```bash
# Open in VS Code and select "Reopen in Container" when prompted
# The devcontainer will automatically set up the environment
```

### Persediaan Aplikasi Kuiz

Aplikasi kuiz adalah aplikasi Vue.js yang berasingan yang terletak di `etc/quiz-app/`:

```bash
cd etc/quiz-app
npm install
npm run serve  # Development server
npm run build  # Production build
npm run lint   # Lint and fix files
```

## Aliran Kerja Pembangunan

### Bekerja dengan Jupyter Notebooks

1. **Pembangunan Tempatan:**
   - Aktifkan persekitaran conda: `conda activate ai4beg`
   - Mulakan Jupyter: `jupyter notebook` atau `jupyter lab`
   - Navigasi ke folder pelajaran dan buka fail `.ipynb`
   - Jalankan sel secara interaktif untuk mengikuti pelajaran

2. **VS Code dengan Sambungan Python:**
   - Buka repositori dalam VS Code
   - Pasang sambungan Python
   - VS Code secara automatik mengesan dan menggunakan persekitaran conda
   - Buka fail `.ipynb` secara langsung dalam VS Code

3. **Pembangunan Awan:**
   - **GitHub Codespaces:** Klik "Code" → "Codespaces" → "Create codespace on main"
   - **Binder:** Gunakan lencana Binder pada README untuk melancarkan dalam pelayar
   - Nota: Binder mempunyai sumber terhad dan beberapa sekatan akses web

### Sokongan GPU untuk Pelajaran Lanjutan

Pelajaran kemudian mendapat manfaat besar daripada pecutan GPU:

- **Azure Data Science VM:** Gunakan VM siri NC dengan sokongan GPU
- **Azure Machine Learning:** Gunakan ciri notebook dengan pengiraan GPU
- **Google Colab:** Muat naik notebook secara individu (mempunyai sokongan GPU percuma)

### Pembangunan Aplikasi Kuiz

```bash
cd etc/quiz-app
npm run serve  # Hot-reload development server at http://localhost:8080
```

## Arahan Pengujian

Ini adalah repositori pendidikan yang fokus pada kandungan pembelajaran dan bukan pengujian perisian. Tiada suite ujian tradisional.

### Pendekatan Pengesahan:

1. **Jupyter Notebooks:** Jalankan sel secara berurutan untuk mengesahkan contoh kod berfungsi
2. **Pengujian Aplikasi Kuiz:** Pengujian manual melalui pelayan pembangunan
3. **Pengesahan Terjemahan:** Periksa kandungan terjemahan dalam folder `translations/`
4. **Linting Aplikasi Kuiz:** `npm run lint` dalam `etc/quiz-app/`

### Menjalankan Contoh Kod:

```bash
# Activate environment first
conda activate ai4beg

# Run Python scripts directly
python lessons/4-ComputerVision/07-ConvNets/pytorchcv.py

# Or execute notebooks
jupyter notebook lessons/3-NeuralNetworks/03-Perceptron/Perceptron.ipynb
```

## Gaya Kod

### Gaya Kod Python

- Konvensyen Python standard untuk kod pendidikan
- Kod yang jelas dan mudah dibaca, mengutamakan pembelajaran berbanding pengoptimuman
- Komen yang menerangkan konsep utama
- Mesra Jupyter Notebook: sel harus berdiri sendiri di mana mungkin
- Tiada keperluan linting ketat untuk kandungan pelajaran

### JavaScript/Vue.js (Aplikasi Kuiz)

- Konfigurasi ESLint dalam `etc/quiz-app/package.json`
- Jalankan `npm run lint` untuk memeriksa dan membetulkan isu secara automatik
- Konvensyen Vue 2.x
- Seni bina berasaskan komponen

### Pengorganisasian Fail

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

## Pembinaan dan Pengedaran

### Kandungan Jupyter

Tiada proses pembinaan diperlukan - Jupyter Notebooks dijalankan secara langsung.

### Aplikasi Kuiz

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

### Laman Dokumentasi

Repositori ini menggunakan Docsify untuk dokumentasi:
- `index.html` berfungsi sebagai titik masuk
- Tiada pembinaan diperlukan - disajikan secara langsung melalui GitHub Pages
- Akses di: https://microsoft.github.io/AI-For-Beginners/

## Garis Panduan Penyumbangan

### Proses Permintaan Tarik

1. **Format Tajuk:** Tajuk yang jelas dan deskriptif menerangkan perubahan
2. **Keperluan CLA:** Microsoft CLA mesti ditandatangani (pemeriksaan automatik)
3. **Garis Panduan Kandungan:**
   - Kekalkan fokus pendidikan dan pendekatan mesra pemula
   - Uji semua contoh kod dalam notebook
   - Pastikan notebook berjalan dari awal hingga akhir
   - Kemas kini terjemahan jika mengubah kandungan bahasa Inggeris
4. **Perubahan Aplikasi Kuiz:** Jalankan `npm run lint` sebelum membuat komit

### Sumbangan Terjemahan

- Terjemahan diotomasi melalui GitHub Actions menggunakan co-op-translator
- Terjemahan manual diletakkan dalam `translations/<language-code>/`
- Terjemahan kuiz dalam `etc/quiz-app/src/assets/translations/`
- Bahasa yang disokong: 40+ bahasa (lihat README untuk senarai penuh)

### Kawasan Sumbangan Aktif

Lihat `etc/CONTRIBUTING.md` untuk keperluan semasa:
- Bahagian Pembelajaran Pengukuhan Mendalam
- Penambahbaikan Pengesanan Objek
- Contoh Pengecaman Entiti Bernama
- Sampel latihan embedding tersuai

## Konfigurasi Persekitaran

### Keperluan Kebergantungan

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

### Pembolehubah Persekitaran

Tiada pembolehubah persekitaran khas diperlukan untuk penggunaan asas.

Untuk pengedaran Azure (aplikasi kuiz):
- `AZURE_STATIC_WEB_APPS_API_TOKEN` (ditetapkan secara automatik oleh Azure)

## Penyahpepijatan dan Penyelesaian Masalah

### Isu Biasa

**Isu:** Penciptaan persekitaran conda gagal
- **Penyelesaian:** Kemas kini conda terlebih dahulu: `conda update conda -y`
- Pastikan ruang cakera mencukupi (50GB disyorkan)

**Isu:** Kernel Jupyter tidak ditemui
- **Penyelesaian:** 
  ```bash
  conda activate ai4beg
  python -m ipykernel install --user --name ai4beg
  ```

**Isu:** GPU tidak dikesan dalam notebook
- **Penyelesaian:** 
  - Sahkan pemasangan CUDA: `nvidia-smi`
  - Periksa GPU PyTorch: `python -c "import torch; print(torch.cuda.is_available())"`
  - Periksa GPU TensorFlow: `python -c "import tensorflow as tf; print(tf.config.list_physical_devices('GPU'))"`

**Isu:** Aplikasi kuiz tidak dapat dimulakan
- **Penyelesaian:**
  ```bash
  cd etc/quiz-app
  rm -rf node_modules package-lock.json
  npm install
  npm run serve
  ```

**Isu:** Binder tamat masa atau menyekat muat turun
- **Penyelesaian:** Gunakan GitHub Codespaces atau persediaan tempatan untuk akses sumber yang lebih baik

### Isu Memori

Beberapa pelajaran memerlukan RAM yang besar (8GB+ disyorkan):
- Gunakan VM awan untuk pelajaran yang memerlukan sumber intensif
- Tutup aplikasi lain semasa melatih model
- Kurangkan saiz batch dalam notebook jika kehabisan memori

## Nota Tambahan

### Untuk Pengajar Kursus

- Lihat `lessons/0-course-setup/for-teachers.md` untuk panduan pengajaran
- Pelajaran adalah berdiri sendiri dan boleh diajar secara berurutan atau dipilih secara individu
- Anggaran masa: 12 minggu dengan 2 pelajaran setiap minggu

### Sumber Awan

- **Azure untuk Pelajar:** Kredit percuma tersedia untuk pelajar
- **Microsoft Learn:** Laluan pembelajaran tambahan yang dihubungkan sepanjang kursus
- **Binder:** Percuma tetapi sumber terhad dan beberapa sekatan rangkaian

### Pilihan Pelaksanaan Kod

1. **Tempatan (Disyorkan):** Kawalan penuh, prestasi terbaik, sokongan GPU
2. **GitHub Codespaces:** VS Code berasaskan awan, baik untuk akses cepat
3. **Binder:** Jupyter berasaskan pelayar, percuma tetapi terhad
4. **Notebook Azure ML:** Pilihan perusahaan dengan sokongan GPU
5. **Google Colab:** Muat naik notebook secara individu, tier GPU percuma tersedia

### Bekerja dengan Notebook

- Notebook direka untuk dijalankan sel demi sel untuk pembelajaran
- Banyak notebook memuat turun dataset pada kali pertama dijalankan (mungkin mengambil masa)
- Beberapa model memerlukan GPU untuk masa latihan yang munasabah
- Model pra-latih digunakan di mana mungkin untuk mengurangkan keperluan pengiraan

### Pertimbangan Prestasi

- Pelajaran penglihatan komputer kemudian (CNN, GAN) mendapat manfaat daripada GPU
- Pelajaran transformer NLP mungkin memerlukan RAM yang besar
- Latihan dari awal adalah pendidikan tetapi memakan masa
- Contoh pembelajaran pemindahan meminimumkan masa latihan

---

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Walaupun kami berusaha untuk memastikan ketepatan, sila ambil perhatian bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidaktepatan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber yang berwibawa. Untuk maklumat yang kritikal, terjemahan manusia profesional adalah disyorkan. Kami tidak bertanggungjawab atas sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.