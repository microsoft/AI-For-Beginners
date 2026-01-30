# AGENTS.md

## Gambaran Proyek

AI for Beginners adalah kurikulum komprehensif selama 12 minggu dengan 24 pelajaran yang mencakup dasar-dasar Kecerdasan Buatan. Repositori edukasi ini mencakup pelajaran praktis menggunakan Jupyter Notebooks, kuis, dan laboratorium langsung. Kurikulum ini mencakup:

- AI Simbolik dengan Representasi Pengetahuan dan Sistem Pakar
- Jaringan Neural dan Pembelajaran Mendalam dengan TensorFlow dan PyTorch
- Teknik dan arsitektur Computer Vision
- Pemrosesan Bahasa Alami (NLP) termasuk transformers dan BERT
- Topik khusus: Algoritma Genetik, Pembelajaran Penguatan, Sistem Multi-Agen
- Etika AI dan prinsip AI yang Bertanggung Jawab

**Teknologi Utama:** Python 3, Jupyter Notebooks, TensorFlow, PyTorch, Keras, OpenCV, Vue.js (untuk aplikasi kuis)

**Arsitektur:** Repositori konten edukasi dengan Jupyter Notebooks yang diorganisasi berdasarkan area topik, dilengkapi dengan aplikasi kuis berbasis Vue.js dan dukungan multi-bahasa yang luas.

## Perintah Pengaturan

### Lingkungan Pengembangan Utama (Python/Jupyter)

Kurikulum dirancang untuk dijalankan dengan Python dan Jupyter Notebooks. Pendekatan yang direkomendasikan adalah menggunakan miniconda:

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

### Pengaturan Aplikasi Kuis

Aplikasi kuis adalah aplikasi Vue.js terpisah yang terletak di `etc/quiz-app/`:

```bash
cd etc/quiz-app
npm install
npm run serve  # Development server
npm run build  # Production build
npm run lint   # Lint and fix files
```

## Alur Kerja Pengembangan

### Bekerja dengan Jupyter Notebooks

1. **Pengembangan Lokal:**
   - Aktifkan lingkungan conda: `conda activate ai4beg`
   - Mulai Jupyter: `jupyter notebook` atau `jupyter lab`
   - Navigasikan ke folder pelajaran dan buka file `.ipynb`
   - Jalankan sel secara interaktif untuk mengikuti pelajaran

2. **VS Code dengan Ekstensi Python:**
   - Buka repositori di VS Code
   - Instal ekstensi Python
   - VS Code secara otomatis mendeteksi dan menggunakan lingkungan conda
   - Buka file `.ipynb` langsung di VS Code

3. **Pengembangan Cloud:**
   - **GitHub Codespaces:** Klik "Code" → "Codespaces" → "Create codespace on main"
   - **Binder:** Gunakan badge Binder di README untuk meluncurkan di browser
   - Catatan: Binder memiliki sumber daya terbatas dan beberapa pembatasan akses web

### Dukungan GPU untuk Pelajaran Lanjutan

Pelajaran lanjutan sangat diuntungkan dari akselerasi GPU:

- **Azure Data Science VM:** Gunakan VM seri NC dengan dukungan GPU
- **Azure Machine Learning:** Gunakan fitur notebook dengan komputasi GPU
- **Google Colab:** Unggah notebook secara individual (memiliki dukungan GPU gratis)

### Pengembangan Aplikasi Kuis

```bash
cd etc/quiz-app
npm run serve  # Hot-reload development server at http://localhost:8080
```

## Instruksi Pengujian

Ini adalah repositori edukasi yang berfokus pada konten pembelajaran daripada pengujian perangkat lunak. Tidak ada suite pengujian tradisional.

### Pendekatan Validasi:

1. **Jupyter Notebooks:** Jalankan sel secara berurutan untuk memverifikasi contoh kode berfungsi
2. **Pengujian Aplikasi Kuis:** Pengujian manual melalui server pengembangan
3. **Validasi Terjemahan:** Periksa konten terjemahan di folder `translations/`
4. **Linting Aplikasi Kuis:** `npm run lint` di `etc/quiz-app/`

### Menjalankan Contoh Kode:

```bash
# Activate environment first
conda activate ai4beg

# Run Python scripts directly
python lessons/4-ComputerVision/07-ConvNets/pytorchcv.py

# Or execute notebooks
jupyter notebook lessons/3-NeuralNetworks/03-Perceptron/Perceptron.ipynb
```

## Gaya Kode

### Gaya Kode Python

- Konvensi Python standar untuk kode edukasi
- Kode yang jelas dan mudah dibaca, memprioritaskan pembelajaran daripada optimasi
- Komentar yang menjelaskan konsep utama
- Ramah Jupyter Notebook: sel harus mandiri jika memungkinkan
- Tidak ada persyaratan linting ketat untuk konten pelajaran

### JavaScript/Vue.js (Aplikasi Kuis)

- Konfigurasi ESLint di `etc/quiz-app/package.json`
- Jalankan `npm run lint` untuk memeriksa dan memperbaiki masalah secara otomatis
- Konvensi Vue 2.x
- Arsitektur berbasis komponen

### Organisasi File

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

## Build dan Deployment

### Konten Jupyter

Tidak diperlukan proses build - Jupyter Notebooks dijalankan langsung.

### Aplikasi Kuis

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

### Situs Dokumentasi

Repositori menggunakan Docsify untuk dokumentasi:
- `index.html` berfungsi sebagai titik masuk
- Tidak diperlukan build - disajikan langsung melalui GitHub Pages
- Akses di: https://microsoft.github.io/AI-For-Beginners/

## Panduan Kontribusi

### Proses Pull Request

