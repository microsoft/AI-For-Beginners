# Cara Menjalankan Kod

Kurikulum ini mengandungi banyak contoh yang boleh dijalankan dan makmal yang anda ingin jalankan. Untuk melakukan ini, anda memerlukan keupayaan untuk melaksanakan kod Python dalam Jupyter Notebooks yang disediakan sebagai sebahagian daripada kurikulum ini. Anda mempunyai beberapa pilihan untuk menjalankan kod:

## Jalankan secara lokal di komputer anda

Untuk menjalankan kod secara lokal di komputer anda, pemasangan Python diperlukan. Satu cadangan adalah untuk memasang **[miniconda](https://conda.io/en/latest/miniconda.html)** - ia adalah pemasangan yang agak ringan yang menyokong pengurus pakej `conda` untuk **persekitaran maya** Python yang berbeza.

Selepas anda memasang miniconda, klon repositori dan buat persekitaran maya yang akan digunakan untuk kursus ini:

```bash
git clone http://github.com/microsoft/ai-for-beginners
cd ai-for-beginners
conda env create --name ai4beg --file .devcontainer/environment.yml
conda activate ai4beg
```

> **Nota Windows**: Jika penciptaan persekitaran gagal semasa memasang `gdk-pixbuf` dengan `UnicodeDecodeError` yang menyebut codec `gbk`, aktifkan mod UTF-8 Python dalam terminal anda dan cuba lagi. Gunakan sintaks untuk terminal yang anda gunakan:
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
> Jika cubaan yang gagal meninggalkan persekitaran `ai4beg`, nyahaktifkan dan alih keluar persekitaran tersebut sebelum cuba lagi. Gunakan `conda deactivate` dahulu apabila persekitaran aktif:
>
> ```text
> conda deactivate
> conda env remove --name ai4beg
> ```

### Menggunakan Visual Studio Code dengan Sambungan Python

Kurikulum ini paling baik digunakan apabila dibuka dalam [Visual Studio Code](http://code.visualstudio.com/?WT.mc_id=academic-77998-cacaste) dengan [Sambungan Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python&WT.mc_id=academic-77998-cacaste).

> **Nota**: Setelah anda klon dan buka direktori dalam VS Code, ia akan secara automatik mencadangkan anda memasang sambungan Python. Anda juga perlu memasang miniconda seperti yang diterangkan di atas.

> **Nota**: Jika VS Code mencadangkan untuk membuka semula repositori dalam bekas, anda harus menolak ini untuk menggunakan pemasangan Python tempatan.

### Menggunakan Jupyter dalam Pelayar

Anda juga boleh menggunakan persekitaran Jupyter dari pelayar di komputer anda sendiri. Kedua-dua Jupyter klasik dan JupyterHub menyediakan persekitaran pembangunan yang mudah dengan pelengkap automatik, penyorotan kod, dan lain-lain.

Untuk memulakan Jupyter secara lokal, pergi ke direktori kursus, dan jalankan:

```bash
jupyter notebook
```
atau
```bash
jupyterhub
```
Anda kemudian boleh melayari mana-mana fail `.ipynb`, membukanya dan mula bekerja.

### Menjalankan dalam bekas

Satu alternatif kepada pemasangan Python adalah menjalankan kod dalam bekas. Oleh kerana repositori kami menyediakan folder khas `.devcontainer` yang mengarahkan bagaimana membina bekas untuk repo ini, VS Code menawarkan peluang untuk membuka semula kod dalam bekas. Ini memerlukan pemasangan Docker, dan juga lebih kompleks, jadi kami mengesyorkan ini kepada pengguna yang lebih berpengalaman.

## Menjalankan dalam Awan

Jika anda tidak mahu memasang Python secara lokal, dan mempunyai akses kepada beberapa sumber awan - alternatif yang baik adalah menjalankan kod dalam awan. Terdapat beberapa cara anda boleh melakukan ini:

* Menggunakan **[GitHub Codespaces](https://github.com/features/codespaces)**, iaitu persekitaran maya yang dicipta untuk anda di GitHub, boleh diakses melalui antara muka pelayar VS Code. Jika anda mempunyai akses ke Codespaces, anda hanya perlu klik butang **Code** dalam repo, mulakan codespace, dan mula dengan cepat.
* Menggunakan **[Binder](https://mybinder.org/v2/gh/microsoft/ai-for-beginners/HEAD)**. [Binder](https://mybinder.org) menawarkan sumber pengkomputeran percuma yang disediakan dalam awan untuk orang seperti anda menguji kod di GitHub. Terdapat butang di halaman utama untuk membuka repositori dalam Binder - ini akan segera membawa anda ke laman binder, yang akan membina bekas asas dan memulakan antara muka web Jupyter untuk anda dengan lancar.

> **Nota**: Untuk mengelakkan penyalahgunaan, Binder mempunyai akses ke beberapa sumber web yang disekat. Ini mungkin menghalang sebahagian kod yang mengambil model dan/atau set data dari Internet awam daripada berfungsi. Anda mungkin perlu mencari jalan penyelesaian. Juga, sumber pengkomputeran yang disediakan oleh Binder agak asas, jadi latihan akan menjadi perlahan, terutamanya dalam pelajaran yang lebih kompleks.

## Menjalankan dalam Awan dengan GPU

Sesetengah pelajaran terakhir dalam kurikulum ini amat mendapat manfaat daripada sokongan GPU. Latihan model, sebagai contoh, boleh menjadi sangat perlahan jika tidak. Terdapat beberapa pilihan yang boleh anda ikut, terutamanya jika anda mempunyai akses kepada awan sama ada melalui [Azure for Students](https://azure.microsoft.com/free/students/?WT.mc_id=academic-77998-cacaste), atau melalui institusi anda:

* Cipta [Mesin Maya Sains Data](https://docs.microsoft.com/learn/modules/intro-to-azure-data-science-virtual-machine/?WT.mc_id=academic-77998-cacaste) dan sambungkan kepadanya melalui Jupyter. Anda kemudian boleh klon repo terus ke mesin itu, dan mula belajar. VM siri NC mempunyai sokongan GPU.

> **Nota**: Sesetengah langganan, termasuk Azure for Students, tidak menyediakan sokongan GPU secara automatik. Anda mungkin perlu memohon teras GPU tambahan dengan permintaan sokongan teknikal.

* Cipta [Azure Machine Learning Workspace](https://azure.microsoft.com/services/machine-learning/?WT.mc_id=academic-77998-cacaste) dan kemudian gunakan ciri Notebook di sana. [Video ini](https://azure-for-academics.github.io/quickstart/azureml-papers/) menunjukkan cara untuk klon repositori ke dalam notebook Azure ML dan mula menggunakannya.

Anda juga boleh menggunakan Google Colab, yang datang dengan beberapa sokongan GPU percuma, dan memuat naik Jupyter Notebooks ke sana untuk menjalankannya satu demi satu.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Penafian**:
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Walaupun kami berusaha untuk ketepatan, sila ambil maklum bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidaktepatan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber yang sahih. Untuk maklumat penting, terjemahan oleh manusia profesional adalah disyorkan. Kami tidak bertanggungjawab terhadap sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->