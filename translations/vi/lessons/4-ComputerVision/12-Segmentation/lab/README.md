# Phân Đoạn Cơ Thể Người

Bài tập thực hành từ [AI for Beginners Curriculum](https://github.com/microsoft/ai-for-beginners).

## Nhiệm vụ

Trong sản xuất video, ví dụ như dự báo thời tiết, chúng ta thường cần cắt hình ảnh của một người từ camera và đặt nó lên một cảnh quay khác. Điều này thường được thực hiện bằng kỹ thuật **chroma key**, khi một người được quay trước nền màu đồng nhất, sau đó nền này sẽ bị loại bỏ. Trong bài thực hành này, chúng ta sẽ huấn luyện một mô hình mạng nơ-ron để cắt ra hình dáng của người.

## Bộ Dữ Liệu

Chúng ta sẽ sử dụng [Segmentation Full Body MADS Dataset](https://www.kaggle.com/datasets/tapakah68/segmentation-full-body-mads-dataset) từ Kaggle. Tải bộ dữ liệu này thủ công từ Kaggle.

## Notebook Bắt Đầu

Bắt đầu bài thực hành bằng cách mở [BodySegmentation.ipynb](BodySegmentation.ipynb)

## Kết Quả Đạt Được

Phân đoạn cơ thể người chỉ là một trong những nhiệm vụ phổ biến mà chúng ta có thể thực hiện với hình ảnh của con người. Các nhiệm vụ quan trọng khác bao gồm **phát hiện khung xương** và **phát hiện tư thế**. Hãy tìm hiểu thư viện [OpenPose](https://github.com/CMU-Perceptual-Computing-Lab/openpose) để xem cách thực hiện những nhiệm vụ này.

---

**Tuyên bố miễn trừ trách nhiệm**:  
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng các bản dịch tự động có thể chứa lỗi hoặc không chính xác. Tài liệu gốc bằng ngôn ngữ bản địa nên được coi là nguồn tham khảo chính thức. Đối với các thông tin quan trọng, nên sử dụng dịch vụ dịch thuật chuyên nghiệp từ con người. Chúng tôi không chịu trách nhiệm cho bất kỳ sự hiểu lầm hoặc diễn giải sai nào phát sinh từ việc sử dụng bản dịch này.