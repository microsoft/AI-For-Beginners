# Representasi Pengetahuan dan Sistem Pakar

![Ringkasan konten AI Simbolik](../../../../translated_images/ai-symbolic.715a30cb610411a6964d2e2f23f24364cb338a07cb4844c1f97084d366e586c3.ms.png)

> Sketchnote oleh [Tomomi Imura](https://twitter.com/girlie_mac)

Pencarian kecerdasan buatan berlandaskan pada pencarian pengetahuan, untuk memahami dunia dengan cara yang mirip dengan manusia. Tapi, bagaimana cara melakukannya?

## [Kuis Pra-perkuliahan](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/102)

Pada masa awal AI, pendekatan top-down untuk menciptakan sistem cerdas (yang dibahas dalam pelajaran sebelumnya) sangat populer. Ide dasarnya adalah mengekstrak pengetahuan dari orang-orang ke dalam bentuk yang dapat dibaca mesin, dan kemudian menggunakannya untuk secara otomatis menyelesaikan masalah. Pendekatan ini didasarkan pada dua ide besar:

* Representasi Pengetahuan
* Penalaran

## Representasi Pengetahuan

Salah satu konsep penting dalam AI Simbolik adalah **pengetahuan**. Penting untuk membedakan pengetahuan dari *informasi* atau *data*. Misalnya, seseorang dapat mengatakan bahwa buku mengandung pengetahuan, karena seseorang dapat mempelajari buku dan menjadi seorang ahli. Namun, apa yang terkandung dalam buku sebenarnya disebut *data*, dan dengan membaca buku serta mengintegrasikan data ini ke dalam model dunia kita, kita mengubah data ini menjadi pengetahuan.

> ✅ **Pengetahuan** adalah sesuatu yang terdapat dalam pikiran kita dan mewakili pemahaman kita tentang dunia. Ia diperoleh melalui proses **pembelajaran** aktif, yang mengintegrasikan potongan informasi yang kita terima ke dalam model dunia kita yang aktif.

Seringkali, kita tidak mendefinisikan pengetahuan secara ketat, tetapi kita mengaitkannya dengan konsep-konsep terkait lainnya menggunakan [Piramida DIKW](https://en.wikipedia.org/wiki/DIKW_pyramid). Ini mencakup konsep-konsep berikut:

* **Data** adalah sesuatu yang diwakili dalam media fisik, seperti teks tertulis atau kata-kata yang diucapkan. Data ada secara independen dari manusia dan dapat dipindahkan antara orang.
* **Informasi** adalah bagaimana kita menginterpretasikan data dalam pikiran kita. Misalnya, ketika kita mendengar kata *komputer*, kita memiliki pemahaman tentang apa itu.
* **Pengetahuan** adalah informasi yang terintegrasi ke dalam model dunia kita. Misalnya, setelah kita belajar apa itu komputer, kita mulai memiliki ide tentang cara kerjanya, berapa biayanya, dan untuk apa ia dapat digunakan. Jaringan konsep yang saling terkait membentuk pengetahuan kita.
* **Kebijaksanaan** adalah satu tingkat lagi dari pemahaman kita tentang dunia, dan mewakili *meta-pengetahuan*, misalnya, beberapa gagasan tentang bagaimana dan kapan pengetahuan harus digunakan.

<img src="images/DIKW_Pyramid.png" width="30%"/>

*Gambar [dari Wikipedia](https://commons.wikimedia.org/w/index.php?curid=37705247), Oleh Longlivetheux - Karya sendiri, CC BY-SA 4.0*

Dengan demikian, masalah **representasi pengetahuan** adalah menemukan cara yang efektif untuk merepresentasikan pengetahuan di dalam komputer dalam bentuk data, agar dapat digunakan secara otomatis. Ini dapat dilihat sebagai spektrum:

![Spektrum representasi pengetahuan](../../../../translated_images/knowledge-spectrum.b60df631852c0217e941485b79c9eee40ebd574f15f18609cec5758fcb384bf3.ms.png)

> Gambar oleh [Dmitry Soshnikov](http://soshnikov.com)

* Di sebelah kiri, ada jenis representasi pengetahuan yang sangat sederhana yang dapat digunakan secara efektif oleh komputer. Yang paling sederhana adalah algoritmik, ketika pengetahuan diwakili oleh program komputer. Namun, ini bukan cara terbaik untuk merepresentasikan pengetahuan, karena tidak fleksibel. Pengetahuan dalam pikiran kita sering kali non-algoritmik.
* Di sebelah kanan, ada representasi seperti teks alami. Ini adalah yang paling kuat, tetapi tidak dapat digunakan untuk penalaran otomatis.

> ✅ Pikirkan sejenak tentang bagaimana Anda merepresentasikan pengetahuan dalam pikiran Anda dan mengubahnya menjadi catatan. Apakah ada format tertentu yang bekerja dengan baik untuk membantu dalam retensi?

## Mengklasifikasikan Representasi Pengetahuan Komputer

Kita dapat mengklasifikasikan berbagai metode representasi pengetahuan komputer ke dalam kategori berikut:

* **Representasi jaringan** didasarkan pada fakta bahwa kita memiliki jaringan konsep yang saling terkait dalam pikiran kita. Kita dapat mencoba mereproduksi jaringan yang sama sebagai grafik di dalam komputer - yang disebut **jaringan semantik**.

1. **Triplet Objek-Atribut-Nilai** atau **pasangan atribut-nilai**. Karena grafik dapat direpresentasikan dalam komputer sebagai daftar simpul dan tepi, kita dapat merepresentasikan jaringan semantik dengan daftar triplet, yang berisi objek, atribut, dan nilai. Misalnya, kita membangun triplet berikut tentang bahasa pemrograman:

Objek | Atribut | Nilai
-------|---------|------
Python | adalah | Bahasa-Tanpa-Tipe
Python | diciptakan-oleh | Guido van Rossum
Python | sintaks-blok | indentasi
Bahasa-Tanpa-Tipe | tidak memiliki | definisi tipe

> ✅ Pikirkan bagaimana triplet dapat digunakan untuk merepresentasikan jenis pengetahuan lainnya.

2. **Representasi hierarkis** menekankan fakta bahwa kita sering kali menciptakan hierarki objek dalam pikiran kita. Misalnya, kita tahu bahwa kenari adalah burung, dan semua burung memiliki sayap. Kita juga memiliki beberapa ide tentang warna yang biasanya dimiliki kenari, dan apa kecepatan terbangnya.

   - **Representasi bingkai** didasarkan pada merepresentasikan setiap objek atau kelas objek sebagai **bingkai** yang berisi **slot**. Slot memiliki nilai default yang mungkin, pembatasan nilai, atau prosedur yang disimpan yang dapat dipanggil untuk mendapatkan nilai dari slot. Semua bingkai membentuk hierarki yang mirip dengan hierarki objek dalam bahasa pemrograman berorientasi objek.
   - **Skenario** adalah jenis bingkai khusus yang merepresentasikan situasi kompleks yang dapat berkembang seiring waktu.

**Python**

Slot | Nilai | Nilai default | Interval |
-----|-------|---------------|----------|
Nama | Python | | |
Adalah | Bahasa-Tanpa-Tipe | | |
Kasus Variabel | | CamelCase | |
Panjang Program | | | 5-5000 baris |
Sintaks Blok | Indentasi | | |

3. **Representasi prosedural** didasarkan pada merepresentasikan pengetahuan melalui daftar tindakan yang dapat dieksekusi ketika kondisi tertentu terjadi.
   - Aturan produksi adalah pernyataan if-then yang memungkinkan kita menarik kesimpulan. Misalnya, seorang dokter dapat memiliki aturan yang mengatakan bahwa **JIKA** seorang pasien memiliki demam tinggi **ATAU** tingkat C-reactive protein yang tinggi dalam tes darah **MAKA** ia memiliki peradangan. Setelah kita menemui salah satu kondisi, kita dapat menarik kesimpulan tentang peradangan, dan kemudian menggunakannya dalam penalaran lebih lanjut.
   - Algoritma dapat dianggap sebagai bentuk lain dari representasi prosedural, meskipun hampir tidak pernah digunakan secara langsung dalam sistem berbasis pengetahuan.

4. **Logika** awalnya diusulkan oleh Aristoteles sebagai cara untuk merepresentasikan pengetahuan manusia universal.
   - Logika Predikat sebagai teori matematis terlalu kaya untuk dapat dihitung, oleh karena itu subsetnya biasanya digunakan, seperti klausul Horn yang digunakan dalam Prolog.
   - Logika Deskriptif adalah keluarga sistem logis yang digunakan untuk merepresentasikan dan menalar tentang hierarki objek yang didistribusikan representasi pengetahuan seperti *web semantik*.

## Sistem Pakar

Salah satu keberhasilan awal dari AI simbolik adalah yang disebut **sistem pakar** - sistem komputer yang dirancang untuk bertindak sebagai seorang ahli dalam domain masalah tertentu. Mereka didasarkan pada **basis pengetahuan** yang diekstrak dari satu atau lebih ahli manusia, dan mereka memiliki **mesin inferensi** yang melakukan beberapa penalaran di atasnya.

![Arsitektur Manusia](../../../../translated_images/arch-human.5d4d35f1bba3ab1cdfda96af2f10b89574eb31e9796d0e3011cd9beda1c35112.ms.png) | ![Sistem Berbasis Pengetahuan](../../../../translated_images/arch-kbs.3ec5c150b09fa8dadc2beb0931a4983c9e2b03913a89eebcc103b5bb841b0212.ms.png)
---------------------------------------------|------------------------------------------------
Struktur sederhana dari sistem saraf manusia | Arsitektur sistem berbasis pengetahuan

Sistem pakar dibangun seperti sistem penalaran manusia, yang memiliki **memori jangka pendek** dan **memori jangka panjang**. Demikian pula, dalam sistem berbasis pengetahuan kita membedakan komponen berikut:

* **Memori masalah**: berisi pengetahuan tentang masalah yang sedang diselesaikan saat ini, misalnya, suhu atau tekanan darah pasien, apakah ia memiliki peradangan atau tidak, dll. Pengetahuan ini juga disebut **pengetahuan statis**, karena ia berisi snapshot dari apa yang kita ketahui saat ini tentang masalah - yang disebut *status masalah*.
* **Basis pengetahuan**: merepresentasikan pengetahuan jangka panjang tentang domain masalah. Ini diekstrak secara manual dari para ahli manusia, dan tidak berubah dari konsultasi ke konsultasi. Karena memungkinkan kita untuk menavigasi dari satu status masalah ke status lainnya, ia juga disebut **pengetahuan dinamis**.
* **Mesin inferensi**: mengorkestrasi seluruh proses pencarian dalam ruang status masalah, mengajukan pertanyaan kepada pengguna jika perlu. Ia juga bertanggung jawab untuk menemukan aturan yang tepat yang akan diterapkan pada setiap status.

Sebagai contoh, mari kita pertimbangkan sistem pakar berikut untuk menentukan hewan berdasarkan karakteristik fisiknya:

![Pohon AND-OR](../../../../translated_images/AND-OR-Tree.5592d2c70187f283703c8e9c0d69d6a786eb370f4ace67f9a7aae5ada3d260b0.ms.png)

> Gambar oleh [Dmitry Soshnikov](http://soshnikov.com)

Diagram ini disebut **pohon AND-OR**, dan merupakan representasi grafis dari sekumpulan aturan produksi. Menggambar pohon ini berguna pada awal pengambilan pengetahuan dari ahli. Untuk merepresentasikan pengetahuan di dalam komputer, lebih nyaman menggunakan aturan:

```
IF the animal eats meat
OR (animal has sharp teeth
    AND animal has claws
    AND animal has forward-looking eyes
) 
THEN the animal is a carnivore
```

Anda dapat melihat bahwa setiap kondisi di sisi kiri aturan dan tindakan pada dasarnya adalah triplet objek-attribut-nilai (OAV). **Memori kerja** berisi kumpulan triplet OAV yang sesuai dengan masalah yang sedang diselesaikan saat ini. **Mesin aturan** mencari aturan yang kondisinya terpenuhi dan menerapkannya, menambahkan triplet lain ke dalam memori kerja.

> ✅ Buat pohon AND-OR Anda sendiri tentang topik yang Anda suka!

### Inferensi Maju vs. Inferensi Mundur

Proses yang dijelaskan di atas disebut **inferensi maju**. Ini dimulai dengan beberapa data awal tentang masalah yang tersedia di memori kerja, dan kemudian menjalankan loop penalaran berikut:

1. Jika atribut target ada di memori kerja - berhenti dan berikan hasilnya
2. Cari semua aturan yang kondisinya saat ini terpenuhi - peroleh **set konflik** aturan.
3. Lakukan **resolusi konflik** - pilih satu aturan yang akan dieksekusi pada langkah ini. Ada berbagai strategi resolusi konflik yang dapat digunakan:
   - Pilih aturan pertama yang dapat diterapkan dalam basis pengetahuan
   - Pilih aturan acak
   - Pilih aturan yang *lebih spesifik*, yaitu yang memenuhi kondisi terbanyak di "sisi kiri" (LHS)
4. Terapkan aturan yang dipilih dan masukkan potongan pengetahuan baru ke dalam status masalah
5. Ulangi dari langkah 1.

Namun, dalam beberapa kasus kita mungkin ingin memulai dengan pengetahuan kosong tentang masalah, dan mengajukan pertanyaan yang akan membantu kita mencapai kesimpulan. Misalnya, saat melakukan diagnosis medis, kita biasanya tidak melakukan semua analisis medis terlebih dahulu sebelum mulai mendiagnosis pasien. Kita lebih suka melakukan analisis ketika keputusan perlu diambil.

Proses ini dapat dimodelkan menggunakan **inferensi mundur**. Ini didorong oleh **tujuan** - nilai atribut yang kita cari untuk ditemukan:

1. Pilih semua aturan yang dapat memberi kita nilai dari tujuan (yaitu, dengan tujuan di RHS ("sisi kanan")) - satu set konflik
2. Jika tidak ada aturan untuk atribut ini, atau ada aturan yang mengatakan bahwa kita harus meminta nilai dari pengguna - minta nilai tersebut, jika tidak:
3. Gunakan strategi resolusi konflik untuk memilih satu aturan yang akan kita gunakan sebagai *hipotesis* - kita akan mencoba membuktikannya
4. Secara berulang ulangi proses untuk semua atribut di LHS aturan, mencoba membuktikannya sebagai tujuan
5. Jika pada titik mana pun proses gagal - gunakan aturan lain pada langkah 3.

> ✅ Dalam situasi apa inferensi maju lebih sesuai? Bagaimana dengan inferensi mundur?

### Mengimplementasikan Sistem Pakar

Sistem pakar dapat diimplementasikan menggunakan berbagai alat:

* Memprogramnya langsung dalam beberapa bahasa pemrograman tingkat tinggi. Ini bukan ide yang terbaik, karena keuntungan utama dari sistem berbasis pengetahuan adalah bahwa pengetahuan terpisah dari inferensi, dan mungkin seorang ahli domain masalah harus dapat menulis aturan tanpa memahami rincian proses inferensi.
* Menggunakan **shell sistem pakar**, yaitu sistem yang dirancang khusus untuk diisi dengan pengetahuan menggunakan beberapa bahasa representasi pengetahuan.

## ✍️ Latihan: Inferensi Hewan

Lihat [Animals.ipynb](https://github.com/microsoft/AI-For-Beginners/blob/main/lessons/2-Symbolic/Animals.ipynb) untuk contoh implementasi sistem pakar inferensi maju dan mundur.

> **Catatan**: Contoh ini cukup sederhana, dan hanya memberikan ide tentang bagaimana tampilan sistem pakar. Setelah Anda mulai membuat sistem semacam itu, Anda hanya akan melihat beberapa perilaku *cerdas* darinya setelah mencapai jumlah aturan tertentu, sekitar 200+. Pada titik tertentu, aturan menjadi terlalu kompleks untuk diingat semuanya, dan pada titik ini Anda mungkin mulai bertanya-tanya mengapa sistem membuat keputusan tertentu. Namun, karakteristik penting dari sistem berbasis pengetahuan adalah bahwa Anda selalu dapat *menjelaskan* dengan tepat bagaimana keputusan yang diambil.

## Ontologi dan Web Semantik

Pada akhir abad ke-20, ada inisiatif untuk menggunakan representasi pengetahuan untuk menandai sumber daya Internet, sehingga akan mungkin untuk menemukan sumber daya yang sesuai dengan kueri yang sangat spesifik. Gerakan ini disebut **Web Semantik**, dan bergantung pada beberapa konsep:

- Representasi pengetahuan khusus berdasarkan **[logika deskripsi](https://en.wikipedia.org/wiki/Description_logic)** (DL). Ini mirip dengan representasi pengetahuan bingkai, karena membangun hierarki objek dengan properti, tetapi memiliki semantik logis formal dan inferensi. Ada seluruh keluarga DL yang menyeimbangkan antara ekspresifitas dan kompleksitas algoritmik dari inferensi.
- Representasi pengetahuan terdistribusi, di mana semua konsep diwakili oleh pengidentifikasi URI global, sehingga memungkinkan untuk membuat hierarki pengetahuan yang menjangkau internet.
- Keluarga bahasa berbasis XML untuk deskripsi pengetahuan: RDF (Resource Description Framework), RDFS (RDF Schema), OWL (Ontology Web Language).

Konsep inti dalam Web Semantik adalah konsep **Ontologi**. Ini mengacu pada spesifikasi eksplisit dari domain masalah menggunakan beberapa representasi pengetahuan formal. Ontologi yang paling sederhana bisa saja hanya hierarki objek dalam domain masalah, tetapi ontologi yang lebih kompleks akan mencakup aturan yang dapat digunakan untuk inferensi.

Dalam web semantik, semua representasi didasarkan pada triplet. Setiap objek dan setiap hubungan diidentifikasi secara unik oleh URI. Misalnya, jika kita ingin menyatakan fakta bahwa Kurikulum AI ini telah dikembangkan oleh Dmitry Soshnikov pada 1 Januari 2022 - berikut adalah triplet yang dapat kita gunakan:

<img src="images/triplet.png" width="30%"/>

```
http://github.com/microsoft/ai-for-beginners http://www.example.com/terms/creation-date “Jan 13, 2007”
http://github.com/microsoft/ai-for-beginners http://purl.org/dc/elements/1.1/creator http://soshnikov.com
```

> ✅ Di sini `http://www.example.com/terms/creation-date` and `http://purl.org/dc/elements/1.1/creator` adalah beberapa URI yang dikenal dan diterima secara universal untuk mengekspresikan konsep *pencipta* dan *tanggal penciptaan*.

Dalam kasus yang lebih kompleks, jika kita ingin mendefinisikan daftar pencipta, kita dapat menggunakan beberapa struktur data yang ditentukan dalam RDF.

<img src="images/triplet-complex.png" width="40%"/>

> Diagram di atas oleh [Dmitry Soshnikov](http://soshnikov.com)

Kemajuan dalam membangun Web Semantik agak terhambat oleh keberhasilan mesin pencari dan teknik pemrosesan bahasa alami, yang memungkinkan ekstraksi data terstruktur dari teks. Namun, di beberapa bidang masih ada upaya signifikan untuk mempertahankan ontologi dan basis pengetahuan. Beberapa proyek yang patut dicatat:

* [WikiData](https://wikidata.org/) adalah kumpulan basis pengetahuan yang dapat dibaca mesin yang terkait dengan Wikipedia. Sebagian besar data diambil dari *InfoBox* Wikipedia, potongan konten terstruktur di dalam halaman Wikipedia. Anda dapat [menanyakan](https://query.wikidata.org/) wikidata dalam SPARQL, bahasa kueri khusus untuk Web Semantik. Berikut adalah contoh kueri yang menampilkan warna mata yang paling populer di antara manusia:

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

> ✅ Jika Anda ingin bereksperimen dengan membangun ontologi Anda sendiri, atau membuka yang sudah ada, ada editor ontologi visual yang hebat bernama [Protégé](https://protege.stanford.edu/). Unduh, atau gunakan secara online.

<img src="images/protege.png" width="70%"/>

*Editor Web Protégé terbuka dengan ontologi Keluarga Romanov. Tangkapan layar oleh Dmitry Soshnikov*

## ✍️ Latihan: Ontologi Keluarga

Lihat [FamilyOntology.ipynb](https://github.com/Ezana135/AI-For-Beginners/blob/main/lessons/2-Symbolic/FamilyOntology.ipynb) untuk contoh penggunaan teknik Web Semantik untuk menalar tentang hubungan keluarga. Kita akan mengambil pohon keluarga yang direpresentasikan dalam format GEDCOM umum dan ontologi hubungan keluarga dan membangun grafik dari semua hubungan keluarga untuk seperangkat individu yang diberikan.

## Grafik Konsep Microsoft

Dalam banyak kasus, ontologi dibuat dengan hati-hati secara manual. Namun, juga mungkin untuk **menambang** ontologi dari data tidak terstruktur, misalnya, dari teks bahasa alami.

Salah satu upaya semacam itu dilakukan oleh Microsoft Research, dan menghasilkan [Grafik Konsep Microsoft](https://blogs.microsoft.com/ai/microsoft-researchers-release-graph-that-helps-machines-conceptualize/?WT.mc_id=academic-77998-cacaste).

Ini adalah koleksi besar entitas yang dikelompokkan bersama menggunakan hubungan pewarisan `is-a`. Ini memungkinkan menjawab pertanyaan seperti "Apa itu Microsoft?" - jawabannya adalah sesuatu seperti "sebuah perusahaan dengan probabilitas 0.87, dan sebuah merek dengan probabilitas 0.75".

Grafik ini tersedia baik sebagai REST API, atau sebagai file teks besar yang dapat diunduh yang mencantumkan semua pasangan entitas.

##

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI berasaskan mesin. Walaupun kami berusaha untuk ketepatan, sila ambil perhatian bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidaktepatan. Dokumen asal dalam bahasa ibundanya harus dianggap sebagai sumber yang berwibawa. Untuk maklumat yang kritikal, terjemahan manusia profesional disyorkan. Kami tidak bertanggungjawab atas sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.