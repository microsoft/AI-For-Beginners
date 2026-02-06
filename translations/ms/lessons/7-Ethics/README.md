# AI Beretika dan Bertanggungjawab

Anda hampir menyelesaikan kursus ini, dan saya berharap pada tahap ini anda sudah jelas bahawa AI berdasarkan beberapa kaedah matematik formal yang membolehkan kita mencari hubungan dalam data dan melatih model untuk meniru beberapa aspek tingkah laku manusia. Pada masa ini dalam sejarah, kita menganggap AI sebagai alat yang sangat berkuasa untuk mengekstrak corak daripada data, dan menerapkan corak tersebut untuk menyelesaikan masalah baharu.

## [Kuiz pra-kuliah](https://white-water-09ec41f0f.azurestaticapps.net/quiz/5/)

Namun, dalam fiksyen sains, kita sering melihat cerita di mana AI menjadi ancaman kepada manusia. Biasanya cerita-cerita ini berpusat pada semacam pemberontakan AI, apabila AI memutuskan untuk menentang manusia. Ini menunjukkan bahawa AI mempunyai semacam emosi atau boleh membuat keputusan yang tidak dijangka oleh pembangunnya.

Jenis AI yang telah kita pelajari dalam kursus ini tidak lebih daripada aritmetik matriks besar. Ia adalah alat yang sangat berkuasa untuk membantu kita menyelesaikan masalah kita, dan seperti alat berkuasa lain - ia boleh digunakan untuk tujuan baik dan buruk. Yang penting, ia boleh *disalahgunakan*.

## Prinsip AI Bertanggungjawab

Untuk mengelakkan penyalahgunaan AI secara tidak sengaja atau sengaja, Microsoft menyatakan [Prinsip AI Bertanggungjawab](https://www.microsoft.com/ai/responsible-ai?WT.mc_id=academic-77998-cacaste) yang penting. Konsep berikut menyokong prinsip ini:

* **Keadilan** berkaitan dengan masalah penting *bias model*, yang boleh disebabkan oleh penggunaan data yang berat sebelah untuk latihan. Sebagai contoh, apabila kita cuba meramalkan kebarangkalian seseorang mendapat pekerjaan sebagai pembangun perisian, model cenderung memberikan keutamaan lebih tinggi kepada lelaki - hanya kerana set data latihan mungkin berat sebelah kepada audiens lelaki. Kita perlu mengimbangi data latihan dengan teliti dan menyiasat model untuk mengelakkan bias, serta memastikan model mengambil kira ciri yang lebih relevan.
* **Kebolehpercayaan dan Keselamatan**. Secara semula jadi, model AI boleh membuat kesilapan. Rangkaian neural mengembalikan kebarangkalian, dan kita perlu mengambil kira ini semasa membuat keputusan. Setiap model mempunyai ketepatan dan ingatan tertentu, dan kita perlu memahaminya untuk mencegah kemudaratan yang boleh disebabkan oleh nasihat yang salah.
* **Privasi dan Keselamatan** mempunyai implikasi khusus untuk AI. Sebagai contoh, apabila kita menggunakan beberapa data untuk melatih model, data ini menjadi sebahagian daripada model. Di satu pihak, ini meningkatkan keselamatan dan privasi, tetapi di pihak lain - kita perlu ingat data apa yang digunakan untuk melatih model.
* **Keterangkuman** bermaksud kita tidak membina AI untuk menggantikan manusia, tetapi untuk meningkatkan manusia dan menjadikan kerja kita lebih kreatif. Ini juga berkaitan dengan keadilan, kerana apabila berurusan dengan komuniti yang kurang diwakili, kebanyakan set data yang kita kumpulkan cenderung berat sebelah, dan kita perlu memastikan bahawa komuniti tersebut disertakan dan ditangani dengan betul oleh AI.
* **Ketelusan**. Ini termasuk memastikan bahawa kita sentiasa jelas tentang penggunaan AI. Juga, di mana mungkin, kita mahu menggunakan sistem AI yang *boleh ditafsirkan*.
* **Kebertanggungjawaban**. Apabila model AI menghasilkan beberapa keputusan, tidak selalu jelas siapa yang bertanggungjawab atas keputusan tersebut. Kita perlu memastikan bahawa kita memahami di mana tanggungjawab keputusan AI terletak. Dalam kebanyakan kes, kita ingin melibatkan manusia dalam proses membuat keputusan penting, supaya orang sebenar bertanggungjawab.

## Alat untuk AI Bertanggungjawab

Microsoft telah membangunkan [Responsible AI Toolbox](https://github.com/microsoft/responsible-ai-toolbox) yang mengandungi satu set alat:

* Interpretability Dashboard (InterpretML)
* Fairness Dashboard (FairLearn)
* Error Analysis Dashboard
* Responsible AI Dashboard yang merangkumi

   - EconML - alat untuk Analisis Kausal, yang memberi tumpuan kepada soalan "bagaimana jika"
   - DiCE - alat untuk Analisis Counterfactual yang membolehkan anda melihat ciri mana yang perlu diubah untuk mempengaruhi keputusan model

Untuk maklumat lanjut tentang Etika AI, sila lawati [pelajaran ini](https://github.com/microsoft/ML-For-Beginners/tree/main/1-Introduction/3-fairness?WT.mc_id=academic-77998-cacaste) dalam Kurikulum Pembelajaran Mesin yang merangkumi tugasan.

## Kajian Semula & Kajian Kendiri

Ambil [Laluan Pembelajaran](https://docs.microsoft.com/learn/modules/responsible-ai-principles/?WT.mc_id=academic-77998-cacaste) ini untuk mengetahui lebih lanjut tentang AI bertanggungjawab.

## [Kuiz pasca-kuliah](https://white-water-09ec41f0f.azurestaticapps.net/quiz/6/)

---

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Walaupun kami berusaha untuk memastikan ketepatan, sila ambil perhatian bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidaktepatan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber yang berwibawa. Untuk maklumat penting, terjemahan manusia profesional adalah disyorkan. Kami tidak bertanggungjawab atas sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.