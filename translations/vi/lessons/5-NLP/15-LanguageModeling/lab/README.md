# Huấn Luyện Mô Hình Skip-Gram

Bài tập thực hành từ [AI for Beginners Curriculum](https://github.com/microsoft/ai-for-beginners).

## Nhiệm Vụ

Trong bài thực hành này, chúng tôi thách thức bạn huấn luyện mô hình Word2Vec sử dụng kỹ thuật Skip-Gram. Huấn luyện một mạng với embedding để dự đoán các từ lân cận trong cửa sổ Skip-Gram rộng $N$ token. Bạn có thể sử dụng [mã từ bài học này](../CBoW-TF.ipynb) và chỉnh sửa một chút.

## Bộ Dữ Liệu

Bạn có thể sử dụng bất kỳ cuốn sách nào. Có rất nhiều văn bản miễn phí tại [Project Gutenberg](https://www.gutenberg.org/), ví dụ, đây là liên kết trực tiếp đến [Alice's Adventures in Wonderland](https://www.gutenberg.org/files/11/11-0.txt) của Lewis Carroll. Hoặc, bạn có thể sử dụng các vở kịch của Shakespeare, mà bạn có thể lấy bằng đoạn mã sau:

```python
path_to_file = tf.keras.utils.get_file(
   'shakespeare.txt', 
   'https://storage.googleapis.com/download.tensorflow.org/data/shakespeare.txt')
text = open(path_to_file, 'rb').read().decode(encoding='utf-8')
```

## Khám Phá!

Nếu bạn có thời gian và muốn tìm hiểu sâu hơn về chủ đề này, hãy thử khám phá một số điều sau:

* Kích thước embedding ảnh hưởng đến kết quả như thế nào?
* Các phong cách văn bản khác nhau ảnh hưởng đến kết quả ra sao?
* Lấy một số từ rất khác nhau và các từ đồng nghĩa của chúng, thu được các biểu diễn vector của chúng, áp dụng PCA để giảm số chiều xuống 2, và vẽ chúng trong không gian 2D. Bạn có thấy bất kỳ mẫu nào không?

---

**Tuyên bố miễn trừ trách nhiệm**:  
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng các bản dịch tự động có thể chứa lỗi hoặc không chính xác. Tài liệu gốc bằng ngôn ngữ bản địa nên được coi là nguồn thông tin chính thức. Đối với các thông tin quan trọng, khuyến nghị sử dụng dịch vụ dịch thuật chuyên nghiệp bởi con người. Chúng tôi không chịu trách nhiệm cho bất kỳ sự hiểu lầm hoặc diễn giải sai nào phát sinh từ việc sử dụng bản dịch này.