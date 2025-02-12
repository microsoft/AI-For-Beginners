# Klasifikasi Pelbagai Kelas dengan Perceptron

Tugasan Makmal dari [Kurikulum AI untuk Pemula](https://github.com/microsoft/ai-for-beginners).

## Tugas

Menggunakan kod yang telah kita bangunkan dalam pelajaran ini untuk klasifikasi binari digit tulisan tangan MNIST, buat klasifikasi pelbagai kelas yang dapat mengenali mana-mana digit. Kira ketepatan klasifikasi pada dataset latihan dan ujian, dan cetak matriks kekeliruan.

## Petunjuk

1. Untuk setiap digit, buat dataset untuk pengklasifikasi binari "digit ini vs. semua digit lain"
1. Latih 10 perceptron yang berbeza untuk klasifikasi binari (satu untuk setiap digit)
1. Definisikan fungsi yang akan mengklasifikasikan digit input

> **Petunjuk**: Jika kita menggabungkan berat semua 10 perceptron ke dalam satu matriks, kita seharusnya dapat menerapkan semua 10 perceptron pada digit input dengan satu pendaraban matriks. Digit yang paling mungkin dapat ditemui hanya dengan menerapkan `argmax` operasi pada output.

## Memulakan Notebook

Mulakan makmal dengan membuka [PerceptronMultiClass.ipynb](../../../../../../lessons/3-NeuralNetworks/03-Perceptron/lab/PerceptronMultiClass.ipynb)

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan berasaskan AI. Walaupun kami berusaha untuk ketepatan, sila sedar bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidakakuratan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber yang sah. Untuk maklumat yang kritikal, terjemahan manusia profesional disyorkan. Kami tidak bertanggungjawab atas sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.