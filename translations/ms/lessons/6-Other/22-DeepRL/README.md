# Pembelajaran Pengukuhan Mendalam

Pembelajaran pengukuhan (RL) dianggap sebagai salah satu paradigma asas pembelajaran mesin, selain pembelajaran diselia dan pembelajaran tanpa penyeliaan. Dalam pembelajaran diselia, kita bergantung pada dataset dengan hasil yang diketahui, manakala RL berasaskan **belajar melalui pengalaman**. Sebagai contoh, apabila kita pertama kali melihat permainan komputer, kita mula bermain walaupun tanpa mengetahui peraturannya, dan tidak lama kemudian kita dapat meningkatkan kemahiran kita hanya melalui proses bermain dan menyesuaikan tingkah laku kita.

## [Kuiz Pra-Kuliah](https://ff-quizzes.netlify.app/en/ai/quiz/43)

Untuk melaksanakan RL, kita memerlukan:

* **Persekitaran** atau **simulator** yang menetapkan peraturan permainan. Kita perlu dapat menjalankan eksperimen dalam simulator dan memerhatikan hasilnya.
* **Fungsi ganjaran**, yang menunjukkan sejauh mana eksperimen kita berjaya. Dalam kes belajar bermain permainan komputer, ganjaran adalah skor akhir kita.

Berdasarkan fungsi ganjaran, kita perlu dapat menyesuaikan tingkah laku kita dan meningkatkan kemahiran kita supaya kita bermain dengan lebih baik pada masa akan datang. Perbezaan utama antara jenis pembelajaran mesin lain dan RL ialah dalam RL kita biasanya tidak tahu sama ada kita menang atau kalah sehingga permainan selesai. Oleh itu, kita tidak dapat mengatakan sama ada satu langkah tertentu sahaja adalah baik atau tidak - kita hanya menerima ganjaran pada akhir permainan.

Semasa RL, kita biasanya menjalankan banyak eksperimen. Dalam setiap eksperimen, kita perlu mengimbangi antara mengikuti strategi optimum yang telah kita pelajari setakat ini (**eksploitasi**) dan meneroka keadaan baru yang mungkin (**eksplorasi**).

## OpenAI Gym

