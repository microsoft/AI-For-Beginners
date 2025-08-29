<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "2efbb183384a50f0fc0cde02534d912f",
  "translation_date": "2025-08-29T12:46:03+00:00",
  "source_file": "lessons/5-NLP/20-LangModels/README.md",
  "language_code": "ms"
}
-->
# Model Bahasa Semula Jadi Pra-Latihan Besar

Dalam semua tugasan sebelum ini, kita melatih rangkaian neural untuk melaksanakan tugas tertentu menggunakan set data berlabel. Dengan model transformer besar seperti BERT, kita menggunakan pemodelan bahasa secara kendiri untuk membina model bahasa, yang kemudiannya disesuaikan untuk tugas hiliran tertentu dengan latihan tambahan yang khusus kepada domain. Walau bagaimanapun, telah dibuktikan bahawa model bahasa besar juga boleh menyelesaikan banyak tugas tanpa latihan khusus domain. Keluarga model yang mampu melakukan ini dipanggil **GPT**: Generative Pre-Trained Transformer.

## [Kuiz Pra-Kuliah](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/120)

## Penjanaan Teks dan Perpleksiti

Idea bahawa rangkaian neural boleh melaksanakan tugas umum tanpa latihan hiliran dibentangkan dalam kertas kerja [Language Models are Unsupervised Multitask Learners](https://cdn.openai.com/better-language-models/language_models_are_unsupervised_multitask_learners.pdf). Idea utama adalah bahawa banyak tugas lain boleh dimodelkan menggunakan **penjanaan teks**, kerana memahami teks pada dasarnya bermaksud mampu menghasilkan teks. Oleh kerana model dilatih menggunakan sejumlah besar teks yang merangkumi pengetahuan manusia, ia juga menjadi berpengetahuan tentang pelbagai subjek.

> Memahami dan mampu menghasilkan teks juga bermaksud mengetahui sesuatu tentang dunia di sekeliling kita. Manusia juga belajar dengan membaca secara meluas, dan rangkaian GPT serupa dalam hal ini.

Rangkaian penjanaan teks berfungsi dengan meramalkan kebarangkalian perkataan seterusnya $$P(w_N)$$. Walau bagaimanapun, kebarangkalian tanpa syarat bagi perkataan seterusnya adalah sama dengan kekerapan perkataan tersebut dalam korpus teks. GPT mampu memberikan **kebarangkalian bersyarat** bagi perkataan seterusnya, berdasarkan perkataan sebelumnya: $$P(w_N | w_{n-1}, ..., w_0)$$

> Anda boleh membaca lebih lanjut tentang kebarangkalian dalam [Kurikulum Sains Data untuk Pemula](https://github.com/microsoft/Data-Science-For-Beginners/tree/main/1-Introduction/04-stats-and-probability).

Kualiti model penjanaan bahasa boleh ditentukan menggunakan **perpleksiti**. Ia adalah metrik intrinsik yang membolehkan kita mengukur kualiti model tanpa sebarang set data khusus tugas. Ia berdasarkan konsep *kebarangkalian ayat* - model memberikan kebarangkalian tinggi kepada ayat yang berkemungkinan nyata (iaitu model tidak **keliru** dengannya), dan kebarangkalian rendah kepada ayat yang kurang masuk akal (contohnya, *Bolehkah ia lakukan apa?*). Apabila kita memberikan model kita ayat daripada korpus teks sebenar, kita menjangkakan ia mempunyai kebarangkalian tinggi dan **perpleksiti** rendah. Secara matematik, ia ditakrifkan sebagai kebarangkalian songsang normalisasi bagi set ujian:
$$
\mathrm{Perplexity}(W) = \sqrt[N]{1\over P(W_1,...,W_N)}
$$ 

**Anda boleh bereksperimen dengan penjanaan teks menggunakan [editor teks berkuasa GPT dari Hugging Face](https://transformer.huggingface.co/doc/gpt2-large)**. Dalam editor ini, anda mula menulis teks anda, dan menekan **[TAB]** akan memberikan beberapa pilihan pelengkap. Jika pilihan tersebut terlalu pendek, atau anda tidak berpuas hati dengannya - tekan [TAB] sekali lagi, dan anda akan mendapat lebih banyak pilihan, termasuk potongan teks yang lebih panjang.

## GPT adalah Sebuah Keluarga

GPT bukan satu model tunggal, tetapi koleksi model yang dibangunkan dan dilatih oleh [OpenAI](https://openai.com). 

Di bawah model GPT, kita mempunyai:

| [GPT-2](https://huggingface.co/docs/transformers/model_doc/gpt2#openai-gpt2) | [GPT-3](https://openai.com/research/language-models-are-few-shot-learners) | [GPT-4](https://openai.com/gpt-4) |
| -- | -- | -- |
|Model bahasa dengan sehingga 1.5 bilion parameter. | Model bahasa dengan sehingga 175 bilion parameter | 100T parameter dan menerima input imej serta teks dan menghasilkan output teks. |

Model GPT-3 dan GPT-4 tersedia [sebagai perkhidmatan kognitif dari Microsoft Azure](https://azure.microsoft.com/en-us/services/cognitive-services/openai-service/#overview?WT.mc_id=academic-77998-cacaste), dan sebagai [API OpenAI](https://openai.com/api/).

## Kejuruteraan Prompt

Oleh kerana GPT telah dilatih menggunakan sejumlah besar data untuk memahami bahasa dan kod, ia memberikan output sebagai tindak balas kepada input (prompt). Prompt adalah input atau pertanyaan kepada GPT di mana seseorang memberikan arahan kepada model tentang tugas yang perlu diselesaikan. Untuk mendapatkan hasil yang diinginkan, anda memerlukan prompt yang paling berkesan, yang melibatkan pemilihan kata, format, frasa, atau simbol yang tepat. Pendekatan ini dikenali sebagai [Kejuruteraan Prompt](https://learn.microsoft.com/en-us/shows/ai-show/the-basics-of-prompt-engineering-with-azure-openai-service?WT.mc_id=academic-77998-bethanycheum).

[Dokumentasi ini](https://learn.microsoft.com/en-us/semantic-kernel/prompt-engineering/?WT.mc_id=academic-77998-bethanycheum) memberikan anda lebih banyak maklumat tentang kejuruteraan prompt.

## ✍️ Buku Nota Contoh: [Bermain dengan OpenAI-GPT](GPT-PyTorch.ipynb)

Teruskan pembelajaran anda dalam buku nota berikut:

* [Menjana teks dengan OpenAI-GPT dan Hugging Face Transformers](GPT-PyTorch.ipynb)

## Kesimpulan

Model bahasa pra-latihan umum yang baru bukan sahaja memodelkan struktur bahasa, tetapi juga mengandungi sejumlah besar bahasa semula jadi. Oleh itu, ia boleh digunakan secara berkesan untuk menyelesaikan beberapa tugas NLP dalam tetapan zero-shot atau few-shot.

## [Kuiz Pasca-Kuliah](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/220)

---

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Walaupun kami berusaha untuk memastikan ketepatan, sila ambil maklum bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidaktepatan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber yang berwibawa. Untuk maklumat penting, terjemahan manusia profesional adalah disyorkan. Kami tidak bertanggungjawab atas sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.