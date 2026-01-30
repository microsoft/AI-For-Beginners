# Cara Menjalankan Kod

Kurikulum ini mengandungi banyak contoh dan makmal yang boleh dilaksanakan yang anda ingin jalankan. Untuk melakukan ini, anda memerlukan keupayaan untuk melaksanakan kod Python dalam Jupyter Notebooks yang disediakan sebagai sebahagian daripada kurikulum ini. Anda mempunyai beberapa pilihan untuk menjalankan kod:

## Jalankan secara tempatan di komputer anda

Untuk menjalankan kod secara tempatan di komputer anda, pemasangan Python diperlukan. Satu cadangan adalah untuk memasang **[miniconda](https://conda.io/en/latest/miniconda.html)** - ia adalah pemasangan yang agak ringan yang menyokong pengurus pakej `conda` untuk pelbagai **persekitaran maya** Python.

Selepas anda memasang miniconda, klon repositori dan buat persekitaran maya untuk digunakan dalam kursus ini:

```bash
git clone http://github.com/microsoft/ai-for-beginners
cd ai-for-beginners
conda env create --name ai4beg --file .devcontainer/environment.yml
conda activate ai4beg
```

### Menggunakan Visual Studio Code dengan Sambungan Python

Kurikulum ini paling baik digunakan apabila dibuka dalam [Visual Studio Code](http://code.visualstudio.com/?WT.mc_id=academic-77998-cacaste) dengan [Sambungan Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python&WT.mc_id=academic-77998-cacaste).

> **Nota**: Setelah anda klon dan buka direktori dalam VS Code, ia akan secara automatik mencadangkan anda memasang sambungan Python. Anda juga perlu memasang miniconda seperti yang diterangkan di atas.

> **Nota**: Jika VS Code mencadangkan anda untuk buka semula repositori dalam bekas, anda harus tolak ini untuk menggunakan pemasangan Python tempatan.

### Menggunakan Jupyter dalam Pelayar

Anda juga boleh menggunakan persekitaran Jupyter dari pelayar pada komputer anda sendiri. Baik Jupyter klasik dan JupyterHub menyediakan persekitaran pembangunan yang mudah dengan auto-selesaian, sorotan kod, dan lain-lain.

Untuk memulakan Jupyter secara tempatan, pergi ke direktori kursus, dan laksanakan:

```bash
jupyter notebook
```
atau
```bash
jupyterhub
```
Anda kemudian boleh navigasi ke mana-mana fail `.ipynb`, bukanya dan mula bekerja.

### Menjalankan dalam bekas

Satu alternatif kepada pemasangan Python adalah menjalankan kod dalam bekas. Oleh kerana repositori kami membekalkan folder `.devcontainer` khas yang memberi arahan bagaimana untuk membina bekas untuk repo ini, VS Code menawarkan peluang untuk membuka semula kod dalam bekas. Ini akan memerlukan pemasangan Docker, dan juga lebih kompleks, jadi kami mengesyorkan ini kepada pengguna yang lebih berpengalaman.

## Menjalankan di Awan

Jika anda tidak mahu memasang Python secara tempatan, dan mempunyai akses kepada beberapa sumber awan - satu alternatif yang baik adalah menjalankan kod di awan. Terdapat beberapa cara anda boleh melakukan ini:

* Menggunakan **[GitHub Codespaces](https://github.com/features/codespaces)**, iaitu persekitaran maya yang dicipta untuk anda di GitHub, boleh diakses melalui antaramuka pelayar VS Code. Jika anda mempunyai akses ke Codespaces, anda hanya perlu klik butang **Code** dalam repo, mulakan codespace, dan mula menjalankan dengan pantas.
* Menggunakan **[Binder](https://mybinder.org/v2/gh/microsoft/ai-for-beginners/HEAD)**. [Binder](https://mybinder.org) menawarkan sumber pengkomputeran percuma yang disediakan di awan untuk orang seperti anda menguji kod di GitHub. Terdapat butang di halaman depan untuk membuka repositori dalam Binder - ini akan membawa anda dengan cepat ke laman binder, yang akan membina bekas asas dan memulakan antaramuka web Jupyter untuk anda tanpa gangguan.

> **Nota**: Untuk mengelakkan penyalahgunaan, Binder menghadkan akses kepada beberapa sumber web. Ini mungkin menghalang beberapa kod daripada berfungsi, yang mengambil model dan/atau set data dari Internet awam. Anda mungkin perlu mencari jalan penyelesaian. Juga, sumber pengkomputeran yang disediakan oleh Binder adalah agak asas, jadi latihan akan lambat, terutamanya dalam pelajaran yang lebih kompleks kemudian.

## Menjalankan di Awan dengan GPU

Beberapa pelajaran kemudian dalam kurikulum ini akan sangat mendapat manfaat daripada sokongan GPU. Latihan model, sebagai contoh, boleh menjadi sangat lambat jika tidak. Terdapat beberapa pilihan yang boleh anda ikuti, terutamanya jika anda mempunyai akses ke awan sama ada melalui [Azure for Students](https://azure.microsoft.com/free/students/?WT.mc_id=academic-77998-cacaste), atau melalui institusi anda:

* Buat [Data Science Virtual Machine](https://docs.microsoft.com/learn/modules/intro-to-azure-data-science-virtual-machine/?WT.mc_id=academic-77998-cacaste) dan sambungkan kepadanya melalui Jupyter. Anda boleh klon repo terus ke mesin itu, dan mula belajar. VM siri NC mempunyai sokongan GPU.

> **Nota**: Sesetengah langganan, termasuk Azure for Students, tidak menyediakan sokongan GPU secara automatik. Anda mungkin perlu memohon teras GPU tambahan dengan permintaan sokongan teknikal.

* Buat [Azure Machine Learning Workspace](https://azure.microsoft.com/services/machine-learning/?WT.mc_id=academic-77998-cacaste) dan kemudian gunakan ciri Notebook di situ. [Video ini](https://azure-for-academics.github.io/quickstart/azureml-papers/) menunjukkan cara untuk klon repositori ke dalam notebook Azure ML dan mula menggunakannya.

Anda juga boleh menggunakan Google Colab, yang datang dengan sokongan GPU percuma, dan memuat naik Jupyter Notebooks di sana untuk melaksanakannya satu persatu.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Walaupun kami berusaha untuk memastikan ketepatan, sila ambil perhatian bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidaktepatan. Dokumen asal dalam bahasa asalnya hendaklah dianggap sebagai sumber yang sahih. Untuk maklumat penting, terjemahan profesional oleh manusia adalah disyorkan. Kami tidak bertanggungjawab terhadap sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->