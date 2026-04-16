# Panduan Penyelesaian Masalah AI-For-Beginners

Panduan ini membantu anda menyelesaikan masalah biasa yang dihadapi semasa menggunakan atau menyumbang kepada repositori [AI-For-Beginners](https://github.com/microsoft/AI-For-Beginners). Setiap masalah disertakan dengan latar belakang, simptom, penjelasan, dan langkah-langkah penyelesaian.

---

## Kandungan

- [Masalah Umum](../..)
- [Masalah Pemasangan](../..)
- [Masalah Konfigurasi](../..)
- [Menjalankan Notebook](../..)
- [Masalah Prestasi](../..)
- [Masalah Laman Web Buku Teks](../..)
- [Masalah Penyumbangan](../..)
- [Soalan Lazim](../..)
- [Mendapatkan Bantuan](../..)

---

## Masalah Umum

### 1. Repositori Tidak Berjaya Diklon

**Latar Belakang:** Klon membolehkan anda menyalin repositori ke mesin anda.

**Simptom:**
- Ralat: `fatal: repository not found`
- Ralat: `Permission denied (publickey)`

**Punca Kemungkinan:**
- URL repositori tidak betul
- Kebenaran tidak mencukupi
- Kunci SSH tidak dikonfigurasi

**Penyelesaian:**
1. **Semak URL repositori.**  
   Gunakan URL HTTPS:  
   ```
   git clone https://github.com/microsoft/AI-For-Beginners.git
   ```
2. **Tukar ke HTTPS jika SSH gagal.**  
   Jika anda melihat `Permission denied (publickey)`, gunakan pautan HTTPS di atas dan bukannya SSH.
3. **Konfigurasi kunci SSH (pilihan).**  
   Jika anda ingin menggunakan SSH, ikuti [panduan SSH GitHub](https://docs.github.com/en/authentication/connecting-to-github-with-ssh).

---

## Masalah Pemasangan

### 2. Masalah Persekitaran Python

**Latar Belakang:** Repositori bergantung pada Python dan pelbagai perpustakaan.

**Simptom:**
- Ralat: `ModuleNotFoundError: No module named '<package>'`
- Ralat import semasa menjalankan skrip atau notebook

**Punca Kemungkinan:**
- Kebergantungan tidak dipasang
- Versi Python tidak sesuai

**Penyelesaian:**
1. **Sediakan persekitaran maya.**  
   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
   ```
2. **Pasang kebergantungan.**  
   ```bash
   pip install -r requirements.txt
   ```
3. **Semak versi Python.**  
   Gunakan Python 3.7 atau lebih baru.  
   ```bash
   python --version
   ```

### 3. Jupyter Tidak Dipasang

**Latar Belakang:** Notebook adalah sumber pembelajaran utama.

**Simptom:**
- Ralat: `jupyter: command not found`
- Notebook gagal dilancarkan

**Punca Kemungkinan:**
- Jupyter tidak dipasang

**Penyelesaian:**
1. **Pasang Jupyter Notebook.**  
   ```bash
   pip install notebook
   ```
   atau, jika menggunakan Anaconda:
   ```bash
   conda install notebook
   ```
2. **Mulakan Jupyter Notebook.**  
   ```bash
   jupyter notebook
   ```

### 4. Konflik Versi Kebergantungan

**Latar Belakang:** Projek boleh gagal jika versi pakej tidak sepadan.

**Simptom:**
- Ralat atau amaran tentang versi yang tidak serasi

**Punca Kemungkinan:**
- Pakej Python lama atau bercanggah

**Penyelesaian:**
1. **Pasang dalam persekitaran bersih.**  
   Padamkan venv/env conda lama dan buat yang baru.
2. **Gunakan versi tepat.**  
   Sentiasa jalankan:
   ```bash
   pip install -r requirements.txt
   ```
   Jika ini gagal, pasang pakej yang hilang secara manual seperti yang diterangkan dalam README.

---

## Masalah Konfigurasi

### 5. Pembolehubah Persekitaran Tidak Ditetapkan

**Latar Belakang:** Sesetengah modul mungkin memerlukan kunci, token, atau tetapan konfigurasi.

**Simptom:**
- Ralat: `KeyError` atau amaran tentang konfigurasi yang hilang

**Punca Kemungkinan:**
- Pembolehubah persekitaran yang diperlukan tidak ditetapkan

**Penyelesaian:**
1. **Semak fail `.env.example` atau fail serupa.**
2. **Buat fail `.env` dan isi nilai yang diperlukan.**
3. **Muat semula terminal atau IDE anda selepas menetapkan pembolehubah persekitaran.**

---

## Menjalankan Notebook

### 6. Notebook Tidak Berjaya Dibuka atau Dijalankan

**Latar Belakang:** Notebook Jupyter memerlukan persediaan yang betul.

**Simptom:**
- Notebook gagal dilancarkan
- Penyemak imbas tidak terbuka secara automatik

**Punca Kemungkinan:**
- Jupyter tidak dipasang
- Masalah konfigurasi penyemak imbas

**Penyelesaian:**
1. **Pasang Jupyter (lihat Masalah Pemasangan di atas).**
2. **Buka notebook secara manual.**
   - Salin URL dari terminal (contoh: `http://localhost:8888/?token=...`) dan tampal ke penyemak imbas anda.

### 7. Kernel Terhenti atau Membeku

**Latar Belakang:** Kernel notebook boleh terhenti disebabkan had sumber atau ralat kod.

**Simptom:**
- Kernel mati atau dimulakan semula berulang kali
- Ralat kekurangan memori

**Punca Kemungkinan:**
- Dataset besar
- Kod atau pakej yang tidak serasi

**Penyelesaian:**
1. **Mulakan semula kernel.**  
   Gunakan butang "Restart Kernel" dalam Jupyter.
2. **Semak penggunaan memori.**  
   Tutup aplikasi yang tidak digunakan.
3. **Jalankan notebook di platform awan.**  
   Gunakan [Google Colab](https://colab.research.google.com/) atau [Azure Notebooks](https://notebooks.azure.com/).

---

## Masalah Prestasi

### 8. Notebook Berjalan Perlahan

**Latar Belakang:** Sesetengah tugas AI memerlukan memori dan CPU yang besar.

**Simptom:**
- Pelaksanaan perlahan
- Kipas komputer riba berbunyi kuat

**Punca Kemungkinan:**
- Dataset atau model besar
- Sumber sistem terhad

**Penyelesaian:**
1. **Gunakan platform awan.**
   - Muat naik notebook ke Colab atau Azure Notebooks.
2. **Kurangkan saiz dataset.**
   - Gunakan data sampel untuk latihan.
3. **Tutup program yang tidak diperlukan.**
   - Bebaskan RAM sistem.

---

## Masalah Laman Web Buku Teks

### 9. Bab Tidak Berjaya Dibuka

**Latar Belakang:** Buku teks dalam talian memaparkan pelajaran dan bab.

**Simptom:**
- Bab (contoh: Transformers/BERT) hilang atau tidak dibuka

**Masalah Diketahui:**  
- [Isu #303](https://github.com/microsoft/AI-For-Beginners/issues/303): “18 Transformers. BERT. tidak boleh dibuka di laman web buku teks.” Disebabkan oleh ralat nama fail (`READMEtransformers.md` dan bukannya `README.md`).

**Penyelesaian:**
1. **Semak ralat penamaan fail.**  
   Jika anda seorang penyumbang, pastikan fail bab dinamakan `README.md`.
2. **Laporkan fail yang hilang.**  
   Buka isu GitHub dengan nama bab dan butiran ralat.

---

## Masalah Penyumbangan

### 10. PR Tidak Diterima atau Pembinaan Gagal

**Latar Belakang:** Sumbangan mesti lulus ujian dan mengikuti garis panduan.

**Simptom:**
- Permintaan tarik ditolak
- Ralat CI/CD pipeline

**Punca Kemungkinan:**
- Ujian gagal
- Tidak mengikuti piawaian pengekodan

**Penyelesaian:**
1. **Baca garis panduan penyumbangan.**
   - Ikuti [CONTRIBUTING.md](https://github.com/microsoft/AI-For-Beginners/blob/main/CONTRIBUTING.md) repositori.
2. **Jalankan ujian secara tempatan sebelum menghantar.**
3. **Semak peraturan linting atau keperluan pemformatan.**

---

## Soalan Lazim

### Di mana saya boleh mendapatkan bantuan untuk modul tertentu?
- Setiap modul biasanya mempunyai README sendiri. Mulakan di sana untuk petua persediaan dan penggunaan.

### Bagaimana saya melaporkan pepijat atau meminta ciri?
- [Buka Isu GitHub](https://github.com/microsoft/AI-For-Beginners/issues/new) dengan penerangan yang jelas dan langkah-langkah untuk menghasilkan semula.

### Bolehkah saya meminta bantuan jika masalah saya tidak disenaraikan?
- Ya! Cari isu yang sedia ada terlebih dahulu, dan jika anda tidak menemui masalah anda, buat isu baru.

---

## Mendapatkan Bantuan

- **Semak Isu:** [GitHub Issues](https://github.com/microsoft/AI-For-Beginners/issues)
- **Ajukan Soalan:** Gunakan Perbincangan GitHub atau buka isu.
- **Komuniti:** Lihat pautan repositori untuk pilihan sembang/forum.

---

_Kemas Kini Terakhir: 2025-09-20_

---

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Walaupun kami berusaha untuk memastikan ketepatan, sila ambil perhatian bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidaktepatan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber yang berwibawa. Untuk maklumat yang kritikal, terjemahan manusia profesional adalah disyorkan. Kami tidak bertanggungjawab atas sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.