1. **Format Judul:** Judul yang jelas dan deskriptif yang menjelaskan perubahan
2. **Persyaratan CLA:** Microsoft CLA harus ditandatangani (pemeriksaan otomatis)
3. **Panduan Konten:**
   - Pertahankan fokus edukasi dan pendekatan ramah pemula
   - Uji semua contoh kode di notebook
   - Pastikan notebook berjalan dari awal hingga akhir
   - Perbarui terjemahan jika memodifikasi konten bahasa Inggris
4. **Perubahan Aplikasi Kuis:** Jalankan `npm run lint` sebelum melakukan commit

### Kontribusi Terjemahan

- Terjemahan dilakukan secara otomatis melalui GitHub Actions menggunakan co-op-translator
- Terjemahan manual ditempatkan di `translations/<kode-bahasa>/`
- Terjemahan kuis di `etc/quiz-app/src/assets/translations/`
- Bahasa yang didukung: 40+ bahasa (lihat README untuk daftar lengkap)

### Area Kontribusi Aktif

Lihat `etc/CONTRIBUTING.md` untuk kebutuhan saat ini:
- Bagian Pembelajaran Penguatan Mendalam
- Peningkatan Deteksi Objek
- Contoh Pengenalan Entitas Bernama
- Sampel pelatihan embedding khusus

## Konfigurasi Lingkungan

### Dependensi yang Diperlukan

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

### Variabel Lingkungan

Tidak diperlukan variabel lingkungan khusus untuk penggunaan dasar.

Untuk deployment Azure (aplikasi kuis):
- `AZURE_STATIC_WEB_APPS_API_TOKEN` (diatur secara otomatis oleh Azure)

## Debugging dan Pemecahan Masalah

### Masalah Umum

**Masalah:** Pembuatan lingkungan conda gagal
- **Solusi:** Perbarui conda terlebih dahulu: `conda update conda -y`
- Pastikan ruang disk cukup (disarankan 50GB)

**Masalah:** Kernel Jupyter tidak ditemukan
- **Solusi:** 
  ```bash
  conda activate ai4beg
  python -m ipykernel install --user --name ai4beg
  ```

**Masalah:** GPU tidak terdeteksi di notebook
- **Solusi:** 
  - Verifikasi instalasi CUDA: `nvidia-smi`
  - Periksa GPU PyTorch: `python -c "import torch; print(torch.cuda.is_available())"`
  - Periksa GPU TensorFlow: `python -c "import tensorflow as tf; print(tf.config.list_physical_devices('GPU'))"`

**Masalah:** Aplikasi kuis tidak dapat dimulai
- **Solusi:**
  ```bash
  cd etc/quiz-app
  rm -rf node_modules package-lock.json
  npm install
  npm run serve
  ```

**Masalah:** Binder timeout atau memblokir unduhan
- **Solusi:** Gunakan GitHub Codespaces atau pengaturan lokal untuk akses sumber daya yang lebih baik

### Masalah Memori

Beberapa pelajaran membutuhkan RAM yang signifikan (disarankan 8GB+):
- Gunakan VM cloud untuk pelajaran yang membutuhkan sumber daya tinggi
- Tutup aplikasi lain saat melatih model
- Kurangi ukuran batch di notebook jika kehabisan memori

## Catatan Tambahan

### Untuk Pengajar Kursus

- Lihat `lessons/0-course-setup/for-teachers.md` untuk panduan pengajaran
- Pelajaran bersifat mandiri dan dapat diajarkan secara berurutan atau dipilih secara individual
- Perkiraan waktu: 12 minggu dengan 2 pelajaran per minggu

### Sumber Daya Cloud

- **Azure untuk Mahasiswa:** Kredit gratis tersedia untuk mahasiswa
- **Microsoft Learn:** Jalur pembelajaran tambahan yang ditautkan di seluruh pelajaran
- **Binder:** Gratis tetapi dengan sumber daya terbatas dan beberapa pembatasan jaringan

### Opsi Eksekusi Kode

1. **Lokal (Direkomendasikan):** Kontrol penuh, kinerja terbaik, dukungan GPU
2. **GitHub Codespaces:** VS Code berbasis cloud, bagus untuk akses cepat
3. **Binder:** Jupyter berbasis browser, gratis tetapi terbatas
4. **Notebook Azure ML:** Opsi perusahaan dengan dukungan GPU
5. **Google Colab:** Unggah notebook secara individual, tersedia tier GPU gratis

### Bekerja dengan Notebook

- Notebook dirancang untuk dijalankan sel demi sel untuk pembelajaran
- Banyak notebook mengunduh dataset saat pertama kali dijalankan (mungkin memakan waktu)
- Beberapa model membutuhkan GPU untuk waktu pelatihan yang wajar
- Model yang sudah dilatih digunakan jika memungkinkan untuk mengurangi kebutuhan komputasi

### Pertimbangan Kinerja

- Pelajaran computer vision lanjutan (CNN, GAN) diuntungkan dari GPU
- Pelajaran NLP transformer mungkin membutuhkan RAM yang signifikan
- Pelatihan dari awal bersifat edukatif tetapi memakan waktu
- Contoh transfer learning meminimalkan waktu pelatihan

---

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan layanan penerjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Meskipun kami berupaya untuk memberikan hasil yang akurat, harap diketahui bahwa terjemahan otomatis mungkin mengandung kesalahan atau ketidakakuratan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber yang otoritatif. Untuk informasi yang penting, disarankan menggunakan jasa penerjemahan manusia profesional. Kami tidak bertanggung jawab atas kesalahpahaman atau interpretasi yang keliru yang timbul dari penggunaan terjemahan ini.