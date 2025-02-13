# AI Etika dan Bertanggungjawab

Anda hampir menyelesaikan kursus ini, dan saya berharap bahawa sekarang anda jelas melihat bahawa AI berdasarkan kepada sejumlah kaedah matematik formal yang membolehkan kita mencari hubungan dalam data dan melatih model untuk meniru beberapa aspek tingkah laku manusia. Pada titik ini dalam sejarah, kita menganggap AI sebagai alat yang sangat berkuasa untuk mengekstrak corak dari data, dan menerapkan corak tersebut untuk menyelesaikan masalah baru.

## [Kuiz pra-ceramah](https://white-water-09ec41f0f.azurestaticapps.net/quiz/5/)

Namun, dalam fiksyen sains, kita sering melihat cerita di mana AI menghadirkan bahaya kepada umat manusia. Biasanya, cerita-cerita tersebut berpusat di sekitar jenis pemberontakan AI, apabila AI memutuskan untuk menentang manusia. Ini menunjukkan bahawa AI mempunyai sejenis emosi atau dapat membuat keputusan yang tidak terduga oleh pemaju mereka.

Jenis AI yang telah kita pelajari dalam kursus ini tidak lebih dari aritmetik matriks besar. Ia adalah alat yang sangat berkuasa untuk membantu kita menyelesaikan masalah kita, dan seperti alat berkuasa lain - ia boleh digunakan untuk tujuan baik dan buruk. Yang penting, ia boleh *disalahgunakan*.

## Prinsip AI Bertanggungjawab

Untuk mengelakkan penyalahgunaan AI yang tidak sengaja atau sengaja, Microsoft menyatakan [Prinsip AI Bertanggungjawab](https://www.microsoft.com/ai/responsible-ai?WT.mc_id=academic-77998-cacaste) yang penting. Konsep-konsep berikut menjadi asas kepada prinsip-prinsip ini:

* **Keadilan** berkaitan dengan masalah penting *bias model*, yang boleh disebabkan oleh penggunaan data yang berat sebelah untuk latihan. Contohnya, apabila kita cuba meramalkan kebarangkalian mendapatkan pekerjaan sebagai pemaju perisian untuk seseorang, model mungkin memberikan keutamaan lebih tinggi kepada lelaki - hanya kerana set data latihan mungkin berat sebelah kepada audiens lelaki. Kita perlu menyeimbangkan data latihan dengan teliti dan menyiasat model untuk mengelakkan bias, dan memastikan bahawa model mengambil kira ciri-ciri yang lebih relevan.
* **Kebolehpercayaan dan Keselamatan**. Secara semulajadi, model AI boleh melakukan kesilapan. Rangkaian neural mengembalikan kebarangkalian, dan kita perlu mengambil kira perkara ini apabila membuat keputusan. Setiap model mempunyai ketepatan dan ingatan, dan kita perlu memahami ini untuk mencegah bahaya yang boleh ditimbulkan oleh nasihat yang salah.
* **Privasi dan Keselamatan** mempunyai beberapa implikasi khusus untuk AI. Contohnya, apabila kita menggunakan beberapa data untuk melatih model, data ini menjadi seolah-olah "terintegrasi" ke dalam model. Di satu sisi, ini meningkatkan keselamatan dan privasi, di sisi lain - kita perlu ingat data mana yang digunakan untuk melatih model.
* **Keterangkuman** bermaksud bahawa kita tidak membina AI untuk menggantikan manusia, tetapi sebaliknya untuk memperkaya manusia dan menjadikan kerja kita lebih kreatif. Ini juga berkaitan dengan keadilan, kerana apabila berurusan dengan komuniti yang kurang terwakili, kebanyakan set data yang kita kumpulkan mungkin berat sebelah, dan kita perlu memastikan bahawa komuniti tersebut disertakan dan ditangani dengan betul oleh AI.
* **Ketelusan**. Ini termasuk memastikan bahawa kita sentiasa jelas tentang penggunaan AI. Juga, di mana sahaja mungkin, kita ingin menggunakan sistem AI yang *boleh diterangkan*.
* **Tanggungjawab**. Apabila model AI membuat keputusan, tidak selalu jelas siapa yang bertanggungjawab untuk keputusan tersebut. Kita perlu memastikan bahawa kita memahami di mana tanggungjawab keputusan AI terletak. Dalam kebanyakan kes, kita ingin melibatkan manusia dalam proses membuat keputusan penting, supaya orang sebenar dapat dipertanggungjawabkan.

## Alat untuk AI Bertanggungjawab

Microsoft telah membangunkan [Kotak Alat AI Bertanggungjawab](https://github.com/microsoft/responsible-ai-toolbox) yang mengandungi set alat:

* Papan Pemuka Interpretabiliti (InterpretML)
* Papan Pemuka Keadilan (FairLearn)
* Papan Pemuka Analisis Ralat
* Papan Pemuka AI Bertanggungjawab yang merangkumi

   - EconML - alat untuk Analisis Kausal, yang memberi tumpuan kepada soalan "apa jika"
   - DiCE - alat untuk Analisis Kontrafaktual yang membolehkan anda melihat ciri mana yang perlu diubah untuk mempengaruhi keputusan model

Untuk maklumat lanjut mengenai Etika AI, sila lawati [pelajaran ini](https://github.com/microsoft/ML-For-Beginners/tree/main/1-Introduction/3-fairness?WT.mc_id=academic-77998-cacaste) dalam Kurikulum Pembelajaran Mesin yang merangkumi tugasan.

## Ulasan & Kajian Sendiri

Ambil [Jalur Pembelajaran](https://docs.microsoft.com/learn/modules/responsible-ai-principles/?WT.mc_id=academic-77998-cacaste) ini untuk belajar lebih lanjut tentang AI bertanggungjawab.

## [Kuiz pasca-ceramah](https://white-water-09ec41f0f.azurestaticapps.net/quiz/6/)

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan berasaskan AI. Walaupun kami berusaha untuk ketepatan, sila ambil perhatian bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidaktepatan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber yang berwibawa. Untuk maklumat penting, terjemahan manusia yang profesional adalah disyorkan. Kami tidak bertanggungjawab atas sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.