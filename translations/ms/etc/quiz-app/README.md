# Kuiz

Kuiz ini adalah kuiz pra- dan pasca-kuliah untuk kurikulum AI di https://aka.ms/ai-beginners

## Menambah set kuiz terjemahan

Tambahkan terjemahan kuiz dengan membuat struktur kuiz yang sesuai dalam folder `assets/translations`. Kuiz kanonik terdapat di `assets/translations/en`. Kuiz dibagi menjadi beberapa kelompok berdasarkan pelajaran. Pastikan untuk menyelaraskan penomoran dengan bagian kuiz yang tepat. Terdapat 40 kuiz dalam kurikulum ini, dengan hitungan dimulai dari 0.

Setelah mengedit terjemahan, edit file index.js dalam folder terjemahan untuk mengimpor semua file mengikuti konvensi di `en`.

Edit file `index.js` di `assets/translations` untuk mengimpor file terjemahan baru.

Kemudian, edit dropdown di `App.vue` dalam aplikasi ini untuk menambahkan bahasa Anda. Sesuaikan singkatan lokal dengan nama folder untuk bahasa Anda.

Akhirnya, edit semua tautan kuiz dalam pelajaran yang diterjemahkan, jika ada, untuk menyertakan lokalisasi ini sebagai parameter kueri: `?loc=fr` misalnya.

## Pengaturan Proyek

```
npm install
```

### Mengkompilasi dan memuat ulang secara panas untuk pengembangan

```
npm run serve
```

### Mengkompilasi dan meminimalkan untuk produksi

```
npm run build
```

### Memeriksa dan memperbaiki file

```
npm run lint
```

### Sesuaikan konfigurasi

Lihat [Referensi Konfigurasi](https://cli.vuejs.org/config/).

Kredit: Terima kasih kepada versi asli aplikasi kuiz ini: https://github.com/arpan45/simple-quiz-vue

## Meng-deploy ke Azure

Berikut adalah panduan langkah-demi-langkah untuk membantu Anda memulai:

1. Fork Repositori GitHub
Pastikan kode aplikasi web statis Anda ada di repositori GitHub Anda. Fork repositori ini.

2. Buat Azure Static Web App
- Buat dan [akun Azure](http://azure.microsoft.com)
- Pergi ke [portal Azure](https://portal.azure.com) 
- Klik “Buat sumber daya” dan cari “Static Web App”.
- Klik “Buat”.

3. Konfigurasikan Static Web App
- Dasar: Langganan: Pilih langganan Azure Anda.
- Grup Sumber Daya: Buat grup sumber daya baru atau gunakan yang sudah ada.
- Nama: Berikan nama untuk aplikasi web statis Anda.
- Wilayah: Pilih wilayah yang paling dekat dengan pengguna Anda.

- #### Detail Penempatan:
- Sumber: Pilih “GitHub”.
- Akun GitHub: Beri izin Azure untuk mengakses akun GitHub Anda.
- Organisasi: Pilih organisasi GitHub Anda.
- Repositori: Pilih repositori yang berisi aplikasi web statis Anda.
- Cabang: Pilih cabang yang ingin Anda gunakan untuk melakukan penempatan.

- #### Detail Build:
- Preset Build: Pilih kerangka kerja yang digunakan aplikasi Anda (misalnya, React, Angular, Vue, dll.).
- Lokasi Aplikasi: Tentukan folder yang berisi kode aplikasi Anda (misalnya, / jika berada di root).
- Lokasi API: Jika Anda memiliki API, tentukan lokasinya (opsional).
- Lokasi Output: Tentukan folder di mana output build dihasilkan (misalnya, build atau dist).

4. Tinjau dan Buat
Tinjau pengaturan Anda dan klik “Buat”. Azure akan menyiapkan sumber daya yang diperlukan dan membuat alur kerja GitHub Actions di repositori Anda.

5. Alur Kerja GitHub Actions
Azure akan secara otomatis membuat file alur kerja GitHub Actions di repositori Anda (.github/workflows/azure-static-web-apps-<name>.yml). Alur kerja ini akan menangani proses build dan penempatan.

6. Pantau Penempatan
Pergi ke tab “Actions” di repositori GitHub Anda.
Anda seharusnya melihat alur kerja yang sedang berjalan. Alur kerja ini akan membangun dan menempatkan aplikasi web statis Anda ke Azure.
Setelah alur kerja selesai, aplikasi Anda akan live di URL Azure yang disediakan.

### Contoh File Alur Kerja

Berikut adalah contoh bagaimana file alur kerja GitHub Actions mungkin terlihat:
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

### Sumber Daya Tambahan
- [Dokumentasi Azure Static Web Apps](https://learn.microsoft.com/azure/static-web-apps/getting-started)
- [Dokumentasi GitHub Actions](https://docs.github.com/actions/use-cases-and-examples/deploying/deploying-to-azure-static-web-app)

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan berasaskan AI. Walaupun kami berusaha untuk ketepatan, sila ambil perhatian bahawa terjemahan automatik mungkin mengandungi ralat atau ketidakakuratan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber yang sah. Untuk maklumat penting, terjemahan manusia yang profesional disyorkan. Kami tidak bertanggungjawab atas sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.