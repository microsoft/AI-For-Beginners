<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "dbacf9b1915612981d76059678e563e5",
  "translation_date": "2025-08-29T12:15:23+00:00",
  "source_file": "lessons/6-Other/22-DeepRL/README.md",
  "language_code": "id"
}
-->
# Pembelajaran Penguatan Mendalam

Pembelajaran penguatan (Reinforcement Learning atau RL) dianggap sebagai salah satu paradigma dasar dalam pembelajaran mesin, selain pembelajaran terawasi (supervised learning) dan pembelajaran tanpa pengawasan (unsupervised learning). Dalam pembelajaran terawasi, kita bergantung pada dataset dengan hasil yang sudah diketahui, sedangkan RL didasarkan pada **belajar dengan melakukan**. Sebagai contoh, ketika kita pertama kali melihat sebuah permainan komputer, kita mulai bermain meskipun tanpa mengetahui aturan, dan segera kita dapat meningkatkan kemampuan kita hanya melalui proses bermain dan menyesuaikan perilaku.

## [Kuis sebelum kuliah](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/122)

Untuk melakukan RL, kita membutuhkan:

* **Lingkungan** atau **simulator** yang menetapkan aturan permainan. Kita harus dapat menjalankan eksperimen di simulator dan mengamati hasilnya.
* **Fungsi reward**, yang menunjukkan seberapa sukses eksperimen kita. Dalam kasus belajar bermain permainan komputer, reward-nya adalah skor akhir kita.

Berdasarkan fungsi reward, kita harus dapat menyesuaikan perilaku kita dan meningkatkan kemampuan, sehingga di kesempatan berikutnya kita bermain lebih baik. Perbedaan utama antara jenis pembelajaran mesin lainnya dan RL adalah bahwa dalam RL kita biasanya tidak tahu apakah kita menang atau kalah sampai permainan selesai. Jadi, kita tidak dapat mengatakan apakah suatu langkah tertentu saja baik atau tidak - kita hanya menerima reward di akhir permainan.

Selama RL, kita biasanya melakukan banyak eksperimen. Dalam setiap eksperimen, kita perlu menyeimbangkan antara mengikuti strategi optimal yang telah kita pelajari sejauh ini (**eksploitasi**) dan menjelajahi kemungkinan keadaan baru (**eksplorasi**).

## OpenAI Gym

