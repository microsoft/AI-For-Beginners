<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f3d2cee9cb3c52160419e560c57a690e",
  "translation_date": "2025-08-29T12:20:20+00:00",
  "source_file": "lessons/4-ComputerVision/07-ConvNets/lab/README.md",
  "language_code": "vi"
}
-->
# Phân loại khuôn mặt thú cưng

Bài tập thực hành từ [AI for Beginners Curriculum](https://github.com/microsoft/ai-for-beginners).

## Nhiệm vụ

Hãy tưởng tượng bạn cần phát triển một ứng dụng cho trung tâm chăm sóc thú cưng để lập danh mục tất cả các thú nuôi. Một trong những tính năng tuyệt vời của ứng dụng này là tự động nhận diện giống loài từ một bức ảnh. Điều này có thể được thực hiện thành công bằng cách sử dụng mạng nơ-ron.

Bạn cần huấn luyện một mạng nơ-ron tích chập để phân loại các giống loài khác nhau của mèo và chó bằng cách sử dụng bộ dữ liệu **Pet Faces**.

## Bộ dữ liệu

Chúng ta sẽ sử dụng bộ dữ liệu **Pet Faces**, được lấy từ bộ dữ liệu thú cưng [Oxford-IIIT](https://www.robots.ox.ac.uk/~vgg/data/pets/). Bộ dữ liệu này chứa 35 giống loài khác nhau của chó và mèo.

![Bộ dữ liệu chúng ta sẽ làm việc](../../../../../../translated_images/data.50b2a9d5484bdbf0f52f5765b381cec9efe2bd296a98f007f90bedb6ac67f2a8.vi.png)

Để tải bộ dữ liệu, hãy sử dụng đoạn mã sau:

```python
!wget https://mslearntensorflowlp.blob.core.windows.net/data/petfaces.tar.gz
!tar xfz petfaces.tar.gz
!rm petfaces.tar.gz
```

## Bắt đầu với Notebook

Bắt đầu bài thực hành bằng cách mở [PetFaces.ipynb](PetFaces.ipynb)

## Kết quả đạt được

Bạn đã giải quyết một vấn đề tương đối phức tạp về phân loại hình ảnh từ đầu! Có khá nhiều lớp, nhưng bạn vẫn có thể đạt được độ chính xác hợp lý! Ngoài ra, việc đo lường độ chính xác top-k cũng rất hợp lý, vì một số lớp có thể dễ bị nhầm lẫn, ngay cả đối với con người.

---

**Tuyên bố miễn trừ trách nhiệm**:  
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng các bản dịch tự động có thể chứa lỗi hoặc không chính xác. Tài liệu gốc bằng ngôn ngữ bản địa nên được coi là nguồn tham khảo chính thức. Đối với các thông tin quan trọng, nên sử dụng dịch vụ dịch thuật chuyên nghiệp từ con người. Chúng tôi không chịu trách nhiệm cho bất kỳ sự hiểu lầm hoặc diễn giải sai nào phát sinh từ việc sử dụng bản dịch này.