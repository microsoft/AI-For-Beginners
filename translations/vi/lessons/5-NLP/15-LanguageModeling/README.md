<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "31b46ba1f3aa78578134d4829f88be53",
  "translation_date": "2025-08-29T12:43:01+00:00",
  "source_file": "lessons/5-NLP/15-LanguageModeling/README.md",
  "language_code": "vi"
}
-->
# Mô hình Ngôn ngữ

Các biểu diễn ngữ nghĩa, như Word2Vec và GloVe, thực chất là bước đầu tiên hướng tới **mô hình ngôn ngữ** - tạo ra các mô hình có thể *hiểu* (hoặc *biểu diễn*) bản chất của ngôn ngữ.

## [Câu hỏi trước bài giảng](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/115)

Ý tưởng chính của mô hình ngôn ngữ là huấn luyện chúng trên các tập dữ liệu không gắn nhãn theo cách không giám sát. Điều này rất quan trọng vì chúng ta có một lượng lớn văn bản không gắn nhãn, trong khi lượng văn bản có gắn nhãn luôn bị giới hạn bởi công sức mà chúng ta có thể bỏ ra để gắn nhãn. Thông thường, chúng ta có thể xây dựng các mô hình ngôn ngữ có khả năng **dự đoán các từ bị thiếu** trong văn bản, bởi vì việc che đi một từ ngẫu nhiên trong văn bản và sử dụng nó làm mẫu huấn luyện là khá dễ dàng.

## Huấn luyện Biểu diễn

Trong các ví dụ trước, chúng ta đã sử dụng các biểu diễn ngữ nghĩa được huấn luyện sẵn, nhưng sẽ rất thú vị khi xem cách các biểu diễn này được huấn luyện. Có một số ý tưởng có thể được sử dụng:

* **Mô hình ngôn ngữ N-Gram**, khi chúng ta dự đoán một token bằng cách nhìn vào N token trước đó (N-gram).
* **Continuous Bag-of-Words** (CBoW), khi chúng ta dự đoán token ở giữa $W_0$ trong một chuỗi token $W_{-N}$, ..., $W_N$.
* **Skip-gram**, nơi chúng ta dự đoán một tập hợp các token lân cận {$W_{-N},\dots, W_{-1}, W_1,\dots, W_N$} từ token ở giữa $W_0$.

![hình ảnh từ bài báo về chuyển đổi từ thành vector](../../../../../translated_images/example-algorithms-for-converting-words-to-vectors.fbe9207a726922f6f0f5de66427e8a6eda63809356114e28fb1fa5f4a83ebda7.vi.png)

> Hình ảnh từ [bài báo này](https://arxiv.org/pdf/1301.3781.pdf)

## ✍️ Ví dụ Notebook: Huấn luyện mô hình CBoW

Tiếp tục học tập với các notebook sau:

* [Huấn luyện CBoW Word2Vec với TensorFlow](CBoW-TF.ipynb)
* [Huấn luyện CBoW Word2Vec với PyTorch](CBoW-PyTorch.ipynb)

## Kết luận

Trong bài học trước, chúng ta đã thấy rằng các biểu diễn từ hoạt động như một phép màu! Giờ đây, chúng ta biết rằng việc huấn luyện các biểu diễn từ không phải là một nhiệm vụ quá phức tạp, và chúng ta hoàn toàn có thể tự huấn luyện các biểu diễn từ cho văn bản thuộc lĩnh vực cụ thể nếu cần.

## [Câu hỏi sau bài giảng](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/215)

## Ôn tập & Tự học

* [Hướng dẫn chính thức của PyTorch về Mô hình Ngôn ngữ](https://pytorch.org/tutorials/beginner/nlp/word_embeddings_tutorial.html).
* [Hướng dẫn chính thức của TensorFlow về huấn luyện mô hình Word2Vec](https://www.TensorFlow.org/tutorials/text/word2vec).
* Sử dụng framework **gensim** để huấn luyện các biểu diễn phổ biến nhất chỉ với vài dòng mã được mô tả [trong tài liệu này](https://pytorch.org/tutorials/beginner/nlp/word_embeddings_tutorial.html).

## 🚀 [Bài tập: Huấn luyện Mô hình Skip-Gram](lab/README.md)

Trong phòng thí nghiệm, chúng tôi thách thức bạn chỉnh sửa mã từ bài học này để huấn luyện mô hình skip-gram thay vì CBoW. [Đọc chi tiết](lab/README.md)

---

**Tuyên bố miễn trừ trách nhiệm**:  
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng các bản dịch tự động có thể chứa lỗi hoặc không chính xác. Tài liệu gốc bằng ngôn ngữ bản địa nên được coi là nguồn thông tin chính thức. Đối với các thông tin quan trọng, khuyến nghị sử dụng dịch vụ dịch thuật chuyên nghiệp bởi con người. Chúng tôi không chịu trách nhiệm cho bất kỳ sự hiểu lầm hoặc diễn giải sai nào phát sinh từ việc sử dụng bản dịch này.