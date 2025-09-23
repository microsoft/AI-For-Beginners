<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "7d097f7fda9166ead615e4c34552381b",
  "translation_date": "2025-09-23T10:41:02+00:00",
  "source_file": "lessons/2-Symbolic/README.md",
  "language_code": "id"
}
-->
# Representasi Pengetahuan dan Sistem Pakar

![Ringkasan konten AI simbolik](../../../../translated_images/ai-symbolic.715a30cb610411a6964d2e2f23f24364cb338a07cb4844c1f97084d366e586c3.id.png)

> Sketchnote oleh [Tomomi Imura](https://twitter.com/girlie_mac)

Pencarian kecerdasan buatan didasarkan pada upaya untuk memahami dunia seperti yang dilakukan manusia. Tapi bagaimana cara melakukannya?

## [Kuis pra-kuliah](https://ff-quizzes.netlify.app/en/ai/quiz/3)

Pada masa awal AI, pendekatan top-down untuk menciptakan sistem cerdas (dibahas dalam pelajaran sebelumnya) sangat populer. Ide dasarnya adalah mengekstrak pengetahuan dari manusia ke dalam bentuk yang dapat dibaca oleh mesin, lalu menggunakannya untuk menyelesaikan masalah secara otomatis. Pendekatan ini didasarkan pada dua gagasan besar:

* Representasi Pengetahuan
* Penalaran

## Representasi Pengetahuan

Salah satu konsep penting dalam AI simbolik adalah **pengetahuan**. Penting untuk membedakan pengetahuan dari *informasi* atau *data*. Misalnya, kita bisa mengatakan bahwa buku mengandung pengetahuan, karena kita bisa mempelajari buku dan menjadi ahli. Namun, apa yang sebenarnya terkandung dalam buku disebut *data*, dan dengan membaca buku serta mengintegrasikan data ini ke dalam model dunia kita, kita mengubah data menjadi pengetahuan.

> ✅ **Pengetahuan** adalah sesuatu yang ada di dalam kepala kita dan mewakili pemahaman kita tentang dunia. Pengetahuan diperoleh melalui proses **pembelajaran** aktif, yang mengintegrasikan potongan informasi yang kita terima ke dalam model dunia kita.

Sering kali, kita tidak secara ketat mendefinisikan pengetahuan, tetapi kita menyelaraskannya dengan konsep terkait lainnya menggunakan [Piramida DIKW](https://en.wikipedia.org/wiki/DIKW_pyramid). Piramida ini mencakup konsep berikut:

* **Data** adalah sesuatu yang direpresentasikan dalam media fisik, seperti teks tertulis atau kata-kata yang diucapkan. Data ada secara independen dari manusia dan dapat ditransfer antar individu.
* **Informasi** adalah cara kita menafsirkan data di dalam kepala kita. Misalnya, ketika kita mendengar kata *komputer*, kita memiliki pemahaman tertentu tentang apa itu.
* **Pengetahuan** adalah informasi yang diintegrasikan ke dalam model dunia kita. Misalnya, setelah kita belajar apa itu komputer, kita mulai memiliki gagasan tentang cara kerjanya, berapa harganya, dan untuk apa komputer dapat digunakan. Jaringan konsep yang saling terkait ini membentuk pengetahuan kita.
* **Kebijaksanaan** adalah tingkat pemahaman dunia yang lebih tinggi, yang mewakili *meta-pengetahuan*, misalnya gagasan tentang bagaimana dan kapan pengetahuan harus digunakan.

<img src="images/DIKW_Pyramid.png" width="30%"/>

*Gambar [dari Wikipedia](https://commons.wikimedia.org/w/index.php?curid=37705247), Oleh Longlivetheux - Karya sendiri, CC BY-SA 4.0*

Dengan demikian, masalah **representasi pengetahuan** adalah menemukan cara yang efektif untuk merepresentasikan pengetahuan di dalam komputer dalam bentuk data, agar dapat digunakan secara otomatis. Ini dapat dilihat sebagai spektrum:

![Spektrum representasi pengetahuan](../../../../translated_images/knowledge-spectrum.b60df631852c0217e941485b79c9eee40ebd574f15f18609cec5758fcb384bf3.id.png)

> Gambar oleh [Dmitry Soshnikov](http://soshnikov.com)

* Di sisi kiri, terdapat jenis representasi pengetahuan yang sangat sederhana yang dapat digunakan secara efektif oleh komputer. Yang paling sederhana adalah algoritmik, di mana pengetahuan direpresentasikan oleh program komputer. Namun, ini bukan cara terbaik untuk merepresentasikan pengetahuan, karena tidak fleksibel. Pengetahuan di dalam kepala kita sering kali tidak bersifat algoritmik.
* Di sisi kanan, terdapat representasi seperti teks alami. Ini adalah yang paling kuat, tetapi tidak dapat digunakan untuk penalaran otomatis.

> ✅ Pikirkan sejenak tentang bagaimana Anda merepresentasikan pengetahuan di dalam kepala Anda dan mengubahnya menjadi catatan. Apakah ada format tertentu yang membantu Anda mengingat lebih baik?

## Klasifikasi Representasi Pengetahuan Komputer

Kita dapat mengklasifikasikan berbagai metode representasi pengetahuan komputer ke dalam kategori berikut:

* **Representasi jaringan** didasarkan pada fakta bahwa kita memiliki jaringan konsep yang saling terkait di dalam kepala kita. Kita dapat mencoba mereproduksi jaringan yang sama sebagai graf di dalam komputer - yang disebut **jaringan semantik**.

1. **Triplet Objek-Atribut-Nilai** atau **pasangan atribut-nilai**. Karena graf dapat direpresentasikan di dalam komputer sebagai daftar simpul dan tepi, kita dapat merepresentasikan jaringan semantik dengan daftar triplet yang berisi objek, atribut, dan nilai. Misalnya, kita membangun triplet berikut tentang bahasa pemrograman:

Objek | Atribut | Nilai
-------|-----------|------
Python | adalah | Bahasa-Tanpa-Tipe
Python | ditemukan-oleh | Guido van Rossum
Python | sintaks-blok | indentasi
Bahasa-Tanpa-Tipe | tidak memiliki | definisi tipe

> ✅ Pikirkan bagaimana triplet dapat digunakan untuk merepresentasikan jenis pengetahuan lainnya.

2. **Representasi hierarkis** menekankan fakta bahwa kita sering kali menciptakan hierarki objek di dalam kepala kita. Misalnya, kita tahu bahwa kenari adalah burung, dan semua burung memiliki sayap. Kita juga memiliki gagasan tentang warna kenari biasanya, dan kecepatan terbangnya.

   - **Representasi bingkai** didasarkan pada merepresentasikan setiap objek atau kelas objek sebagai **bingkai** yang berisi **slot**. Slot memiliki nilai default yang mungkin, batasan nilai, atau prosedur yang disimpan yang dapat dipanggil untuk mendapatkan nilai slot. Semua bingkai membentuk hierarki yang mirip dengan hierarki objek dalam bahasa pemrograman berorientasi objek.
   - **Skenario** adalah jenis bingkai khusus yang merepresentasikan situasi kompleks yang dapat berkembang seiring waktu.

**Python**

Slot | Nilai | Nilai Default | Interval |
-----|-------|---------------|----------|
Nama | Python | | |
Adalah | Bahasa-Tanpa-Tipe | | |
Penulisan Variabel | | CamelCase | |
Panjang Program | | | 5-5000 baris |
Sintaks Blok | Indentasi | | |

3. **Representasi prosedural** didasarkan pada merepresentasikan pengetahuan dengan daftar tindakan yang dapat dieksekusi ketika kondisi tertentu terjadi.
   - Aturan produksi adalah pernyataan if-then yang memungkinkan kita menarik kesimpulan. Misalnya, seorang dokter dapat memiliki aturan yang mengatakan bahwa **JIKA** pasien memiliki demam tinggi **ATAU** tingkat protein C-reaktif tinggi dalam tes darah **MAKA** ia mengalami peradangan. Setelah kita menemukan salah satu kondisi, kita dapat membuat kesimpulan tentang peradangan, lalu menggunakannya dalam penalaran lebih lanjut.
   - Algoritma dapat dianggap sebagai bentuk lain dari representasi prosedural, meskipun hampir tidak pernah digunakan langsung dalam sistem berbasis pengetahuan.

4. **Logika** awalnya diusulkan oleh Aristoteles sebagai cara untuk merepresentasikan pengetahuan manusia universal.
   - Logika Predikat sebagai teori matematika terlalu kaya untuk dapat dihitung, sehingga biasanya digunakan subsetnya, seperti klausa Horn yang digunakan dalam Prolog.
   - Logika Deskriptif adalah keluarga sistem logika yang digunakan untuk merepresentasikan dan menalar tentang hierarki objek dalam representasi pengetahuan terdistribusi seperti *web semantik*.

## Sistem Pakar

Salah satu keberhasilan awal AI simbolik adalah **sistem pakar** - sistem komputer yang dirancang untuk bertindak sebagai pakar dalam domain masalah yang terbatas. Sistem ini didasarkan pada **basis pengetahuan** yang diekstraksi dari satu atau lebih pakar manusia, dan mereka memiliki **mesin inferensi** yang melakukan penalaran di atasnya.

![Arsitektur Manusia](../../../../translated_images/arch-human.5d4d35f1bba3ab1cdfda96af2f10b89574eb31e9796d0e3011cd9beda1c35112.id.png) | ![Sistem Berbasis Pengetahuan](../../../../translated_images/arch-kbs.3ec5c150b09fa8dadc2beb0931a4983c9e2b03913a89eebcc103b5bb841b0212.id.png)
---------------------------------------------|------------------------------------------------
Struktur sederhana sistem saraf manusia       | Arsitektur sistem berbasis pengetahuan

Sistem pakar dibangun seperti sistem penalaran manusia, yang mengandung **memori jangka pendek** dan **memori jangka panjang**. Demikian pula, dalam sistem berbasis pengetahuan kita membedakan komponen berikut:

* **Memori masalah**: berisi pengetahuan tentang masalah yang sedang diselesaikan, misalnya suhu atau tekanan darah pasien, apakah ia mengalami peradangan atau tidak, dll. Pengetahuan ini juga disebut **pengetahuan statis**, karena berisi snapshot dari apa yang kita ketahui tentang masalah saat ini - yang disebut *status masalah*.
* **Basis pengetahuan**: merepresentasikan pengetahuan jangka panjang tentang domain masalah. Basis ini diekstraksi secara manual dari pakar manusia, dan tidak berubah dari satu konsultasi ke konsultasi lainnya. Karena memungkinkan kita untuk menavigasi dari satu status masalah ke status lainnya, basis ini juga disebut **pengetahuan dinamis**.
* **Mesin inferensi**: mengatur seluruh proses pencarian dalam ruang status masalah, mengajukan pertanyaan kepada pengguna jika diperlukan. Mesin ini juga bertanggung jawab untuk menemukan aturan yang tepat untuk diterapkan pada setiap status.

Sebagai contoh, mari kita pertimbangkan sistem pakar berikut untuk menentukan hewan berdasarkan karakteristik fisiknya:

![Pohon AND-OR](../../../../translated_images/AND-OR-Tree.5592d2c70187f283703c8e9c0d69d6a786eb370f4ace67f9a7aae5ada3d260b0.id.png)

> Gambar oleh [Dmitry Soshnikov](http://soshnikov.com)

Diagram ini disebut **pohon AND-OR**, dan merupakan representasi grafis dari serangkaian aturan produksi. Menggambar pohon berguna pada awal proses ekstraksi pengetahuan dari pakar. Untuk merepresentasikan pengetahuan di dalam komputer, lebih nyaman menggunakan aturan:

```
IF the animal eats meat
OR (animal has sharp teeth
    AND animal has claws
    AND animal has forward-looking eyes
) 
THEN the animal is a carnivore
```

Anda dapat melihat bahwa setiap kondisi di sisi kiri aturan dan tindakan pada dasarnya adalah triplet objek-atribut-nilai (OAV). **Memori kerja** berisi kumpulan triplet OAV yang sesuai dengan masalah yang sedang diselesaikan. **Mesin aturan** mencari aturan yang kondisinya terpenuhi dan menerapkannya, menambahkan triplet baru ke memori kerja.

> ✅ Buat pohon AND-OR Anda sendiri tentang topik yang Anda sukai!

### Inferensi Maju vs. Inferensi Mundur

Proses yang dijelaskan di atas disebut **inferensi maju**. Proses ini dimulai dengan beberapa data awal tentang masalah yang tersedia di memori kerja, lalu menjalankan loop penalaran berikut:

1. Jika atribut target ada di memori kerja - berhenti dan berikan hasil
2. Cari semua aturan yang kondisinya saat ini terpenuhi - dapatkan **set konflik** aturan.
3. Lakukan **resolusi konflik** - pilih satu aturan yang akan dieksekusi pada langkah ini. Ada berbagai strategi resolusi konflik:
   - Pilih aturan pertama yang dapat diterapkan dalam basis pengetahuan
   - Pilih aturan secara acak
   - Pilih aturan yang *lebih spesifik*, yaitu aturan yang memenuhi sebagian besar kondisi di "sisi kiri" (LHS)
4. Terapkan aturan yang dipilih dan masukkan potongan pengetahuan baru ke dalam status masalah
5. Ulangi dari langkah 1.

Namun, dalam beberapa kasus kita mungkin ingin memulai dengan pengetahuan kosong tentang masalah, dan mengajukan pertanyaan yang akan membantu kita mencapai kesimpulan. Misalnya, saat melakukan diagnosis medis, kita biasanya tidak melakukan semua analisis medis sebelumnya sebelum mulai mendiagnosis pasien. Sebaliknya, kita ingin melakukan analisis saat keputusan perlu dibuat.

Proses ini dapat dimodelkan menggunakan **inferensi mundur**. Proses ini didorong oleh **tujuan** - nilai atribut yang ingin kita temukan:

1. Pilih semua aturan yang dapat memberikan nilai tujuan (yaitu dengan tujuan di RHS ("sisi kanan")) - set konflik
1. Jika tidak ada aturan untuk atribut ini, atau ada aturan yang mengatakan bahwa kita harus meminta nilai dari pengguna - tanyakan, jika tidak:
1. Gunakan strategi resolusi konflik untuk memilih satu aturan yang akan kita gunakan sebagai *hipotesis* - kita akan mencoba membuktikannya
1. Ulangi proses secara rekursif untuk semua atribut di LHS aturan, mencoba membuktikan mereka sebagai tujuan
1. Jika pada titik mana pun proses gagal - gunakan aturan lain pada langkah 3.

> ✅ Dalam situasi apa inferensi maju lebih tepat? Bagaimana dengan inferensi mundur?

### Mengimplementasikan Sistem Pakar

Sistem pakar dapat diimplementasikan menggunakan berbagai alat:

* Memprogramnya langsung dalam bahasa pemrograman tingkat tinggi. Ini bukan ide terbaik, karena keuntungan utama dari sistem berbasis pengetahuan adalah bahwa pengetahuan dipisahkan dari inferensi, dan pakar domain masalah seharusnya dapat menulis aturan tanpa memahami detail proses inferensi.
* Menggunakan **kerangka sistem pakar**, yaitu sistem yang dirancang khusus untuk diisi dengan pengetahuan menggunakan bahasa representasi pengetahuan tertentu.

## ✍️ Latihan: Inferensi Hewan

Lihat [Animals.ipynb](https://github.com/microsoft/AI-For-Beginners/blob/main/lessons/2-Symbolic/Animals.ipynb) untuk contoh implementasi sistem pakar inferensi maju dan mundur.

> **Catatan**: Contoh ini cukup sederhana, dan hanya memberikan gambaran tentang bagaimana sistem pakar terlihat. Setelah Anda mulai membuat sistem seperti itu, Anda hanya akan melihat beberapa perilaku *cerdas* dari sistem tersebut setelah mencapai jumlah aturan tertentu, sekitar 200+. Pada titik tertentu, aturan menjadi terlalu kompleks untuk diingat semuanya, dan pada titik ini Anda mungkin mulai bertanya-tanya mengapa sistem membuat keputusan tertentu. Namun, karakteristik penting dari sistem berbasis pengetahuan adalah bahwa Anda selalu dapat *menjelaskan* dengan tepat bagaimana keputusan apa pun dibuat.

## Ontologi dan Web Semantik

Pada akhir abad ke-20, ada inisiatif untuk menggunakan representasi pengetahuan untuk memberi anotasi pada sumber daya Internet, sehingga memungkinkan untuk menemukan sumber daya yang sesuai dengan kueri yang sangat spesifik. Gerakan ini disebut **Web Semantik**, dan bergantung pada beberapa konsep:

- Representasi pengetahuan khusus berdasarkan **[logika deskriptif](https://en.wikipedia.org/wiki/Description_logic)** (DL). Representasi ini mirip dengan representasi pengetahuan bingkai, karena membangun hierarki objek dengan properti, tetapi memiliki semantik logis formal dan inferensi. Ada seluruh keluarga DL yang menyeimbangkan antara ekspresivitas dan kompleksitas algoritmik inferensi.
- Representasi pengetahuan terdistribusi, di mana semua konsep direpresentasikan oleh pengidentifikasi URI global, memungkinkan pembuatan hierarki pengetahuan yang mencakup internet.
- Sebuah keluarga bahasa berbasis XML untuk deskripsi pengetahuan: RDF (Resource Description Framework), RDFS (RDF Schema), OWL (Ontology Web Language).

Konsep inti dalam Semantic Web adalah konsep **Ontologi**. Ini merujuk pada spesifikasi eksplisit dari domain masalah menggunakan representasi pengetahuan formal. Ontologi paling sederhana bisa berupa hierarki objek dalam domain masalah, tetapi ontologi yang lebih kompleks akan mencakup aturan yang dapat digunakan untuk penalaran.

Dalam Semantic Web, semua representasi didasarkan pada triplet. Setiap objek dan setiap hubungan diidentifikasi secara unik oleh URI. Sebagai contoh, jika kita ingin menyatakan fakta bahwa Kurikulum AI ini dikembangkan oleh Dmitry Soshnikov pada 1 Januari 2022 - berikut adalah triplet yang dapat kita gunakan:

<img src="images/triplet.png" width="30%"/>

```
http://github.com/microsoft/ai-for-beginners http://www.example.com/terms/creation-date “Jan 13, 2007”
http://github.com/microsoft/ai-for-beginners http://purl.org/dc/elements/1.1/creator http://soshnikov.com
```

> ✅ Di sini `http://www.example.com/terms/creation-date` dan `http://purl.org/dc/elements/1.1/creator` adalah beberapa URI yang dikenal luas dan diterima secara universal untuk mengekspresikan konsep *pencipta* dan *tanggal pembuatan*.

Dalam kasus yang lebih kompleks, jika kita ingin mendefinisikan daftar pencipta, kita dapat menggunakan beberapa struktur data yang didefinisikan dalam RDF.

<img src="images/triplet-complex.png" width="40%"/>

> Diagram di atas oleh [Dmitry Soshnikov](http://soshnikov.com)

Kemajuan dalam membangun Semantic Web agak terhambat oleh kesuksesan mesin pencari dan teknik pemrosesan bahasa alami, yang memungkinkan ekstraksi data terstruktur dari teks. Namun, dalam beberapa bidang masih ada upaya signifikan untuk mempertahankan ontologi dan basis pengetahuan. Beberapa proyek yang patut dicatat:

* [WikiData](https://wikidata.org/) adalah kumpulan basis pengetahuan yang dapat dibaca mesin yang terkait dengan Wikipedia. Sebagian besar data ditambang dari *InfoBoxes* Wikipedia, potongan konten terstruktur di dalam halaman Wikipedia. Anda dapat [melakukan query](https://query.wikidata.org/) pada WikiData menggunakan SPARQL, bahasa query khusus untuk Semantic Web. Berikut adalah contoh query yang menampilkan warna mata paling populer di antara manusia:

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

* [DBpedia](https://www.dbpedia.org/) adalah upaya lain yang mirip dengan WikiData.

> ✅ Jika Anda ingin bereksperimen dengan membangun ontologi Anda sendiri, atau membuka ontologi yang sudah ada, ada editor ontologi visual yang hebat bernama [Protégé](https://protege.stanford.edu/). Unduh, atau gunakan secara online.

<img src="images/protege.png" width="70%"/>

*Editor Web Protégé terbuka dengan ontologi Keluarga Romanov. Screenshot oleh Dmitry Soshnikov*

## ✍️ Latihan: Ontologi Keluarga

Lihat [FamilyOntology.ipynb](https://github.com/Ezana135/AI-For-Beginners/blob/main/lessons/2-Symbolic/FamilyOntology.ipynb) untuk contoh penggunaan teknik Semantic Web untuk menalar hubungan keluarga. Kita akan mengambil pohon keluarga yang direpresentasikan dalam format GEDCOM umum dan ontologi hubungan keluarga, lalu membangun grafik semua hubungan keluarga untuk kumpulan individu tertentu.

## Microsoft Concept Graph

Dalam banyak kasus, ontologi dibuat dengan hati-hati secara manual. Namun, juga memungkinkan untuk **menambang** ontologi dari data tidak terstruktur, misalnya dari teks bahasa alami.

Salah satu upaya tersebut dilakukan oleh Microsoft Research, yang menghasilkan [Microsoft Concept Graph](https://blogs.microsoft.com/ai/microsoft-researchers-release-graph-that-helps-machines-conceptualize/?WT.mc_id=academic-77998-cacaste).

Ini adalah kumpulan besar entitas yang dikelompokkan menggunakan hubungan pewarisan `is-a`. Ini memungkinkan menjawab pertanyaan seperti "Apa itu Microsoft?" - jawabannya adalah sesuatu seperti "sebuah perusahaan dengan probabilitas 0,87, dan sebuah merek dengan probabilitas 0,75".

Graph ini tersedia baik sebagai REST API, maupun sebagai file teks besar yang dapat diunduh yang mencantumkan semua pasangan entitas.

## ✍️ Latihan: Concept Graph

Coba notebook [MSConceptGraph.ipynb](https://github.com/microsoft/AI-For-Beginners/blob/main/lessons/2-Symbolic/MSConceptGraph.ipynb) untuk melihat bagaimana kita dapat menggunakan Microsoft Concept Graph untuk mengelompokkan artikel berita ke dalam beberapa kategori.

## Kesimpulan

Saat ini, AI sering dianggap sebagai sinonim untuk *Machine Learning* atau *Neural Networks*. Namun, manusia juga menunjukkan kemampuan penalaran eksplisit, yang saat ini belum ditangani oleh neural networks. Dalam proyek dunia nyata, penalaran eksplisit masih digunakan untuk melakukan tugas yang membutuhkan penjelasan, atau kemampuan untuk mengubah perilaku sistem dengan cara yang terkontrol.

## 🚀 Tantangan

Dalam notebook Ontologi Keluarga yang terkait dengan pelajaran ini, ada kesempatan untuk bereksperimen dengan hubungan keluarga lainnya. Cobalah untuk menemukan koneksi baru antara orang-orang dalam pohon keluarga.

## [Kuis setelah pelajaran](https://ff-quizzes.netlify.app/en/ai/quiz/4)

## Tinjauan & Studi Mandiri

Lakukan penelitian di internet untuk menemukan area di mana manusia telah mencoba mengukur dan mengkodekan pengetahuan. Lihatlah Taksonomi Bloom, dan kembali ke sejarah untuk mempelajari bagaimana manusia mencoba memahami dunia mereka. Jelajahi karya Linnaeus dalam menciptakan taksonomi organisme, dan amati cara Dmitri Mendeleev menciptakan cara untuk mendeskripsikan dan mengelompokkan elemen kimia. Apa contoh menarik lainnya yang dapat Anda temukan?

**Tugas**: [Bangun Ontologi](assignment.md)

---

