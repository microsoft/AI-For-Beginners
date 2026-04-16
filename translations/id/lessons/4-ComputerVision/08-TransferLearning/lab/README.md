# Klasifikasi Oxford Pets menggunakan Transfer Learning

Tugas Praktikum dari [Kurikulum AI untuk Pemula](https://github.com/microsoft/ai-for-beginners).

## Tugas

Bayangkan Anda perlu mengembangkan aplikasi untuk tempat penitipan hewan peliharaan guna mencatat semua hewan peliharaan. Salah satu fitur hebat dari aplikasi semacam itu adalah kemampuan untuk secara otomatis mengenali ras hewan dari sebuah foto. Dalam tugas ini, kita akan menggunakan transfer learning untuk mengklasifikasikan gambar hewan peliharaan nyata dari dataset [Oxford-IIIT](https://www.robots.ox.ac.uk/~vgg/data/pets/).

## Dataset

Kita akan menggunakan dataset asli [Oxford-IIIT](https://www.robots.ox.ac.uk/~vgg/data/pets/), yang berisi 35 jenis ras anjing dan kucing yang berbeda.

Untuk mengunduh dataset, gunakan potongan kode berikut:

```python
!wget https://www.robots.ox.ac.uk/~vgg/data/pets/data/images.tar.gz
!tar xfz images.tar.gz
!rm images.tar.gz
```

## Memulai Notebook

Mulailah praktikum dengan membuka [OxfordPets.ipynb](OxfordPets.ipynb)

## Kesimpulan

Transfer learning dan jaringan yang telah dilatih sebelumnya memungkinkan kita untuk menyelesaikan masalah klasifikasi gambar dunia nyata dengan relatif mudah. Namun, jaringan yang telah dilatih sebelumnya bekerja dengan baik pada gambar yang serupa, dan jika kita mulai mengklasifikasikan gambar yang sangat berbeda (misalnya, gambar medis), kemungkinan besar kita akan mendapatkan hasil yang jauh lebih buruk.

---

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan layanan penerjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Meskipun kami berupaya untuk memberikan hasil yang akurat, harap diperhatikan bahwa terjemahan otomatis mungkin mengandung kesalahan atau ketidakakuratan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber yang berwenang. Untuk informasi yang bersifat kritis, disarankan menggunakan jasa penerjemahan manusia profesional. Kami tidak bertanggung jawab atas kesalahpahaman atau penafsiran yang keliru yang timbul dari penggunaan terjemahan ini.