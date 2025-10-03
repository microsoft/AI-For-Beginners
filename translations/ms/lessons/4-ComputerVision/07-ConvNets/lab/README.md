<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f3d2cee9cb3c52160419e560c57a690e",
  "translation_date": "2025-08-29T11:48:08+00:00",
  "source_file": "lessons/4-ComputerVision/07-ConvNets/lab/README.md",
  "language_code": "ms"
}
-->
# Pengelasan Wajah Haiwan Peliharaan

Tugasan Makmal daripada [Kurikulum AI untuk Pemula](https://github.com/microsoft/ai-for-beginners).

## Tugasan

Bayangkan anda perlu membangunkan aplikasi untuk pusat penjagaan haiwan peliharaan bagi mengkatalogkan semua haiwan peliharaan. Salah satu ciri hebat aplikasi tersebut ialah mengenal pasti baka secara automatik daripada gambar. Ini boleh dilakukan dengan jayanya menggunakan rangkaian neural.

Anda perlu melatih rangkaian neural konvolusi untuk mengelaskan pelbagai baka kucing dan anjing menggunakan dataset **Pet Faces**.

## Dataset

Kita akan menggunakan dataset **Pet Faces**, yang diambil daripada dataset haiwan peliharaan [Oxford-IIIT](https://www.robots.ox.ac.uk/~vgg/data/pets/). Ia mengandungi 35 baka anjing dan kucing yang berbeza.

![Dataset yang akan kita gunakan](../../../../../../translated_images/data.50b2a9d5484bdbf0f52f5765b381cec9efe2bd296a98f007f90bedb6ac67f2a8.ms.png)

Untuk memuat turun dataset, gunakan kod berikut:

```python
!wget https://thor.robots.ox.ac.uk/~vgg/data/pets/images.tar.gz
!tar xfz images.tar.gz
!rm images.tar.gz
```

## Memulakan Notebook

Mulakan makmal dengan membuka [PetFaces.ipynb](PetFaces.ipynb)

## Kesimpulan

Anda telah menyelesaikan masalah pengelasan imej yang agak kompleks dari awal! Terdapat banyak kelas, dan anda masih mampu mencapai ketepatan yang munasabah! Ia juga masuk akal untuk mengukur ketepatan top-k, kerana mudah untuk mengelirukan beberapa kelas yang tidak begitu jelas berbeza walaupun kepada manusia.

---

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Walaupun kami berusaha untuk memastikan ketepatan, sila ambil perhatian bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidaktepatan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber yang berwibawa. Untuk maklumat penting, terjemahan manusia profesional adalah disyorkan. Kami tidak bertanggungjawab atas sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.