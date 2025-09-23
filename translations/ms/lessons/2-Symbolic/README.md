<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "7d097f7fda9166ead615e4c34552381b",
  "translation_date": "2025-09-23T10:51:20+00:00",
  "source_file": "lessons/2-Symbolic/README.md",
  "language_code": "ms"
}
-->
# Perwakilan Pengetahuan dan Sistem Pakar

![Ringkasan kandungan AI Simbolik](../../../../translated_images/ai-symbolic.715a30cb610411a6964d2e2f23f24364cb338a07cb4844c1f97084d366e586c3.ms.png)

> Sketchnote oleh [Tomomi Imura](https://twitter.com/girlie_mac)

Pencarian untuk kecerdasan buatan adalah berdasarkan usaha untuk mencari pengetahuan, bagi memahami dunia seperti manusia. Tetapi bagaimana caranya untuk melakukannya?

## [Kuiz pra-kuliah](https://ff-quizzes.netlify.app/en/ai/quiz/3)

Pada zaman awal AI, pendekatan dari atas ke bawah untuk mencipta sistem pintar (dibincangkan dalam pelajaran sebelumnya) adalah popular. Ideanya adalah untuk mengekstrak pengetahuan daripada manusia ke dalam bentuk yang boleh dibaca mesin, dan kemudian menggunakannya untuk menyelesaikan masalah secara automatik. Pendekatan ini berdasarkan dua idea besar:

* Perwakilan Pengetahuan
* Penaakulan

## Perwakilan Pengetahuan

Salah satu konsep penting dalam AI Simbolik ialah **pengetahuan**. Adalah penting untuk membezakan pengetahuan daripada *maklumat* atau *data*. Sebagai contoh, seseorang boleh mengatakan bahawa buku mengandungi pengetahuan, kerana seseorang boleh belajar daripada buku dan menjadi pakar. Walau bagaimanapun, apa yang terkandung dalam buku sebenarnya dipanggil *data*, dan dengan membaca buku serta mengintegrasikan data ini ke dalam model dunia kita, kita menukar data ini kepada pengetahuan.

> ✅ **Pengetahuan** adalah sesuatu yang terkandung dalam fikiran kita dan mewakili pemahaman kita tentang dunia. Ia diperoleh melalui proses **pembelajaran** yang aktif, yang mengintegrasikan kepingan maklumat yang kita terima ke dalam model dunia kita yang aktif.

Kebiasaannya, kita tidak mentakrifkan pengetahuan secara ketat, tetapi kita menyelaraskannya dengan konsep berkaitan lain menggunakan [Piramid DIKW](https://en.wikipedia.org/wiki/DIKW_pyramid). Ia mengandungi konsep berikut:

* **Data** adalah sesuatu yang diwakili dalam media fizikal, seperti teks bertulis atau kata-kata yang diucapkan. Data wujud secara bebas daripada manusia dan boleh dipindahkan antara individu.
* **Maklumat** adalah bagaimana kita mentafsir data dalam fikiran kita. Sebagai contoh, apabila kita mendengar perkataan *komputer*, kita mempunyai pemahaman tertentu tentang apa itu.
* **Pengetahuan** adalah maklumat yang diintegrasikan ke dalam model dunia kita. Sebagai contoh, setelah kita belajar apa itu komputer, kita mula mempunyai idea tentang bagaimana ia berfungsi, berapa harganya, dan untuk apa ia boleh digunakan. Rangkaian konsep yang saling berkaitan ini membentuk pengetahuan kita.
* **Kebijaksanaan** adalah satu lagi tahap pemahaman kita tentang dunia, dan ia mewakili *meta-pengetahuan*, contohnya, beberapa tanggapan tentang bagaimana dan bila pengetahuan itu harus digunakan.

<img src="images/DIKW_Pyramid.png" width="30%"/>

*Imej [dari Wikipedia](https://commons.wikimedia.org/w/index.php?curid=37705247), Oleh Longlivetheux - Karya sendiri, CC BY-SA 4.0*

Oleh itu, masalah **perwakilan pengetahuan** adalah untuk mencari cara yang berkesan untuk mewakili pengetahuan dalam komputer dalam bentuk data, supaya ia boleh digunakan secara automatik. Ini boleh dilihat sebagai spektrum:

![Spektrum perwakilan pengetahuan](../../../../translated_images/knowledge-spectrum.b60df631852c0217e941485b79c9eee40ebd574f15f18609cec5758fcb384bf3.ms.png)

> Imej oleh [Dmitry Soshnikov](http://soshnikov.com)

* Di sebelah kiri, terdapat jenis perwakilan pengetahuan yang sangat mudah yang boleh digunakan secara berkesan oleh komputer. Yang paling mudah ialah algoritma, di mana pengetahuan diwakili oleh program komputer. Walau bagaimanapun, ini bukan cara terbaik untuk mewakili pengetahuan, kerana ia tidak fleksibel. Pengetahuan dalam fikiran kita sering kali tidak bersifat algoritma.
* Di sebelah kanan, terdapat perwakilan seperti teks semula jadi. Ia adalah yang paling berkuasa, tetapi tidak boleh digunakan untuk penaakulan automatik.

> ✅ Fikirkan sejenak bagaimana anda mewakili pengetahuan dalam fikiran anda dan menukarkannya kepada nota. Adakah terdapat format tertentu yang berkesan untuk membantu anda mengingati?

## Mengklasifikasikan Perwakilan Pengetahuan Komputer

Kita boleh mengklasifikasikan pelbagai kaedah perwakilan pengetahuan komputer dalam kategori berikut:

* **Perwakilan rangkaian** adalah berdasarkan fakta bahawa kita mempunyai rangkaian konsep yang saling berkaitan dalam fikiran kita. Kita boleh cuba menghasilkan semula rangkaian yang sama sebagai graf dalam komputer - yang dipanggil **rangkaian semantik**.

1. **Triplet Objek-Atribut-Nilai** atau **pasangan atribut-nilai**. Oleh kerana graf boleh diwakili dalam komputer sebagai senarai nod dan tepi, kita boleh mewakili rangkaian semantik dengan senarai triplet, yang mengandungi objek, atribut, dan nilai. Sebagai contoh, kita membina triplet berikut tentang bahasa pengaturcaraan:

Objek | Atribut | Nilai
-------|---------|------
Python | ialah | Bahasa-Tanpa-Taip
Python | dicipta-oleh | Guido van Rossum
Python | sintaks-blok | indentasi
Bahasa-Tanpa-Taip | tidak mempunyai | definisi jenis

> ✅ Fikirkan bagaimana triplet boleh digunakan untuk mewakili jenis pengetahuan lain.

2. **Perwakilan hierarki** menekankan fakta bahawa kita sering mencipta hierarki objek dalam fikiran kita. Sebagai contoh, kita tahu bahawa kenari adalah burung, dan semua burung mempunyai sayap. Kita juga mempunyai idea tentang warna kenari biasanya, dan kelajuan penerbangannya.

   - **Perwakilan bingkai** adalah berdasarkan mewakili setiap objek atau kelas objek sebagai **bingkai** yang mengandungi **slot**. Slot mempunyai nilai lalai yang mungkin, sekatan nilai, atau prosedur yang disimpan yang boleh dipanggil untuk mendapatkan nilai slot. Semua bingkai membentuk hierarki yang serupa dengan hierarki objek dalam bahasa pengaturcaraan berorientasikan objek.
   - **Senario** adalah jenis bingkai khas yang mewakili situasi kompleks yang boleh berkembang mengikut masa.

**Python**

Slot | Nilai | Nilai Lalai | Julat |
-----|-------|-------------|-------|
Nama | Python | | |
Adalah | Bahasa-Tanpa-Taip | | |
Kes Pemboleh Ubah | | CamelCase | |
Panjang Program | | | 5-5000 baris |
Sintaks Blok | Indentasi | | |

3. **Perwakilan prosedural** adalah berdasarkan mewakili pengetahuan dengan senarai tindakan yang boleh dilaksanakan apabila keadaan tertentu berlaku.
   - Peraturan pengeluaran adalah pernyataan if-then yang membolehkan kita membuat kesimpulan. Sebagai contoh, seorang doktor boleh mempunyai peraturan yang mengatakan bahawa **JIKA** pesakit mempunyai demam tinggi **ATAU** tahap protein C-reaktif yang tinggi dalam ujian darah **MAKA** dia mempunyai keradangan. Sebaik sahaja kita menemui salah satu keadaan, kita boleh membuat kesimpulan tentang keradangan, dan kemudian menggunakannya dalam penaakulan selanjutnya.
   - Algoritma boleh dianggap sebagai satu lagi bentuk perwakilan prosedural, walaupun ia hampir tidak pernah digunakan secara langsung dalam sistem berasaskan pengetahuan.

4. **Logik** pada asalnya dicadangkan oleh Aristotle sebagai cara untuk mewakili pengetahuan manusia sejagat.
   - Logik Predikat sebagai teori matematik terlalu kaya untuk dikira, oleh itu beberapa subsetnya biasanya digunakan, seperti klausa Horn yang digunakan dalam Prolog.
   - Logik Deskriptif adalah keluarga sistem logik yang digunakan untuk mewakili dan membuat penaakulan tentang hierarki objek dalam perwakilan pengetahuan teragih seperti *web semantik*.

## Sistem Pakar

Salah satu kejayaan awal AI simbolik ialah **sistem pakar** - sistem komputer yang direka untuk bertindak sebagai pakar dalam domain masalah yang terhad. Ia berdasarkan **pangkalan pengetahuan** yang diekstrak daripada satu atau lebih pakar manusia, dan mengandungi **enjin inferens** yang melakukan beberapa penaakulan di atasnya.

![Seni Bina Manusia](../../../../translated_images/arch-human.5d4d35f1bba3ab1cdfda96af2f10b89574eb31e9796d0e3011cd9beda1c35112.ms.png) | ![Sistem Berasaskan Pengetahuan](../../../../translated_images/arch-kbs.3ec5c150b09fa8dadc2beb0931a4983c9e2b03913a89eebcc103b5bb841b0212.ms.png)
---------------------------------------------|------------------------------------------------
Struktur ringkas sistem saraf manusia         | Seni bina sistem berasaskan pengetahuan

Sistem pakar dibina seperti sistem penaakulan manusia, yang mengandungi **memori jangka pendek** dan **memori jangka panjang**. Begitu juga, dalam sistem berasaskan pengetahuan kita membezakan komponen berikut:

* **Memori masalah**: mengandungi pengetahuan tentang masalah yang sedang diselesaikan, contohnya suhu atau tekanan darah pesakit, sama ada dia mempunyai keradangan atau tidak, dan sebagainya. Pengetahuan ini juga dipanggil **pengetahuan statik**, kerana ia mengandungi gambaran tentang apa yang kita ketahui tentang masalah itu - yang dipanggil *keadaan masalah*.
* **Pangkalan pengetahuan**: mewakili pengetahuan jangka panjang tentang domain masalah. Ia diekstrak secara manual daripada pakar manusia, dan tidak berubah dari satu konsultasi ke konsultasi yang lain. Oleh kerana ia membolehkan kita menavigasi dari satu keadaan masalah ke keadaan yang lain, ia juga dipanggil **pengetahuan dinamik**.
* **Enjin inferens**: mengatur keseluruhan proses pencarian dalam ruang keadaan masalah, bertanya soalan kepada pengguna apabila perlu. Ia juga bertanggungjawab untuk mencari peraturan yang betul untuk digunakan pada setiap keadaan.

Sebagai contoh, mari kita pertimbangkan sistem pakar berikut untuk menentukan haiwan berdasarkan ciri fizikalnya:

![Pokok AND-OR](../../../../translated_images/AND-OR-Tree.5592d2c70187f283703c8e9c0d69d6a786eb370f4ace67f9a7aae5ada3d260b0.ms.png)

> Imej oleh [Dmitry Soshnikov](http://soshnikov.com)

Rajah ini dipanggil **pokok AND-OR**, dan ia adalah perwakilan grafik bagi satu set peraturan pengeluaran. Melukis pokok adalah berguna pada permulaan proses mengekstrak pengetahuan daripada pakar. Untuk mewakili pengetahuan dalam komputer, lebih mudah menggunakan peraturan:

```
IF the animal eats meat
OR (animal has sharp teeth
    AND animal has claws
    AND animal has forward-looking eyes
) 
THEN the animal is a carnivore
```

Anda boleh perhatikan bahawa setiap keadaan di sebelah kiri peraturan dan tindakan pada dasarnya adalah triplet objek-atribut-nilai (OAV). **Memori kerja** mengandungi set triplet OAV yang sepadan dengan masalah yang sedang diselesaikan. **Enjin peraturan** mencari peraturan yang keadaannya dipenuhi dan menerapkannya, menambah satu lagi triplet ke dalam memori kerja.

> ✅ Lukis pokok AND-OR anda sendiri tentang topik yang anda suka!

### Inferens Maju vs. Inferens Mundur

Proses yang diterangkan di atas dipanggil **inferens maju**. Ia bermula dengan beberapa data awal tentang masalah yang tersedia dalam memori kerja, dan kemudian melaksanakan gelung penaakulan berikut:

1. Jika atribut sasaran terdapat dalam memori kerja - berhenti dan berikan hasil
2. Cari semua peraturan yang keadaannya dipenuhi - dapatkan **set konflik** peraturan.
3. Lakukan **resolusi konflik** - pilih satu peraturan yang akan dilaksanakan pada langkah ini. Terdapat pelbagai strategi resolusi konflik:
   - Pilih peraturan pertama yang boleh digunakan dalam pangkalan pengetahuan
   - Pilih peraturan secara rawak
   - Pilih peraturan yang *lebih spesifik*, iaitu yang memenuhi kebanyakan keadaan di "sebelah kiri" (LHS)
4. Terapkan peraturan yang dipilih dan masukkan pengetahuan baru ke dalam keadaan masalah
5. Ulangi dari langkah 1.

Walau bagaimanapun, dalam beberapa kes kita mungkin ingin bermula dengan pengetahuan kosong tentang masalah, dan bertanya soalan yang akan membantu kita mencapai kesimpulan. Sebagai contoh, semasa membuat diagnosis perubatan, kita biasanya tidak melakukan semua analisis perubatan terlebih dahulu sebelum mula mendiagnosis pesakit. Sebaliknya, kita ingin melakukan analisis apabila keputusan perlu dibuat.

Proses ini boleh dimodelkan menggunakan **inferens mundur**. Ia didorong oleh **matlamat** - nilai atribut yang kita cari:

1. Pilih semua peraturan yang boleh memberikan nilai matlamat (iaitu dengan matlamat di RHS ("sebelah kanan")) - set konflik
1. Jika tiada peraturan untuk atribut ini, atau terdapat peraturan yang mengatakan bahawa kita harus bertanya nilai daripada pengguna - tanyakan, jika tidak:
1. Gunakan strategi resolusi konflik untuk memilih satu peraturan yang akan kita gunakan sebagai *hipotesis* - kita akan cuba membuktikannya
1. Ulangi proses ini secara berulang untuk semua atribut di LHS peraturan, cuba membuktikannya sebagai matlamat
1. Jika pada bila-bila masa proses gagal - gunakan peraturan lain pada langkah 3.

> ✅ Dalam situasi apakah inferens maju lebih sesuai? Bagaimana pula dengan inferens mundur?

### Melaksanakan Sistem Pakar

Sistem pakar boleh dilaksanakan menggunakan pelbagai alat:

* Memprogramkannya secara langsung dalam beberapa bahasa pengaturcaraan peringkat tinggi. Ini bukan idea terbaik, kerana kelebihan utama sistem berasaskan pengetahuan ialah pengetahuan dipisahkan daripada inferens, dan berpotensi seorang pakar domain masalah sepatutnya dapat menulis peraturan tanpa memahami butiran proses inferens.
* Menggunakan **kerangka sistem pakar**, iaitu sistem yang direka khusus untuk diisi dengan pengetahuan menggunakan beberapa bahasa perwakilan pengetahuan.

## ✍️ Latihan: Inferens Haiwan

Lihat [Animals.ipynb](https://github.com/microsoft/AI-For-Beginners/blob/main/lessons/2-Symbolic/Animals.ipynb) untuk contoh melaksanakan sistem pakar inferens maju dan mundur.

> **Nota**: Contoh ini agak mudah, dan hanya memberikan idea tentang bagaimana rupa sistem pakar. Sebaik sahaja anda mula mencipta sistem seperti ini, anda hanya akan melihat beberapa tingkah laku *pintar* daripadanya apabila anda mencapai bilangan peraturan tertentu, sekitar 200+. Pada satu ketika, peraturan menjadi terlalu kompleks untuk diingati semuanya, dan pada ketika ini anda mungkin mula tertanya-tanya mengapa sistem membuat keputusan tertentu. Walau bagaimanapun, ciri penting sistem berasaskan pengetahuan ialah anda sentiasa boleh *menjelaskan* dengan tepat bagaimana mana-mana keputusan dibuat.

## Ontologi dan Web Semantik

Pada akhir abad ke-20, terdapat inisiatif untuk menggunakan perwakilan pengetahuan untuk memberi anotasi kepada sumber Internet, supaya ia mungkin untuk mencari sumber yang sepadan dengan pertanyaan yang sangat spesifik. Gerakan ini dipanggil **Web Semantik**, dan ia bergantung pada beberapa konsep:

- Perwakilan pengetahuan khas berdasarkan **[logik deskriptif](https://en.wikipedia.org/wiki/Description_logic)** (DL). Ia serupa dengan perwakilan pengetahuan bingkai, kerana ia membina hierarki objek dengan sifat, tetapi ia mempunyai semantik logik formal dan inferens. Terdapat keseluruhan keluarga DL yang mengimbangi antara ekspresiviti dan kerumitan algoritma inferens.
- Perwakilan pengetahuan teragih, di mana semua konsep diwakili oleh pengenal URI global, menjadikannya mungkin untuk mencipta hierarki pengetahuan yang merangkumi internet.
- Satu keluarga bahasa berasaskan XML untuk penerangan pengetahuan: RDF (Resource Description Framework), RDFS (RDF Schema), OWL (Ontology Web Language).

Konsep utama dalam Web Semantik ialah konsep **Ontologi**. Ia merujuk kepada spesifikasi eksplisit bagi domain masalah menggunakan beberapa representasi pengetahuan formal. Ontologi yang paling mudah boleh menjadi hierarki objek dalam domain masalah, tetapi ontologi yang lebih kompleks akan merangkumi peraturan yang boleh digunakan untuk inferens.

Dalam web semantik, semua representasi adalah berdasarkan triplet. Setiap objek dan setiap hubungan dikenalpasti secara unik oleh URI. Sebagai contoh, jika kita ingin menyatakan fakta bahawa Kurikulum AI ini telah dibangunkan oleh Dmitry Soshnikov pada 1 Januari 2022 - berikut adalah triplet yang boleh kita gunakan:

<img src="images/triplet.png" width="30%"/>

```
http://github.com/microsoft/ai-for-beginners http://www.example.com/terms/creation-date “Jan 13, 2007”
http://github.com/microsoft/ai-for-beginners http://purl.org/dc/elements/1.1/creator http://soshnikov.com
```

> ✅ Di sini `http://www.example.com/terms/creation-date` dan `http://purl.org/dc/elements/1.1/creator` adalah beberapa URI yang terkenal dan diterima secara universal untuk menyatakan konsep *creator* dan *creation date*.

Dalam kes yang lebih kompleks, jika kita ingin menentukan senarai pencipta, kita boleh menggunakan beberapa struktur data yang ditakrifkan dalam RDF.

<img src="images/triplet-complex.png" width="40%"/>

> Diagram di atas oleh [Dmitry Soshnikov](http://soshnikov.com)

Kemajuan membina Web Semantik sedikit terhalang oleh kejayaan enjin carian dan teknik pemprosesan bahasa semula jadi, yang membolehkan pengekstrakan data berstruktur daripada teks. Walau bagaimanapun, dalam beberapa bidang masih terdapat usaha yang signifikan untuk mengekalkan ontologi dan pangkalan pengetahuan. Beberapa projek yang patut diberi perhatian:

* [WikiData](https://wikidata.org/) adalah koleksi pangkalan pengetahuan yang boleh dibaca mesin yang berkaitan dengan Wikipedia. Kebanyakan data diperoleh daripada *InfoBoxes* Wikipedia, iaitu kandungan berstruktur dalam halaman Wikipedia. Anda boleh [menyiasat](https://query.wikidata.org/) WikiData menggunakan SPARQL, bahasa pertanyaan khas untuk Web Semantik. Berikut adalah contoh pertanyaan yang memaparkan warna mata paling popular di kalangan manusia:

```sparql
#defaultView:BubbleChart
SELECT ?eyeColorLabel (COUNT(?human) AS ?count)
WHERE
{
  ?human wdt:P31 wd:Q5.       # human instance-of homo sapiens
  ?human wdt:P1340 ?eyeColor. # human eye-color ?eyeColor
  SERVICE wikibase:label { bd:serviceParam wikibase:language "en". }
}
GROUP BY ?eyeColorLabel
```

* [DBpedia](https://www.dbpedia.org/) adalah satu lagi usaha yang serupa dengan WikiData.

> ✅ Jika anda ingin bereksperimen dengan membina ontologi anda sendiri, atau membuka ontologi yang sedia ada, terdapat editor ontologi visual yang hebat dipanggil [Protégé](https://protege.stanford.edu/). Muat turun, atau gunakannya secara dalam talian.

<img src="images/protege.png" width="70%"/>

*Editor Web Protégé dibuka dengan ontologi Keluarga Romanov. Tangkapan skrin oleh Dmitry Soshnikov*

## ✍️ Latihan: Ontologi Keluarga

Lihat [FamilyOntology.ipynb](https://github.com/Ezana135/AI-For-Beginners/blob/main/lessons/2-Symbolic/FamilyOntology.ipynb) untuk contoh menggunakan teknik Web Semantik untuk membuat inferens tentang hubungan keluarga. Kita akan mengambil pokok keluarga yang diwakili dalam format GEDCOM biasa dan ontologi hubungan keluarga, serta membina graf semua hubungan keluarga untuk set individu yang diberikan.

## Microsoft Concept Graph

Dalam kebanyakan kes, ontologi dibuat dengan teliti secara manual. Walau bagaimanapun, ia juga boleh **diperoleh** daripada data tidak berstruktur, contohnya, daripada teks bahasa semula jadi.

Salah satu usaha sedemikian dilakukan oleh Microsoft Research, dan menghasilkan [Microsoft Concept Graph](https://blogs.microsoft.com/ai/microsoft-researchers-release-graph-that-helps-machines-conceptualize/?WT.mc_id=academic-77998-cacaste).

Ia adalah koleksi besar entiti yang dikelompokkan bersama menggunakan hubungan pewarisan `is-a`. Ia membolehkan menjawab soalan seperti "Apa itu Microsoft?" - jawapannya adalah sesuatu seperti "sebuah syarikat dengan kebarangkalian 0.87, dan jenama dengan kebarangkalian 0.75".

Graf ini tersedia sama ada sebagai REST API, atau sebagai fail teks besar yang menyenaraikan semua pasangan entiti.

## ✍️ Latihan: Graf Konsep

Cuba notebook [MSConceptGraph.ipynb](https://github.com/microsoft/AI-For-Beginners/blob/main/lessons/2-Symbolic/MSConceptGraph.ipynb) untuk melihat bagaimana kita boleh menggunakan Microsoft Concept Graph untuk mengelompokkan artikel berita ke dalam beberapa kategori.

## Kesimpulan

Pada masa kini, AI sering dianggap sebagai sinonim untuk *Pembelajaran Mesin* atau *Rangkaian Neural*. Walau bagaimanapun, manusia juga menunjukkan penaakulan eksplisit, sesuatu yang pada masa ini tidak ditangani oleh rangkaian neural. Dalam projek dunia sebenar, penaakulan eksplisit masih digunakan untuk melaksanakan tugas yang memerlukan penjelasan, atau keupayaan untuk mengubah tingkah laku sistem dengan cara yang terkawal.

## 🚀 Cabaran

Dalam notebook Ontologi Keluarga yang berkaitan dengan pelajaran ini, terdapat peluang untuk bereksperimen dengan hubungan keluarga lain. Cuba temui hubungan baru antara orang dalam pokok keluarga.

## [Kuiz selepas kuliah](https://ff-quizzes.netlify.app/en/ai/quiz/4)

## Kajian & Pembelajaran Kendiri

Lakukan penyelidikan di internet untuk menemui bidang di mana manusia telah cuba mengukur dan mengkodkan pengetahuan. Lihat Taksonomi Bloom, dan kembali ke sejarah untuk belajar bagaimana manusia cuba memahami dunia mereka. Terokai kerja Linnaeus untuk mencipta taksonomi organisma, dan perhatikan cara Dmitri Mendeleev mencipta cara untuk menerangkan dan mengelompokkan unsur kimia. Apakah contoh menarik lain yang boleh anda temui?

**Tugasan**: [Bina Ontologi](assignment.md)

---

