# Klasifikasi Haiwan Peliharaan Oxford menggunakan Pembelajaran Pemindahan

Tugasan Makmal dari [Kurikulum AI untuk Pemula](https://github.com/microsoft/ai-for-beginners).

## Tugas

Bayangkan anda perlu membangunkan aplikasi untuk pusat penjagaan haiwan peliharaan untuk mengkatalog semua haiwan peliharaan. Salah satu ciri hebat aplikasi tersebut adalah penemuan automatik baka dari gambar. Dalam tugasan ini, kita akan menggunakan pembelajaran pemindahan untuk mengklasifikasikan imej haiwan peliharaan sebenar dari dataset haiwan peliharaan [Oxford-IIIT](https://www.robots.ox.ac.uk/~vgg/data/pets/).

## Dataset

Kita akan menggunakan dataset haiwan peliharaan [Oxford-IIIT](https://www.robots.ox.ac.uk/~vgg/data/pets/) yang asal, yang mengandungi 35 baka anjing dan kucing yang berbeza.

Untuk memuat turun dataset, gunakan petikan kod ini:

```python
!wget https://www.robots.ox.ac.uk/~vgg/data/pets/data/images.tar.gz
!tar xfz images.tar.gz
!rm images.tar.gz
```

## Memulakan Notebook

Mulakan makmal dengan membuka [OxfordPets.ipynb](../../../../../../lessons/4-ComputerVision/08-TransferLearning/lab/OxfordPets.ipynb)

## Pengajaran

Pembelajaran pemindahan dan rangkaian yang telah dilatih membolehkan kita menyelesaikan masalah pengklasifikasian imej dunia nyata dengan agak mudah. Walau bagaimanapun, rangkaian yang telah dilatih berfungsi dengan baik pada imej yang sejenis, dan jika kita mula mengklasifikasikan imej yang sangat berbeza (contohnya, imej perubatan), kita mungkin akan mendapatkan hasil yang jauh lebih buruk.

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI berasaskan mesin. Walaupun kami berusaha untuk ketepatan, sila ambil perhatian bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidakakuratan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber yang sah. Untuk maklumat yang kritikal, terjemahan manusia profesional disyorkan. Kami tidak bertanggungjawab atas sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.