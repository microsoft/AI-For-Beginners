# Cara Menjalankan Kode

Kurikulum ini mengandung banyak contoh dan lab yang dapat dieksekusi yang ingin Anda jalankan. Untuk melakukan ini, Anda perlu kemampuan untuk menjalankan kode Python di Jupyter Notebooks yang disediakan sebagai bagian dari kurikulum ini. Anda memiliki beberapa opsi untuk menjalankan kode:

## Menjalankan secara lokal di komputer Anda

Untuk menjalankan kode secara lokal di komputer Anda, Anda perlu memiliki beberapa versi Python yang terinstal. Saya pribadi merekomendasikan untuk menginstal **[miniconda](https://conda.io/en/latest/miniconda.html)** - ini adalah instalasi yang cukup ringan yang mendukung manajer paket `conda` untuk berbagai **lingkungan virtual** Python.

Setelah Anda menginstal miniconda, Anda perlu mengkloning repositori dan membuat lingkungan virtual yang akan digunakan untuk kursus ini:

```bash
git clone http://github.com/microsoft/ai-for-beginners
cd ai-for-beginners
conda env create --name ai4beg --file .devcontainer/environment.yml
conda activate ai4beg
```

### Menggunakan Visual Studio Code dengan Ekstensi Python

Mungkin cara terbaik untuk menggunakan kurikulum ini adalah dengan membukanya di [Visual Studio Code](http://code.visualstudio.com/?WT.mc_id=academic-77998-cacaste) dengan [Ekstensi Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python&WT.mc_id=academic-77998-cacaste).

> **Catatan**: Setelah Anda mengkloning dan membuka direktori di VS Code, ia akan secara otomatis menyarankan Anda untuk menginstal ekstensi Python. Anda juga harus menginstal miniconda seperti yang dijelaskan di atas.

> **Catatan**: Jika VS Code menyarankan Anda untuk membuka kembali repositori di dalam kontainer, Anda perlu menolak ini untuk menggunakan instalasi Python lokal.

### Menggunakan Jupyter di Browser

Anda juga dapat menggunakan lingkungan Jupyter langsung dari browser di komputer Anda sendiri. Sebenarnya, baik Jupyter klasik maupun Jupyter Hub menyediakan lingkungan pengembangan yang cukup nyaman dengan pelengkapan otomatis, penyorotan kode, dll.

Untuk memulai Jupyter secara lokal, pergi ke direktori kursus, dan jalankan:

```bash
jupyter notebook
```
atau
```bash
jupyterhub
```
Anda kemudian dapat menavigasi ke salah satu folder `.ipynb` files, open them and start working.

### Running in container

One alternative to Python installation would be to run the code in container. Since our repository contains special `.devcontainer` yang menginstruksikan cara membangun kontainer untuk repositori ini, VS Code akan menawarkan Anda untuk membuka kembali kode di dalam kontainer. Ini akan memerlukan instalasi Docker, dan juga akan lebih kompleks, jadi kami merekomendasikan ini untuk pengguna yang lebih berpengalaman.

## Menjalankan di Cloud

Jika Anda tidak ingin menginstal Python secara lokal, dan memiliki akses ke beberapa sumber daya cloud - alternatif yang baik adalah menjalankan kode di cloud. Ada beberapa cara untuk melakukan ini:

* Menggunakan **[GitHub Codespaces](https://github.com/features/codespaces)**, yang merupakan lingkungan virtual yang dibuat untuk Anda di GitHub, dapat diakses melalui antarmuka browser VS Code. Jika Anda memiliki akses ke Codespaces, Anda dapat langsung mengklik tombol **Code** di repositori, memulai codespace, dan mulai menjalankannya dalam waktu singkat.
* Menggunakan **[Binder](https://mybinder.org/v2/gh/microsoft/ai-for-beginners/HEAD)**. [Binder](https://mybinder.org) adalah sumber daya komputasi gratis yang disediakan di cloud untuk orang-orang seperti Anda untuk menguji beberapa kode di GitHub. Ada tombol di halaman depan untuk membuka repositori di Binder - ini seharusnya dengan cepat membawa Anda ke situs binder, yang akan membangun kontainer yang mendasari dan memulai antarmuka web Jupyter untuk Anda tanpa hambatan.

> **Catatan**: Untuk mencegah penyalahgunaan, Binder memiliki akses ke beberapa sumber daya web yang diblokir. Ini mungkin mencegah beberapa kode berfungsi, yang mengambil model dan/atau dataset dari Internet publik. Anda mungkin perlu mencari beberapa solusi alternatif. Juga, sumber daya komputasi yang disediakan oleh Binder cukup dasar, jadi pelatihan akan lambat, terutama di pelajaran yang lebih kompleks nanti.

## Menjalankan di Cloud dengan GPU

Beberapa pelajaran terakhir dalam kurikulum ini akan sangat diuntungkan dari dukungan GPU, karena jika tidak, pelatihan akan sangat lambat. Ada beberapa opsi yang dapat Anda ikuti, terutama jika Anda memiliki akses ke cloud baik melalui [Azure for Students](https://azure.microsoft.com/free/students/?WT.mc_id=academic-77998-cacaste), atau melalui institusi Anda:

* Buat [Data Science Virtual Machine](https://docs.microsoft.com/learn/modules/intro-to-azure-data-science-virtual-machine/?WT.mc_id=academic-77998-cacaste) dan sambungkan ke dalamnya melalui Jupyter. Anda kemudian dapat mengkloning repositori langsung ke mesin, dan mulai belajar. VM seri NC memiliki dukungan GPU.

> **Catatan**: Beberapa langganan, termasuk Azure for Students, tidak menyediakan dukungan GPU secara langsung. Anda mungkin perlu meminta tambahan inti GPU melalui permintaan dukungan teknis.

* Buat [Azure Machine Learning Workspace](https://azure.microsoft.com/services/machine-learning/?WT.mc_id=academic-77998-cacaste) dan kemudian gunakan fitur Notebook di sana. [Video ini](https://azure-for-academics.github.io/quickstart/azureml-papers/) menunjukkan cara mengkloning repositori ke dalam notebook Azure ML dan mulai menggunakannya.

Anda juga dapat menggunakan Google Colab, yang dilengkapi dengan beberapa dukungan GPU gratis, dan mengunggah Jupyter Notebooks di sana untuk mengeksekusinya satu per satu.

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan berasaskan AI. Walaupun kami berusaha untuk ketepatan, sila sedar bahawa terjemahan automatik mungkin mengandungi ralat atau ketidakakuratan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber yang berwibawa. Untuk maklumat yang kritikal, terjemahan manusia profesional disyorkan. Kami tidak bertanggungjawab atas sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.