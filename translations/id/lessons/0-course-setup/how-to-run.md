# Cara Menjalankan Kode

Kurikulum ini berisi banyak contoh dan lab yang dapat dieksekusi yang ingin Anda jalankan. Untuk melakukan ini, Anda memerlukan kemampuan untuk menjalankan kode Python di Jupyter Notebooks yang disediakan sebagai bagian dari kurikulum ini. Anda memiliki beberapa opsi untuk menjalankan kodenya:

## Menjalankan secara lokal di komputer Anda

Untuk menjalankan kode secara lokal di komputer Anda, diperlukan instalasi Python. Salah satu rekomendasinya adalah menginstal **[miniconda](https://conda.io/en/latest/miniconda.html)** - ini adalah instalasi yang relatif ringan yang mendukung pengelola paket `conda` untuk berbagai **lingkungan virtual** Python.

Setelah Anda menginstal miniconda, kloning repositori dan buat lingkungan virtual yang akan digunakan untuk kursus ini:

```bash
git clone http://github.com/microsoft/ai-for-beginners
cd ai-for-beginners
conda env create --name ai4beg --file .devcontainer/environment.yml
conda activate ai4beg
```

### Menggunakan Visual Studio Code dengan Ekstensi Python

Kurikulum ini paling baik digunakan saat membukanya di [Visual Studio Code](http://code.visualstudio.com/?WT.mc_id=academic-77998-cacaste) dengan [Ekstensi Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python&WT.mc_id=academic-77998-cacaste).

> **Catatan**: Setelah Anda mengkloning dan membuka direktori di VS Code, secara otomatis akan menyarankan Anda untuk menginstal ekstensi Python. Anda juga perlu menginstal miniconda seperti yang dijelaskan di atas.

> **Catatan**: Jika VS Code menyarankan Anda untuk membuka kembali repositori dalam sebuah kontainer, Anda harus menolak ini untuk menggunakan instalasi Python lokal.

### Menggunakan Jupyter di Peramban

Anda juga dapat menggunakan lingkungan Jupyter dari peramban di komputer Anda sendiri. Baik Jupyter klasik maupun JupyterHub menyediakan lingkungan pengembangan yang nyaman dengan fitur pelengkapan otomatis, penyorotan kode, dll.

Untuk memulai Jupyter secara lokal, buka direktori kursus, dan jalankan:

```bash
jupyter notebook
```
atau
```bash
jupyterhub
```
Kemudian Anda dapat menavigasi ke salah satu file `.ipynb`, membukanya, dan mulai bekerja.

### Menjalankan dalam kontainer

Alternatif lain untuk instalasi Python adalah menjalankan kode dalam sebuah kontainer. Karena repositori kami menyediakan folder khusus `.devcontainer` yang menunjukkan cara membangun kontainer untuk repositori ini, VS Code menawarkan kesempatan untuk membuka kembali kode di dalam kontainer. Ini memerlukan instalasi Docker, dan juga akan lebih kompleks, sehingga kami merekomendasikan ini untuk pengguna yang lebih berpengalaman.

## Menjalankan di Cloud

Jika Anda tidak ingin menginstal Python secara lokal, dan memiliki akses ke beberapa sumber daya cloud - alternatif yang baik adalah menjalankan kode di cloud. Ada beberapa cara yang bisa Anda lakukan:

* Menggunakan **[GitHub Codespaces](https://github.com/features/codespaces)**, yang merupakan lingkungan virtual yang dibuat untuk Anda di GitHub, dapat diakses melalui antarmuka peramban VS Code. Jika Anda memiliki akses ke Codespaces, Anda cukup mengklik tombol **Code** di repo, memulai codespace, dan langsung dapat menjalankan kodenya.
* Menggunakan **[Binder](https://mybinder.org/v2/gh/microsoft/ai-for-beginners/HEAD)**. [Binder](https://mybinder.org) menyediakan sumber daya komputasi gratis di cloud bagi orang-orang seperti Anda untuk mencoba beberapa kode di GitHub. Ada tombol di halaman depan untuk membuka repositori di Binder - ini akan membawa Anda dengan cepat ke situs binder, yang akan membangun kontainer dasar dan memulai antarmuka web Jupyter untuk Anda dengan mulus.

> **Catatan**: Untuk mencegah penyalahgunaan, Binder memblokir akses ke beberapa sumber daya web. Ini mungkin menyebabkan beberapa kode tidak dapat bekerja, yang mengambil model dan/atau dataset dari Internet publik. Anda mungkin perlu mencari solusi alternatif. Selain itu, sumber daya komputasi yang disediakan oleh Binder cukup dasar, sehingga pelatihan akan lambat, terutama pada pelajaran selanjutnya yang lebih kompleks.

## Menjalankan di Cloud dengan GPU

Beberapa pelajaran akhir dalam kurikulum ini akan sangat diuntungkan dengan dukungan GPU. Pelatihan model, misalnya, bisa sangat lambat jika tidak menggunakan GPU. Ada beberapa opsi yang dapat Anda ikuti, terutama jika Anda memiliki akses ke cloud baik melalui [Azure for Students](https://azure.microsoft.com/free/students/?WT.mc_id=academic-77998-cacaste), atau melalui institusi Anda:

* Buat [Data Science Virtual Machine](https://docs.microsoft.com/learn/modules/intro-to-azure-data-science-virtual-machine/?WT.mc_id=academic-77998-cacaste) dan sambungkan ke sana melalui Jupyter. Anda kemudian dapat mengkloning repo langsung ke mesin tersebut, dan mulai belajar. NC-series VM menyediakan dukungan GPU.

> **Catatan**: Beberapa langganan, termasuk Azure for Students, tidak menyediakan dukungan GPU secara default. Anda mungkin perlu mengajukan permintaan dukungan teknis untuk mendapatkan core GPU tambahan.

* Buat [Azure Machine Learning Workspace](https://azure.microsoft.com/services/machine-learning/?WT.mc_id=academic-77998-cacaste) dan gunakan fitur Notebook di sana. [Video ini](https://azure-for-academics.github.io/quickstart/azureml-papers/) menunjukkan cara mengkloning repositori ke notebook Azure ML dan mulai menggunakannya.

Anda juga dapat menggunakan Google Colab, yang menyediakan dukungan GPU gratis terbatas, dan mengunggah Jupyter Notebooks ke sana untuk dijalankan satu per satu.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Penafian**:
Dokumen ini telah diterjemahkan menggunakan layanan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Meskipun kami berusaha untuk akurasi, harap diketahui bahwa terjemahan otomatis mungkin mengandung kesalahan atau ketidaktepatan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber yang berwenang. Untuk informasi yang penting, disarankan menggunakan terjemahan profesional oleh manusia. Kami tidak bertanggung jawab atas kesalahpahaman atau salah tafsir yang timbul dari penggunaan terjemahan ini.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->