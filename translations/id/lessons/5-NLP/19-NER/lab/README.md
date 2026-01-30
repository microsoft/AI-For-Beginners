# NER

Tugas Lab dari [AI for Beginners Curriculum](https://github.com/microsoft/ai-for-beginners).

## Tugas

Dalam lab ini, Anda perlu melatih model pengenalan entitas bernama (NER) untuk istilah medis.

## Dataset

Untuk melatih model NER, kita membutuhkan dataset yang diberi label dengan entitas medis. [Dataset BC5CDR](https://biocreative.bioinformatics.udel.edu/tasks/biocreative-v/track-3-cdr/) berisi entitas penyakit dan bahan kimia yang diberi label dari lebih dari 1500 makalah. Anda dapat mengunduh dataset ini setelah mendaftar di situs web mereka.

Dataset BC5CDR terlihat seperti ini:

```
6794356|t|Tricuspid valve regurgitation and lithium carbonate toxicity in a newborn infant.
6794356|a|A newborn with massive tricuspid regurgitation, atrial flutter, congestive heart failure, and a high serum lithium level is described. This is the first patient to initially manifest tricuspid regurgitation and atrial flutter, and the 11th described patient with cardiac disease among infants exposed to lithium compounds in the first trimester of pregnancy. Sixty-three percent of these infants had tricuspid valve involvement. Lithium carbonate may be a factor in the increasing incidence of congenital heart disease when taken during early pregnancy. It also causes neurologic depression, cyanosis, and cardiac arrhythmia when consumed prior to delivery.
6794356	0	29	Tricuspid valve regurgitation	Disease	D014262
6794356	34	51	lithium carbonate	Chemical	D016651
6794356	52	60	toxicity	Disease	D064420
...
```

Dalam dataset ini, terdapat judul dan abstrak makalah di dua baris pertama, kemudian terdapat entitas individu, dengan posisi awal dan akhir dalam blok judul+abstrak. Selain jenis entitas, Anda juga mendapatkan ID ontologi dari entitas ini dalam beberapa ontologi medis.

Anda perlu menulis beberapa kode Python untuk mengonversi ini ke dalam format BIO encoding.

## Jaringan

Percobaan pertama untuk NER dapat dilakukan dengan menggunakan jaringan LSTM, seperti yang telah Anda lihat dalam contoh selama pelajaran. Namun, dalam tugas NLP, [arsitektur transformer](https://en.wikipedia.org/wiki/Transformer_(machine_learning_model)), dan khususnya [model bahasa BERT](https://en.wikipedia.org/wiki/BERT_(language_model)) menunjukkan hasil yang jauh lebih baik. Model BERT yang telah dilatih sebelumnya memahami struktur umum suatu bahasa, dan dapat disesuaikan untuk tugas-tugas spesifik dengan dataset yang relatif kecil dan biaya komputasi yang rendah.

Karena kita berencana untuk menerapkan NER pada skenario medis, masuk akal untuk menggunakan model BERT yang dilatih pada teks medis. Microsoft Research telah merilis model yang telah dilatih sebelumnya bernama [PubMedBERT][PubMedBERT] ([publikasi][PubMedBERT-Pub]), yang telah disesuaikan menggunakan teks dari repositori [PubMed](https://pubmed.ncbi.nlm.nih.gov/).

Standar *de facto* untuk melatih model transformer adalah pustaka [Hugging Face Transformers](https://huggingface.co/). Pustaka ini juga berisi repositori model yang telah dilatih sebelumnya dan dikelola oleh komunitas, termasuk PubMedBERT. Untuk memuat dan menggunakan model ini, kita hanya membutuhkan beberapa baris kode:

```python
model_name = "microsoft/BiomedNLP-PubMedBERT-base-uncased-abstract"
classes = ... # number of classes: 2*entities+1
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = BertForTokenClassification.from_pretrained(model_name, classes)
```

Kode ini memberikan kita `model` itu sendiri, yang dibangun untuk tugas klasifikasi token menggunakan sejumlah `classes`, serta objek `tokenizer` yang dapat membagi teks input menjadi token. Anda perlu mengonversi dataset ke format BIO, dengan mempertimbangkan tokenisasi PubMedBERT. Anda dapat menggunakan [potongan kode Python ini](https://gist.github.com/shwars/580b55684be3328eb39ecf01b9cbbd88) sebagai inspirasi.

## Kesimpulan

Tugas ini sangat mirip dengan tugas nyata yang kemungkinan besar akan Anda hadapi jika ingin mendapatkan wawasan lebih dalam dari sejumlah besar teks bahasa alami. Dalam kasus kita, kita dapat menerapkan model yang telah dilatih ke [dataset makalah terkait COVID](https://www.kaggle.com/allen-institute-for-ai/CORD-19-research-challenge) dan melihat wawasan apa yang dapat kita peroleh. [Postingan blog ini](https://soshnikov.com/science/analyzing-medical-papers-with-azure-and-text-analytics-for-health/) dan [makalah ini](https://www.mdpi.com/2504-2289/6/1/4) menjelaskan penelitian yang dapat dilakukan pada kumpulan makalah ini menggunakan NER.

---

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan layanan penerjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Meskipun kami berusaha untuk memberikan hasil yang akurat, harap diingat bahwa terjemahan otomatis mungkin mengandung kesalahan atau ketidakakuratan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber yang otoritatif. Untuk informasi yang bersifat kritis, disarankan menggunakan jasa penerjemahan profesional oleh manusia. Kami tidak bertanggung jawab atas kesalahpahaman atau penafsiran yang keliru yang timbul dari penggunaan terjemahan ini.