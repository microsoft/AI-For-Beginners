# Kuiz

Kuiz-kuiz ini adalah kuiz sebelum dan selepas kuliah untuk kurikulum AI di https://aka.ms/ai-beginners

## Menambah set kuiz terjemahan

Tambah terjemahan kuiz dengan mencipta struktur kuiz yang sepadan dalam folder `assets/translations`. Kuiz asal terdapat dalam `assets/translations/en`. Kuiz-kuiz ini dibahagikan kepada beberapa kumpulan mengikut pelajaran. Pastikan nombor kuiz sejajar dengan bahagian kuiz yang betul. Terdapat 40 kuiz keseluruhan dalam kurikulum ini, dengan kiraan bermula dari 0.

Selepas mengedit terjemahan, edit fail index.js dalam folder terjemahan untuk mengimport semua fail mengikut konvensyen dalam `en`.

Edit fail `index.js` dalam `assets/translations` untuk mengimport fail terjemahan yang baru.

Kemudian, edit dropdown dalam `App.vue` dalam aplikasi ini untuk menambah bahasa anda. Padankan singkatan bahasa tempatan dengan nama folder untuk bahasa anda.

Akhir sekali, edit semua pautan kuiz dalam pelajaran yang diterjemahkan, jika ada, untuk memasukkan lokalisasi ini sebagai parameter pertanyaan: `?loc=fr` sebagai contoh.

## Persediaan Projek

```
npm install
```

### Kompil dan muat semula secara langsung untuk pembangunan

```
npm run serve
```

### Kompil dan minimakan untuk pengeluaran

```
npm run build
```

### Lint dan betulkan fail

```
npm run lint
```

### Sesuaikan konfigurasi

Lihat [Rujukan Konfigurasi](https://cli.vuejs.org/config/).

Kredit: Terima kasih kepada versi asal aplikasi kuiz ini: https://github.com/arpan45/simple-quiz-vue

## Menyebarkan ke Azure

Berikut adalah panduan langkah demi langkah untuk membantu anda bermula:

1. Fork Repositori GitHub
Pastikan kod aplikasi web statik anda berada dalam repositori GitHub anda. Fork repositori ini.

2. Cipta Aplikasi Web Statik Azure
- Cipta [akaun Azure](http://azure.microsoft.com)
- Pergi ke [portal Azure](https://portal.azure.com) 
- Klik “Create a resource” dan cari “Static Web App”.
- Klik “Create”.

3. Konfigurasi Aplikasi Web Statik
- Asas: Langganan: Pilih langganan Azure anda.
- Kumpulan Sumber: Cipta kumpulan sumber baru atau gunakan yang sedia ada.
- Nama: Berikan nama untuk aplikasi web statik anda.
- Wilayah: Pilih wilayah yang paling dekat dengan pengguna anda.

- #### Butiran Penyebaran:
- Sumber: Pilih “GitHub”.
- Akaun GitHub: Benarkan Azure mengakses akaun GitHub anda.
- Organisasi: Pilih organisasi GitHub anda.
- Repositori: Pilih repositori yang mengandungi aplikasi web statik anda.
- Cawangan: Pilih cawangan yang anda ingin sebarkan.

- #### Butiran Pembinaan:
- Preset Pembinaan: Pilih kerangka kerja yang digunakan oleh aplikasi anda (contoh: React, Angular, Vue, dll.).
- Lokasi Aplikasi: Nyatakan folder yang mengandungi kod aplikasi anda (contoh: / jika ia berada di root).
- Lokasi API: Jika anda mempunyai API, nyatakan lokasinya (pilihan).
- Lokasi Output: Nyatakan folder di mana output pembinaan dihasilkan (contoh: build atau dist).

4. Semak dan Cipta
Semak tetapan anda dan klik “Create”. Azure akan menyediakan sumber yang diperlukan dan mencipta fail aliran kerja GitHub Actions dalam repositori anda.

5. Aliran Kerja GitHub Actions
Azure akan secara automatik mencipta fail aliran kerja GitHub Actions dalam repositori anda (.github/workflows/azure-static-web-apps-<name>.yml). Aliran kerja ini akan mengendalikan proses pembinaan dan penyebaran.

6. Pantau Penyebaran
Pergi ke tab “Actions” dalam repositori GitHub anda.
Anda sepatutnya melihat aliran kerja sedang berjalan. Aliran kerja ini akan membina dan menyebarkan aplikasi web statik anda ke Azure.
Setelah aliran kerja selesai, aplikasi anda akan tersedia secara langsung pada URL Azure yang disediakan.

### Contoh Fail Aliran Kerja

Berikut adalah contoh bagaimana fail aliran kerja GitHub Actions mungkin kelihatan:
name: Azure Static Web Apps CI/CD
```
on:
  push:
    branches:
      - main
  pull_request:
    types: [opened, synchronize, reopened, closed]
    branches:
      - main

jobs:
  build_and_deploy_job:
    runs-on: ubuntu-latest
    name: Build and Deploy Job
    steps:
      - uses: actions/checkout@v2
      - name: Build And Deploy
        id: builddeploy
        uses: Azure/static-web-apps-deploy@v1
        with:
          azure_static_web_apps_api_token: ${{ secrets.AZURE_STATIC_WEB_APPS_API_TOKEN }}
          repo_token: ${{ secrets.GITHUB_TOKEN }}
          action: "upload"
          app_location: "etc/quiz-app # App source code path"
          api_location: ""API source code path optional
          output_location: "dist" #Built app content directory - optional
```

### Sumber Tambahan
- [Dokumentasi Azure Static Web Apps](https://learn.microsoft.com/azure/static-web-apps/getting-started)
- [Dokumentasi GitHub Actions](https://docs.github.com/actions/use-cases-and-examples/deploying/deploying-to-azure-static-web-app)

---

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Walaupun kami berusaha untuk memastikan ketepatan, sila ambil perhatian bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidaktepatan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber yang berwibawa. Untuk maklumat yang kritikal, terjemahan manusia profesional adalah disyorkan. Kami tidak bertanggungjawab atas sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.