Satu alat yang hebat untuk RL ialah [OpenAI Gym](https://gym.openai.com/) - sebuah **persekitaran simulasi**, yang boleh mensimulasikan pelbagai persekitaran bermula dari permainan Atari hingga fizik di sebalik keseimbangan tiang. Ia adalah salah satu persekitaran simulasi paling popular untuk melatih algoritma pembelajaran pengukuhan, dan diselenggara oleh [OpenAI](https://openai.com/).

> **Note**: Anda boleh melihat semua persekitaran yang tersedia dari OpenAI Gym [di sini](https://gym.openai.com/envs/#classic_control).

## Keseimbangan CartPole

Anda mungkin pernah melihat alat keseimbangan moden seperti *Segway* atau *Gyroscooters*. Alat ini dapat secara automatik menyeimbangkan dengan menyesuaikan roda mereka sebagai tindak balas kepada isyarat dari accelerometer atau giroskop. Dalam bahagian ini, kita akan belajar bagaimana menyelesaikan masalah serupa - menyeimbangkan tiang. Ia serupa dengan situasi di mana seorang pemain sarkas perlu menyeimbangkan tiang di tangannya - tetapi keseimbangan tiang ini hanya berlaku dalam 1D.

Versi ringkas keseimbangan dikenali sebagai masalah **CartPole**. Dalam dunia cartpole, kita mempunyai slider mendatar yang boleh bergerak ke kiri atau kanan, dan matlamatnya adalah untuk menyeimbangkan tiang menegak di atas slider semasa ia bergerak.

<img alt="a cartpole" src="../../../../../translated_images/ms/cartpole.f52a67f27e058170.webp" width="200"/>

Untuk mencipta dan menggunakan persekitaran ini, kita memerlukan beberapa baris kod Python:

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

Setiap persekitaran boleh diakses dengan cara yang sama:
* `env.reset` memulakan eksperimen baru
* `env.step` melaksanakan langkah simulasi. Ia menerima **tindakan** dari **ruang tindakan**, dan mengembalikan **pemerhatian** (dari ruang pemerhatian), serta ganjaran dan bendera penamatan.

Dalam contoh di atas, kita melaksanakan tindakan rawak pada setiap langkah, sebab itu jangka hayat eksperimen sangat pendek:

![non-balancing cartpole](../../../../../lessons/6-Other/22-DeepRL/images/cartpole-nobalance.gif)

Matlamat algoritma RL adalah untuk melatih model - yang dipanggil **polisi** &pi; - yang akan mengembalikan tindakan sebagai tindak balas kepada keadaan tertentu. Kita juga boleh menganggap polisi sebagai probabilistik, contohnya untuk mana-mana keadaan *s* dan tindakan *a*, ia akan mengembalikan kebarangkalian &pi;(*a*|*s*) bahawa kita harus mengambil *a* dalam keadaan *s*.

## Algoritma Policy Gradients

Cara yang paling jelas untuk memodelkan polisi adalah dengan mencipta rangkaian neural yang akan mengambil keadaan sebagai input, dan mengembalikan tindakan yang sepadan (atau lebih tepat lagi kebarangkalian semua tindakan). Dalam satu aspek, ia serupa dengan tugas klasifikasi biasa, dengan perbezaan utama - kita tidak tahu terlebih dahulu tindakan mana yang harus kita ambil pada setiap langkah.

Idea di sini adalah untuk menganggarkan kebarangkalian tersebut. Kita membina vektor **ganjaran kumulatif** yang menunjukkan ganjaran keseluruhan kita pada setiap langkah eksperimen. Kita juga menggunakan **diskaun ganjaran** dengan mendarabkan ganjaran awal dengan beberapa pekali &gamma;=0.99, untuk mengurangkan peranan ganjaran awal. Kemudian, kita memperkuat langkah-langkah tersebut sepanjang laluan eksperimen yang menghasilkan ganjaran yang lebih besar.

> Ketahui lebih lanjut tentang algoritma Policy Gradient dan lihat ia beraksi dalam [notebook contoh](CartPole-RL-TF.ipynb).

## Algoritma Actor-Critic

Versi yang diperbaiki dari pendekatan Policy Gradients dipanggil **Actor-Critic**. Idea utama di sebaliknya ialah rangkaian neural akan dilatih untuk mengembalikan dua perkara:

* Polisi, yang menentukan tindakan mana yang perlu diambil. Bahagian ini dipanggil **actor**
* Anggaran ganjaran keseluruhan yang boleh kita harapkan pada keadaan ini - bahagian ini dipanggil **critic**.

Dalam satu aspek, seni bina ini menyerupai [GAN](../../4-ComputerVision/10-GANs/README.md), di mana kita mempunyai dua rangkaian yang dilatih melawan satu sama lain. Dalam model actor-critic, actor mencadangkan tindakan yang perlu kita ambil, dan critic cuba menjadi kritikal dan menganggarkan hasilnya. Walau bagaimanapun, matlamat kita adalah untuk melatih rangkaian tersebut secara serentak.

Kerana kita tahu kedua-dua ganjaran kumulatif sebenar dan hasil yang dikembalikan oleh critic semasa eksperimen, agak mudah untuk membina fungsi kehilangan yang akan meminimumkan perbezaan antara mereka. Itu akan memberikan kita **critic loss**. Kita boleh mengira **actor loss** dengan menggunakan pendekatan yang sama seperti dalam algoritma policy gradient.

Selepas menjalankan salah satu algoritma tersebut, kita boleh mengharapkan CartPole kita berkelakuan seperti ini:

![a balancing cartpole](../../../../../lessons/6-Other/22-DeepRL/images/cartpole-balance.gif)

## ✍️ Latihan: Policy Gradients dan Actor-Critic RL

Teruskan pembelajaran anda dalam notebook berikut:

* [RL dalam TensorFlow](CartPole-RL-TF.ipynb)
* [RL dalam PyTorch](CartPole-RL-PyTorch.ipynb)

## Tugas RL Lain

Pembelajaran Pengukuhan kini merupakan bidang penyelidikan yang berkembang pesat. Beberapa contoh menarik pembelajaran pengukuhan adalah:

* Mengajar komputer bermain **Permainan Atari**. Bahagian yang mencabar dalam masalah ini ialah kita tidak mempunyai keadaan mudah yang diwakili sebagai vektor, tetapi sebaliknya tangkapan skrin - dan kita perlu menggunakan CNN untuk menukar imej skrin ini kepada vektor ciri, atau untuk mengekstrak maklumat ganjaran. Permainan Atari tersedia dalam Gym.
* Mengajar komputer bermain permainan papan, seperti Catur dan Go. Baru-baru ini, program canggih seperti **Alpha Zero** dilatih dari awal oleh dua agen yang bermain melawan satu sama lain, dan meningkatkan prestasi pada setiap langkah.
* Dalam industri, RL digunakan untuk mencipta sistem kawalan dari simulasi. Perkhidmatan yang dipanggil [Bonsai](https://azure.microsoft.com/services/project-bonsai/?WT.mc_id=academic-77998-cacaste) direka khusus untuk itu.

## Kesimpulan

Kita kini telah belajar bagaimana melatih agen untuk mencapai hasil yang baik hanya dengan memberikan mereka fungsi ganjaran yang menentukan keadaan permainan yang diinginkan, dan dengan memberi mereka peluang untuk meneroka ruang carian dengan bijak. Kita telah berjaya mencuba dua algoritma, dan mencapai hasil yang baik dalam tempoh masa yang agak singkat. Walau bagaimanapun, ini hanyalah permulaan perjalanan anda ke dalam RL, dan anda harus mempertimbangkan untuk mengambil kursus yang berasingan jika anda ingin mendalami lebih lanjut.

## 🚀 Cabaran

Terokai aplikasi yang disenaraikan dalam bahagian 'Tugas RL Lain' dan cuba laksanakan salah satu daripadanya!

## [Kuiz Pasca-Kuliah](https://ff-quizzes.netlify.app/en/ai/quiz/44)

## Kajian & Pembelajaran Kendiri

Ketahui lebih lanjut tentang pembelajaran pengukuhan klasik dalam [Kurikulum Pembelajaran Mesin untuk Pemula](https://github.com/microsoft/ML-For-Beginners/blob/main/8-Reinforcement/README.md).

Tonton [video hebat ini](https://www.youtube.com/watch?v=qv6UVOQ0F44) yang membincangkan bagaimana komputer boleh belajar bermain Super Mario.

## Tugasan: [Latih Kereta Gunung](lab/README.md)

Matlamat anda semasa tugasan ini adalah untuk melatih persekitaran Gym yang berbeza - [Mountain Car](https://www.gymlibrary.ml/environments/classic_control/mountain_car/).

---

