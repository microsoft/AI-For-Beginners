# Sistem Pelbagai Ejen

Salah satu cara yang mungkin untuk mencapai kecerdasan adalah melalui pendekatan **emergent** (atau **synergetic**), yang berdasarkan fakta bahawa tingkah laku gabungan banyak ejen yang relatif sederhana boleh menghasilkan tingkah laku yang lebih kompleks (atau cerdas) bagi sistem secara keseluruhan. Secara teori, ini berdasarkan prinsip-prinsip [Kecerdasan Kolektif](https://en.wikipedia.org/wiki/Collective_intelligence), [Emergentism](https://en.wikipedia.org/wiki/Global_brain) dan [Sibernetik Evolusi](https://en.wikipedia.org/wiki/Global_brain), yang menyatakan bahawa sistem tahap tinggi memperoleh nilai tambah apabila digabungkan dengan betul dari sistem tahap rendah (dikenali sebagai *prinsip peralihan metasistem*).

## [Kuiz pra-ceramah](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/123)

Arah **Sistem Pelbagai Ejen** telah muncul dalam AI pada tahun 1990-an sebagai respons kepada pertumbuhan Internet dan sistem teragih. Salah satu buku teks AI klasik, [Kecerdasan Buatan: Pendekatan Moden](https://en.wikipedia.org/wiki/Artificial_Intelligence:_A_Modern_Approach), menumpukan kepada pandangan AI klasik dari sudut sistem pelbagai ejen.

Inti kepada pendekatan pelbagai ejen adalah konsep **Ejen** - entiti yang hidup dalam **persekitaran** tertentu, yang dapat dirasai dan bertindak ke atasnya. Ini adalah definisi yang sangat luas, dan terdapat banyak jenis dan klasifikasi ejen yang berbeza:

* Mengikut kemampuan mereka untuk berfikir:
   - Ejen **Reaktif** biasanya mempunyai tingkah laku jenis permintaan-tindak balas yang sederhana
   - Ejen **Deliberatif** menggunakan sejenis pemikiran logik dan/atau kemampuan perancangan
* Mengikut tempat di mana ejen menjalankan kodnya:
   - Ejen **Statik** berfungsi pada nod rangkaian khusus
   - Ejen **Mudah Alih** boleh memindahkan kod mereka antara nod rangkaian
* Mengikut tingkah laku mereka:
   - Ejen **Pasif** tidak mempunyai matlamat tertentu. Ejen seperti ini boleh bertindak balas terhadap rangsangan luar, tetapi tidak akan memulakan sebarang tindakan sendiri.
   - Ejen **Aktif** mempunyai matlamat yang mereka kejar
   - Ejen **Kognitif** melibatkan perancangan dan pemikiran yang kompleks

Sistem pelbagai ejen kini digunakan dalam pelbagai aplikasi:

* Dalam permainan, banyak watak bukan pemain menggunakan sejenis AI, dan boleh dianggap sebagai ejen cerdas
* Dalam pengeluaran video, merender adegan 3D yang kompleks yang melibatkan orang ramai biasanya dilakukan menggunakan simulasi pelbagai ejen
* Dalam pemodelan sistem, pendekatan pelbagai ejen digunakan untuk mensimulasikan tingkah laku model yang kompleks. Sebagai contoh, pendekatan pelbagai ejen telah berjaya digunakan untuk meramalkan penyebaran penyakit COVID-19 di seluruh dunia. Pendekatan serupa boleh digunakan untuk memodelkan lalu lintas di bandar, dan melihat bagaimana ia bertindak balas terhadap perubahan dalam peraturan lalu lintas.
* Dalam sistem automasi yang kompleks, setiap peranti boleh bertindak sebagai ejen bebas, yang menjadikan keseluruhan sistem kurang monolitik dan lebih kukuh.

Kami tidak akan menghabiskan banyak masa untuk menyelami sistem pelbagai ejen, tetapi akan mempertimbangkan satu contoh **Pemodelan Pelbagai Ejen**.

## NetLogo

[NetLogo](https://ccl.northwestern.edu/netlogo/) adalah persekitaran pemodelan pelbagai ejen yang berdasarkan versi yang diubah suai dari bahasa pengaturcaraan [Logo](https://en.wikipedia.org/wiki/Logo_(programming_language)). Bahasa ini dibangunkan untuk mengajar konsep pengaturcaraan kepada kanak-kanak, dan ia membolehkan anda mengawal ejen yang dipanggil **kura-kura**, yang boleh bergerak, meninggalkan jejak di belakang. Ini membolehkan penciptaan figura geometri yang kompleks, yang merupakan cara yang sangat visual untuk memahami tingkah laku ejen.

Dalam NetLogo, kita boleh mencipta banyak kura-kura dengan menggunakan arahan `create-turtles`. Kita kemudian boleh mengarahkan semua kura-kura untuk melakukan beberapa tindakan (dalam contoh di bawah - lebih 10 langkah ke hadapan):

```
create-turtles 10
ask turtles [
  forward 10
]
```

Sudah tentu, ia tidak menarik apabila semua kura-kura melakukan perkara yang sama, jadi kita boleh `ask` groups of turtles, eg. those who are in the vicinity of a certain point. We can also create turtles of different *breeds* using `breed [cats cat]` command. Here `cat` adalah nama satu baka, dan kita perlu menyatakan kedua-dua bentuk tunggal dan jamak, kerana arahan yang berbeza menggunakan bentuk yang berbeza untuk kejelasan.

> ✅ Kami tidak akan mendalami pembelajaran bahasa NetLogo itu sendiri - anda boleh melawat sumber hebat [Kamus Interaktif NetLogo untuk Pemula](https://ccl.northwestern.edu/netlogo/bind/) jika anda berminat untuk belajar lebih lanjut.

Anda boleh [muat turun](https://ccl.northwestern.edu/netlogo/download.shtml) dan memasang NetLogo untuk mencubanya.

### Perpustakaan Model

Satu perkara hebat tentang NetLogo adalah bahawa ia mengandungi perpustakaan model yang berfungsi yang boleh anda cuba. Pergi ke **File → Models Library**, dan anda mempunyai banyak kategori model untuk dipilih.

<img alt="Perpustakaan Model NetLogo" src="images/NetLogo-ModelLib.png" width="60%"/>

> Tangkapan skrin perpustakaan model oleh Dmitry Soshnikov

Anda boleh membuka salah satu model, contohnya **Biologi → Kumpulan**.

### Prinsip Utama

Setelah membuka model, anda dibawa ke skrin utama NetLogo. Berikut adalah contoh model yang menerangkan populasi serigala dan biri-biri, dengan sumber terhad (rumput).

![Skrin Utama NetLogo](../../../../../translated_images/NetLogo-Main.32653711ec1a01b3cab22ec0b148e64193d0b979b055285bef329d5e3d6958c5.ms.png)

> Tangkapan skrin oleh Dmitry Soshnikov

Di skrin ini, anda boleh melihat:

* Bahagian **Antaramuka** yang mengandungi:
  - Medan utama, di mana semua ejen hidup
  - Pelbagai kawalan: butang, penggeser, dan lain-lain
  - Graf yang boleh anda gunakan untuk memaparkan parameter simulasi
* Tab **Kod** yang mengandungi penyunting, di mana anda boleh menaip program NetLogo

Dalam kebanyakan kes, antaramuka akan mempunyai butang **Setup**, yang menginisialisasi keadaan simulasi, dan butang **Go** yang memulakan pelaksanaan. Itu diuruskan oleh pengendali yang sesuai dalam kod yang kelihatan seperti ini:

```
to go [
...
]
```

Dunia NetLogo terdiri daripada objek-objek berikut:

* **Ejen** (kura-kura) yang boleh bergerak di seluruh medan dan melakukan sesuatu. Anda mengarahkan ejen dengan menggunakan `ask turtles [...]` syntax, and the code in brackets is executed by all agents in *turtle mode*.
* **Patches** are square areas of the field, on which agents live. You can refer to all agents on the same patch, or you can change patch colors and some other properties. You can also `ask patches` untuk melakukan sesuatu.
* **Pengamat** adalah ejen unik yang mengawal dunia. Semua pengendali butang dilaksanakan dalam *mod pengamat*.

> ✅ Keindahan persekitaran pelbagai ejen adalah bahawa kod yang dijalankan dalam mod kura-kura atau dalam mod patch dilaksanakan pada masa yang sama oleh semua ejen secara selari. Oleh itu, dengan menulis sedikit kod dan memprogram tingkah laku ejen individu, anda boleh mencipta tingkah laku kompleks bagi sistem simulasi secara keseluruhan.

### Kumpulan

Sebagai contoh tingkah laku pelbagai ejen, mari kita pertimbangkan **[Kumpulan](https://en.wikipedia.org/wiki/Flocking_(behavior))**. Kumpulan adalah corak kompleks yang sangat mirip dengan bagaimana sekumpulan burung terbang. Melihat mereka terbang, anda mungkin berfikir bahawa mereka mengikuti sejenis algoritma kolektif, atau bahawa mereka mempunyai sejenis *kecerdasan kolektif*. Namun, tingkah laku kompleks ini timbul apabila setiap ejen individu (dalam kes ini, *burung*) hanya memerhatikan beberapa ejen lain dalam jarak dekat, dan mengikuti tiga peraturan sederhana:

* **Penyelarasan** - ia mengarahkan ke arah arah purata ejen jiran
* **Kohesi** - ia berusaha untuk mengarahkan ke arah kedudukan purata jiran (*tarikan jarak jauh*)
* **Pemisahan** - apabila terlalu dekat dengan burung lain, ia berusaha untuk bergerak menjauh (*tolakan jarak dekat*)

Anda boleh menjalankan contoh kumpulan dan memerhatikan tingkah lakunya. Anda juga boleh menyesuaikan parameter, seperti *derajat pemisahan*, atau *jangka pandang*, yang menentukan seberapa jauh setiap burung boleh melihat. Perhatikan bahawa jika anda mengurangkan jangka pandang kepada 0, semua burung menjadi buta, dan kumpulan berhenti. Jika anda mengurangkan pemisahan kepada 0, semua burung berkumpul dalam satu barisan lurus.

> ✅ Tukar ke tab **Kod** dan lihat di mana tiga peraturan kumpulan (penyelarasan, kohesi dan pemisahan) dilaksanakan dalam kod. Perhatikan bagaimana kita hanya merujuk kepada ejen yang berada dalam pandangan.

### Model Lain untuk Dilihat

Terdapat beberapa model menarik lagi yang boleh anda eksperimen:

* **Seni → Kembang Api** menunjukkan bagaimana kembang api boleh dianggap sebagai tingkah laku kolektif aliran api individu
* **Sains Sosial → Asas Lalu Lintas** dan **Sains Sosial → Jaringan Lalu Lintas** menunjukkan model lalu lintas bandar dalam Grid 1D dan 2D dengan atau tanpa lampu isyarat. Setiap kereta dalam simulasi mengikuti peraturan berikut:
   - Jika ruang di hadapannya kosong - percepat (hingga kelajuan maksimum tertentu)
   - Jika ia melihat halangan di hadapan - brek (dan anda boleh menyesuaikan sejauh mana pemandu boleh melihat)
* **Sains Sosial → Pesta** menunjukkan bagaimana orang berkumpul semasa pesta koktel. Anda boleh mencari kombinasi parameter yang membawa kepada peningkatan kebahagiaan kumpulan yang paling cepat.

Seperti yang anda lihat dari contoh-contoh ini, simulasi pelbagai ejen boleh menjadi cara yang berguna untuk memahami tingkah laku sistem kompleks yang terdiri daripada individu yang mengikuti logik yang sama atau serupa. Ia juga boleh digunakan untuk mengawal ejen maya, seperti [NPCs](https://en.wikipedia.org/wiki/NPC) dalam permainan komputer, atau ejen dalam dunia animasi 3D.

## Ejen Deliberatif

Ejen yang diterangkan di atas sangat sederhana, bertindak balas terhadap perubahan dalam persekitaran menggunakan sejenis algoritma. Oleh itu, mereka adalah **ejen reaktif**. Walau bagaimanapun, kadangkala ejen boleh berfikir dan merancang tindakan mereka, dalam kes ini mereka dipanggil **deliberatif**.

Contoh tipikal adalah ejen peribadi yang menerima arahan dari manusia untuk menempah percutian. Katakan terdapat banyak ejen yang hidup di internet, yang boleh membantunya. Ia kemudian harus menghubungi ejen lain untuk melihat penerbangan yang tersedia, berapa harga hotel untuk tarikh yang berbeza, dan cuba merundingkan harga terbaik. Setelah pelan percutian selesai dan disahkan oleh pemilik, ia boleh meneruskan dengan tempahan.

Untuk melakukan itu, ejen perlu **berkomunikasi**. Untuk komunikasi yang berjaya mereka memerlukan:

* Beberapa **bahasa standard untuk bertukar pengetahuan**, seperti [Knowledge Interchange Format](https://en.wikipedia.org/wiki/Knowledge_Interchange_Format) (KIF) dan [Knowledge Query and Manipulation Language](https://en.wikipedia.org/wiki/Knowledge_Query_and_Manipulation_Language) (KQML). Bahasa-bahasa ini direka berdasarkan [Teori Tindakan Ucapan](https://en.wikipedia.org/wiki/Speech_act).
* Bahasa-bahasa ini juga harus merangkumi beberapa **protokol untuk rundingan**, berdasarkan pelbagai **jenis lelongan**.
* Sebuah **ontologi umum** untuk digunakan, supaya mereka merujuk kepada konsep yang sama dengan mengetahui semantiknya
* Cara untuk **menemui** apa yang boleh dilakukan oleh ejen yang berbeza, juga berdasarkan sejenis ontologi

Ejen deliberatif adalah jauh lebih kompleks daripada reaktif, kerana mereka tidak hanya bertindak balas terhadap perubahan dalam persekitaran, mereka juga harus mampu *memulakan* tindakan. Salah satu seni bina yang dicadangkan untuk ejen deliberatif adalah ejen yang dikenali sebagai Kepercayaan-Kehendak-Niat (BDI):

* **Kepercayaan** membentuk satu set pengetahuan tentang persekitaran ejen. Ia boleh disusun sebagai pangkalan pengetahuan atau set peraturan yang boleh digunakan oleh ejen untuk situasi tertentu dalam persekitaran.
* **Kehendak** mendefinisikan apa yang ejen ingin lakukan, iaitu matlamatnya. Sebagai contoh, matlamat ejen pembantu peribadi di atas adalah untuk menempah lawatan, dan matlamat ejen hotel adalah untuk memaksimumkan keuntungan.
* **Niat** adalah tindakan khusus yang dirancang oleh ejen untuk mencapai matlamatnya. Tindakan biasanya mengubah persekitaran dan menyebabkan komunikasi dengan ejen lain.

Terdapat beberapa platform yang tersedia untuk membina sistem pelbagai ejen, seperti [JADE](https://jade.tilab.com/). [Kertas ini](https://arxiv.org/ftp/arxiv/papers/2007/2007.08961.pdf) mengandungi ulasan mengenai platform pelbagai ejen, bersama dengan sejarah ringkas sistem pelbagai ejen dan pelbagai senario penggunaannya.

## Kesimpulan

Sistem Pelbagai Ejen boleh mengambil pelbagai bentuk dan digunakan dalam banyak aplikasi yang berbeza. 
Mereka semua cenderung menumpukan pada tingkah laku yang lebih sederhana bagi ejen individu, dan mencapai tingkah laku yang lebih kompleks bagi keseluruhan sistem disebabkan oleh **kesan sinergi**.

## 🚀 Cabaran

Bawa pelajaran ini ke dunia nyata dan cuba untuk mengkonseptualisasikan sistem pelbagai ejen yang boleh menyelesaikan masalah. Apa, sebagai contoh, yang diperlukan oleh sistem pelbagai ejen untuk mengoptimumkan laluan bas sekolah? Bagaimana ia boleh berfungsi di sebuah kedai roti?

## [Kuiz pasca-ceramah](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/223)

## Ulasan & Pembelajaran Sendiri

Tinjau penggunaan jenis sistem ini dalam industri. Pilih satu domain seperti pembuatan atau industri permainan video dan temui bagaimana sistem pelbagai ejen boleh digunakan untuk menyelesaikan masalah unik.

## [Tugasan NetLogo](assignment.md)

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan berasaskan AI. Walaupun kami berusaha untuk mencapai ketepatan, sila ambil perhatian bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidakakuratan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber yang sah. Untuk maklumat kritikal, terjemahan manusia profesional disyorkan. Kami tidak bertanggungjawab atas sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.