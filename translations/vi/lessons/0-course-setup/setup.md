<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "c4c545eb30765a49469ced84cfb4379f",
  "translation_date": "2025-08-29T12:17:02+00:00",
  "source_file": "lessons/0-course-setup/setup.md",
  "language_code": "vi"
}
-->
# Bắt đầu với chương trình học này

## Bạn là sinh viên?

Hãy bắt đầu với các tài nguyên sau:

* [Trang Hub dành cho sinh viên](https://docs.microsoft.com/learn/student-hub?WT.mc_id=academic-77998-cacaste) Trên trang này, bạn sẽ tìm thấy các tài nguyên dành cho người mới bắt đầu, các gói hỗ trợ cho sinh viên, và thậm chí là cách để nhận voucher chứng chỉ miễn phí. Đây là một trang bạn nên đánh dấu và kiểm tra thường xuyên vì nội dung được cập nhật ít nhất hàng tháng.
* [Đại sứ học tập Microsoft Student](https://studentambassadors.microsoft.com?WT.mc_id=academic-77998-cacaste) Tham gia cộng đồng đại sứ sinh viên toàn cầu, đây có thể là con đường dẫn bạn đến với Microsoft.

**Sinh viên**, có một vài cách để sử dụng chương trình học này. Trước tiên, bạn có thể chỉ cần đọc văn bản và xem qua mã nguồn trực tiếp trên GitHub. Nếu bạn muốn chạy mã trong bất kỳ notebook nào - [đọc hướng dẫn của chúng tôi](./etc/how-to-run.md), và tìm thêm lời khuyên về cách thực hiện [trong bài viết blog này](https://soshnikov.com/education/how-to-execute-notebooks-from-github/).

> **Note**: [Hướng dẫn cách chạy mã trong chương trình học này](./how-to-run.md)

## Tự học

Tuy nhiên, nếu bạn muốn học khóa học này như một dự án tự học, chúng tôi gợi ý bạn fork toàn bộ repo vào tài khoản GitHub của mình và hoàn thành các bài tập một mình hoặc cùng nhóm:

* Bắt đầu với bài kiểm tra trước bài giảng.
* Đọc phần giới thiệu cho bài giảng.
* Nếu bài giảng có các notebook bổ sung, hãy xem qua chúng, đọc và chạy mã. Nếu có cả notebook TensorFlow và PyTorch, bạn có thể tập trung vào một trong hai - chọn framework yêu thích của bạn.
* Các notebook thường chứa một số thử thách yêu cầu bạn chỉnh sửa mã một chút để thử nghiệm.
* Làm bài kiểm tra sau bài giảng.
* Nếu có bài lab đi kèm với module - hoàn thành bài tập.
* Tham gia [Bảng thảo luận](https://github.com/microsoft/AI-For-Beginners/discussions) để "học hỏi công khai".

> Để học thêm, chúng tôi khuyến nghị bạn theo dõi các module và lộ trình học [Microsoft Learn](https://docs.microsoft.com/en-us/users/dmitrysoshnikov-9132/collections/31zgizg2p418yo/?WT.mc_id=academic-77998-cacaste).

**Giáo viên**, chúng tôi đã [bao gồm một số gợi ý](/for-teachers.md) về cách sử dụng chương trình học này.

---

## Phương pháp giảng dạy

Chúng tôi đã chọn hai nguyên tắc giảng dạy khi xây dựng chương trình học này: đảm bảo rằng nó mang tính thực hành **dựa trên dự án** và bao gồm **các bài kiểm tra thường xuyên**.

Bằng cách đảm bảo nội dung gắn liền với các dự án, quá trình học trở nên hấp dẫn hơn đối với sinh viên và khả năng ghi nhớ các khái niệm sẽ được tăng cường. Ngoài ra, một bài kiểm tra với mức độ áp lực thấp trước lớp học sẽ giúp sinh viên tập trung vào việc học một chủ đề, trong khi bài kiểm tra thứ hai sau lớp học sẽ đảm bảo khả năng ghi nhớ lâu hơn. Chương trình học này được thiết kế linh hoạt và thú vị, có thể học toàn bộ hoặc từng phần. Các dự án bắt đầu từ nhỏ và trở nên phức tạp hơn vào cuối chu kỳ 12 tuần.

> **Lưu ý về các bài kiểm tra**: Tất cả các bài kiểm tra được chứa [trong ứng dụng này](https://red-field-0a6ddfd03.1.azurestaticapps.net/), với tổng cộng 50 bài kiểm tra, mỗi bài gồm ba câu hỏi. Chúng được liên kết từ trong các bài học nhưng ứng dụng kiểm tra có thể chạy cục bộ; làm theo hướng dẫn trong thư mục `etc/quiz-app`.

## Truy cập ngoại tuyến

Bạn có thể chạy tài liệu này ngoại tuyến bằng cách sử dụng [Docsify](https://docsify.js.org/#/). Fork repo này, [cài đặt Docsify](https://docsify.js.org/#/quickstart) trên máy của bạn, và sau đó trong thư mục gốc của repo này, gõ `docsify serve`. Website sẽ được phục vụ trên cổng 3000 trên localhost của bạn: `localhost:3000`. Một tệp pdf của chương trình học có sẵn [tại liên kết này](../../../../../../../../../etc/pdf/readme.pdf).

---

**Tuyên bố miễn trừ trách nhiệm**:  
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng các bản dịch tự động có thể chứa lỗi hoặc không chính xác. Tài liệu gốc bằng ngôn ngữ bản địa nên được coi là nguồn tham khảo chính thức. Đối với các thông tin quan trọng, chúng tôi khuyến nghị sử dụng dịch vụ dịch thuật chuyên nghiệp từ con người. Chúng tôi không chịu trách nhiệm cho bất kỳ sự hiểu lầm hoặc diễn giải sai nào phát sinh từ việc sử dụng bản dịch này.