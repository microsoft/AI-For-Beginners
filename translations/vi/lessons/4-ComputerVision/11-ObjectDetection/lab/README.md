# Phát hiện đầu người sử dụng Hollywood Heads Dataset

Bài tập thực hành từ [AI for Beginners Curriculum](https://github.com/microsoft/ai-for-beginners).

## Nhiệm vụ

Đếm số lượng người trên luồng camera giám sát là một nhiệm vụ quan trọng, giúp chúng ta ước tính số lượng khách hàng trong cửa hàng, giờ cao điểm tại nhà hàng, v.v. Để giải quyết nhiệm vụ này, chúng ta cần có khả năng phát hiện đầu người từ nhiều góc độ khác nhau. Để huấn luyện mô hình phát hiện đối tượng nhằm phát hiện đầu người, chúng ta có thể sử dụng [Hollywood Heads Dataset](https://www.di.ens.fr/willow/research/headdetection/).

## Bộ dữ liệu

[Hollywood Heads Dataset](https://www.di.ens.fr/willow/research/headdetection/release/HollywoodHeads.zip) chứa 369,846 đầu người được chú thích trong 224,740 khung hình từ các bộ phim Hollywood. Bộ dữ liệu này được cung cấp theo định dạng [https://host.robots.ox.ac.uk/pascal/VOC/](../../../../../../lessons/4-ComputerVision/11-ObjectDetection/lab/PASCAL VOC), trong đó mỗi hình ảnh đều có một tệp mô tả XML đi kèm, trông như sau:

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

Trong bộ dữ liệu này, chỉ có một loại đối tượng là `head`, và với mỗi đầu người, bạn sẽ nhận được tọa độ của hộp giới hạn. Bạn có thể phân tích XML bằng các thư viện Python, hoặc sử dụng [thư viện này](https://pypi.org/project/pascal-voc/) để làm việc trực tiếp với định dạng PASCAL VOC.

## Huấn luyện mô hình phát hiện đối tượng

Bạn có thể huấn luyện mô hình phát hiện đối tượng bằng một trong các cách sau:

* Sử dụng [Azure Custom Vision](https://docs.microsoft.com/azure/cognitive-services/custom-vision-service/quickstarts/object-detection?tabs=visual-studio&WT.mc_id=academic-77998-cacaste) và API Python của nó để lập trình huấn luyện mô hình trên đám mây. Custom Vision sẽ không thể sử dụng hơn vài trăm hình ảnh để huấn luyện mô hình, vì vậy bạn có thể cần giới hạn bộ dữ liệu.
* Sử dụng ví dụ từ [Keras tutorial](https://keras.io/examples/vision/retinanet/) để huấn luyện mô hình RetunaNet.
* Sử dụng module tích hợp [torchvision.models.detection.RetinaNet](https://pytorch.org/vision/stable/_modules/torchvision/models/detection/retinanet.html) trong torchvision.

## Kết luận

Phát hiện đối tượng là một nhiệm vụ thường xuyên được yêu cầu trong ngành công nghiệp. Mặc dù có một số dịch vụ có thể được sử dụng để thực hiện phát hiện đối tượng (chẳng hạn như [Azure Custom Vision](https://docs.microsoft.com/azure/cognitive-services/custom-vision-service/quickstarts/object-detection?tabs=visual-studio&WT.mc_id=academic-77998-cacaste)), việc hiểu cách phát hiện đối tượng hoạt động và có khả năng tự huấn luyện mô hình của riêng mình là rất quan trọng.

---

**Tuyên bố miễn trừ trách nhiệm**:  
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng các bản dịch tự động có thể chứa lỗi hoặc sự không chính xác. Tài liệu gốc bằng ngôn ngữ bản địa nên được coi là nguồn tham khảo chính thức. Đối với các thông tin quan trọng, nên sử dụng dịch vụ dịch thuật chuyên nghiệp từ con người. Chúng tôi không chịu trách nhiệm cho bất kỳ sự hiểu lầm hoặc diễn giải sai nào phát sinh từ việc sử dụng bản dịch này.