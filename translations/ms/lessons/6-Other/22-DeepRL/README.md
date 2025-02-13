# Pembelajaran Penguatan Dalam

Pembelajaran penguatan (RL) dilihat sebagai salah satu paradigma dasar pembelajaran mesin, bersebelahan dengan pembelajaran terawasi dan pembelajaran tidak terawasi. Sementara dalam pembelajaran terawasi kita bergantung pada dataset dengan hasil yang diketahui, RL didasarkan pada **belajar melalui pengalaman**. Sebagai contoh, ketika kita pertama kali melihat permainan komputer, kita mulai bermain, bahkan tanpa mengetahui aturannya, dan segera kita dapat meningkatkan keterampilan kita hanya melalui proses bermain dan menyesuaikan perilaku kita.

## [Kuiz Pra-kuliah](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/122)

Untuk melakukan RL, kita memerlukan:

* **Lingkungan** atau **simulator** yang menetapkan aturan permainan. Kita harus dapat menjalankan eksperimen dalam simulator dan mengamati hasilnya.
* Beberapa **Fungsi Reward**, yang menunjukkan seberapa sukses eksperimen kita. Dalam hal belajar bermain permainan komputer, reward akan menjadi skor akhir kita.

Berdasarkan fungsi reward, kita harus dapat menyesuaikan perilaku kita dan meningkatkan keterampilan kita, sehingga di lain waktu kita bermain dengan lebih baik. Perbedaan utama antara jenis pembelajaran mesin lainnya dan RL adalah bahwa dalam RL kita biasanya tidak tahu apakah kita menang atau kalah sampai kita menyelesaikan permainan. Dengan demikian, kita tidak dapat mengatakan apakah gerakan tertentu baik atau tidak - kita hanya menerima reward di akhir permainan.

Selama RL, kita biasanya melakukan banyak eksperimen. Selama setiap eksperimen, kita perlu menyeimbangkan antara mengikuti strategi optimal yang telah kita pelajari sejauh ini (**eksploitasi**) dan menjelajahi kemungkinan keadaan baru (**eksplorasi**).

## OpenAI Gym

