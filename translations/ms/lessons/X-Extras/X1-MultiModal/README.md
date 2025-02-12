# Rangkaian Multi-Modus

Selepas kejayaan model transformer untuk menyelesaikan tugas NLP, seni bina yang sama atau serupa telah diterapkan pada tugas penglihatan komputer. Terdapat minat yang semakin meningkat dalam membina model yang akan *menggabungkan* kemampuan penglihatan dan bahasa semula jadi. Salah satu usaha tersebut telah dilakukan oleh OpenAI, dan ia dipanggil CLIP dan DALL.E.

## Pra-Latihan Imej Kontrastif (CLIP)

Idea utama CLIP adalah untuk dapat membandingkan arahan teks dengan imej dan menentukan sejauh mana imej tersebut sepadan dengan arahan tersebut.

![Arsitektur CLIP](../../../../../translated_images/clip-arch.b3dbf20b4e8ed8be1c38e2bc6100fd3cc257c33cda4692b301be91f791b13ea7.ms.png)

> *Gambar dari [post blog ini](https://openai.com/blog/clip/)*

Model ini dilatih menggunakan imej yang diperoleh dari Internet dan kapsyen mereka. Untuk setiap batch, kita mengambil N pasangan (imej, teks), dan menukarnya kepada beberapa representasi vektor I dan T. Representasi tersebut kemudian dipadankan bersama. Fungsi kehilangan ditentukan untuk memaksimumkan kesamaan kosinus antara vektor yang sepadan dengan satu pasangan (contohnya, I dan T), dan meminimumkan kesamaan kosinus antara semua pasangan lain. Itulah sebabnya pendekatan ini dipanggil **kontrastif**.

Model/perpustakaan CLIP boleh didapati dari [OpenAI GitHub](https://github.com/openai/CLIP). Pendekatan ini diterangkan dalam [post blog ini](https://openai.com/blog/clip/), dan dengan lebih terperinci dalam [kertas ini](https://arxiv.org/pdf/2103.00020.pdf).

Setelah model ini dilatih, kita boleh memberikannya satu batch imej dan satu batch arahan teks, dan ia akan mengembalikan tensor dengan kebarangkalian. CLIP boleh digunakan untuk beberapa tugas:

**Klasifikasi Imej**

Katakan kita perlu mengklasifikasikan imej antara, katakan, kucing, anjing dan manusia. Dalam kes ini, kita boleh memberikan model imej, dan satu siri arahan teks: "*gambar kucing*", "*gambar anjing*", "*gambar manusia*". Dalam vektor kebarangkalian yang terhasil, kita hanya perlu memilih indeks dengan nilai tertinggi.

![CLIP untuk Klasifikasi Imej](../../../../../translated_images/clip-class.3af42ef0b2b19369a633df5f20ddf4f5a01d6c8ffa181e9d3a0572c19f919f72.ms.png)

> *Gambar dari [post blog ini](https://openai.com/blog/clip/)*

**Carian Imej Berdasarkan Teks**

Kita juga boleh melakukan sebaliknya. Jika kita mempunyai koleksi imej, kita boleh menghantar koleksi ini kepada model, dan satu arahan teks - ini akan memberikan kita imej yang paling serupa dengan arahan yang diberikan.

## ✍️ Contoh: [Menggunakan CLIP untuk Klasifikasi Imej dan Carian Imej](../../../../../lessons/X-Extras/X1-MultiModal/Clip.ipynb)

Buka notebook [Clip.ipynb](../../../../../lessons/X-Extras/X1-MultiModal/Clip.ipynb) untuk melihat CLIP beraksi.

## Penjanaan Imej dengan VQGAN+ CLIP

CLIP juga boleh digunakan untuk **penjanaan imej** daripada arahan teks. Untuk melakukan ini, kita memerlukan **model penjana** yang akan dapat menjana imej berdasarkan beberapa input vektor. Salah satu model tersebut dipanggil [VQGAN](https://compvis.github.io/taming-transformers/) (Vector-Quantized GAN).

Idea utama VQGAN yang membezakannya daripada [GAN](../../4-ComputerVision/10-GANs/README.md) biasa adalah seperti berikut:
* Menggunakan seni bina transformer autoregressive untuk menjana urutan bahagian visual yang kaya konteks yang membentuk imej. Bahagian visual tersebut seterusnya dipelajari oleh [CNN](../../4-ComputerVision/07-ConvNets/README.md)
* Menggunakan diskriminator sub-imej yang mengesan sama ada bahagian imej adalah "nyata" atau "palsu" (berbeza dengan pendekatan "semua atau tiada" dalam GAN tradisional).

Ketahui lebih lanjut tentang VQGAN di laman web [Taming Transformers](https://compvis.github.io/taming-transformers/).

Salah satu perbezaan penting antara VQGAN dan GAN tradisional adalah bahawa yang terakhir boleh menghasilkan imej yang baik daripada mana-mana vektor input, sementara VQGAN kemungkinan besar akan menghasilkan imej yang tidak koheren. Oleh itu, kita perlu membimbing proses penciptaan imej lebih lanjut, dan itu boleh dilakukan menggunakan CLIP.

![Arsitektur VQGAN+CLIP](../../../../../translated_images/vqgan.5027fe05051dfa3101950cfa930303f66e6478b9bd273e83766731796e462d9b.ms.png)

Untuk menjana imej yang sepadan dengan arahan teks, kita bermula dengan beberapa vektor pengkodan rawak yang dihantar melalui VQGAN untuk menghasilkan imej. Kemudian CLIP digunakan untuk menghasilkan fungsi kehilangan yang menunjukkan sejauh mana imej tersebut sepadan dengan arahan teks. Matlamatnya adalah untuk meminimumkan kehilangan ini, menggunakan pembalikan propagasi untuk menyesuaikan parameter vektor input.

Satu perpustakaan hebat yang mengimplementasikan VQGAN+CLIP adalah [Pixray](http://github.com/pixray/pixray)

![Gambar yang dihasilkan oleh Pixray](../../../../../translated_images/a_closeup_watercolor_portrait_of_young_male_teacher_of_literature_with_a_book.2384968e9db8a0d09dc96de938b9f95bde8a7e1c721f48f286a7795bf16d56c7.ms.png) |  ![Gambar yang dihasilkan oleh pixray](../../../../../translated_images/a_closeup_oil_portrait_of_young_female_teacher_of_computer_science_with_a_computer.e0b6495f210a439077e1c32cc8afdf714e634fe24dc78dc5aa45fd2f560b0ed5.ms.png) | ![Gambar yang dihasilkan oleh Pixray](../../../../../translated_images/a_closeup_oil_portrait_of_old_male_teacher_of_math.5362e67aa7fc2683b9d36a613b364deb7454760cd39205623fc1e3938fa133c0.ms.png)
----|----|----
Gambar yang dihasilkan dari arahan *gambar closeup potret cat air seorang guru lelaki muda dengan sebuah buku* | Gambar yang dihasilkan dari arahan *gambar closeup potret minyak seorang guru wanita muda dengan sains komputer dengan sebuah komputer* | Gambar yang dihasilkan dari arahan *gambar closeup potret minyak seorang guru lelaki tua dengan matematik di hadapan papan hitam*

> Gambar dari koleksi **Guru Tiruan** oleh [Dmitry Soshnikov](http://soshnikov.com)

## DALL-E
### [DALL-E 1](https://openai.com/research/dall-e)
DALL-E adalah versi GPT-3 yang dilatih untuk menjana imej daripada arahan. Ia telah dilatih dengan 12 bilion parameter.

Berbeza dengan CLIP, DALL-E menerima kedua-dua teks dan imej sebagai satu aliran token untuk kedua-dua imej dan teks. Oleh itu, daripada pelbagai arahan, anda boleh menjana imej berdasarkan teks.

### [DALL-E 2](https://openai.com/dall-e-2)
Perbezaan utama antara DALL-E 1 dan 2 adalah bahawa ia menghasilkan imej dan seni yang lebih realistik.

Contoh penjanaan imej dengan DALL-E:
![Gambar yang dihasilkan oleh Pixray](../../../../../translated_images/DALL·E%202023-06-20%2015.56.56%20-%20a%20closeup%20watercolor%20portrait%20of%20young%20male%20teacher%20of%20literature%20with%20a%20book.6c235e8271d9ed10ce985d86aeb241a58518958647973af136912116b9518fce.ms.png) |  ![Gambar yang dihasilkan oleh pixray](../../../../../translated_images/DALL·E%202023-06-20%2015.57.43%20-%20a%20closeup%20oil%20portrait%20of%20young%20female%20teacher%20of%20computer%20science%20with%20a%20computer.f21dc4166340b6c8b4d1cb57efd1e22127407f9b28c9ac7afe11344065369e64.ms.png) | ![Gambar yang dihasilkan oleh Pixray](../../../../../translated_images/DALL·E%202023-06-20%2015.58.42%20-%20%20a%20closeup%20oil%20portrait%20of%20old%20male%20teacher%20of%20mathematics%20in%20front%20of%20blackboard.d331c2dfbdc3f7c46aa65c0809066f5e7ed4b49609cd259852e760df21051e4a.ms.png)
----|----|----
Gambar yang dihasilkan dari arahan *gambar closeup potret cat air seorang guru lelaki muda dengan sebuah buku* | Gambar yang dihasilkan dari arahan *gambar closeup potret minyak seorang guru wanita muda dengan sains komputer dengan sebuah komputer* | Gambar yang dihasilkan dari arahan *gambar closeup potret minyak seorang guru lelaki tua dengan matematik di hadapan papan hitam*

## Rujukan

* Kertas VQGAN: [Taming Transformers for High-Resolution Image Synthesis](https://compvis.github.io/taming-transformers/paper/paper.pdf)
* Kertas CLIP: [Learning Transferable Visual Models From Natural Language Supervision](https://arxiv.org/pdf/2103.00020.pdf)

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan berasaskan AI. Walaupun kami berusaha untuk ketepatan, sila ambil perhatian bahawa terjemahan automatik mungkin mengandungi ralat atau ketidakakuratan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber yang sah. Untuk maklumat penting, terjemahan manusia profesional disyorkan. Kami tidak bertanggungjawab atas sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.