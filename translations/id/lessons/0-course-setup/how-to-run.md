# Cara Menjalankan Kode

Kurikulum ini berisi banyak contoh dan lab yang dapat dijalankan yang ingin Anda jalankan. Untuk melakukan ini, Anda perlu kemampuan untuk mengeksekusi kode Python di Jupyter Notebooks yang disediakan sebagai bagian dari kurikulum ini. Anda memiliki beberapa opsi untuk menjalankan kode:

## Jalankan secara lokal di komputer Anda

Untuk menjalankan kode secara lokal di komputer Anda, diperlukan instalasi Python. Salah satu rekomendasi adalah menginstal **[miniconda](https://conda.io/en/latest/miniconda.html)** - ini adalah instalasi yang cukup ringan yang mendukung pengelola paket `conda` untuk berbagai **lingkungan virtual** Python.

Setelah Anda menginstal miniconda, klon repositori dan buat lingkungan virtual yang akan digunakan untuk kursus ini:

```bash
git clone http://github.com/microsoft/ai-for-beginners
cd ai-for-beginners
conda env create --name ai4beg --file .devcontainer/environment.yml
conda activate ai4beg
```

> **Catatan Windows**: Jika pembuatan lingkungan gagal saat menginstal `gdk-pixbuf` dengan sebuah `UnicodeDecodeError` yang menyebutkan codec `gbk`, aktifkan mode UTF-8 Python di terminal Anda dan coba lagi. Gunakan sintaks untuk terminal yang Anda gunakan:
>
> **PowerShell:**
>
> ```powershell
> $env:PYTHONUTF8 = "1"
> conda env create --name ai4beg --file .devcontainer/environment.yml
> ```
>
> **Command Prompt (`cmd.exe`) atau Anaconda Prompt:**
>
> ```cmd
> set PYTHONUTF8=1
> conda env create --name ai4beg --file .devcontainer/environment.yml
> ```
>
> **Bash, termasuk Git Bash:**
>
> ```bash
> export PYTHONUTF8=1
> conda env create --name ai4beg --file .devcontainer/environment.yml
> ```
>
> Jika percobaan yang gagal meninggalkan lingkungan `ai4beg`, nonaktifkan dan hapus lingkungan tersebut sebelum mencoba lagi. Gunakan `conda deactivate` terlebih dahulu ketika lingkungan masih aktif:
>
> ```text
> conda deactivate
> conda env remove --name ai4beg
> ```

### Menggunakan Visual Studio Code dengan Ekstensi Python

Kurikulum ini paling baik digunakan saat membukanya di [Visual Studio Code](http://code.visualstudio.com/?WT.mc_id=academic-77998-cacaste) dengan [Ekstensi Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python&WT.mc_id=academic-77998-cacaste).

> **Catatan**: Setelah Anda mengkloning dan membuka direktori di VS Code, otomatis akan menyarankan Anda menginstal ekstensi Python. Anda juga harus menginstal miniconda seperti dijelaskan di atas.

> **Catatan**: Jika VS Code menyarankan Anda membuka kembali repositori dalam sebuah container, Anda harus menolak ini untuk menggunakan instalasi Python lokal. 

### Menggunakan Jupyter di Browser

Anda juga dapat menggunakan lingkungan Jupyter dari browser di komputer Anda sendiri. Baik Jupyter klasik maupun JupyterHub menyediakan lingkungan pengembangan yang nyaman dengan auto-completion, penyorotan kode, dll.

Untuk memulai Jupyter secara lokal, pindah ke direktori kursus, dan jalankan:

```bash
jupyter notebook
```
atau
```bash
jupyterhub
```
Anda kemudian bisa menavigasi ke file `.ipynb` mana pun, membukanya dan mulai bekerja.

### Menjalankan di dalam container

Salah satu alternatif untuk instalasi Python adalah menjalankan kode di dalam container. Karena repositori kami menyediakan folder `.devcontainer` khusus yang menginstruksikan cara membangun container untuk repo ini, VS Code menawarkan kesempatan untuk membuka kode kembali dalam container. Ini akan memerlukan instalasi Docker, dan juga akan lebih kompleks, jadi kami merekomendasikan ini untuk pengguna yang lebih berpengalaman.

## Menjalankan di Cloud

Jika Anda tidak ingin menginstal Python secara lokal, dan memiliki akses ke beberapa sumber daya cloud - alternatif yang baik adalah menjalankan kode di cloud. Ada beberapa cara Anda dapat melakukannya:

* Menggunakan **[GitHub Codespaces](https://github.com/features/codespaces)**, yang merupakan lingkungan virtual yang dibuat untuk Anda di GitHub, dapat diakses melalui antarmuka browser VS Code. Jika Anda memiliki akses ke Codespaces, cukup klik tombol **Code** di repo, mulai codespace, dan langsung jalankan.
* Menggunakan **[Binder](https://mybinder.org/v2/gh/microsoft/ai-for-beginners/HEAD)**. [Binder](https://mybinder.org) menyediakan sumber daya komputasi gratis yang disediakan di cloud bagi orang seperti Anda untuk menguji beberapa kode di GitHub. Ada tombol di halaman depan untuk membuka repositori di Binder - ini harus cepat membawa Anda ke situs binder, yang akan membangun container di belakang layar dan memulai antarmuka web Jupyter untuk Anda secara mulus.

> **Catatan**: Untuk mencegah penyalahgunaan, Binder memblokir akses ke beberapa sumber daya web. Ini mungkin mencegah beberapa kode berjalan, yang mengambil model dan/atau dataset dari Internet publik. Anda mungkin perlu mencari solusi. Juga, sumber daya komputasi yang disediakan oleh Binder cukup dasar, jadi pelatihan akan lambat, terutama di pelajaran yang lebih kompleks nanti.

## Menjalankan di Cloud dengan GPU

Beberapa pelajaran di kurikulum ini akan sangat diuntungkan dari dukungan GPU. Pelatihan model, misalnya, bisa sangat lambat jika tidak menggunakan GPU. Ada beberapa opsi yang dapat Anda ikuti, terutama jika Anda memiliki akses ke cloud melalui [Azure for Students](https://azure.microsoft.com/free/students/?WT.mc_id=academic-77998-cacaste), atau melalui institusi Anda:

* Buat [Data Science Virtual Machine](https://docs.microsoft.com/learn/modules/intro-to-azure-data-science-virtual-machine/?WT.mc_id=academic-77998-cacaste) dan hubungkan ke dalamnya melalui Jupyter. Anda kemudian dapat mengkloning repo langsung ke mesin tersebut, dan mulai belajar. VM seri NC memiliki dukungan GPU.

> **Catatan**: Beberapa langganan, termasuk Azure for Students, tidak menyediakan dukungan GPU secara langsung. Anda mungkin perlu mengajukan permintaan dukungan teknis untuk memperoleh core GPU tambahan.

* Buat [Azure Machine Learning Workspace](https://azure.microsoft.com/services/machine-learning/?WT.mc_id=academic-77998-cacaste) dan kemudian gunakan fitur Notebook di sana. [Video ini](https://azure-for-academics.github.io/quickstart/azureml-papers/) menunjukkan cara mengkloning repositori ke dalam notebook Azure ML dan mulai menggunakannya.

Anda juga dapat menggunakan Google Colab, yang menyediakan beberapa dukungan GPU gratis, dan mengunggah Jupyter Notebooks ke sana untuk mengeksekusinya satu per satu.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Penafian**:
Dokumen ini telah diterjemahkan menggunakan layanan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Meskipun kami berupaya untuk mencapai akurasi, harap diketahui bahwa terjemahan otomatis mungkin mengandung kesalahan atau ketidakakuratan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber yang sah. Untuk informasi penting, disarankan menggunakan terjemahan profesional oleh manusia. Kami tidak bertanggung jawab atas kesalahpahaman atau penafsiran yang keliru yang timbul dari penggunaan terjemahan ini.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->