# Contoh AI Ramah Pemula

Selamat datang! Direktori ini berisi contoh sederhana dan mandiri untuk membantu Anda memulai dengan AI dan pembelajaran mesin. Setiap contoh dirancang agar mudah dipahami dengan komentar yang rinci dan penjelasan langkah demi langkah.

## 📚 Gambaran Contoh

| Contoh | Deskripsi | Tingkat Kesulitan | Prasyarat |
|--------|-----------|-------------------|-----------|
| [Hello AI World](../../../examples/01-hello-ai-world.py) | Program AI pertama Anda - pengenalan pola sederhana | ⭐ Pemula | Dasar-dasar Python |
| [Simple Neural Network](../../../examples/02-simple-neural-network.py) | Membangun jaringan neural dari awal | ⭐⭐ Pemula+ | Python, matematika dasar |
| [Image Classifier](./03-image-classifier.ipynb) | Mengklasifikasi gambar dengan model yang sudah dilatih | ⭐⭐ Pemula+ | Python, numpy |
| [Text Sentiment](../../../examples/04-text-sentiment.py) | Menganalisis sentimen teks (positif/negatif) | ⭐⭐ Pemula+ | Python |

## 🚀 Memulai

### Prasyarat

Pastikan Anda sudah menginstal Python (disarankan versi 3.8 atau lebih tinggi). Instal paket yang diperlukan:

```bash
# For Python scripts
pip install numpy

# For Jupyter notebooks (image classifier)
pip install jupyter numpy pillow tensorflow
```

Atau gunakan lingkungan conda dari kurikulum utama:

```bash
conda env create --name ai4beg --file ../environment.yml
conda activate ai4beg
```

### Menjalankan Contoh

**Untuk skrip Python (.py files):**
```bash
python 01-hello-ai-world.py
```

**Untuk Jupyter notebooks (.ipynb files):**
```bash
jupyter notebook 03-image-classifier.ipynb
```

## 📖 Jalur Pembelajaran

Kami merekomendasikan mengikuti contoh secara berurutan:

1. **Mulai dengan "Hello AI World"** - Pelajari dasar-dasar pengenalan pola
2. **Bangun Jaringan Neural Sederhana** - Pahami cara kerja jaringan neural
3. **Coba Pengklasifikasi Gambar** - Lihat AI beraksi dengan gambar nyata
4. **Analisis Sentimen Teks** - Jelajahi pemrosesan bahasa alami

## 💡 Tips untuk Pemula

- **Baca komentar kode dengan cermat** - Mereka menjelaskan apa yang dilakukan setiap baris
- **Bereksperimen!** - Coba ubah nilai dan lihat apa yang terjadi
- **Jangan khawatir jika tidak memahami semuanya** - Belajar membutuhkan waktu
- **Ajukan pertanyaan** - Gunakan [Papan Diskusi](https://github.com/microsoft/AI-For-Beginners/discussions)

## 🔗 Langkah Selanjutnya

Setelah menyelesaikan contoh-contoh ini, jelajahi kurikulum lengkap:
- [Pengantar AI](../lessons/1-Intro/README.md)
- [Jaringan Neural](../lessons/3-NeuralNetworks/README.md)
- [Visi Komputer](../lessons/4-ComputerVision/README.md)
- [Pemrosesan Bahasa Alami](../lessons/5-NLP/README.md)

## 🤝 Kontribusi

Apakah contoh-contoh ini membantu Anda? Bantu kami untuk meningkatkannya:
- Laporkan masalah atau usulkan perbaikan
- Tambahkan lebih banyak contoh untuk pemula
- Tingkatkan dokumentasi dan komentar

---

*Ingat: Setiap ahli pernah menjadi pemula. Selamat belajar! 🎓*

---

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan layanan penerjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Meskipun kami berusaha untuk memberikan hasil yang akurat, harap diperhatikan bahwa terjemahan otomatis mungkin mengandung kesalahan atau ketidakakuratan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber yang otoritatif. Untuk informasi yang bersifat kritis, disarankan menggunakan jasa penerjemahan manusia profesional. Kami tidak bertanggung jawab atas kesalahpahaman atau penafsiran yang keliru yang timbul dari penggunaan terjemahan ini.