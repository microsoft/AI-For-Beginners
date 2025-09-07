<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "7df19702b8d2d3f7c4238c51bec2c8fc",
  "translation_date": "2025-08-29T11:46:23+00:00",
  "source_file": "lessons/0-course-setup/how-to-run.md",
  "language_code": "ms"
}
-->
# Cara Menjalankan Kod

Kurikulum ini mengandungi banyak contoh kod yang boleh dijalankan dan makmal yang anda mungkin ingin cuba. Untuk melakukannya, anda perlu mempunyai keupayaan untuk menjalankan kod Python dalam Jupyter Notebooks yang disediakan sebagai sebahagian daripada kurikulum ini. Terdapat beberapa pilihan untuk menjalankan kod:

## Jalankan secara tempatan di komputer anda

Untuk menjalankan kod secara tempatan di komputer anda, anda perlu mempunyai beberapa versi Python yang dipasang. Saya secara peribadi mengesyorkan memasang **[miniconda](https://conda.io/en/latest/miniconda.html)** - ia adalah pemasangan yang ringan dan menyokong pengurus pakej `conda` untuk pelbagai **persekitaran maya** Python.

Selepas anda memasang miniconda, anda perlu mengklon repositori dan mencipta persekitaran maya untuk digunakan dalam kursus ini:

```bash
git clone http://github.com/microsoft/ai-for-beginners
cd ai-for-beginners
conda env create --name ai4beg --file .devcontainer/environment.yml
conda activate ai4beg
```

### Menggunakan Visual Studio Code dengan Sambungan Python

Cara terbaik untuk menggunakan kurikulum ini adalah dengan membukanya dalam [Visual Studio Code](http://code.visualstudio.com/?WT.mc_id=academic-77998-cacaste) bersama [Python Extension](https://marketplace.visualstudio.com/items?itemName=ms-python.python&WT.mc_id=academic-77998-cacaste).

> **Nota**: Setelah anda mengklon dan membuka direktori dalam VS Code, ia akan secara automatik mencadangkan anda untuk memasang sambungan Python. Anda juga perlu memasang miniconda seperti yang diterangkan di atas.

> **Nota**: Jika VS Code mencadangkan anda untuk membuka semula repositori dalam container, anda perlu menolak cadangan ini untuk menggunakan pemasangan Python tempatan.

### Menggunakan Jupyter dalam Pelayar

Anda juga boleh menggunakan persekitaran Jupyter terus dari pelayar di komputer anda. Sebenarnya, kedua-dua Jupyter klasik dan Jupyter Hub menyediakan persekitaran pembangunan yang cukup mudah dengan auto-lengkap, penyorotan kod, dan sebagainya.

Untuk memulakan Jupyter secara tempatan, pergi ke direktori kursus, dan jalankan:

```bash
jupyter notebook
```
atau
```bash
jupyterhub
```
Anda kemudian boleh menavigasi ke mana-mana fail `.ipynb`, membukanya dan mula bekerja.

### Menjalankan dalam Container

Satu alternatif kepada pemasangan Python adalah menjalankan kod dalam container. Oleh kerana repositori kami mengandungi folder `.devcontainer` khas yang memberikan arahan bagaimana membina container untuk repositori ini, VS Code akan menawarkan anda untuk membuka semula kod dalam container. Ini memerlukan pemasangan Docker, dan juga lebih kompleks, jadi kami mencadangkan ini untuk pengguna yang lebih berpengalaman.

## Menjalankan di Awan

Jika anda tidak mahu memasang Python secara tempatan, dan mempunyai akses kepada beberapa sumber awan - alternatif yang baik adalah menjalankan kod di awan. Terdapat beberapa cara untuk melakukannya:

* Menggunakan **[GitHub Codespaces](https://github.com/features/codespaces)**, yang merupakan persekitaran maya yang dicipta untuk anda di GitHub, boleh diakses melalui antara muka pelayar VS Code. Jika anda mempunyai akses kepada Codespaces, anda hanya perlu klik butang **Code** dalam repositori, mulakan codespace, dan mula bekerja dengan segera.
* Menggunakan **[Binder](https://mybinder.org/v2/gh/microsoft/ai-for-beginners/HEAD)**. [Binder](https://mybinder.org) adalah sumber pengkomputeran percuma yang disediakan di awan untuk orang seperti anda mencuba beberapa kod di GitHub. Terdapat butang di halaman utama untuk membuka repositori dalam Binder - ini akan membawa anda ke laman Binder, yang akan membina container asas dan memulakan antara muka web Jupyter untuk anda dengan lancar.

> **Nota**: Untuk mengelakkan penyalahgunaan, Binder mempunyai akses kepada beberapa sumber web yang disekat. Ini mungkin menghalang beberapa kod daripada berfungsi, terutamanya yang memuat model dan/atau dataset dari Internet awam. Anda mungkin perlu mencari penyelesaian alternatif. Juga, sumber pengkomputeran yang disediakan oleh Binder agak asas, jadi latihan akan menjadi perlahan, terutamanya dalam pelajaran yang lebih kompleks kemudian.

## Menjalankan di Awan dengan GPU

Beberapa pelajaran kemudian dalam kurikulum ini akan mendapat manfaat besar daripada sokongan GPU, kerana tanpa GPU, latihan akan menjadi sangat perlahan. Terdapat beberapa pilihan yang boleh anda ikuti, terutamanya jika anda mempunyai akses kepada awan sama ada melalui [Azure for Students](https://azure.microsoft.com/free/students/?WT.mc_id=academic-77998-cacaste), atau melalui institusi anda:

* Cipta [Data Science Virtual Machine](https://docs.microsoft.com/learn/modules/intro-to-azure-data-science-virtual-machine/?WT.mc_id=academic-77998-cacaste) dan sambungkan ke dalamnya melalui Jupyter. Anda kemudian boleh mengklon repositori terus ke mesin tersebut, dan mula belajar. VM siri NC mempunyai sokongan GPU.

> **Nota**: Beberapa langganan, termasuk Azure for Students, tidak menyediakan sokongan GPU secara lalai. Anda mungkin perlu meminta teras GPU tambahan melalui permintaan sokongan teknikal.

* Cipta [Azure Machine Learning Workspace](https://azure.microsoft.com/services/machine-learning/?WT.mc_id=academic-77998-cacaste) dan kemudian gunakan ciri Notebook di sana. [Video ini](https://azure-for-academics.github.io/quickstart/azureml-papers/) menunjukkan cara mengklon repositori ke dalam notebook Azure ML dan mula menggunakannya.

Anda juga boleh menggunakan Google Colab, yang menyediakan beberapa sokongan GPU percuma, dan memuat naik Jupyter Notebooks ke sana untuk menjalankannya satu persatu.

---

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Walaupun kami berusaha untuk memastikan ketepatan, sila ambil perhatian bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidaktepatan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber yang berwibawa. Untuk maklumat penting, terjemahan manusia profesional adalah disyorkan. Kami tidak bertanggungjawab atas sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.