Salah satu alat yang hebat untuk RL adalah [OpenAI Gym](https://gym.openai.com/) - sebuah **lingkungan simulasi** yang dapat mensimulasikan berbagai lingkungan mulai dari permainan Atari hingga fisika di balik keseimbangan tiang. Ini adalah salah satu lingkungan simulasi paling populer untuk melatih algoritma pembelajaran penguatan, dan dikelola oleh [OpenAI](https://openai.com/).

> **Note**: Anda dapat melihat semua lingkungan yang tersedia dari OpenAI Gym [di sini](https://gym.openai.com/envs/#classic_control).

## Keseimbangan CartPole

Anda mungkin pernah melihat perangkat keseimbangan modern seperti *Segway* atau *Gyroscooters*. Mereka dapat secara otomatis menyeimbangkan dengan menyesuaikan roda mereka sebagai respons terhadap sinyal dari akselerometer atau giroskop. Dalam bagian ini, kita akan belajar bagaimana menyelesaikan masalah serupa - menyeimbangkan sebuah tiang. Ini mirip dengan situasi ketika seorang pemain sirkus perlu menyeimbangkan tiang di tangannya - tetapi keseimbangan tiang ini hanya terjadi dalam 1D.

Versi sederhana dari keseimbangan ini dikenal sebagai masalah **CartPole**. Dalam dunia cartpole, kita memiliki slider horizontal yang dapat bergerak ke kiri atau ke kanan, dan tujuannya adalah untuk menyeimbangkan tiang vertikal di atas slider saat bergerak.

<img alt="a cartpole" src="images/cartpole.png" width="200"/>

Untuk membuat dan menggunakan lingkungan ini, kita membutuhkan beberapa baris kode Python:

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

Setiap lingkungan dapat diakses dengan cara yang sama persis:
* `env.reset` memulai eksperimen baru
* `env.step` melakukan langkah simulasi. Fungsi ini menerima sebuah **aksi** dari **ruang aksi**, dan mengembalikan **observasi** (dari ruang observasi), serta reward dan flag penghentian.

Dalam contoh di atas, kita melakukan aksi acak di setiap langkah, itulah sebabnya eksperimen berumur sangat pendek:

![non-balancing cartpole](../../../../../lessons/6-Other/22-DeepRL/images/cartpole-nobalance.gif)

Tujuan dari algoritma RL adalah melatih sebuah model - yang disebut **policy** π - yang akan mengembalikan aksi sebagai respons terhadap keadaan tertentu. Kita juga dapat menganggap policy sebagai probabilistik, misalnya untuk setiap keadaan *s* dan aksi *a*, policy akan mengembalikan probabilitas π(*a*|*s*) bahwa kita harus mengambil *a* dalam keadaan *s*.

## Algoritma Policy Gradients

Cara paling jelas untuk memodelkan policy adalah dengan membuat jaringan saraf yang akan menerima keadaan sebagai input, dan mengembalikan aksi yang sesuai (atau lebih tepatnya probabilitas dari semua aksi). Dalam beberapa hal, ini mirip dengan tugas klasifikasi biasa, dengan perbedaan utama - kita tidak tahu sebelumnya aksi mana yang harus kita ambil di setiap langkah.

Idenya di sini adalah untuk memperkirakan probabilitas tersebut. Kita membangun sebuah vektor **reward kumulatif** yang menunjukkan total reward kita di setiap langkah eksperimen. Kita juga menerapkan **diskon reward** dengan mengalikan reward awal dengan koefisien γ=0.99, untuk mengurangi peran reward awal. Kemudian, kita memperkuat langkah-langkah sepanjang jalur eksperimen yang menghasilkan reward lebih besar.

> Pelajari lebih lanjut tentang algoritma Policy Gradient dan lihat aksinya dalam [notebook contoh](CartPole-RL-TF.ipynb).

## Algoritma Actor-Critic

Versi yang lebih baik dari pendekatan Policy Gradients disebut **Actor-Critic**. Ide utama di baliknya adalah bahwa jaringan saraf akan dilatih untuk mengembalikan dua hal:

* Policy, yang menentukan aksi apa yang harus diambil. Bagian ini disebut **actor**
* Estimasi total reward yang dapat kita harapkan di keadaan ini - bagian ini disebut **critic**.

Dalam beberapa hal, arsitektur ini menyerupai [GAN](../../4-ComputerVision/10-GANs/README.md), di mana kita memiliki dua jaringan yang dilatih satu sama lain. Dalam model actor-critic, actor mengusulkan aksi yang perlu kita ambil, dan critic mencoba bersikap kritis dan memperkirakan hasilnya. Namun, tujuan kita adalah melatih kedua jaringan ini secara bersamaan.

Karena kita mengetahui baik reward kumulatif nyata maupun hasil yang dikembalikan oleh critic selama eksperimen, relatif mudah untuk membangun fungsi loss yang akan meminimalkan perbedaan di antara keduanya. Ini akan memberikan kita **critic loss**. Kita dapat menghitung **actor loss** dengan menggunakan pendekatan yang sama seperti dalam algoritma policy gradient.

Setelah menjalankan salah satu algoritma tersebut, kita dapat mengharapkan CartPole kita berperilaku seperti ini:

![a balancing cartpole](../../../../../lessons/6-Other/22-DeepRL/images/cartpole-balance.gif)

## ✍️ Latihan: Policy Gradients dan Actor-Critic RL

Lanjutkan pembelajaran Anda dalam notebook berikut:

* [RL di TensorFlow](CartPole-RL-TF.ipynb)
* [RL di PyTorch](CartPole-RL-PyTorch.ipynb)

## Tugas RL Lainnya

Pembelajaran Penguatan saat ini adalah bidang penelitian yang berkembang pesat. Beberapa contoh menarik dari pembelajaran penguatan adalah:

* Mengajari komputer bermain **Permainan Atari**. Bagian yang menantang dalam masalah ini adalah kita tidak memiliki keadaan sederhana yang direpresentasikan sebagai vektor, melainkan tangkapan layar - dan kita perlu menggunakan CNN untuk mengonversi gambar layar ini menjadi vektor fitur, atau untuk mengekstrak informasi reward. Permainan Atari tersedia di Gym.
* Mengajari komputer bermain permainan papan, seperti Catur dan Go. Baru-baru ini, program mutakhir seperti **Alpha Zero** dilatih dari awal oleh dua agen yang bermain satu sama lain, dan meningkat di setiap langkah.
* Dalam industri, RL digunakan untuk membuat sistem kontrol dari simulasi. Layanan bernama [Bonsai](https://azure.microsoft.com/services/project-bonsai/?WT.mc_id=academic-77998-cacaste) dirancang khusus untuk itu.

## Kesimpulan

Kita telah belajar bagaimana melatih agen untuk mencapai hasil yang baik hanya dengan memberikan mereka fungsi reward yang mendefinisikan keadaan yang diinginkan dari permainan, dan dengan memberi mereka kesempatan untuk menjelajahi ruang pencarian secara cerdas. Kita telah mencoba dua algoritma dengan sukses, dan mencapai hasil yang baik dalam waktu yang relatif singkat. Namun, ini hanyalah awal dari perjalanan Anda ke dalam RL, dan Anda harus mempertimbangkan untuk mengambil kursus terpisah jika Anda ingin mendalami lebih jauh.

## 🚀 Tantangan

Jelajahi aplikasi yang tercantum di bagian 'Tugas RL Lainnya' dan coba implementasikan salah satunya!

## [Kuis setelah kuliah](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/222)

## Tinjauan & Studi Mandiri

Pelajari lebih lanjut tentang pembelajaran penguatan klasik dalam [Kurikulum Pembelajaran Mesin untuk Pemula](https://github.com/microsoft/ML-For-Beginners/blob/main/8-Reinforcement/README.md).

Tonton [video hebat ini](https://www.youtube.com/watch?v=qv6UVOQ0F44) yang membahas bagaimana komputer dapat belajar bermain Super Mario.

## Tugas: [Latih Mountain Car](lab/README.md)

Tujuan Anda dalam tugas ini adalah melatih lingkungan Gym yang berbeda - [Mountain Car](https://www.gymlibrary.ml/environments/classic_control/mountain_car/).

---

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan layanan penerjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Meskipun kami berusaha untuk memberikan hasil yang akurat, harap diingat bahwa terjemahan otomatis mungkin mengandung kesalahan atau ketidakakuratan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber yang otoritatif. Untuk informasi yang bersifat kritis, disarankan menggunakan jasa penerjemahan profesional oleh manusia. Kami tidak bertanggung jawab atas kesalahpahaman atau penafsiran yang keliru yang timbul dari penggunaan terjemahan ini.