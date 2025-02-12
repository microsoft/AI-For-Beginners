# Klasifikasi Muka Haiwan Peliharaan

Tugasan Makmal dari [Kurikulum AI untuk Pemula](https://github.com/microsoft/ai-for-beginners).

## Tugas

Bayangkan anda perlu membangunkan aplikasi untuk pusat jagaan haiwan peliharaan untuk mengatalogkan semua haiwan peliharaan. Salah satu ciri hebat aplikasi seperti itu adalah penemuan automatik baka dari gambar. Ini boleh dilakukan dengan berjaya menggunakan rangkaian neural.

Anda perlu melatih rangkaian neural konvolusi untuk mengklasifikasikan pelbagai baka kucing dan anjing menggunakan dataset **Muka Haiwan Peliharaan**.

## Dataset

Kami akan menggunakan dataset **Muka Haiwan Peliharaan**, yang diperoleh dari dataset haiwan peliharaan [Oxford-IIIT](https://www.robots.ox.ac.uk/~vgg/data/pets/). Ia mengandungi 35 baka berbeza bagi anjing dan kucing.

![Dataset yang akan kami uruskan](../../../../../../translated_images/data.50b2a9d5484bdbf0f52f5765b381cec9efe2bd296a98f007f90bedb6ac67f2a8.ms.png)

Untuk memuat turun dataset, gunakan petikan kod ini:

```python
!wget https://mslearntensorflowlp.blob.core.windows.net/data/petfaces.tar.gz
!tar xfz petfaces.tar.gz
!rm petfaces.tar.gz
```

## Memulakan Notebook

Mulakan makmal dengan membuka [PetFaces.ipynb](../../../../../../lessons/4-ComputerVision/07-ConvNets/lab/PetFaces.ipynb)

## Pengajaran

Anda telah menyelesaikan masalah yang agak kompleks dalam pengklasifikasian imej dari awal! Terdapat banyak kelas, dan anda masih mampu mencapai ketepatan yang munasabah! Ia juga masuk akal untuk mengukur ketepatan top-k, kerana mudah untuk mengelirukan beberapa kelas yang tidak jelas berbeza walaupun kepada manusia.

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI berasaskan mesin. Walaupun kami berusaha untuk ketepatan, sila ambil perhatian bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidaktepatan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber yang berwibawa. Untuk maklumat yang kritikal, terjemahan manusia profesional disyorkan. Kami tidak bertanggungjawab atas sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.