# Klasifikasi Multi-Kelas dengan Perceptron

Tugas Lab dari [AI for Beginners Curriculum](https://github.com/microsoft/ai-for-beginners).

## Tugas

Menggunakan kode yang telah kita kembangkan dalam pelajaran ini untuk klasifikasi biner pada digit tulisan tangan MNIST, buatlah sebuah klasifikasi multi-kelas yang dapat mengenali semua digit. Hitung akurasi klasifikasi pada dataset pelatihan dan pengujian, lalu cetak matriks kebingungan.

## Petunjuk

1. Untuk setiap digit, buat dataset untuk klasifikasi biner "digit ini vs. semua digit lainnya"
1. Latih 10 perceptron berbeda untuk klasifikasi biner (satu untuk setiap digit)
1. Definisikan fungsi yang akan mengklasifikasikan digit input

> **Petunjuk**: Jika kita menggabungkan bobot dari semua 10 perceptron ke dalam satu matriks, kita dapat menerapkan semua 10 perceptron ke digit input hanya dengan satu operasi perkalian matriks. Digit yang paling mungkin dapat ditemukan hanya dengan menerapkan operasi `argmax` pada output.

## Notebook Awal

Mulailah lab dengan membuka [PerceptronMultiClass.ipynb](PerceptronMultiClass.ipynb)

---

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan layanan penerjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Meskipun kami berusaha untuk memberikan hasil yang akurat, harap diingat bahwa terjemahan otomatis mungkin mengandung kesalahan atau ketidakakuratan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber yang otoritatif. Untuk informasi yang bersifat kritis, disarankan menggunakan jasa penerjemahan profesional oleh manusia. Kami tidak bertanggung jawab atas kesalahpahaman atau penafsiran yang keliru yang timbul dari penggunaan terjemahan ini.