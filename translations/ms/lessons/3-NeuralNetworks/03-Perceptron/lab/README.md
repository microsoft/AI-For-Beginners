# Pengelasan Pelbagai Kelas dengan Perceptron

Tugasan Makmal daripada [Kurikulum AI untuk Pemula](https://github.com/microsoft/ai-for-beginners).

## Tugasan

Menggunakan kod yang telah kita bangunkan dalam pelajaran ini untuk pengelasan binari digit tulisan tangan MNIST, bina pengelas pelbagai kelas yang mampu mengenal pasti sebarang digit. Kira ketepatan pengelasan pada dataset latihan dan ujian, dan cetak matriks kekeliruan.

## Petunjuk

1. Untuk setiap digit, cipta dataset untuk pengelas binari "digit ini vs. semua digit lain"
1. Latih 10 perceptron berbeza untuk pengelasan binari (satu untuk setiap digit)
1. Definisikan fungsi yang akan mengelaskan digit input

> **Petunjuk**: Jika kita gabungkan berat bagi kesemua 10 perceptron ke dalam satu matriks, kita sepatutnya dapat menggunakan kesemua 10 perceptron pada digit input dengan satu pendaraban matriks. Digit yang paling mungkin boleh ditemui hanya dengan menggunakan operasi `argmax` pada output.

## Notebook Permulaan

Mulakan makmal dengan membuka [PerceptronMultiClass.ipynb](PerceptronMultiClass.ipynb)

---

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Walaupun kami berusaha untuk memastikan ketepatan, sila ambil perhatian bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidaktepatan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber yang berwibawa. Untuk maklumat yang kritikal, terjemahan manusia profesional adalah disyorkan. Kami tidak bertanggungjawab atas sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.