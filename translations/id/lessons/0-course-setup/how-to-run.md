<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "7df19702b8d2d3f7c4238c51bec2c8fc",
  "translation_date": "2025-08-29T12:16:47+00:00",
  "source_file": "lessons/0-course-setup/how-to-run.md",
  "language_code": "id"
}
-->
# Cara Menjalankan Kode

Kurikulum ini berisi banyak contoh kode yang dapat dijalankan dan laboratorium yang mungkin ingin Anda coba. Untuk melakukannya, Anda perlu kemampuan untuk menjalankan kode Python di Jupyter Notebooks yang disediakan sebagai bagian dari kurikulum ini. Ada beberapa opsi untuk menjalankan kode:

## Menjalankan secara lokal di komputer Anda

Untuk menjalankan kode secara lokal di komputer Anda, Anda perlu memiliki beberapa versi Python yang terinstal. Saya pribadi merekomendasikan untuk menginstal **[miniconda](https://conda.io/en/latest/miniconda.html)** - ini adalah instalasi yang cukup ringan yang mendukung pengelola paket `conda` untuk berbagai **lingkungan virtual** Python.

Setelah Anda menginstal miniconda, Anda perlu mengkloning repositori dan membuat lingkungan virtual yang akan digunakan untuk kursus ini:

```bash
git clone http://github.com/microsoft/ai-for-beginners
cd ai-for-beginners
conda env create --name ai4beg --file .devcontainer/environment.yml
conda activate ai4beg
```

### Menggunakan Visual Studio Code dengan Ekstensi Python

Cara terbaik untuk menggunakan kurikulum ini adalah dengan membukanya di [Visual Studio Code](http://code.visualstudio.com/?WT.mc_id=academic-77998-cacaste) dengan [Ekstensi Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python&WT.mc_id=academic-77998-cacaste).

> **Note**: Setelah Anda mengkloning dan membuka direktori di VS Code, VS Code akan secara otomatis menyarankan Anda untuk menginstal ekstensi Python. Anda juga perlu menginstal miniconda seperti yang dijelaskan di atas.

> **Note**: Jika VS Code menyarankan Anda untuk membuka kembali repositori dalam container, Anda perlu menolak ini untuk menggunakan instalasi Python lokal.

### Menggunakan Jupyter di Browser

Anda juga dapat menggunakan lingkungan Jupyter langsung dari browser di komputer Anda. Sebenarnya, baik Jupyter klasik maupun Jupyter Hub menyediakan lingkungan pengembangan yang cukup nyaman dengan fitur auto-completion, penyorotan kode, dll.

Untuk memulai Jupyter secara lokal, pergi ke direktori kursus, dan jalankan:

```bash
jupyter notebook
```
atau
```bash
jupyterhub
```
Kemudian Anda dapat menavigasi ke salah satu file `.ipynb`, membukanya, dan mulai bekerja.

### Menjalankan di container

Alternatif lain untuk instalasi Python adalah menjalankan kode di container. Karena repositori kami berisi folder `.devcontainer` khusus yang memberikan instruksi tentang cara membangun container untuk repositori ini, VS Code akan menawarkan Anda untuk membuka kembali kode di container. Ini akan membutuhkan instalasi Docker, dan juga lebih kompleks, jadi kami merekomendasikan ini untuk pengguna yang lebih berpengalaman.

## Menjalankan di Cloud

Jika Anda tidak ingin menginstal Python secara lokal, dan memiliki akses ke beberapa sumber daya cloud - alternatif yang baik adalah menjalankan kode di cloud. Ada beberapa cara untuk melakukannya:

* Menggunakan **[GitHub Codespaces](https://github.com/features/codespaces)**, yang merupakan lingkungan virtual yang dibuat untuk Anda di GitHub, dapat diakses melalui antarmuka browser VS Code. Jika Anda memiliki akses ke Codespaces, Anda hanya perlu mengklik tombol **Code** di repositori, memulai codespace, dan langsung menjalankan kode.

* Menggunakan **[Binder](https://mybinder.org/v2/gh/microsoft/ai-for-beginners/HEAD)**. [Binder](https://mybinder.org) adalah sumber daya komputasi gratis yang disediakan di cloud untuk orang-orang seperti Anda untuk mencoba beberapa kode di GitHub. Ada tombol di halaman depan untuk membuka repositori di Binder - ini akan dengan cepat membawa Anda ke situs Binder, yang akan membangun container yang mendasari dan memulai antarmuka web Jupyter untuk Anda secara mulus.

> **Note**: Untuk mencegah penyalahgunaan, Binder memiliki akses ke beberapa sumber daya web yang diblokir. Hal ini dapat mencegah beberapa kode yang mengambil model dan/atau dataset dari Internet publik untuk bekerja. Anda mungkin perlu mencari solusi alternatif. Selain itu, sumber daya komputasi yang disediakan oleh Binder cukup dasar, sehingga pelatihan akan lambat, terutama pada pelajaran yang lebih kompleks di kemudian hari.

## Menjalankan di Cloud dengan GPU

Beberapa pelajaran di kemudian hari dalam kurikulum ini akan sangat diuntungkan dari dukungan GPU, karena jika tidak, pelatihan akan sangat lambat. Ada beberapa opsi yang dapat Anda ikuti, terutama jika Anda memiliki akses ke cloud baik melalui [Azure for Students](https://azure.microsoft.com/free/students/?WT.mc_id=academic-77998-cacaste), atau melalui institusi Anda:

* Membuat [Data Science Virtual Machine](https://docs.microsoft.com/learn/modules/intro-to-azure-data-science-virtual-machine/?WT.mc_id=academic-77998-cacaste) dan menghubungkannya melalui Jupyter. Anda kemudian dapat mengkloning repositori langsung ke mesin tersebut, dan mulai belajar. VM seri NC memiliki dukungan GPU.

> **Note**: Beberapa langganan, termasuk Azure for Students, tidak menyediakan dukungan GPU secara default. Anda mungkin perlu meminta tambahan inti GPU melalui permintaan dukungan teknis.

* Membuat [Azure Machine Learning Workspace](https://azure.microsoft.com/services/machine-learning/?WT.mc_id=academic-77998-cacaste) dan kemudian menggunakan fitur Notebook di sana. [Video ini](https://azure-for-academics.github.io/quickstart/azureml-papers/) menunjukkan cara mengkloning repositori ke notebook Azure ML dan mulai menggunakannya.

Anda juga dapat menggunakan Google Colab, yang dilengkapi dengan beberapa dukungan GPU gratis, dan mengunggah Jupyter Notebooks ke sana untuk menjalankannya satu per satu.

---

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan layanan penerjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Meskipun kami berusaha untuk memberikan hasil yang akurat, harap diingat bahwa terjemahan otomatis mungkin mengandung kesalahan atau ketidakakuratan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber yang otoritatif. Untuk informasi yang bersifat kritis, disarankan menggunakan jasa penerjemahan profesional oleh manusia. Kami tidak bertanggung jawab atas kesalahpahaman atau penafsiran yang keliru yang timbul dari penggunaan terjemahan ini.