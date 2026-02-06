# Contoh AI Mesra Pemula

Selamat datang! Direktori ini mengandungi contoh mudah dan berdiri sendiri untuk membantu anda memulakan dengan AI dan pembelajaran mesin. Setiap contoh direka untuk mesra pemula dengan komen terperinci dan penjelasan langkah demi langkah.

## 📚 Gambaran Keseluruhan Contoh

| Contoh | Penerangan | Kesukaran | Prasyarat |
|--------|------------|-----------|-----------|
| [Hello AI World](../../../examples/01-hello-ai-world.py) | Program AI pertama anda - pengenalan corak yang mudah | ⭐ Pemula | Asas Python |
| [Simple Neural Network](../../../examples/02-simple-neural-network.py) | Bina rangkaian neural dari awal | ⭐⭐ Pemula+ | Python, matematik asas |
| [Image Classifier](./03-image-classifier.ipynb) | Klasifikasi imej dengan model yang telah dilatih | ⭐⭐ Pemula+ | Python, numpy |
| [Text Sentiment](../../../examples/04-text-sentiment.py) | Analisis sentimen teks (positif/negatif) | ⭐⭐ Pemula+ | Python |

## 🚀 Memulakan

### Prasyarat

Pastikan anda telah memasang Python (disarankan versi 3.8 atau lebih tinggi). Pasang pakej yang diperlukan:

```bash
# For Python scripts
pip install numpy

# For Jupyter notebooks (image classifier)
pip install jupyter numpy pillow tensorflow
```

Atau gunakan persekitaran conda dari kurikulum utama:

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

## 📖 Laluan Pembelajaran

Kami mengesyorkan mengikuti contoh-contoh ini mengikut urutan:

1. **Mulakan dengan "Hello AI World"** - Pelajari asas pengenalan corak
2. **Bina Rangkaian Neural Mudah** - Fahami cara rangkaian neural berfungsi
3. **Cuba Pengklasifikasi Imej** - Lihat AI beraksi dengan imej sebenar
4. **Analisis Sentimen Teks** - Terokai pemprosesan bahasa semula jadi

## 💡 Petua untuk Pemula

- **Baca komen kod dengan teliti** - Ia menerangkan apa yang dilakukan oleh setiap baris
- **Bereksperimen!** - Cuba ubah nilai dan lihat apa yang berlaku
- **Jangan risau jika tidak memahami semuanya** - Pembelajaran memerlukan masa
- **Tanya soalan** - Gunakan [Papan Perbincangan](https://github.com/microsoft/AI-For-Beginners/discussions)

## 🔗 Langkah Seterusnya

Selepas melengkapkan contoh-contoh ini, terokai kurikulum penuh:
- [Pengenalan kepada AI](../lessons/1-Intro/README.md)
- [Rangkaian Neural](../lessons/3-NeuralNetworks/README.md)
- [Penglihatan Komputer](../lessons/4-ComputerVision/README.md)
- [Pemprosesan Bahasa Semula Jadi](../lessons/5-NLP/README.md)

## 🤝 Menyumbang

Mendapati contoh-contoh ini berguna? Bantu kami memperbaikinya:
- Laporkan isu atau cadangkan penambahbaikan
- Tambah lebih banyak contoh untuk pemula
- Perbaiki dokumentasi dan komen

---

*Ingat: Setiap pakar pernah menjadi pemula. Selamat belajar! 🎓*

---

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Walaupun kami berusaha untuk memastikan ketepatan, sila ambil perhatian bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidaktepatan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber yang berwibawa. Untuk maklumat yang kritikal, terjemahan manusia profesional adalah disyorkan. Kami tidak bertanggungjawab atas sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.