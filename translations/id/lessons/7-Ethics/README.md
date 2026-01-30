# AI yang Etis dan Bertanggung Jawab

Anda hampir menyelesaikan kursus ini, dan saya harap sekarang Anda sudah memahami bahwa AI didasarkan pada sejumlah metode matematika formal yang memungkinkan kita menemukan hubungan dalam data dan melatih model untuk meniru beberapa aspek perilaku manusia. Pada titik ini dalam sejarah, kita menganggap AI sebagai alat yang sangat kuat untuk mengekstrak pola dari data, dan menerapkan pola tersebut untuk menyelesaikan masalah baru.

## [Pre-lecture quiz](https://white-water-09ec41f0f.azurestaticapps.net/quiz/5/)

Namun, dalam fiksi ilmiah kita sering melihat cerita di mana AI menjadi ancaman bagi umat manusia. Biasanya cerita-cerita tersebut berpusat pada semacam pemberontakan AI, ketika AI memutuskan untuk melawan manusia. Ini mengimplikasikan bahwa AI memiliki semacam emosi atau dapat mengambil keputusan yang tidak terduga oleh pengembangnya.

Jenis AI yang telah kita pelajari dalam kursus ini tidak lebih dari aritmatika matriks besar. Ini adalah alat yang sangat kuat untuk membantu kita menyelesaikan masalah, dan seperti alat kuat lainnya - dapat digunakan untuk tujuan baik maupun buruk. Yang penting, AI dapat *disalahgunakan*.

## Prinsip AI yang Bertanggung Jawab

Untuk menghindari penyalahgunaan AI secara tidak sengaja atau sengaja, Microsoft menetapkan [Prinsip AI yang Bertanggung Jawab](https://www.microsoft.com/ai/responsible-ai?WT.mc_id=academic-77998-cacaste). Konsep-konsep berikut mendasari prinsip-prinsip ini:

* **Keadilan** berkaitan dengan masalah penting *bias model*, yang dapat disebabkan oleh penggunaan data yang bias untuk pelatihan. Sebagai contoh, ketika kita mencoba memprediksi kemungkinan seseorang mendapatkan pekerjaan sebagai pengembang perangkat lunak, model cenderung memberikan preferensi lebih tinggi kepada laki-laki - hanya karena dataset pelatihan kemungkinan besar bias terhadap audiens laki-laki. Kita perlu menyeimbangkan data pelatihan dengan hati-hati dan menyelidiki model untuk menghindari bias, serta memastikan bahwa model mempertimbangkan fitur yang lebih relevan.
* **Keandalan dan Keamanan**. Secara alami, model AI dapat membuat kesalahan. Jaringan neural mengembalikan probabilitas, dan kita perlu mempertimbangkan hal ini saat membuat keputusan. Setiap model memiliki presisi dan recall tertentu, dan kita perlu memahaminya untuk mencegah kerugian yang dapat disebabkan oleh saran yang salah.
* **Privasi dan Keamanan** memiliki implikasi khusus untuk AI. Sebagai contoh, ketika kita menggunakan data untuk melatih model, data tersebut menjadi "terintegrasi" ke dalam model. Di satu sisi, ini meningkatkan keamanan dan privasi, tetapi di sisi lain - kita perlu mengingat data apa yang digunakan untuk melatih model.
* **Inklusivitas** berarti bahwa kita tidak membangun AI untuk menggantikan manusia, melainkan untuk melengkapi manusia dan membuat pekerjaan kita lebih kreatif. Ini juga berkaitan dengan keadilan, karena ketika berurusan dengan komunitas yang kurang terwakili, sebagian besar dataset yang kita kumpulkan kemungkinan besar bias, dan kita perlu memastikan bahwa komunitas tersebut termasuk dan ditangani dengan benar oleh AI.
* **Transparansi**. Ini mencakup memastikan bahwa kita selalu jelas tentang penggunaan AI. Selain itu, di mana pun memungkinkan, kita ingin menggunakan sistem AI yang *dapat diinterpretasikan*.
* **Akuntabilitas**. Ketika model AI menghasilkan keputusan, tidak selalu jelas siapa yang bertanggung jawab atas keputusan tersebut. Kita perlu memastikan bahwa kita memahami di mana tanggung jawab atas keputusan AI berada. Dalam banyak kasus, kita ingin melibatkan manusia dalam proses pengambilan keputusan penting, sehingga orang yang sebenarnya bertanggung jawab.

## Alat untuk AI yang Bertanggung Jawab

Microsoft telah mengembangkan [Responsible AI Toolbox](https://github.com/microsoft/responsible-ai-toolbox) yang berisi serangkaian alat:

* Interpretability Dashboard (InterpretML)
* Fairness Dashboard (FairLearn)
* Error Analysis Dashboard
* Responsible AI Dashboard yang mencakup:

   - EconML - alat untuk Analisis Kausal, yang berfokus pada pertanyaan "bagaimana jika"
   - DiCE - alat untuk Analisis Kontrafaktual yang memungkinkan Anda melihat fitur mana yang perlu diubah untuk memengaruhi keputusan model

Untuk informasi lebih lanjut tentang Etika AI, silakan kunjungi [pelajaran ini](https://github.com/microsoft/ML-For-Beginners/tree/main/1-Introduction/3-fairness?WT.mc_id=academic-77998-cacaste) dalam Kurikulum Pembelajaran Mesin yang mencakup tugas-tugas.

## Tinjauan & Studi Mandiri

Ikuti [Learn Path](https://docs.microsoft.com/learn/modules/responsible-ai-principles/?WT.mc_id=academic-77998-cacaste) ini untuk mempelajari lebih lanjut tentang AI yang bertanggung jawab.

## [Post-lecture quiz](https://white-water-09ec41f0f.azurestaticapps.net/quiz/6/)

---

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan layanan penerjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Meskipun kami berusaha untuk memberikan hasil yang akurat, harap diketahui bahwa terjemahan otomatis mungkin mengandung kesalahan atau ketidakakuratan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber yang otoritatif. Untuk informasi yang bersifat kritis, disarankan menggunakan jasa penerjemahan profesional oleh manusia. Kami tidak bertanggung jawab atas kesalahpahaman atau penafsiran yang keliru yang timbul dari penggunaan terjemahan ini.