# การตรวจจับศีรษะด้วยชุดข้อมูล Hollywood Heads

งานในห้องปฏิบัติการจาก [AI for Beginners Curriculum](https://github.com/microsoft/ai-for-beginners)

## งานที่ต้องทำ

การนับจำนวนคนในสตรีมกล้องวงจรปิดเป็นงานสำคัญที่ช่วยให้เราประเมินจำนวนผู้เยี่ยมชมในร้านค้า ช่วงเวลาที่มีคนหนาแน่นในร้านอาหาร เป็นต้น เพื่อแก้ปัญหานี้ เราจำเป็นต้องสามารถตรวจจับศีรษะของมนุษย์จากมุมต่างๆ ได้ ในการฝึกโมเดลตรวจจับวัตถุเพื่อให้สามารถตรวจจับศีรษะมนุษย์ได้ เราสามารถใช้ [ชุดข้อมูล Hollywood Heads](https://www.di.ens.fr/willow/research/headdetection/) ได้

## ชุดข้อมูล

[ชุดข้อมูล Hollywood Heads](https://www.di.ens.fr/willow/research/headdetection/release/HollywoodHeads.zip) มีข้อมูลศีรษะมนุษย์ที่ถูกระบุไว้จำนวน 369,846 จุดในเฟรมภาพยนตร์ฮอลลีวูด 224,740 เฟรม ชุดข้อมูลนี้ถูกจัดเตรียมในรูปแบบ [https://host.robots.ox.ac.uk/pascal/VOC/](../../../../../../lessons/4-ComputerVision/11-ObjectDetection/lab/PASCAL VOC) ซึ่งในแต่ละภาพจะมีไฟล์คำอธิบาย XML ที่มีลักษณะดังนี้:

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

ในชุดข้อมูลนี้มีเพียงคลาสเดียวคือ `head` และสำหรับแต่ละศีรษะ คุณจะได้รับพิกัดของกรอบสี่เหลี่ยมที่ครอบศีรษะนั้น คุณสามารถใช้ไลบรารี Python ในการแปลงไฟล์ XML หรือใช้ [ไลบรารีนี้](https://pypi.org/project/pascal-voc/) เพื่อจัดการกับรูปแบบ PASCAL VOC โดยตรง

## การฝึกโมเดลตรวจจับวัตถุ

คุณสามารถฝึกโมเดลตรวจจับวัตถุได้ด้วยวิธีการดังต่อไปนี้:

* ใช้ [Azure Custom Vision](https://docs.microsoft.com/azure/cognitive-services/custom-vision-service/quickstarts/object-detection?tabs=visual-studio&WT.mc_id=academic-77998-cacaste) และ API ของ Python เพื่อฝึกโมเดลในคลาวด์แบบโปรแกรมมิ่ง Custom Vision จะไม่สามารถใช้ภาพจำนวนมากเกินไปในการฝึกโมเดล ดังนั้นคุณอาจต้องจำกัดขนาดชุดข้อมูล
* ใช้ตัวอย่างจาก [Keras tutorial](https://keras.io/examples/vision/retinanet/) เพื่อฝึกโมเดล RetunaNet
* ใช้ [torchvision.models.detection.RetinaNet](https://pytorch.org/vision/stable/_modules/torchvision/models/detection/retinanet.html) โมดูลที่มีอยู่ใน torchvision

## สิ่งที่ได้เรียนรู้

การตรวจจับวัตถุเป็นงานที่มีความต้องการสูงในอุตสาหกรรม แม้ว่าจะมีบริการบางอย่างที่สามารถใช้ในการตรวจจับวัตถุ (เช่น [Azure Custom Vision](https://docs.microsoft.com/azure/cognitive-services/custom-vision-service/quickstarts/object-detection?tabs=visual-studio&WT.mc_id=academic-77998-cacaste)) แต่สิ่งสำคัญคือการเข้าใจว่าการตรวจจับวัตถุทำงานอย่างไรและสามารถฝึกโมเดลของคุณเองได้

---

**ข้อจำกัดความรับผิดชอบ**:  
เอกสารนี้ได้รับการแปลโดยใช้บริการแปลภาษา AI [Co-op Translator](https://github.com/Azure/co-op-translator) แม้ว่าเราจะพยายามให้การแปลมีความถูกต้อง แต่โปรดทราบว่าการแปลอัตโนมัติอาจมีข้อผิดพลาดหรือความไม่แม่นยำ เอกสารต้นฉบับในภาษาต้นทางควรถือเป็นแหล่งข้อมูลที่เชื่อถือได้ สำหรับข้อมูลที่สำคัญ ขอแนะนำให้ใช้บริการแปลภาษามนุษย์ที่เป็นมืออาชีพ เราจะไม่รับผิดชอบต่อความเข้าใจผิดหรือการตีความที่ผิดพลาดซึ่งเกิดจากการใช้การแปลนี้