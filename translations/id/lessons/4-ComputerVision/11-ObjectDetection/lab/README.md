# Deteksi Kepala menggunakan Dataset Hollywood Heads

Tugas Lab dari [Kurikulum AI untuk Pemula](https://github.com/microsoft/ai-for-beginners).

## Tugas

Menghitung jumlah orang pada aliran kamera pengawasan video adalah tugas penting yang memungkinkan kita memperkirakan jumlah pengunjung di toko, jam sibuk di restoran, dan sebagainya. Untuk menyelesaikan tugas ini, kita perlu mampu mendeteksi kepala manusia dari berbagai sudut. Untuk melatih model deteksi objek agar dapat mendeteksi kepala manusia, kita dapat menggunakan [Dataset Hollywood Heads](https://www.di.ens.fr/willow/research/headdetection/).

## Dataset

[Dataset Hollywood Heads](https://www.di.ens.fr/willow/research/headdetection/release/HollywoodHeads.zip) berisi 369.846 kepala manusia yang diberi anotasi dalam 224.740 frame film dari film-film Hollywood. Dataset ini disediakan dalam format [https://host.robots.ox.ac.uk/pascal/VOC/](../../../../../../lessons/4-ComputerVision/11-ObjectDetection/lab/PASCAL VOC), di mana untuk setiap gambar juga terdapat file deskripsi XML yang terlihat seperti ini:

```xml
<annotation>
	<folder>HollywoodHeads</folder>
	<filename>mov_021_149390.jpeg</filename>
	<source>
		<database>HollywoodHeads 2015 Database</database>
		<annotation>HollywoodHeads 2015</annotation>
		<image>WILLOW</image>
	</source>
	<size>
		<width>608</width>
		<height>320</height>
		<depth>3</depth>
	</size>
	<segmented>0</segmented>
	<object>
		<name>head</name>
		<bndbox>
			<xmin>201</xmin>
			<ymin>1</ymin>
			<xmax>480</xmax>
			<ymax>263</ymax>
		</bndbox>
		<difficult>0</difficult>
	</object>
	<object>
		<name>head</name>
		<bndbox>
			<xmin>3</xmin>
			<ymin>4</ymin>
			<xmax>241</xmax>
			<ymax>285</ymax>
		</bndbox>
		<difficult>0</difficult>
	</object>
</annotation>
```

Dalam dataset ini, hanya ada satu kelas objek yaitu `head`, dan untuk setiap kepala, Anda mendapatkan koordinat kotak pembatas. Anda dapat mem-parsing XML menggunakan pustaka Python, atau menggunakan [pustaka ini](https://pypi.org/project/pascal-voc/) untuk langsung menangani format PASCAL VOC.

## Melatih Deteksi Objek

Anda dapat melatih model deteksi objek menggunakan salah satu cara berikut:

* Menggunakan [Azure Custom Vision](https://docs.microsoft.com/azure/cognitive-services/custom-vision-service/quickstarts/object-detection?tabs=visual-studio&WT.mc_id=academic-77998-cacaste) dan API Python-nya untuk melatih model secara programatis di cloud. Custom Vision tidak dapat menggunakan lebih dari beberapa ratus gambar untuk melatih model, jadi Anda mungkin perlu membatasi dataset.
* Menggunakan contoh dari [tutorial Keras](https://keras.io/examples/vision/retinanet/) untuk melatih model RetunaNet.
* Menggunakan modul bawaan [torchvision.models.detection.RetinaNet](https://pytorch.org/vision/stable/_modules/torchvision/models/detection/retinanet.html) di torchvision.

## Kesimpulan

Deteksi objek adalah tugas yang sering dibutuhkan di industri. Meskipun ada beberapa layanan yang dapat digunakan untuk melakukan deteksi objek (seperti [Azure Custom Vision](https://docs.microsoft.com/azure/cognitive-services/custom-vision-service/quickstarts/object-detection?tabs=visual-studio&WT.mc_id=academic-77998-cacaste)), penting untuk memahami cara kerja deteksi objek dan mampu melatih model Anda sendiri.

---

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan layanan penerjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Meskipun kami berupaya untuk memberikan hasil yang akurat, harap diperhatikan bahwa terjemahan otomatis mungkin mengandung kesalahan atau ketidakakuratan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber yang berwenang. Untuk informasi yang bersifat kritis, disarankan menggunakan jasa penerjemahan manusia profesional. Kami tidak bertanggung jawab atas kesalahpahaman atau penafsiran yang keliru yang timbul dari penggunaan terjemahan ini.