Salah satu alat hebat untuk RL adalah [OpenAI Gym](https://gym.openai.com/) - sebuah **lingkungan simulasi**, yang dapat mensimulasikan banyak lingkungan berbeda mulai dari permainan Atari hingga fisika di balik penyeimbangan tiang. Ini adalah salah satu lingkungan simulasi yang paling populer untuk melatih algoritma pembelajaran penguatan, dan dikelola oleh [OpenAI](https://openai.com/).

> **Catatan**: Anda dapat melihat semua lingkungan yang tersedia dari OpenAI Gym [di sini](https://gym.openai.com/envs/#classic_control).

## Penyeimbangan CartPole

Anda mungkin semua telah melihat perangkat penyeimbang modern seperti *Segway* atau *Gyroscooters*. Mereka mampu menyeimbangkan secara otomatis dengan menyesuaikan roda mereka sebagai respons terhadap sinyal dari akselerometer atau giroskop. Dalam bagian ini, kita akan belajar bagaimana menyelesaikan masalah serupa - menyeimbangkan sebuah tiang. Ini mirip dengan situasi ketika seorang penghibur sirkus perlu menyeimbangkan tiang di tangannya - tetapi penyeimbangan tiang ini hanya terjadi dalam 1D.

Versi sederhana dari penyeimbangan dikenal sebagai masalah **CartPole**. Dalam dunia cartpole, kita memiliki penggeser horizontal yang dapat bergerak ke kiri atau kanan, dan tujuannya adalah untuk menyeimbangkan tiang vertikal di atas penggeser saat bergerak.

<img alt="a cartpole" src="images/cartpole.png" width="200"/>

Untuk membuat dan menggunakan lingkungan ini, kita memerlukan beberapa baris kode Python:

```python
import gym
env = gym.make("CartPole-v1")

env.reset()
done = False
total_reward = 0
while not done:
   env.render()
   action = env.action_space.sample()
   observaton, reward, done, info = env.step(action)
   total_reward += reward

print(f"Total reward: {total_reward}")
```

Setiap lingkungan dapat diakses dengan cara yang sama:
* `env.reset` starts a new experiment
* `env.step` melakukan langkah simulasi. Ini menerima **aksi** dari **ruang aksi**, dan mengembalikan **observasi** (dari ruang observasi), serta reward dan bendera penghentian.

Dalam contoh di atas kita melakukan aksi acak di setiap langkah, itulah sebabnya kehidupan eksperimen sangat singkat:

![non-balancing cartpole](../../../../../lessons/6-Other/22-DeepRL/images/cartpole-nobalance.gif)

Tujuan dari algoritma RL adalah untuk melatih model - yang disebut **kebijakan** π - yang akan mengembalikan aksi sebagai respons terhadap keadaan tertentu. Kita juga dapat mempertimbangkan kebijakan ini bersifat probabilistik, misalnya untuk setiap keadaan *s* dan aksi *a* akan mengembalikan probabilitas π(*a*|*s*) bahwa kita harus mengambil *a* dalam keadaan *s*.

## Algoritma Gradien Kebijakan

Cara paling jelas untuk memodelkan kebijakan adalah dengan membuat jaringan saraf yang akan mengambil keadaan sebagai input, dan mengembalikan aksi yang sesuai (atau lebih tepatnya probabilitas dari semua aksi). Dalam arti tertentu, ini akan mirip dengan tugas klasifikasi normal, dengan perbedaan utama - kita tidak tahu sebelumnya aksi mana yang harus kita ambil di setiap langkah.

Ide di sini adalah untuk memperkirakan probabilitas tersebut. Kita membangun vektor **reward kumulatif** yang menunjukkan total reward kita di setiap langkah eksperimen. Kita juga menerapkan **diskonto reward** dengan mengalikan reward sebelumnya dengan beberapa koefisien γ=0.99, untuk mengurangi peran reward sebelumnya. Kemudian, kita memperkuat langkah-langkah tersebut sepanjang jalur eksperimen yang menghasilkan reward lebih besar.

> Pelajari lebih lanjut tentang algoritma Gradien Kebijakan dan lihat dalam aksi di [notebook contoh](../../../../../lessons/6-Other/22-DeepRL/CartPole-RL-TF.ipynb).

## Algoritma Aktor-Kritik

Versi yang lebih baik dari pendekatan Gradien Kebijakan disebut **Aktor-Kritik**. Ide utama di baliknya adalah bahwa jaringan saraf akan dilatih untuk mengembalikan dua hal:

* Kebijakan, yang menentukan aksi mana yang harus diambil. Bagian ini disebut **aktor**
* Estimasi total reward yang dapat kita harapkan untuk didapatkan pada keadaan ini - bagian ini disebut **kritik**.

Dalam arti tertentu, arsitektur ini menyerupai [GAN](../../4-ComputerVision/10-GANs/README.md), di mana kita memiliki dua jaringan yang dilatih melawan satu sama lain. Dalam model aktor-kritik, aktor mengusulkan aksi yang perlu kita ambil, dan kritik berusaha untuk bersikap kritis dan memperkirakan hasilnya. Namun, tujuan kita adalah untuk melatih jaringan tersebut secara bersamaan.

Karena kita mengetahui baik reward kumulatif yang sebenarnya maupun hasil yang dikembalikan oleh kritik selama eksperimen, relatif mudah untuk membangun fungsi kerugian yang akan meminimalkan perbedaan antara keduanya. Itu akan memberi kita **kerugian kritik**. Kita dapat menghitung **kerugian aktor** dengan menggunakan pendekatan yang sama seperti dalam algoritma gradien kebijakan.

Setelah menjalankan salah satu algoritma tersebut, kita dapat mengharapkan CartPole kita berperilaku seperti ini:

![a balancing cartpole](../../../../../lessons/6-Other/22-DeepRL/images/cartpole-balance.gif)

## ✍️ Latihan: Gradien Kebijakan dan RL Aktor-Kritik

Lanjutkan pembelajaran Anda di notebook berikut:

* [RL dalam TensorFlow](../../../../../lessons/6-Other/22-DeepRL/CartPole-RL-TF.ipynb)
* [RL dalam PyTorch](../../../../../lessons/6-Other/22-DeepRL/CartPole-RL-PyTorch.ipynb)

## Tugas RL Lainnya

Pembelajaran Penguatan saat ini adalah bidang penelitian yang berkembang pesat. Beberapa contoh menarik dari pembelajaran penguatan adalah:

* Mengajarkan komputer untuk bermain **Permainan Atari**. Bagian yang menantang dalam masalah ini adalah bahwa kita tidak memiliki keadaan sederhana yang direpresentasikan sebagai vektor, tetapi lebih sebagai tangkapan layar - dan kita perlu menggunakan CNN untuk mengonversi gambar layar ini menjadi vektor fitur, atau untuk mengekstrak informasi reward. Permainan Atari tersedia di Gym.
* Mengajarkan komputer untuk bermain permainan papan, seperti Catur dan Go. Baru-baru ini program-program mutakhir seperti **Alpha Zero** dilatih dari awal oleh dua agen yang bermain satu sama lain, dan meningkat di setiap langkah.
* Dalam industri, RL digunakan untuk membuat sistem kontrol dari simulasi. Layanan bernama [Bonsai](https://azure.microsoft.com/services/project-bonsai/?WT.mc_id=academic-77998-cacaste) dirancang khusus untuk itu.

## Kesimpulan

Kita sekarang telah belajar bagaimana melatih agen untuk mencapai hasil yang baik hanya dengan memberikan mereka fungsi reward yang mendefinisikan keadaan yang diinginkan dari permainan, dan dengan memberi mereka kesempatan untuk menjelajahi ruang pencarian secara cerdas. Kita telah berhasil mencoba dua algoritma, dan mencapai hasil yang baik dalam waktu yang relatif singkat. Namun, ini hanyalah awal dari perjalanan Anda ke dalam RL, dan Anda pasti harus mempertimbangkan untuk mengambil kursus terpisah jika Anda ingin menyelami lebih dalam.

## 🚀 Tantangan

Jelajahi aplikasi yang terdaftar di bagian 'Tugas RL Lainnya' dan coba untuk mengimplementasikan salah satunya!

## [Kuiz Pasca-kuliah](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/222)

## Tinjauan & Studi Mandiri

Pelajari lebih lanjut tentang pembelajaran penguatan klasik dalam [Kurikulum Pembelajaran Mesin untuk Pemula](https://github.com/microsoft/ML-For-Beginners/blob/main/8-Reinforcement/README.md).

Tonton [video hebat ini](https://www.youtube.com/watch?v=qv6UVOQ0F44) yang membahas bagaimana komputer dapat belajar bermain Super Mario.

## Tugas: [Latih Mobil Gunung](lab/README.md)

Tujuan Anda selama tugas ini adalah untuk melatih lingkungan Gym yang berbeda - [Mobil Gunung](https://www.gymlibrary.ml/environments/classic_control/mountain_car/).

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan berasaskan AI. Walaupun kami berusaha untuk ketepatan, sila ambil perhatian bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidakakuratan. Dokumen asal dalam bahasa ibundanya harus dianggap sebagai sumber yang sah. Untuk maklumat yang kritikal, terjemahan manusia profesional disyorkan. Kami tidak bertanggungjawab atas sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.