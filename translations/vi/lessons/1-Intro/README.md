<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "5d1cbc67a9690adb5b33adf297794087",
  "translation_date": "2025-08-29T12:32:34+00:00",
  "source_file": "lessons/1-Intro/README.md",
  "language_code": "vi"
}
-->
> Hình ảnh bởi [Dmitry Soshnikov](http://soshnikov.com)

Theo thời gian, tài nguyên tính toán trở nên rẻ hơn và lượng dữ liệu có sẵn ngày càng nhiều, các phương pháp mạng nơ-ron bắt đầu thể hiện hiệu suất vượt trội trong việc cạnh tranh với con người ở nhiều lĩnh vực, chẳng hạn như thị giác máy tính hoặc hiểu giọng nói. Trong thập kỷ qua, thuật ngữ Trí tuệ Nhân tạo thường được sử dụng như một từ đồng nghĩa với Mạng Nơ-ron, vì hầu hết các thành công của AI mà chúng ta nghe đến đều dựa trên chúng.

Chúng ta có thể quan sát cách các phương pháp thay đổi, ví dụ, trong việc tạo ra một chương trình máy tính chơi cờ vua:

* Các chương trình cờ vua ban đầu dựa trên tìm kiếm – chương trình cố gắng ước tính các nước đi có thể của đối thủ trong một số nước đi tiếp theo và chọn nước đi tối ưu dựa trên vị trí tối ưu có thể đạt được trong vài nước đi. Điều này dẫn đến sự phát triển của thuật toán tìm kiếm [alpha-beta pruning](https://en.wikipedia.org/wiki/Alpha%E2%80%93beta_pruning).
* Chiến lược tìm kiếm hoạt động tốt ở cuối ván cờ, nơi không gian tìm kiếm bị giới hạn bởi một số lượng nhỏ các nước đi có thể. Tuy nhiên, ở đầu ván cờ, không gian tìm kiếm rất lớn, và thuật toán có thể được cải thiện bằng cách học từ các trận đấu có sẵn giữa các người chơi. Các thí nghiệm sau đó đã sử dụng phương pháp gọi là [case-based reasoning](https://en.wikipedia.org/wiki/Case-based_reasoning), nơi chương trình tìm kiếm các trường hợp trong cơ sở dữ liệu tương tự với vị trí hiện tại trong ván cờ.
* Các chương trình hiện đại đánh bại người chơi con người dựa trên mạng nơ-ron và [học tăng cường](https://en.wikipedia.org/wiki/Reinforcement_learning), nơi các chương trình học chơi hoàn toàn bằng cách tự chơi với chính mình trong một thời gian dài và học từ những sai lầm của chính mình – giống như cách con người học chơi cờ. Tuy nhiên, một chương trình máy tính có thể chơi nhiều ván hơn trong thời gian ngắn hơn nhiều, và do đó có thể học nhanh hơn.

✅ Hãy nghiên cứu một chút về các trò chơi khác mà AI đã tham gia chơi.

Tương tự, chúng ta có thể thấy cách tiếp cận trong việc tạo ra các “chương trình nói chuyện” (có thể vượt qua bài kiểm tra Turing) đã thay đổi:

* Các chương trình ban đầu thuộc loại này, chẳng hạn như [Eliza](https://en.wikipedia.org/wiki/ELIZA), dựa trên các quy tắc ngữ pháp rất đơn giản và việc tái cấu trúc câu đầu vào thành một câu hỏi.
* Các trợ lý hiện đại, chẳng hạn như Cortana, Siri hoặc Google Assistant, đều là các hệ thống lai sử dụng mạng nơ-ron để chuyển đổi giọng nói thành văn bản và nhận diện ý định của chúng ta, sau đó sử dụng một số lý luận hoặc thuật toán rõ ràng để thực hiện các hành động cần thiết.
* Trong tương lai, chúng ta có thể mong đợi một mô hình hoàn toàn dựa trên mạng nơ-ron để xử lý hội thoại một cách độc lập. Các mạng nơ-ron gần đây như GPT và [Turing-NLG](https://turing.microsoft.com/) đã cho thấy thành công lớn trong lĩnh vực này.

> Hình ảnh của Dmitry Soshnikov, [ảnh](https://unsplash.com/photos/r8LmVbUKgns) bởi [Marina Abrosimova](https://unsplash.com/@abrosimova_marina_foto), Unsplash

## Nghiên cứu AI gần đây

Sự phát triển mạnh mẽ gần đây trong nghiên cứu mạng nơ-ron bắt đầu từ khoảng năm 2010, khi các tập dữ liệu công khai lớn bắt đầu xuất hiện. Một bộ sưu tập hình ảnh khổng lồ mang tên [ImageNet](https://en.wikipedia.org/wiki/ImageNet), chứa khoảng 14 triệu hình ảnh được chú thích, đã khai sinh ra [Cuộc thi Nhận diện Hình ảnh Quy mô Lớn ImageNet](https://image-net.org/challenges/LSVRC/).

![Độ chính xác của ILSVRC](../../../../lessons/1-Intro/images/ilsvrc.gif)

> Hình ảnh của [Dmitry Soshnikov](http://soshnikov.com)

Vào năm 2012, [Mạng Nơ-ron Tích chập](../4-ComputerVision/07-ConvNets/README.md) lần đầu tiên được sử dụng trong phân loại hình ảnh, dẫn đến sự giảm đáng kể trong lỗi phân loại (từ gần 30% xuống còn 16,4%). Đến năm 2015, kiến trúc ResNet từ Microsoft Research đã [đạt được độ chính xác ngang tầm con người](https://doi.org/10.1109/ICCV.2015.123).

Kể từ đó, Mạng Nơ-ron đã thể hiện hiệu quả vượt trội trong nhiều nhiệm vụ:

---

Năm | Đạt được độ chính xác ngang tầm con người
-----|--------
2015 | [Phân loại hình ảnh](https://doi.org/10.1109/ICCV.2015.123)
2016 | [Nhận diện giọng nói hội thoại](https://arxiv.org/abs/1610.05256)
2018 | [Dịch máy tự động](https://arxiv.org/abs/1803.05567) (từ tiếng Trung sang tiếng Anh)
2020 | [Tạo chú thích hình ảnh](https://arxiv.org/abs/2009.13682)

Trong vài năm qua, chúng ta đã chứng kiến những thành công lớn với các mô hình ngôn ngữ lớn, như BERT và GPT-3. Điều này chủ yếu xảy ra nhờ vào lượng lớn dữ liệu văn bản tổng quát có sẵn, cho phép chúng ta huấn luyện các mô hình để nắm bắt cấu trúc và ý nghĩa của văn bản, tiền huấn luyện chúng trên các bộ sưu tập văn bản tổng quát, và sau đó chuyên biệt hóa các mô hình này cho các nhiệm vụ cụ thể hơn. Chúng ta sẽ tìm hiểu thêm về [Xử lý Ngôn ngữ Tự nhiên](../5-NLP/README.md) sau trong khóa học này.

## 🚀 Thử thách

Hãy khám phá trên internet để xác định, theo ý kiến của bạn, AI được sử dụng hiệu quả nhất ở đâu. Có phải trong một ứng dụng bản đồ, một dịch vụ chuyển giọng nói thành văn bản, hay một trò chơi điện tử? Nghiên cứu cách hệ thống đó được xây dựng.

## [Câu hỏi kiểm tra sau bài giảng](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/201)

## Ôn tập & Tự học

Ôn lại lịch sử của AI và ML bằng cách đọc qua [bài học này](https://github.com/microsoft/ML-For-Beginners/tree/main/1-Introduction/2-history-of-ML). Chọn một yếu tố từ bản vẽ phác thảo ở đầu bài học đó hoặc bài học này và nghiên cứu sâu hơn để hiểu bối cảnh văn hóa ảnh hưởng đến sự phát triển của nó.

**Bài tập**: [Game Jam](assignment.md)

---

**Tuyên bố miễn trừ trách nhiệm**:  
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng các bản dịch tự động có thể chứa lỗi hoặc không chính xác. Tài liệu gốc bằng ngôn ngữ bản địa nên được coi là nguồn thông tin chính thức. Đối với các thông tin quan trọng, khuyến nghị sử dụng dịch vụ dịch thuật chuyên nghiệp bởi con người. Chúng tôi không chịu trách nhiệm cho bất kỳ sự hiểu lầm hoặc diễn giải sai nào phát sinh từ việc sử dụng bản dịch này.