# Thuật toán Di truyền

## [Câu hỏi trước bài giảng](https://ff-quizzes.netlify.app/en/ai/quiz/41)

**Thuật toán Di truyền** (GA) dựa trên một **phương pháp tiến hóa** trong AI, trong đó các phương pháp tiến hóa của một quần thể được sử dụng để tìm ra giải pháp tối ưu cho một vấn đề cụ thể. Chúng được đề xuất vào năm 1975 bởi [John Henry Holland](https://wikipedia.org/wiki/John_Henry_Holland).

Thuật toán Di truyền dựa trên các ý tưởng sau:

* Các giải pháp hợp lệ cho vấn đề có thể được biểu diễn dưới dạng **gen**
* **Lai ghép** cho phép chúng ta kết hợp hai giải pháp lại với nhau để tạo ra một giải pháp hợp lệ mới
* **Chọn lọc** được sử dụng để chọn các giải pháp tối ưu hơn bằng cách sử dụng một **hàm đánh giá**
* **Đột biến** được giới thiệu để làm mất ổn định tối ưu hóa và giúp thoát khỏi cực tiểu cục bộ

Nếu bạn muốn triển khai một Thuật toán Di truyền, bạn cần:

 * Tìm một phương pháp mã hóa các giải pháp của vấn đề bằng **gen** g&in;&Gamma;
 * Trên tập hợp các gen &Gamma;, cần định nghĩa **hàm đánh giá** fit: &Gamma;&rightarrow;**R**. Giá trị hàm càng nhỏ thì giải pháp càng tốt.
 * Định nghĩa cơ chế **lai ghép** để kết hợp hai gen lại với nhau và tạo ra một giải pháp hợp lệ mới crossover: &Gamma;<sup>2</sub>&rightarrow;&Gamma;.
 * Định nghĩa cơ chế **đột biến** mutate: &Gamma;&rightarrow;&Gamma;.

Trong nhiều trường hợp, lai ghép và đột biến là các thuật toán khá đơn giản để thao tác với gen dưới dạng chuỗi số hoặc vector bit.

Việc triển khai cụ thể của một thuật toán di truyền có thể thay đổi tùy từng trường hợp, nhưng cấu trúc tổng thể như sau:

1. Chọn một quần thể ban đầu G&subset;&Gamma;
2. Ngẫu nhiên chọn một trong các thao tác sẽ được thực hiện ở bước này: lai ghép hoặc đột biến
3. **Lai ghép**:
  * Ngẫu nhiên chọn hai gen g<sub>1</sub>, g<sub>2</sub> &in; G
  * Tính toán lai ghép g=crossover(g<sub>1</sub>,g<sub>2</sub>)
  * Nếu fit(g)<fit(g<sub>1</sub>) hoặc fit(g)<fit(g<sub>2</sub>) - thay thế gen tương ứng trong quần thể bằng g.
4. **Đột biến** - chọn ngẫu nhiên một gen g&in;G và thay thế nó bằng mutate(g)
5. Lặp lại từ bước 2, cho đến khi đạt được giá trị đủ nhỏ của fit, hoặc cho đến khi đạt giới hạn số bước.

## Các Nhiệm vụ Điển hình

Các nhiệm vụ thường được giải quyết bằng Thuật toán Di truyền bao gồm:

1. Tối ưu hóa lịch trình
1. Đóng gói tối ưu
1. Cắt tối ưu
1. Tăng tốc tìm kiếm toàn diện

## ✍️ Bài tập: Thuật toán Di truyền

Tiếp tục học trong các notebook sau:

Truy cập [notebook này](Genetic.ipynb) để xem hai ví dụ về việc sử dụng Thuật toán Di truyền:

1. Phân chia kho báu công bằng
1. Bài toán 8 quân hậu

## Kết luận

Thuật toán Di truyền được sử dụng để giải quyết nhiều vấn đề, bao gồm các vấn đề về logistics và tìm kiếm. Lĩnh vực này được lấy cảm hứng từ nghiên cứu kết hợp các chủ đề trong Tâm lý học và Khoa học Máy tính.

## 🚀 Thử thách

"Thuật toán di truyền dễ triển khai, nhưng hành vi của chúng rất khó hiểu." [nguồn](https://wikipedia.org/wiki/Genetic_algorithm) Hãy nghiên cứu để tìm một triển khai của thuật toán di truyền, chẳng hạn như giải một câu đố Sudoku, và giải thích cách nó hoạt động dưới dạng phác thảo hoặc sơ đồ luồng.

## [Câu hỏi sau bài giảng](https://ff-quizzes.netlify.app/en/ai/quiz/42)

## Ôn tập & Tự học

Xem [video tuyệt vời này](https://www.youtube.com/watch?v=qv6UVOQ0F44) nói về cách máy tính có thể học chơi Super Mario bằng mạng nơ-ron được huấn luyện bởi thuật toán di truyền. Chúng ta sẽ tìm hiểu thêm về việc máy tính học chơi các trò chơi như vậy [trong phần tiếp theo](../22-DeepRL/README.md).

## [Bài tập: Phương trình Diophantine](Diophantine.ipynb)

Mục tiêu của bạn là giải quyết cái gọi là **phương trình Diophantine** - một phương trình có nghiệm nguyên. Ví dụ, hãy xem xét phương trình a+2b+3c+4d=30. Bạn cần tìm các nghiệm nguyên thỏa mãn phương trình này.

*Bài tập này được lấy cảm hứng từ [bài viết này](https://habr.com/post/128704/).*

Gợi ý:

1. Bạn có thể xem xét các nghiệm trong khoảng [0;30]
1. Là một gen, hãy xem xét sử dụng danh sách các giá trị nghiệm

Sử dụng [Diophantine.ipynb](Diophantine.ipynb) làm điểm bắt đầu.

---

