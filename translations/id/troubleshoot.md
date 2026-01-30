# Panduan Pemecahan Masalah AI-For-Beginners

Panduan ini membantu Anda mengatasi masalah umum yang sering terjadi saat menggunakan atau berkontribusi pada repositori [AI-For-Beginners](https://github.com/microsoft/AI-For-Beginners). Setiap masalah mencakup latar belakang, gejala, penjelasan, dan solusi langkah demi langkah.

---

## Daftar Isi

- [Masalah Umum](../..)
- [Masalah Instalasi](../..)
- [Masalah Konfigurasi](../..)
- [Menjalankan Notebook](../..)
- [Masalah Performa](../..)
- [Masalah Situs Web Buku Teks](../..)
- [Masalah Kontribusi](../..)
- [FAQ](../..)
- [Mendapatkan Bantuan](../..)

---

## Masalah Umum

### 1. Repositori Tidak Terkloning dengan Benar

**Latar Belakang:** Kloning memungkinkan Anda menyalin repositori ke mesin Anda.

**Gejala:**
- Error: `fatal: repository not found`
- Error: `Permission denied (publickey)`

**Kemungkinan Penyebab:**
- URL repositori salah
- Izin tidak mencukupi
- Kunci SSH belum dikonfigurasi

**Solusi:**
1. **Periksa URL repositori.**  
   Gunakan URL HTTPS:  
   ```
   git clone https://github.com/microsoft/AI-For-Beginners.git
   ```
2. **Beralih ke HTTPS jika SSH gagal.**  
   Jika Anda melihat `Permission denied (publickey)`, gunakan tautan HTTPS di atas sebagai pengganti SSH.
3. **Konfigurasi kunci SSH (opsional).**  
   Jika Anda ingin menggunakan SSH, ikuti [panduan SSH GitHub](https://docs.github.com/en/authentication/connecting-to-github-with-ssh).

---

## Masalah Instalasi

### 2. Masalah Lingkungan Python

**Latar Belakang:** Repositori ini bergantung pada Python dan berbagai pustaka.

**Gejala:**
- Error: `ModuleNotFoundError: No module named '<package>'`
- Error impor saat menjalankan skrip atau notebook

**Kemungkinan Penyebab:**
- Dependensi belum diinstal
- Versi Python salah

**Solusi:**
1. **Siapkan lingkungan virtual.**  
   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
   ```
2. **Instal dependensi.**  
   ```bash
   pip install -r requirements.txt
   ```
3. **Periksa versi Python.**  
   Gunakan Python 3.7 atau lebih baru.  
   ```bash
   python --version
   ```

### 3. Jupyter Tidak Terinstal

**Latar Belakang:** Notebook adalah sumber pembelajaran utama.

**Gejala:**
- Error: `jupyter: command not found`
- Notebook gagal diluncurkan

**Kemungkinan Penyebab:**
- Jupyter belum diinstal

**Solusi:**
1. **Instal Jupyter Notebook.**  
   ```bash
   pip install notebook
   ```
   atau, jika menggunakan Anaconda:
   ```bash
   conda install notebook
   ```
2. **Mulai Jupyter Notebook.**  
   ```bash
   jupyter notebook
   ```

### 4. Konflik Versi Dependensi

**Latar Belakang:** Proyek dapat rusak jika versi paket tidak cocok.

**Gejala:**
- Error atau peringatan tentang versi yang tidak kompatibel

**Kemungkinan Penyebab:**
- Paket Python lama atau konflik

**Solusi:**
1. **Instal di lingkungan yang bersih.**  
   Hapus venv/conda env lama dan buat yang baru.
2. **Gunakan versi yang tepat.**  
   Selalu jalankan:
   ```bash
   pip install -r requirements.txt
   ```
   Jika ini gagal, instal paket yang hilang secara manual seperti yang dijelaskan di README.

---

## Masalah Konfigurasi

### 5. Variabel Lingkungan Tidak Disetel

**Latar Belakang:** Beberapa modul mungkin memerlukan kunci, token, atau pengaturan konfigurasi.

**Gejala:**
- Error: `KeyError` atau peringatan tentang konfigurasi yang hilang

**Kemungkinan Penyebab:**
- Variabel lingkungan yang diperlukan belum disetel

**Solusi:**
1. **Periksa file `.env.example` atau file serupa.**
2. **Buat file `.env` dan isi nilai yang diperlukan.**
3. **Muat ulang terminal atau IDE Anda setelah menyetel variabel lingkungan.**

---

## Menjalankan Notebook

### 6. Notebook Tidak Bisa Dibuka atau Dijalankan

**Latar Belakang:** Notebook Jupyter memerlukan pengaturan yang tepat.

**Gejala:**
- Notebook gagal diluncurkan
- Browser tidak terbuka secara otomatis

**Kemungkinan Penyebab:**
- Jupyter belum diinstal
- Masalah konfigurasi browser

**Solusi:**
1. **Instal Jupyter (lihat Masalah Instalasi di atas).**
2. **Buka notebook secara manual.**
   - Salin URL dari terminal (misalnya, `http://localhost:8888/?token=...`) dan tempelkan ke browser Anda.

### 7. Kernel Crash atau Membeku

**Latar Belakang:** Kernel notebook dapat crash karena batas sumber daya atau kesalahan kode.

**Gejala:**
- Kernel mati atau restart berulang kali
- Error out-of-memory

**Kemungkinan Penyebab:**
- Dataset besar
- Kode atau paket yang tidak kompatibel

**Solusi:**
1. **Restart kernel.**  
   Gunakan tombol "Restart Kernel" di Jupyter.
2. **Periksa penggunaan memori.**  
   Tutup aplikasi yang tidak digunakan.
3. **Jalankan notebook di platform cloud.**  
   Gunakan [Google Colab](https://colab.research.google.com/) atau [Azure Notebooks](https://notebooks.azure.com/).

---

## Masalah Performa

### 8. Notebook Berjalan Lambat

**Latar Belakang:** Beberapa tugas AI memerlukan memori dan CPU yang signifikan.

**Gejala:**
- Eksekusi lambat
- Kipas laptop berbunyi keras

**Kemungkinan Penyebab:**
- Dataset atau model besar
- Sumber daya sistem terbatas

**Solusi:**
1. **Gunakan platform cloud.**
   - Unggah notebook ke Colab atau Azure Notebooks.
2. **Kurangi ukuran dataset.**
   - Gunakan data sampel untuk latihan.
3. **Tutup program yang tidak diperlukan.**
   - Bebaskan RAM sistem.

---

## Masalah Situs Web Buku Teks

### 9. Bab Tidak Bisa Dibuka

**Latar Belakang:** Buku teks online menampilkan pelajaran dan bab.

**Gejala:**
- Bab (misalnya, Transformers/BERT) hilang atau tidak bisa dibuka

**Masalah yang Diketahui:**  
- [Masalah #303](https://github.com/microsoft/AI-For-Beginners/issues/303): “18 Transformers. BERT. tidak bisa dibuka di situs web buku teks.” Disebabkan oleh kesalahan nama file (`READMEtransformers.md` alih-alih `README.md`).

**Solusi:**
1. **Periksa kesalahan penamaan file.**  
   Jika Anda adalah kontributor, pastikan file bab diberi nama `README.md`.
2. **Laporkan file yang hilang.**  
   Buka masalah GitHub dengan nama bab dan detail error.

---

## Masalah Kontribusi

### 10. PR Tidak Diterima atau Build Gagal

**Latar Belakang:** Kontribusi harus lulus pengujian dan mengikuti pedoman.

**Gejala:**
- Pull request ditolak
- Error pipeline CI/CD

**Kemungkinan Penyebab:**
- Pengujian gagal
- Tidak mengikuti standar kode

**Solusi:**
1. **Baca pedoman kontribusi.**
   - Ikuti [CONTRIBUTING.md](https://github.com/microsoft/AI-For-Beginners/blob/main/CONTRIBUTING.md) repositori.
2. **Jalankan pengujian secara lokal sebelum push.**
3. **Periksa aturan linting atau persyaratan format.**

---

## FAQ

### Di mana saya bisa menemukan bantuan untuk modul tertentu?
- Setiap modul biasanya memiliki README sendiri. Mulailah dari sana untuk tips pengaturan dan penggunaan.

### Bagaimana cara melaporkan bug atau meminta fitur?
- [Buka Masalah GitHub](https://github.com/microsoft/AI-For-Beginners/issues/new) dengan deskripsi yang jelas dan langkah-langkah untuk mereproduksi.

### Bisakah saya meminta bantuan jika masalah saya tidak tercantum?
- Tentu! Cari masalah yang sudah ada terlebih dahulu, dan jika Anda tidak menemukan masalah Anda, buat masalah baru.

---

## Mendapatkan Bantuan

- **Periksa Masalah:** [Masalah GitHub](https://github.com/microsoft/AI-For-Beginners/issues)
- **Ajukan Pertanyaan:** Gunakan Diskusi GitHub atau buka masalah.
- **Komunitas:** Lihat tautan repositori untuk opsi obrolan/forum.

---

_Terakhir Diperbarui: 20 September 2025_

---

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan layanan penerjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Meskipun kami berupaya untuk memberikan hasil yang akurat, harap diketahui bahwa terjemahan otomatis mungkin mengandung kesalahan atau ketidakakuratan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber yang otoritatif. Untuk informasi yang bersifat kritis, disarankan menggunakan jasa penerjemahan manusia profesional. Kami tidak bertanggung jawab atas kesalahpahaman atau penafsiran yang keliru yang timbul dari penggunaan terjemahan ini.