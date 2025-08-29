<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "d7f8a25ff13cfe9f4cd671cc23351fad",
  "translation_date": "2025-08-29T12:26:33+00:00",
  "source_file": "lessons/4-ComputerVision/12-Segmentation/README.md",
  "language_code": "vi"
}
-->
# Phân đoạn

Chúng ta đã học về Phát hiện Đối tượng, một kỹ thuật cho phép xác định vị trí các đối tượng trong hình ảnh bằng cách dự đoán *hộp giới hạn* của chúng. Tuy nhiên, trong một số nhiệm vụ, chúng ta không chỉ cần hộp giới hạn mà còn cần định vị đối tượng chính xác hơn. Nhiệm vụ này được gọi là **phân đoạn**.

## [Câu hỏi trước bài giảng](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/112)

Phân đoạn có thể được xem như là **phân loại từng điểm ảnh**, trong đó đối với **mỗi** điểm ảnh của hình ảnh, chúng ta phải dự đoán lớp của nó (*nền* cũng được xem là một lớp). Có hai thuật toán phân đoạn chính:

* **Phân đoạn ngữ nghĩa** chỉ xác định lớp của điểm ảnh mà không phân biệt các đối tượng khác nhau thuộc cùng một lớp.
* **Phân đoạn theo đối tượng** chia các lớp thành các đối tượng riêng biệt.

Ví dụ, trong phân đoạn theo đối tượng, các con cừu này được xem là các đối tượng khác nhau, nhưng trong phân đoạn ngữ nghĩa, tất cả các con cừu được đại diện bởi một lớp duy nhất.

<img src="images/instance_vs_semantic.jpeg" width="50%">

> Hình ảnh từ [bài viết này](https://nirmalamurali.medium.com/image-classification-vs-semantic-segmentation-vs-instance-segmentation-625c33a08d50)

Có nhiều kiến trúc mạng nơ-ron khác nhau dành cho phân đoạn, nhưng tất cả đều có cấu trúc tương tự. Theo một cách nào đó, nó giống với autoencoder mà bạn đã học trước đây, nhưng thay vì tái tạo lại hình ảnh gốc, mục tiêu của chúng ta là tái tạo một **mặt nạ**. Do đó, một mạng phân đoạn bao gồm các phần sau:

* **Bộ mã hóa (Encoder)** trích xuất các đặc trưng từ hình ảnh đầu vào.
* **Bộ giải mã (Decoder)** chuyển đổi các đặc trưng đó thành **hình ảnh mặt nạ**, với cùng kích thước và số kênh tương ứng với số lượng lớp.

<img src="images/segm.png" width="80%">

> Hình ảnh từ [ấn phẩm này](https://arxiv.org/pdf/2001.05566.pdf)

Chúng ta cần đặc biệt lưu ý đến hàm mất mát được sử dụng cho phân đoạn. Khi sử dụng autoencoder cổ điển, chúng ta cần đo lường sự tương đồng giữa hai hình ảnh và có thể sử dụng lỗi bình phương trung bình (MSE) để làm điều đó. Trong phân đoạn, mỗi điểm ảnh trong hình ảnh mặt nạ mục tiêu đại diện cho số lớp (được mã hóa one-hot theo chiều thứ ba), vì vậy chúng ta cần sử dụng các hàm mất mát dành riêng cho phân loại - hàm mất mát cross-entropy, được tính trung bình trên tất cả các điểm ảnh. Nếu mặt nạ là nhị phân - **hàm mất mát binary cross-entropy (BCE)** được sử dụng.

> ✅ Mã hóa one-hot là một cách để mã hóa nhãn lớp thành một vector có độ dài bằng với số lượng lớp. Hãy xem [bài viết này](https://datagy.io/sklearn-one-hot-encode/) để tìm hiểu thêm về kỹ thuật này.

## Phân đoạn trong Hình ảnh Y tế

Trong bài học này, chúng ta sẽ thấy phân đoạn hoạt động như thế nào bằng cách huấn luyện mạng để nhận diện nốt ruồi (còn được gọi là nevi) trên hình ảnh y tế. Chúng ta sẽ sử dụng <a href="https://www.fc.up.pt/addi/ph2%20database.html">Cơ sở dữ liệu PH<sup>2</sup></a> của các hình ảnh soi da làm nguồn hình ảnh. Bộ dữ liệu này chứa 200 hình ảnh thuộc ba lớp: nốt ruồi điển hình, nốt ruồi không điển hình, và u hắc tố. Tất cả các hình ảnh đều đi kèm với một **mặt nạ** tương ứng để xác định đường viền của nốt ruồi.

> ✅ Kỹ thuật này đặc biệt phù hợp với loại hình ảnh y tế này, nhưng bạn có thể tưởng tượng ra những ứng dụng thực tế nào khác?

<img alt="navi" src="images/navi.png"/>

> Hình ảnh từ Cơ sở dữ liệu PH<sup>2</sup>

Chúng ta sẽ huấn luyện một mô hình để phân đoạn bất kỳ nốt ruồi nào ra khỏi nền.

## ✍️ Bài tập: Phân đoạn Ngữ nghĩa

Mở các notebook dưới đây để tìm hiểu thêm về các kiến trúc phân đoạn ngữ nghĩa khác nhau, thực hành làm việc với chúng và xem chúng hoạt động như thế nào.

* [Phân đoạn Ngữ nghĩa với Pytorch](SemanticSegmentationPytorch.ipynb)
* [Phân đoạn Ngữ nghĩa với TensorFlow](SemanticSegmentationTF.ipynb)

## [Câu hỏi sau bài giảng](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/212)

## Kết luận

Phân đoạn là một kỹ thuật rất mạnh mẽ trong phân loại hình ảnh, vượt ra ngoài hộp giới hạn để phân loại ở cấp độ điểm ảnh. Đây là một kỹ thuật được sử dụng trong hình ảnh y tế và nhiều ứng dụng khác.

## 🚀 Thử thách

Phân đoạn cơ thể chỉ là một trong những nhiệm vụ phổ biến mà chúng ta có thể thực hiện với hình ảnh của con người. Các nhiệm vụ quan trọng khác bao gồm **phát hiện khung xương** và **phát hiện tư thế**. Hãy thử thư viện [OpenPose](https://github.com/CMU-Perceptual-Computing-Lab/openpose) để xem cách phát hiện tư thế có thể được sử dụng.

## Ôn tập & Tự học

Bài viết [Wikipedia này](https://wikipedia.org/wiki/Image_segmentation) cung cấp một cái nhìn tổng quan tốt về các ứng dụng khác nhau của kỹ thuật này. Tìm hiểu thêm về các phân ngành của Phân đoạn theo đối tượng và Phân đoạn toàn cảnh trong lĩnh vực này.

## [Bài tập](lab/README.md)

Trong bài thực hành này, hãy thử **phân đoạn cơ thể người** bằng cách sử dụng [Bộ dữ liệu Phân đoạn Toàn thân MADS](https://www.kaggle.com/datasets/tapakah68/segmentation-full-body-mads-dataset) từ Kaggle.

---

**Tuyên bố miễn trừ trách nhiệm**:  
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng các bản dịch tự động có thể chứa lỗi hoặc không chính xác. Tài liệu gốc bằng ngôn ngữ bản địa nên được coi là nguồn tham khảo chính thức. Đối với các thông tin quan trọng, nên sử dụng dịch vụ dịch thuật chuyên nghiệp từ con người. Chúng tôi không chịu trách nhiệm cho bất kỳ sự hiểu lầm hoặc diễn giải sai nào phát sinh từ việc sử dụng bản dịch này.