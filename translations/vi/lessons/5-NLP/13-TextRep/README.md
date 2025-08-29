<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "4522e22e150be0845e03aa41209a39d5",
  "translation_date": "2025-08-29T12:49:45+00:00",
  "source_file": "lessons/5-NLP/13-TextRep/README.md",
  "language_code": "vi"
}
-->
# Biểu Diễn Văn Bản Dưới Dạng Tensor

## [Câu hỏi trước bài giảng](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/113)

## Phân Loại Văn Bản

Trong phần đầu của chương này, chúng ta sẽ tập trung vào nhiệm vụ **phân loại văn bản**. Chúng ta sẽ sử dụng Bộ Dữ Liệu [AG News](https://www.kaggle.com/amananandrai/ag-news-classification-dataset), bao gồm các bài báo như sau:

* Danh mục: Khoa học/Công nghệ  
* Tiêu đề: Công ty Ky. Nhận Được Tài Trợ Để Nghiên Cứu Peptide (AP)  
* Nội dung: AP - Một công ty được thành lập bởi một nhà nghiên cứu hóa học tại Đại học Louisville đã nhận được tài trợ để phát triển...

Mục tiêu của chúng ta là phân loại bài báo vào một trong các danh mục dựa trên văn bản.

## Biểu Diễn Văn Bản

Nếu chúng ta muốn giải quyết các nhiệm vụ Xử Lý Ngôn Ngữ Tự Nhiên (NLP) bằng mạng nơ-ron, chúng ta cần một cách để biểu diễn văn bản dưới dạng tensor. Máy tính đã biểu diễn các ký tự văn bản dưới dạng số, được ánh xạ tới các phông chữ trên màn hình của bạn bằng các mã hóa như ASCII hoặc UTF-8.

<img alt="Hình ảnh minh họa sơ đồ ánh xạ một ký tự sang biểu diễn ASCII và nhị phân" src="images/ascii-character-map.png" width="50%"/>

> [Nguồn hình ảnh](https://www.seobility.net/en/wiki/ASCII)

Là con người, chúng ta hiểu mỗi chữ cái **đại diện** cho điều gì, và cách các ký tự kết hợp lại để tạo thành từ trong câu. Tuy nhiên, máy tính không tự hiểu được điều này, và mạng nơ-ron phải học ý nghĩa trong quá trình huấn luyện.

Do đó, chúng ta có thể sử dụng các cách tiếp cận khác nhau để biểu diễn văn bản:

* **Biểu diễn cấp ký tự**, khi chúng ta biểu diễn văn bản bằng cách coi mỗi ký tự là một số. Giả sử chúng ta có *C* ký tự khác nhau trong tập văn bản, từ *Hello* sẽ được biểu diễn bằng tensor 5x*C*. Mỗi chữ cái sẽ tương ứng với một cột tensor trong mã hóa one-hot.  
* **Biểu diễn cấp từ**, trong đó chúng ta tạo một **từ vựng** của tất cả các từ trong văn bản, sau đó biểu diễn từ bằng mã hóa one-hot. Cách tiếp cận này tốt hơn ở một mức độ nào đó, vì mỗi chữ cái tự nó không mang nhiều ý nghĩa, và bằng cách sử dụng các khái niệm ngữ nghĩa cao hơn - từ - chúng ta đơn giản hóa nhiệm vụ cho mạng nơ-ron. Tuy nhiên, với kích thước từ điển lớn, chúng ta cần xử lý các tensor thưa có kích thước cao.

Dù sử dụng cách biểu diễn nào, trước tiên chúng ta cần chuyển đổi văn bản thành một chuỗi **token**, mỗi token có thể là một ký tự, một từ, hoặc đôi khi là một phần của từ. Sau đó, chúng ta chuyển đổi token thành một số, thường sử dụng **từ vựng**, và số này có thể được đưa vào mạng nơ-ron bằng mã hóa one-hot.

## N-Grams

Trong ngôn ngữ tự nhiên, ý nghĩa chính xác của từ chỉ có thể được xác định trong ngữ cảnh. Ví dụ, ý nghĩa của *mạng nơ-ron* và *mạng đánh cá* hoàn toàn khác nhau. Một trong những cách để tính đến điều này là xây dựng mô hình dựa trên các cặp từ, và coi các cặp từ như các token từ vựng riêng biệt. Theo cách này, câu *Tôi thích đi câu cá* sẽ được biểu diễn bằng chuỗi token sau: *Tôi thích*, *thích đi*, *đi câu*, *câu cá*. Vấn đề với cách tiếp cận này là kích thước từ điển tăng đáng kể, và các tổ hợp như *đi câu* và *đi mua sắm* được biểu diễn bằng các token khác nhau, không chia sẻ bất kỳ sự tương đồng ngữ nghĩa nào mặc dù cùng động từ.

Trong một số trường hợp, chúng ta có thể xem xét sử dụng tri-grams -- tổ hợp ba từ -- nữa. Do đó, cách tiếp cận này thường được gọi là **n-grams**. Ngoài ra, cũng hợp lý khi sử dụng n-grams với biểu diễn cấp ký tự, trong trường hợp này n-grams sẽ tương ứng với các âm tiết khác nhau.

## Bag-of-Words và TF/IDF

Khi giải quyết các nhiệm vụ như phân loại văn bản, chúng ta cần có khả năng biểu diễn văn bản bằng một vector kích thước cố định, vector này sẽ được sử dụng làm đầu vào cho bộ phân loại dày đặc cuối cùng. Một trong những cách đơn giản nhất để làm điều đó là kết hợp tất cả các biểu diễn từ riêng lẻ, ví dụ bằng cách cộng chúng lại. Nếu chúng ta cộng các mã hóa one-hot của từng từ, chúng ta sẽ có một vector tần suất, cho thấy mỗi từ xuất hiện bao nhiêu lần trong văn bản. Biểu diễn văn bản như vậy được gọi là **bag of words** (BoW).

<img src="images/bow.png" width="90%"/>

> Hình ảnh của tác giả

BoW về cơ bản biểu diễn những từ nào xuất hiện trong văn bản và với số lượng bao nhiêu, điều này thực sự có thể là một chỉ báo tốt về nội dung của văn bản. Ví dụ, một bài báo về chính trị có khả năng chứa các từ như *tổng thống* và *quốc gia*, trong khi một bài báo khoa học có thể có các từ như *máy gia tốc*, *phát hiện*, v.v. Do đó, tần suất từ trong nhiều trường hợp có thể là một chỉ báo tốt về nội dung văn bản.

Vấn đề với BoW là một số từ phổ biến, như *và*, *là*, v.v. xuất hiện trong hầu hết các văn bản, và chúng có tần suất cao nhất, làm lu mờ các từ thực sự quan trọng. Chúng ta có thể giảm tầm quan trọng của những từ này bằng cách tính đến tần suất xuất hiện của chúng trong toàn bộ tập hợp văn bản. Đây là ý tưởng chính đằng sau phương pháp TF/IDF, được trình bày chi tiết hơn trong các sổ tay đính kèm bài học này.

Tuy nhiên, không có phương pháp nào trong số này có thể hoàn toàn tính đến **ngữ nghĩa** của văn bản. Chúng ta cần các mô hình mạng nơ-ron mạnh mẽ hơn để làm điều này, điều mà chúng ta sẽ thảo luận sau trong chương này.

## ✍️ Bài Tập: Biểu Diễn Văn Bản

Tiếp tục học trong các sổ tay sau:

* [Biểu Diễn Văn Bản với PyTorch](TextRepresentationPyTorch.ipynb)  
* [Biểu Diễn Văn Bản với TensorFlow](TextRepresentationTF.ipynb)  

## Kết Luận

Cho đến nay, chúng ta đã nghiên cứu các kỹ thuật có thể thêm trọng số tần suất cho các từ khác nhau. Tuy nhiên, chúng không thể biểu diễn ý nghĩa hoặc thứ tự. Như nhà ngôn ngữ học nổi tiếng J. R. Firth đã nói vào năm 1935, "Ý nghĩa đầy đủ của một từ luôn mang tính ngữ cảnh, và không có nghiên cứu nào về ý nghĩa mà không tính đến ngữ cảnh có thể được coi là nghiêm túc." Chúng ta sẽ học cách nắm bắt thông tin ngữ cảnh từ văn bản bằng cách sử dụng mô hình ngôn ngữ trong các phần sau của khóa học.

## 🚀 Thử Thách

Thử một số bài tập khác sử dụng bag-of-words và các mô hình dữ liệu khác nhau. Bạn có thể lấy cảm hứng từ [cuộc thi này trên Kaggle](https://www.kaggle.com/competitions/word2vec-nlp-tutorial/overview/part-1-for-beginners-bag-of-words)

## [Câu hỏi sau bài giảng](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/213)

## Ôn Tập & Tự Học

Luyện tập kỹ năng của bạn với các kỹ thuật nhúng văn bản và bag-of-words trên [Microsoft Learn](https://docs.microsoft.com/learn/modules/intro-natural-language-processing-pytorch/?WT.mc_id=academic-77998-cacaste)

## [Bài Tập: Sổ Tay](assignment.md)  

---

**Tuyên bố miễn trừ trách nhiệm**:  
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng các bản dịch tự động có thể chứa lỗi hoặc không chính xác. Tài liệu gốc bằng ngôn ngữ bản địa nên được coi là nguồn thông tin chính thức. Đối với các thông tin quan trọng, khuyến nghị sử dụng dịch vụ dịch thuật chuyên nghiệp bởi con người. Chúng tôi không chịu trách nhiệm cho bất kỳ sự hiểu lầm hoặc diễn giải sai nào phát sinh từ việc sử dụng bản dịch này.