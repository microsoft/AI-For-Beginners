# Pengelasan Haiwan Peliharaan Oxford menggunakan Pembelajaran Pindahan

Tugasan Makmal daripada [Kurikulum AI untuk Pemula](https://github.com/microsoft/ai-for-beginners).

## Tugasan

Bayangkan anda perlu membangunkan aplikasi untuk pusat penjagaan haiwan peliharaan bagi mengkatalogkan semua haiwan peliharaan. Salah satu ciri hebat aplikasi tersebut adalah mengenal pasti baka secara automatik daripada gambar. Dalam tugasan ini, kita akan menggunakan pembelajaran pindahan untuk mengelaskan imej haiwan peliharaan sebenar daripada set data haiwan peliharaan [Oxford-IIIT](https://www.robots.ox.ac.uk/~vgg/data/pets/).

## Set Data

Kita akan menggunakan set data asal [Oxford-IIIT](https://www.robots.ox.ac.uk/~vgg/data/pets/), yang mengandungi 35 baka anjing dan kucing yang berbeza.

Untuk memuat turun set data, gunakan petikan kod berikut:

```python
!wget https://www.robots.ox.ac.uk/~vgg/data/pets/data/images.tar.gz
!tar xfz images.tar.gz
!rm images.tar.gz
```

## Memulakan Notebook

Mulakan makmal dengan membuka [OxfordPets.ipynb](OxfordPets.ipynb)

## Kesimpulan

Pembelajaran pindahan dan rangkaian pra-latih membolehkan kita menyelesaikan masalah pengelasan imej dunia sebenar dengan agak mudah. Walau bagaimanapun, rangkaian pra-latih berfungsi dengan baik pada imej yang serupa, dan jika kita mula mengelaskan imej yang sangat berbeza (contohnya, imej perubatan), kemungkinan besar kita akan mendapat keputusan yang jauh lebih buruk.

---

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Walaupun kami berusaha untuk memastikan ketepatan, sila ambil perhatian bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidaktepatan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber yang berwibawa. Untuk maklumat penting, terjemahan manusia profesional adalah disyorkan. Kami tidak bertanggungjawab atas sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.