# Menyumbang dengan menterjemah pelajaran

Kami mengalu-alukan terjemahan untuk pelajaran dalam kurikulum ini!

## Garis Panduan

Terdapat folder dalam setiap folder pelajaran dan folder pengenalan pelajaran yang mengandungi fail markdown yang telah diterjemahkan.

> Nota, sila jangan terjemahkan sebarang kod dalam fail sampel kod; perkara yang perlu diterjemahkan hanyalah README, tugasan, dan kuiz. Terima kasih!

Fail yang diterjemahkan harus mengikuti konvensyen penamaan berikut:

**README._[bahasa]_.md**

di mana _[bahasa]_ adalah singkatan dua huruf bahasa mengikut standard ISO 639-1 (contohnya `README.es.md` untuk bahasa Sepanyol dan `README.nl.md` untuk bahasa Belanda).

**assignment._[bahasa]_.md**

Sama seperti README, sila terjemahkan tugasan juga.

**Kuiz**

1. Tambahkan terjemahan anda ke aplikasi kuiz dengan menambah fail di sini: https://github.com/microsoft/AI-For-Beginners/tree/main/etc/quiz-app/src/assets/translations, dengan konvensyen penamaan yang betul (en.json, fr.json). **Sila jangan alih bahasa perkataan 'true' atau 'false'. Terima kasih!**

2. Tambahkan kod bahasa anda ke dropdown dalam fail App.vue aplikasi kuiz.

3. Edit fail [translations index.js aplikasi kuiz](https://github.com/microsoft/AI-For-Beginners/blob/main/etc/quiz-app/src/assets/translations/index.js) untuk menambah bahasa anda.

4. Akhir sekali, edit SEMUA pautan kuiz dalam fail README.md yang telah diterjemahkan untuk menunjuk terus ke kuiz yang telah diterjemahkan: https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/1 menjadi https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/1?loc=id

**TERIMA KASIH**

Kami benar-benar menghargai usaha anda!

---

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Walaupun kami berusaha untuk memastikan ketepatan, sila ambil perhatian bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidaktepatan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber yang berwibawa. Untuk maklumat yang kritikal, terjemahan manusia profesional adalah disyorkan. Kami tidak bertanggungjawab atas sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.