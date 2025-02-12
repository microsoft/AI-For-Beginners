# Model Bahasa Besar yang Ditraining Sebelumnya

Dalam semua tugas sebelumnya, kami melatih jaringan saraf untuk melakukan tugas tertentu menggunakan dataset yang dilabeli. Dengan model transformer besar, seperti BERT, kami menggunakan pemodelan bahasa dengan cara yang diawasi sendiri untuk membangun model bahasa, yang kemudian disesuaikan untuk tugas hilir tertentu dengan pelatihan spesifik domain lebih lanjut. Namun, telah dibuktikan bahwa model bahasa besar juga dapat menyelesaikan banyak tugas tanpa pelatihan spesifik domain. Keluarga model yang mampu melakukan hal itu disebut **GPT**: Generative Pre-Trained Transformer.

## [Kuis Pra-perkuliahan](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/120)

## Generasi Teks dan Perplexity

Ide tentang jaringan saraf yang dapat melakukan tugas umum tanpa pelatihan hilir disajikan dalam makalah [Language Models are Unsupervised Multitask Learners](https://cdn.openai.com/better-language-models/language_models_are_unsupervised_multitask_learners.pdf). Ide utamanya adalah banyak tugas lain dapat dimodelkan menggunakan **generasi teks**, karena memahami teks pada dasarnya berarti mampu memproduksinya. Karena model dilatih pada sejumlah besar teks yang mencakup pengetahuan manusia, ia juga menjadi mengetahui berbagai subjek.

> Memahami dan mampu memproduksi teks juga berarti mengetahui sesuatu tentang dunia di sekitar kita. Orang juga belajar dengan membaca dalam jumlah besar, dan jaringan GPT serupa dalam hal ini.

Jaringan generasi teks bekerja dengan memprediksi probabilitas kata berikutnya $$P(w_N)$$ Namun, probabilitas tanpa syarat dari kata berikutnya sama dengan frekuensi kata ini dalam korpus teks. GPT mampu memberikan **probabilitas bersyarat** dari kata berikutnya, mengingat kata-kata sebelumnya: $$P(w_N | w_{n-1}, ..., w_0)$$

> Anda dapat membaca lebih lanjut tentang probabilitas dalam [Kurikulum Data Science untuk Pemula kami](https://github.com/microsoft/Data-Science-For-Beginners/tree/main/1-Introduction/04-stats-and-probability)

Kualitas model penghasil bahasa dapat didefinisikan menggunakan **perplexity**. Ini adalah metrik intrinsik yang memungkinkan kita mengukur kualitas model tanpa dataset spesifik tugas. Ini didasarkan pada pengertian *probabilitas sebuah kalimat* - model memberikan probabilitas tinggi pada kalimat yang kemungkinan besar nyata (yaitu model tidak **perplexed** olehnya), dan probabilitas rendah pada kalimat yang kurang masuk akal (misalnya *Bisakah itu melakukan apa?*). Ketika kami memberikan kalimat dari korpus teks nyata kepada model kami, kami berharap kalimat tersebut memiliki probabilitas tinggi, dan **perplexity** rendah. Secara matematis, ini didefinisikan sebagai probabilitas invers ternormalisasi dari set uji:
$$
\mathrm{Perplexity}(W) = \sqrt[N]{1\over P(W_1,...,W_N)}
$$ 

**Anda dapat bereksperimen dengan generasi teks menggunakan [editor teks bertenaga GPT dari Hugging Face](https://transformer.huggingface.co/doc/gpt2-large)**. Di editor ini, Anda mulai menulis teks Anda, dan menekan **[TAB]** akan menawarkan beberapa opsi penyelesaian. Jika opsi tersebut terlalu pendek, atau Anda tidak puas dengan mereka - tekan [TAB] lagi, dan Anda akan mendapatkan lebih banyak opsi, termasuk potongan teks yang lebih panjang.

## GPT adalah Sebuah Keluarga

GPT bukanlah model tunggal, melainkan kumpulan model yang dikembangkan dan dilatih oleh [OpenAI](https://openai.com). 

Di bawah model GPT, kami memiliki:

| [GPT-2](https://huggingface.co/docs/transformers/model_doc/gpt2#openai-gpt2) | [GPT 3](https://openai.com/research/language-models-are-few-shot-learners) | [GPT-4](https://openai.com/gpt-4) |
| -- | -- | -- |
|Model bahasa dengan hingga 1,5 miliar parameter. | Model bahasa dengan hingga 175 miliar parameter | 100T parameter dan menerima input serta output teks dari gambar. |


Model GPT-3 dan GPT-4 tersedia [sebagai layanan kognitif dari Microsoft Azure](https://azure.microsoft.com/en-us/services/cognitive-services/openai-service/#overview?WT.mc_id=academic-77998-cacaste), dan sebagai [API OpenAI](https://openai.com/api/).

## Rekayasa Prompt

Karena GPT telah dilatih pada volume data yang sangat besar untuk memahami bahasa dan kode, mereka memberikan keluaran sebagai respons terhadap masukan (prompt). Prompt adalah masukan atau kueri GPT di mana seseorang memberikan instruksi kepada model tentang tugas yang akan mereka selesaikan selanjutnya. Untuk mendapatkan hasil yang diinginkan, Anda perlu menggunakan prompt yang paling efektif yang melibatkan pemilihan kata, format, frasa, atau bahkan simbol yang tepat. Pendekatan ini adalah [Rekayasa Prompt](https://learn.microsoft.com/en-us/shows/ai-show/the-basics-of-prompt-engineering-with-azure-openai-service?WT.mc_id=academic-77998-bethanycheum)

[Dokumentasi ini](https://learn.microsoft.com/en-us/semantic-kernel/prompt-engineering/?WT.mc_id=academic-77998-bethanycheum) memberikan Anda informasi lebih lanjut tentang rekayasa prompt.

## ✍️ Contoh Notebook: [Bermain dengan OpenAI-GPT](../../../../../lessons/5-NLP/20-LangModels/GPT-PyTorch.ipynb)

Lanjutkan pembelajaran Anda di notebook berikut:

* [Menghasilkan teks dengan OpenAI-GPT dan Hugging Face Transformers](../../../../../lessons/5-NLP/20-LangModels/GPT-PyTorch.ipynb)

## Kesimpulan

Model bahasa umum yang baru dilatih sebelumnya tidak hanya memodelkan struktur bahasa, tetapi juga mengandung sejumlah besar bahasa alami. Dengan demikian, mereka dapat digunakan secara efektif untuk menyelesaikan beberapa tugas NLP dalam pengaturan zero-shot atau few-shot.

## [Kuis Pasca-perkuliahan](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/220)

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI berasaskan mesin. Walaupun kami berusaha untuk ketepatan, sila sedar bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidaktepatan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber yang sah. Untuk maklumat yang kritikal, terjemahan manusia profesional adalah disyorkan. Kami tidak bertanggungjawab atas sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.