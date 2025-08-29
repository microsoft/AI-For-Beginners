<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "e40b47ac3fd48f71304ede1474e66293",
  "translation_date": "2025-08-29T12:48:37+00:00",
  "source_file": "lessons/5-NLP/14-Embeddings/README.md",
  "language_code": "vi"
}
-->
# Nhúng (Embeddings)

## [Câu hỏi trước bài giảng](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/114)

Khi huấn luyện các bộ phân loại dựa trên BoW hoặc TF/IDF, chúng ta làm việc với các vector túi từ (bag-of-words) có chiều cao với độ dài `vocab_size`, và chúng ta đã chuyển đổi rõ ràng từ các vector biểu diễn vị trí có chiều thấp sang biểu diễn one-hot thưa thớt. Tuy nhiên, biểu diễn one-hot này không tiết kiệm bộ nhớ. Ngoài ra, mỗi từ được xử lý độc lập với nhau, tức là các vector mã hóa one-hot không thể hiện bất kỳ sự tương đồng ngữ nghĩa nào giữa các từ.

Ý tưởng của **embedding** là biểu diễn các từ bằng các vector dày đặc có chiều thấp hơn, phản ánh phần nào ý nghĩa ngữ nghĩa của từ. Chúng ta sẽ thảo luận sau về cách xây dựng các nhúng từ có ý nghĩa, nhưng hiện tại hãy chỉ nghĩ về embedding như một cách để giảm chiều của vector từ.

Vì vậy, lớp embedding sẽ nhận một từ làm đầu vào và tạo ra một vector đầu ra với kích thước `embedding_size` được chỉ định. Theo một cách nào đó, nó rất giống với lớp `Linear`, nhưng thay vì nhận một vector mã hóa one-hot, nó có thể nhận số thứ tự của từ làm đầu vào, giúp chúng ta tránh phải tạo ra các vector mã hóa one-hot lớn.

Bằng cách sử dụng lớp embedding làm lớp đầu tiên trong mạng phân loại của chúng ta, chúng ta có thể chuyển từ mô hình túi từ (bag-of-words) sang mô hình **embedding bag**, trong đó chúng ta đầu tiên chuyển đổi mỗi từ trong văn bản thành embedding tương ứng, sau đó tính toán một hàm tổng hợp nào đó trên tất cả các embedding này, chẳng hạn như `sum`, `average` hoặc `max`.

![Hình ảnh minh họa một bộ phân loại embedding cho năm từ trong chuỗi.](../../../../../translated_images/embedding-classifier-example.b77f021a7ee67eeec8e68bfe11636c5b97d6eaa067515a129bfb1d0034b1ac5b.vi.png)

> Hình ảnh của tác giả

## ✍️ Bài tập: Nhúng (Embeddings)

Tiếp tục học trong các sổ tay sau:
* [Embeddings với PyTorch](EmbeddingsPyTorch.ipynb)
* [Embeddings với TensorFlow](EmbeddingsTF.ipynb)

## Nhúng ngữ nghĩa: Word2Vec

Mặc dù lớp embedding học cách ánh xạ các từ thành biểu diễn vector, nhưng biểu diễn này không nhất thiết phải mang nhiều ý nghĩa ngữ nghĩa. Sẽ rất hữu ích nếu học được một biểu diễn vector sao cho các từ tương tự hoặc đồng nghĩa tương ứng với các vector gần nhau theo một khoảng cách vector nào đó (ví dụ: khoảng cách Euclid).

