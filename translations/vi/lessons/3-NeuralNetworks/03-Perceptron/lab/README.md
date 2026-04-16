# Phân Loại Đa Lớp với Perceptron

Bài tập thực hành từ [AI for Beginners Curriculum](https://github.com/microsoft/ai-for-beginners).

## Nhiệm vụ

Sử dụng mã mà chúng ta đã phát triển trong bài học này để phân loại nhị phân các chữ số viết tay MNIST, tạo một bộ phân loại đa lớp có thể nhận diện bất kỳ chữ số nào. Tính độ chính xác phân loại trên tập dữ liệu huấn luyện và kiểm tra, và in ra ma trận nhầm lẫn.

## Gợi ý

1. Đối với mỗi chữ số, tạo một tập dữ liệu cho bộ phân loại nhị phân "chữ số này so với tất cả các chữ số khác".
1. Huấn luyện 10 perceptron khác nhau để phân loại nhị phân (mỗi perceptron cho một chữ số).
1. Định nghĩa một hàm để phân loại một chữ số đầu vào.

> **Gợi ý**: Nếu chúng ta kết hợp các trọng số của cả 10 perceptron vào một ma trận, chúng ta có thể áp dụng cả 10 perceptron lên các chữ số đầu vào chỉ bằng một phép nhân ma trận. Chữ số có khả năng cao nhất có thể được tìm thấy chỉ bằng cách áp dụng phép `argmax` trên đầu ra.

## Notebook Bắt Đầu

Bắt đầu bài thực hành bằng cách mở [PerceptronMultiClass.ipynb](PerceptronMultiClass.ipynb)

---

**Tuyên bố miễn trừ trách nhiệm**:  
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng các bản dịch tự động có thể chứa lỗi hoặc không chính xác. Tài liệu gốc bằng ngôn ngữ bản địa nên được coi là nguồn thông tin chính thức. Đối với các thông tin quan trọng, khuyến nghị sử dụng dịch vụ dịch thuật chuyên nghiệp bởi con người. Chúng tôi không chịu trách nhiệm cho bất kỳ sự hiểu lầm hoặc diễn giải sai nào phát sinh từ việc sử dụng bản dịch này.