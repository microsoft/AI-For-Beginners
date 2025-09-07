<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f3d2cee9cb3c52160419e560c57a690e",
  "translation_date": "2025-08-29T12:20:28+00:00",
  "source_file": "lessons/4-ComputerVision/07-ConvNets/lab/README.md",
  "language_code": "id"
}
-->
# Klasifikasi Wajah Hewan Peliharaan

Tugas Lab dari [AI for Beginners Curriculum](https://github.com/microsoft/ai-for-beginners).

## Tugas

Bayangkan Anda perlu mengembangkan aplikasi untuk tempat penitipan hewan peliharaan guna mencatat semua hewan. Salah satu fitur hebat dari aplikasi semacam itu adalah kemampuan untuk secara otomatis mengenali ras dari sebuah foto. Hal ini dapat dilakukan dengan sukses menggunakan jaringan saraf.

Anda perlu melatih jaringan saraf konvolusi untuk mengklasifikasikan berbagai ras kucing dan anjing menggunakan dataset **Pet Faces**.

## Dataset

Kita akan menggunakan dataset **Pet Faces**, yang berasal dari dataset hewan peliharaan [Oxford-IIIT](https://www.robots.ox.ac.uk/~vgg/data/pets/). Dataset ini berisi 35 ras berbeda dari anjing dan kucing.

![Dataset yang akan kita gunakan](../../../../../../translated_images/data.50b2a9d5484bdbf0f52f5765b381cec9efe2bd296a98f007f90bedb6ac67f2a8.id.png)

Untuk mengunduh dataset, gunakan cuplikan kode berikut:

```python
!wget https://mslearntensorflowlp.blob.core.windows.net/data/petfaces.tar.gz
!tar xfz petfaces.tar.gz
!rm petfaces.tar.gz
```

## Memulai Notebook

Mulailah lab dengan membuka [PetFaces.ipynb](PetFaces.ipynb)

## Kesimpulan

Anda telah menyelesaikan masalah yang cukup kompleks dalam klasifikasi gambar dari awal! Ada cukup banyak kelas, dan Anda masih mampu mendapatkan akurasi yang masuk akal! Selain itu, masuk akal untuk mengukur akurasi top-k, karena mudah untuk membingungkan beberapa kelas yang bahkan tidak jelas berbeda bagi manusia.

---

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan layanan penerjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Meskipun kami berupaya untuk memberikan hasil yang akurat, harap diperhatikan bahwa terjemahan otomatis mungkin mengandung kesalahan atau ketidakakuratan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber yang berwenang. Untuk informasi yang bersifat kritis, disarankan menggunakan jasa penerjemahan manusia profesional. Kami tidak bertanggung jawab atas kesalahpahaman atau penafsiran yang keliru yang timbul dari penggunaan terjemahan ini.