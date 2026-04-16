# Các Ví dụ AI Dễ Hiểu

Chào mừng bạn! Thư mục này chứa các ví dụ đơn giản, độc lập để giúp bạn bắt đầu với AI và học máy. Mỗi ví dụ được thiết kế thân thiện với người mới bắt đầu, kèm theo các bình luận chi tiết và hướng dẫn từng bước.

## 📚 Tổng Quan Các Ví Dụ

| Ví dụ | Mô tả | Mức độ khó | Yêu cầu trước |
|-------|-------|------------|---------------|
| [Hello AI World](../../../examples/01-hello-ai-world.py) | Chương trình AI đầu tiên của bạn - nhận diện mẫu đơn giản | ⭐ Dễ | Kiến thức cơ bản về Python |
| [Simple Neural Network](../../../examples/02-simple-neural-network.py) | Tạo một mạng nơ-ron từ đầu | ⭐⭐ Dễ+ | Python, toán học cơ bản |
| [Image Classifier](./03-image-classifier.ipynb) | Phân loại hình ảnh với mô hình đã được huấn luyện trước | ⭐⭐ Dễ+ | Python, numpy |
| [Text Sentiment](../../../examples/04-text-sentiment.py) | Phân tích cảm xúc văn bản (tích cực/tiêu cực) | ⭐⭐ Dễ+ | Python |

## 🚀 Bắt Đầu

### Yêu Cầu Trước

Hãy đảm bảo bạn đã cài đặt Python (khuyến nghị phiên bản 3.8 hoặc cao hơn). Cài đặt các gói cần thiết:

```bash
# For Python scripts
pip install numpy

# For Jupyter notebooks (image classifier)
pip install jupyter numpy pillow tensorflow
```

Hoặc sử dụng môi trường conda từ chương trình học chính:

```bash
conda env create --name ai4beg --file ../environment.yml
conda activate ai4beg
```

### Chạy Các Ví Dụ

**Đối với các tập tin Python (.py):**
```bash
python 01-hello-ai-world.py
```

**Đối với các notebook Jupyter (.ipynb):**
```bash
jupyter notebook 03-image-classifier.ipynb
```

## 📖 Lộ Trình Học Tập

Chúng tôi khuyến nghị bạn làm theo thứ tự các ví dụ:

1. **Bắt đầu với "Hello AI World"** - Tìm hiểu cơ bản về nhận diện mẫu
2. **Xây dựng Mạng Nơ-ron Đơn Giản** - Hiểu cách hoạt động của mạng nơ-ron
3. **Thử Phân Loại Hình Ảnh** - Xem AI hoạt động với hình ảnh thực tế
4. **Phân Tích Cảm Xúc Văn Bản** - Khám phá xử lý ngôn ngữ tự nhiên

## 💡 Mẹo Cho Người Mới Bắt Đầu

- **Đọc kỹ các bình luận trong mã** - Chúng giải thích từng dòng mã
- **Thử nghiệm!** - Thay đổi các giá trị và xem điều gì xảy ra
- **Đừng lo lắng nếu chưa hiểu hết** - Học tập cần thời gian
- **Đặt câu hỏi** - Sử dụng [Diễn đàn thảo luận](https://github.com/microsoft/AI-For-Beginners/discussions)

## 🔗 Bước Tiếp Theo

Sau khi hoàn thành các ví dụ này, hãy khám phá chương trình học đầy đủ:
- [Giới thiệu về AI](../lessons/1-Intro/README.md)
- [Mạng Nơ-ron](../lessons/3-NeuralNetworks/README.md)
- [Thị Giác Máy Tính](../lessons/4-ComputerVision/README.md)
- [Xử Lý Ngôn Ngữ Tự Nhiên](../lessons/5-NLP/README.md)

## 🤝 Đóng Góp

Thấy các ví dụ này hữu ích? Hãy giúp chúng tôi cải thiện:
- Báo cáo lỗi hoặc đề xuất cải tiến
- Thêm nhiều ví dụ hơn cho người mới bắt đầu
- Cải thiện tài liệu và các bình luận

---

*Hãy nhớ: Mọi chuyên gia đều từng là người mới bắt đầu. Chúc bạn học tập vui vẻ! 🎓*

---

**Tuyên bố miễn trừ trách nhiệm**:  
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng các bản dịch tự động có thể chứa lỗi hoặc không chính xác. Tài liệu gốc bằng ngôn ngữ bản địa nên được coi là nguồn thông tin chính thức. Đối với các thông tin quan trọng, khuyến nghị sử dụng dịch vụ dịch thuật chuyên nghiệp bởi con người. Chúng tôi không chịu trách nhiệm cho bất kỳ sự hiểu lầm hoặc diễn giải sai nào phát sinh từ việc sử dụng bản dịch này.