# Pengesanan Kepala menggunakan Dataset Hollywood Heads

Tugasan Makmal dari [Kurikulum AI untuk Pemula](https://github.com/microsoft/ai-for-beginners).

## Tugas

Mengira jumlah orang dalam aliran kamera pengawasan video adalah tugas penting yang membolehkan kita menganggarkan jumlah pengunjung di kedai, waktu sibuk di restoran, dan sebagainya. Untuk menyelesaikan tugas ini, kita perlu dapat mengesan kepala manusia dari pelbagai sudut. Untuk melatih model pengesanan objek bagi mengesan kepala manusia, kita boleh menggunakan [Hollywood Heads Dataset](https://www.di.ens.fr/willow/research/headdetection/).

## Dataset

[Hollywood Heads Dataset](https://www.di.ens.fr/willow/research/headdetection/release/HollywoodHeads.zip) mengandungi 369,846 kepala manusia yang ditandakan dalam 224,740 bingkai filem dari filem Hollywood. Ia disediakan dalam format [https://host.robots.ox.ac.uk/pascal/VOC/](../../../../../../lessons/4-ComputerVision/11-ObjectDetection/lab/PASCAL VOC), di mana untuk setiap imej terdapat juga fail penerangan XML yang kelihatan seperti ini:

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

Dalam dataset ini, terdapat hanya satu kelas objek `head`, dan untuk setiap kepala, anda akan mendapatkan koordinat kotak pembatas. Anda boleh menguraikan XML menggunakan perpustakaan Python, atau menggunakan [perpustakaan ini](https://pypi.org/project/pascal-voc/) untuk berurusan secara langsung dengan format PASCAL VOC.

## Melatih Pengesanan Objek 

Anda boleh melatih model pengesanan objek menggunakan salah satu cara berikut:

* Menggunakan [Azure Custom Vision](https://docs.microsoft.com/azure/cognitive-services/custom-vision-service/quickstarts/object-detection?tabs=visual-studio&WT.mc_id=academic-77998-cacaste) dan API Python-nya untuk melatih model secara programatik di awan. Penglihatan khusus tidak dapat menggunakan lebih daripada beberapa ratus imej untuk melatih model, jadi anda mungkin perlu mengehadkan dataset.
* Menggunakan contoh dari [tutorial Keras](https://keras.io/examples/vision/retinanet/) untuk melatih model RetinaNet.
* Menggunakan modul terbina dalam [torchvision.models.detection.RetinaNet](https://pytorch.org/vision/stable/_modules/torchvision/models/detection/retinanet.html) dalam torchvision.

## Pengajaran

Pengesanan objek adalah tugas yang sering diperlukan dalam industri. Walaupun terdapat beberapa perkhidmatan yang boleh digunakan untuk melakukan pengesanan objek (seperti [Azure Custom Vision](https://docs.microsoft.com/azure/cognitive-services/custom-vision-service/quickstarts/object-detection?tabs=visual-studio&WT.mc_id=academic-77998-cacaste)), adalah penting untuk memahami bagaimana pengesanan objek berfungsi dan untuk dapat melatih model anda sendiri.

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan berasaskan AI. Walaupun kami berusaha untuk ketepatan, sila ambil perhatian bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidakakuratan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber yang berwibawa. Untuk maklumat yang kritikal, terjemahan manusia yang profesional disyorkan. Kami tidak bertanggungjawab atas sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.