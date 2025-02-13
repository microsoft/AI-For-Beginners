# Sumbang dengan menterjemah pelajaran

Kami mengalu-alukan terjemahan untuk pelajaran dalam kurikulum ini!

## Garis Panduan

Terdapat folder dalam setiap folder pelajaran dan folder pengenalan pelajaran yang mengandungi fail markdown yang telah diterjemahkan.

> Nota, sila jangan menterjemah sebarang kod dalam fail contoh kod; perkara yang perlu diterjemah hanyalah README, tugasan, dan kuiz. Terima kasih!

Fail yang diterjemah harus mengikuti konvensyen penamaan ini:

**README._[language]_.md**

di mana _[language]_ adalah singkatan dua huruf untuk bahasa yang mengikuti standard ISO 639-1 (contohnya `README.es.md` untuk bahasa Sepanyol dan `README.nl.md` untuk bahasa Belanda).

**assignment._[language]_.md**

Serupa dengan README, sila terjemahkan juga tugasan.

**Kuiz**

1. Tambahkan terjemahan anda ke dalam aplikasi kuiz dengan menambahkan fail di sini: https://github.com/microsoft/AI-For-Beginners/tree/main/etc/quiz-app/src/assets/translations, dengan konvensyen penamaan yang betul (en.json, fr.json). **Sila jangan melokalisasi perkataan 'true' atau 'false' bagaimanapun. Terima kasih!**

2. Tambahkan kod bahasa anda ke dalam dropdown dalam fail App.vue aplikasi kuiz.

3. Edit fail [translations index.js aplikasi kuiz](https://github.com/microsoft/AI-For-Beginners/blob/main/etc/quiz-app/src/assets/translations/index.js) untuk menambah bahasa anda.

4. Akhir sekali, edit SEMUA pautan kuiz dalam fail README.md yang telah diterjemah untuk menunjuk terus ke kuiz yang telah diterjemah: https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/1 menjadi https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/1?loc=id

**TERIMA KASIH**

Kami benar-benar menghargai usaha anda!

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan berasaskan AI. Walaupun kami berusaha untuk ketepatan, sila sedar bahawa terjemahan automatik mungkin mengandungi ralat atau ketidaktepatan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber yang berwibawa. Untuk maklumat kritikal, terjemahan manusia profesional disyorkan. Kami tidak bertanggungjawab atas sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.