Để làm điều đó, chúng ta cần huấn luyện trước mô hình embedding trên một tập hợp văn bản lớn theo một cách cụ thể. Một cách để huấn luyện nhúng ngữ nghĩa được gọi là [Word2Vec](https://en.wikipedia.org/wiki/Word2vec). Nó dựa trên hai kiến trúc chính được sử dụng để tạo ra biểu diễn phân tán của từ:

 - **Continuous bag-of-words** (CBoW) — trong kiến trúc này, chúng ta huấn luyện mô hình để dự đoán một từ từ ngữ cảnh xung quanh. Với ngram $(W_{-2},W_{-1},W_0,W_1,W_2)$, mục tiêu của mô hình là dự đoán $W_0$ từ $(W_{-2},W_{-1},W_1,W_2)$.
 - **Continuous skip-gram** thì ngược lại với CBoW. Mô hình sử dụng cửa sổ ngữ cảnh xung quanh để dự đoán từ hiện tại.

CBoW nhanh hơn, trong khi skip-gram chậm hơn nhưng làm tốt hơn trong việc biểu diễn các từ ít xuất hiện.

![Hình ảnh minh họa cả hai thuật toán CBoW và Skip-Gram để chuyển đổi từ thành vector.](../../../../../translated_images/example-algorithms-for-converting-words-to-vectors.fbe9207a726922f6f0f5de66427e8a6eda63809356114e28fb1fa5f4a83ebda7.vi.png)

> Hình ảnh từ [bài báo này](https://arxiv.org/pdf/1301.3781.pdf)

Các nhúng Word2Vec đã được huấn luyện trước (cũng như các mô hình tương tự khác như GloVe) cũng có thể được sử dụng thay cho lớp embedding trong mạng nơ-ron. Tuy nhiên, chúng ta cần xử lý các từ vựng, vì từ vựng được sử dụng để huấn luyện trước Word2Vec/GloVe có khả năng khác với từ vựng trong tập văn bản của chúng ta. Hãy xem các sổ tay ở trên để tìm hiểu cách giải quyết vấn đề này.

## Nhúng ngữ cảnh

Một hạn chế chính của các biểu diễn embedding được huấn luyện trước truyền thống như Word2Vec là vấn đề phân biệt nghĩa của từ. Mặc dù các embedding được huấn luyện trước có thể nắm bắt một phần ý nghĩa của từ trong ngữ cảnh, nhưng mọi nghĩa có thể có của một từ đều được mã hóa vào cùng một embedding. Điều này có thể gây ra vấn đề trong các mô hình hạ nguồn, vì nhiều từ như từ 'play' có các nghĩa khác nhau tùy thuộc vào ngữ cảnh mà chúng được sử dụng.

Ví dụ, từ 'play' trong hai câu sau có ý nghĩa khá khác nhau:

- Tôi đã đi xem một **vở kịch** ở nhà hát.
- John muốn **chơi** với bạn bè của mình.

Các embedding được huấn luyện trước ở trên biểu diễn cả hai nghĩa của từ 'play' trong cùng một embedding. Để khắc phục hạn chế này, chúng ta cần xây dựng các embedding dựa trên **mô hình ngôn ngữ**, được huấn luyện trên một tập hợp văn bản lớn và *hiểu* cách các từ có thể được sắp xếp trong các ngữ cảnh khác nhau. Việc thảo luận về nhúng ngữ cảnh nằm ngoài phạm vi của bài học này, nhưng chúng ta sẽ quay lại chúng khi nói về các mô hình ngôn ngữ sau trong khóa học.

## Kết luận

Trong bài học này, bạn đã khám phá cách xây dựng và sử dụng các lớp embedding trong TensorFlow và PyTorch để phản ánh tốt hơn ý nghĩa ngữ nghĩa của từ.

## 🚀 Thử thách

Word2Vec đã được sử dụng cho một số ứng dụng thú vị, bao gồm tạo lời bài hát và thơ. Hãy xem [bài viết này](https://www.politetype.com/blog/word2vec-color-poems) để tìm hiểu cách tác giả sử dụng Word2Vec để tạo thơ. Xem [video này của Dan Shiffmann](https://www.youtube.com/watch?v=LSS_bos_TPI&ab_channel=TheCodingTrain) để khám phá một cách giải thích khác về kỹ thuật này. Sau đó, hãy thử áp dụng các kỹ thuật này vào tập văn bản của riêng bạn, có thể lấy từ Kaggle.

## [Câu hỏi sau bài giảng](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/214)

## Ôn tập & Tự học

Đọc bài báo này về Word2Vec: [Efficient Estimation of Word Representations in Vector Space](https://arxiv.org/pdf/1301.3781.pdf)

## [Bài tập: Sổ tay](assignment.md)

---

**Tuyên bố miễn trừ trách nhiệm**:  
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng các bản dịch tự động có thể chứa lỗi hoặc không chính xác. Tài liệu gốc bằng ngôn ngữ bản địa nên được coi là nguồn thông tin chính thức. Đối với các thông tin quan trọng, nên sử dụng dịch vụ dịch thuật chuyên nghiệp từ con người. Chúng tôi không chịu trách nhiệm cho bất kỳ sự hiểu lầm hoặc diễn giải sai nào phát sinh từ việc sử dụng bản dịch này.