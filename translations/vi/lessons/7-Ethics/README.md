# AI Đạo Đức và Trách Nhiệm

Bạn đã gần hoàn thành khóa học này, và tôi hy vọng rằng đến thời điểm này bạn đã thấy rõ rằng AI dựa trên một số phương pháp toán học chính thức cho phép chúng ta tìm ra mối quan hệ trong dữ liệu và huấn luyện các mô hình để tái tạo một số khía cạnh của hành vi con người. Tại thời điểm lịch sử này, chúng ta coi AI là một công cụ rất mạnh mẽ để trích xuất các mẫu từ dữ liệu và áp dụng các mẫu đó để giải quyết các vấn đề mới.

## [Câu hỏi trước bài giảng](https://white-water-09ec41f0f.azurestaticapps.net/quiz/5/)

Tuy nhiên, trong khoa học viễn tưởng, chúng ta thường thấy những câu chuyện mà AI gây nguy hiểm cho nhân loại. Thông thường, những câu chuyện này xoay quanh một loại "cuộc nổi loạn của AI", khi AI quyết định đối đầu với con người. Điều này ngụ ý rằng AI có một loại cảm xúc hoặc có thể đưa ra các quyết định không lường trước được bởi các nhà phát triển.

Loại AI mà chúng ta đã học trong khóa học này không gì khác ngoài các phép toán ma trận lớn. Đây là một công cụ rất mạnh mẽ để giúp chúng ta giải quyết các vấn đề, và giống như bất kỳ công cụ mạnh mẽ nào khác - nó có thể được sử dụng cho mục đích tốt và xấu. Quan trọng hơn, nó có thể bị *lạm dụng*.

## Nguyên tắc AI Trách Nhiệm

Để tránh việc lạm dụng AI một cách vô tình hoặc có chủ đích, Microsoft đã đưa ra các [Nguyên tắc AI Trách Nhiệm](https://www.microsoft.com/ai/responsible-ai?WT.mc_id=academic-77998-cacaste). Các khái niệm sau đây là nền tảng của các nguyên tắc này:

* **Công bằng** liên quan đến vấn đề quan trọng về *thiên vị mô hình*, có thể xảy ra khi sử dụng dữ liệu thiên vị để huấn luyện. Ví dụ, khi chúng ta cố gắng dự đoán khả năng một người nhận được công việc lập trình viên, mô hình có thể ưu tiên nam giới hơn - chỉ vì tập dữ liệu huấn luyện có thể đã thiên về đối tượng nam giới. Chúng ta cần cân bằng dữ liệu huấn luyện một cách cẩn thận và điều tra mô hình để tránh thiên vị, đồng thời đảm bảo rằng mô hình xem xét các đặc điểm liên quan hơn.
* **Độ tin cậy và an toàn**. Theo bản chất, các mô hình AI có thể mắc sai lầm. Một mạng nơ-ron trả về các xác suất, và chúng ta cần tính đến điều này khi đưa ra quyết định. Mỗi mô hình đều có độ chính xác và độ hồi tưởng nhất định, và chúng ta cần hiểu điều đó để ngăn chặn những tổn hại mà lời khuyên sai lầm có thể gây ra.
* **Quyền riêng tư và bảo mật** có một số tác động cụ thể đối với AI. Ví dụ, khi chúng ta sử dụng một số dữ liệu để huấn luyện mô hình, dữ liệu này bằng cách nào đó trở thành "tích hợp" vào mô hình. Một mặt, điều này tăng cường bảo mật và quyền riêng tư, mặt khác - chúng ta cần nhớ dữ liệu nào đã được sử dụng để huấn luyện mô hình.
* **Tính bao gồm** có nghĩa là chúng ta không xây dựng AI để thay thế con người, mà là để hỗ trợ con người và làm cho công việc của chúng ta sáng tạo hơn. Điều này cũng liên quan đến tính công bằng, bởi vì khi xử lý các cộng đồng ít được đại diện, hầu hết các tập dữ liệu chúng ta thu thập có khả năng bị thiên vị, và chúng ta cần đảm bảo rằng các cộng đồng đó được bao gồm và xử lý đúng cách bởi AI.
* **Tính minh bạch**. Điều này bao gồm việc đảm bảo rằng chúng ta luôn rõ ràng về việc AI đang được sử dụng. Ngoài ra, bất cứ khi nào có thể, chúng ta muốn sử dụng các hệ thống AI có thể *giải thích được*.
* **Trách nhiệm**. Khi các mô hình AI đưa ra một số quyết định, không phải lúc nào cũng rõ ai chịu trách nhiệm cho những quyết định đó. Chúng ta cần đảm bảo rằng chúng ta hiểu trách nhiệm của các quyết định AI nằm ở đâu. Trong hầu hết các trường hợp, chúng ta muốn đưa con người vào quy trình đưa ra các quyết định quan trọng, để những người thực sự chịu trách nhiệm.

## Công cụ cho AI Trách Nhiệm

Microsoft đã phát triển [Responsible AI Toolbox](https://github.com/microsoft/responsible-ai-toolbox) bao gồm một bộ công cụ:

* Bảng điều khiển Giải thích (InterpretML)
* Bảng điều khiển Công bằng (FairLearn)
* Bảng điều khiển Phân tích Lỗi
* Bảng điều khiển AI Trách Nhiệm bao gồm:

   - EconML - công cụ Phân tích Nhân quả, tập trung vào các câu hỏi "nếu như"
   - DiCE - công cụ Phân tích Phản thực cho phép bạn thấy những đặc điểm nào cần thay đổi để ảnh hưởng đến quyết định của mô hình

Để biết thêm thông tin về Đạo Đức AI, vui lòng truy cập [bài học này](https://github.com/microsoft/ML-For-Beginners/tree/main/1-Introduction/3-fairness?WT.mc_id=academic-77998-cacaste) trong Giáo trình Học máy, bao gồm các bài tập.

## Ôn tập & Tự học

Tham gia [Lộ trình học tập này](https://docs.microsoft.com/learn/modules/responsible-ai-principles/?WT.mc_id=academic-77998-cacaste) để tìm hiểu thêm về AI trách nhiệm.

## [Câu hỏi sau bài giảng](https://white-water-09ec41f0f.azurestaticapps.net/quiz/6/)

---

**Tuyên bố miễn trừ trách nhiệm**:  
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng các bản dịch tự động có thể chứa lỗi hoặc không chính xác. Tài liệu gốc bằng ngôn ngữ bản địa nên được coi là nguồn thông tin chính thức. Đối với các thông tin quan trọng, khuyến nghị sử dụng dịch vụ dịch thuật chuyên nghiệp bởi con người. Chúng tôi không chịu trách nhiệm cho bất kỳ sự hiểu lầm hoặc diễn giải sai nào phát sinh từ việc sử dụng bản dịch này.