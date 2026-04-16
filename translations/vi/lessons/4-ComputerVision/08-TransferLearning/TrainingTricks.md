# Các Mẹo Huấn Luyện Deep Learning

Khi mạng nơ-ron trở nên sâu hơn, quá trình huấn luyện chúng ngày càng trở nên thách thức hơn. Một vấn đề lớn là [gradient biến mất](https://en.wikipedia.org/wiki/Vanishing_gradient_problem) hoặc [gradient bùng nổ](https://deepai.org/machine-learning-glossary-and-terms/exploding-gradient-problem#:~:text=Exploding%20gradients%20are%20a%20problem,updates%20are%20small%20and%20controlled.). [Bài viết này](https://towardsdatascience.com/the-vanishing-exploding-gradient-problem-in-deep-neural-networks-191358470c11) cung cấp một giới thiệu tốt về các vấn đề này.

Để làm cho việc huấn luyện mạng sâu hiệu quả hơn, có một số kỹ thuật có thể được sử dụng.

## Giữ giá trị trong khoảng hợp lý

Để làm cho các tính toán số học ổn định hơn, chúng ta cần đảm bảo rằng tất cả các giá trị trong mạng nơ-ron nằm trong một phạm vi hợp lý, thường là [-1..1] hoặc [0..1]. Đây không phải là một yêu cầu quá nghiêm ngặt, nhưng bản chất của các phép tính số thực là các giá trị có độ lớn khác nhau không thể được xử lý chính xác cùng nhau. Ví dụ, nếu chúng ta cộng 10<sup>-10</sup> và 10<sup>10</sup>, kết quả có khả năng là 10<sup>10</sup>, vì giá trị nhỏ hơn sẽ bị "chuyển đổi" sang cùng bậc với giá trị lớn hơn, và do đó phần mantissa sẽ bị mất.

Hầu hết các hàm kích hoạt có tính phi tuyến trong khoảng [-1..1], do đó việc chuẩn hóa tất cả dữ liệu đầu vào về khoảng [-1..1] hoặc [0..1] là hợp lý.

## Khởi tạo trọng số ban đầu

Lý tưởng nhất, chúng ta muốn các giá trị nằm trong cùng một phạm vi sau khi đi qua các lớp của mạng. Vì vậy, việc khởi tạo trọng số sao cho phân phối giá trị được bảo toàn là rất quan trọng.

Phân phối chuẩn **N(0,1)** không phải là một ý tưởng tốt, vì nếu chúng ta có *n* đầu vào, độ lệch chuẩn của đầu ra sẽ là *n*, và các giá trị có khả năng vượt ra ngoài khoảng [0..1].

Các phương pháp khởi tạo thường được sử dụng bao gồm:

- Phân phối đều -- `uniform`
- **N(0,1/n)** -- `gaussian`
- **N(0,1/√n_in)** đảm bảo rằng với đầu vào có trung bình bằng 0 và độ lệch chuẩn bằng 1, trung bình và độ lệch chuẩn sẽ được giữ nguyên
- **N(0,√2/(n_in+n_out))** -- được gọi là **Xavier initialization** (`glorot`), giúp giữ tín hiệu trong phạm vi trong cả quá trình lan truyền xuôi và ngược

## Chuẩn hóa theo lô (Batch Normalization)

Ngay cả khi đã khởi tạo trọng số đúng cách, trọng số có thể trở nên quá lớn hoặc quá nhỏ trong quá trình huấn luyện, khiến tín hiệu vượt ra ngoài phạm vi hợp lý. Chúng ta có thể đưa tín hiệu trở lại bằng cách sử dụng một trong các kỹ thuật **chuẩn hóa**. Mặc dù có nhiều kỹ thuật (Chuẩn hóa trọng số, Chuẩn hóa lớp), kỹ thuật được sử dụng phổ biến nhất là Chuẩn hóa theo lô.

Ý tưởng của **chuẩn hóa theo lô** là xem xét tất cả các giá trị trong một minibatch và thực hiện chuẩn hóa (tức là trừ đi trung bình và chia cho độ lệch chuẩn) dựa trên các giá trị đó. Nó được triển khai như một lớp mạng thực hiện chuẩn hóa này sau khi áp dụng trọng số, nhưng trước khi áp dụng hàm kích hoạt. Kết quả là, chúng ta có khả năng đạt được độ chính xác cao hơn và huấn luyện nhanh hơn.

Đây là [bài báo gốc](https://arxiv.org/pdf/1502.03167.pdf) về chuẩn hóa theo lô, [giải thích trên Wikipedia](https://en.wikipedia.org/wiki/Batch_normalization), và [một bài viết giới thiệu hay](https://towardsdatascience.com/batch-normalization-in-3-levels-of-understanding-14c2da90a338) (và một bài viết [bằng tiếng Nga](https://habrahabr.ru/post/309302/)).

## Dropout

**Dropout** là một kỹ thuật thú vị loại bỏ một tỷ lệ phần trăm nhất định các nơ-ron ngẫu nhiên trong quá trình huấn luyện. Nó cũng được triển khai như một lớp với một tham số (tỷ lệ phần trăm nơ-ron bị loại bỏ, thường là 10%-50%), và trong quá trình huấn luyện, nó đặt giá trị 0 cho các phần tử ngẫu nhiên của vector đầu vào trước khi chuyển chúng sang lớp tiếp theo.

Mặc dù nghe có vẻ kỳ lạ, bạn có thể thấy hiệu quả của dropout khi huấn luyện bộ phân loại chữ số MNIST trong notebook [`Dropout.ipynb`](Dropout.ipynb). Nó tăng tốc độ huấn luyện và cho phép đạt được độ chính xác cao hơn trong ít epoch hơn.

Hiệu ứng này có thể được giải thích theo nhiều cách:

- Nó có thể được coi là một yếu tố gây "sốc" ngẫu nhiên cho mô hình, giúp tối ưu hóa thoát khỏi cực tiểu cục bộ
- Nó có thể được coi là *trung bình mô hình ngầm định*, vì trong quá trình dropout, chúng ta đang huấn luyện các mô hình hơi khác nhau

> *Một số người nói rằng khi một người say rượu cố gắng học điều gì đó, họ sẽ nhớ tốt hơn vào sáng hôm sau so với một người tỉnh táo, vì não với một số nơ-ron không hoạt động cố gắng thích nghi tốt hơn để nắm bắt ý nghĩa. Chúng tôi chưa bao giờ kiểm chứng điều này có đúng hay không.*

## Ngăn chặn overfitting

Một khía cạnh rất quan trọng của deep learning là khả năng ngăn chặn [overfitting](../../3-NeuralNetworks/05-Frameworks/Overfitting.md). Mặc dù có thể rất hấp dẫn khi sử dụng một mô hình mạng nơ-ron rất mạnh, chúng ta luôn cần cân bằng số lượng tham số của mô hình với số lượng mẫu huấn luyện.

> Hãy đảm bảo rằng bạn hiểu khái niệm [overfitting](../../3-NeuralNetworks/05-Frameworks/Overfitting.md) mà chúng ta đã giới thiệu trước đó!

Có một số cách để ngăn chặn overfitting:

- Dừng sớm (Early stopping) -- liên tục theo dõi lỗi trên tập kiểm tra và dừng huấn luyện khi lỗi kiểm tra bắt đầu tăng.
- Suy giảm trọng số rõ ràng / Regularization -- thêm một hình phạt bổ sung vào hàm mất mát cho các giá trị tuyệt đối cao của trọng số, giúp mô hình tránh được các kết quả không ổn định.
- Trung bình mô hình -- huấn luyện nhiều mô hình và sau đó lấy trung bình kết quả. Điều này giúp giảm thiểu phương sai.
- Dropout (Trung bình mô hình ngầm định)

## Bộ tối ưu hóa / Thuật toán huấn luyện

Một khía cạnh quan trọng khác của huấn luyện là chọn thuật toán huấn luyện tốt. Mặc dù **gradient descent** cổ điển là một lựa chọn hợp lý, đôi khi nó có thể quá chậm hoặc dẫn đến các vấn đề khác.

Trong deep learning, chúng ta sử dụng **Stochastic Gradient Descent** (SGD), là gradient descent được áp dụng cho các minibatch được chọn ngẫu nhiên từ tập huấn luyện. Trọng số được điều chỉnh theo công thức:

w<sup>t+1</sup> = w<sup>t</sup> - η∇ℒ

### Momentum

Trong **momentum SGD**, chúng ta giữ lại một phần gradient từ các bước trước đó. Điều này tương tự như khi chúng ta di chuyển với quán tính, và nhận một cú đẩy theo hướng khác, quỹ đạo của chúng ta không thay đổi ngay lập tức mà giữ lại một phần chuyển động ban đầu. Ở đây, chúng ta giới thiệu một vector khác v để biểu diễn *tốc độ*:

- v<sup>t+1</sup> = γ v<sup>t</sup> - η∇ℒ
- w<sup>t+1</sup> = w<sup>t</sup> + v<sup>t+1</sup>

Tham số γ biểu thị mức độ chúng ta tính đến quán tính: γ=0 tương ứng với SGD cổ điển; γ=1 là phương trình chuyển động thuần túy.

### Adam, Adagrad, v.v.

Vì trong mỗi lớp, chúng ta nhân tín hiệu với một ma trận W<sub>i</sub>, tùy thuộc vào ||W<sub>i</sub>||, gradient có thể hoặc giảm dần về gần 0, hoặc tăng lên vô hạn. Đây là bản chất của vấn đề Gradient Bùng Nổ/Biến Mất.

Một trong những giải pháp cho vấn đề này là chỉ sử dụng hướng của gradient trong phương trình và bỏ qua giá trị tuyệt đối, tức là:

w<sup>t+1</sup> = w<sup>t</sup> - η(∇ℒ/||∇ℒ||), trong đó ||∇ℒ|| = √∑(∇ℒ)<sup>2</sup>

Thuật toán này được gọi là **Adagrad**. Các thuật toán khác sử dụng cùng ý tưởng: **RMSProp**, **Adam**

> **Adam** được coi là một thuật toán rất hiệu quả cho nhiều ứng dụng, vì vậy nếu bạn không chắc chắn nên sử dụng thuật toán nào - hãy sử dụng Adam.

### Gradient clipping

Gradient clipping là một mở rộng của ý tưởng trên. Khi ||∇ℒ|| ≤ θ, chúng ta sử dụng gradient gốc trong tối ưu hóa trọng số, và khi ||∇ℒ|| > θ - chúng ta chia gradient cho chuẩn của nó. Ở đây θ là một tham số, trong hầu hết các trường hợp chúng ta có thể lấy θ=1 hoặc θ=10.

### Giảm tốc độ học

Thành công của huấn luyện thường phụ thuộc vào tham số tốc độ học η. Có thể giả định rằng giá trị lớn của η dẫn đến huấn luyện nhanh hơn, điều mà chúng ta thường muốn ở giai đoạn đầu của huấn luyện, và sau đó giá trị nhỏ hơn của η cho phép chúng ta tinh chỉnh mạng. Do đó, trong hầu hết các trường hợp, chúng ta muốn giảm η trong quá trình huấn luyện.

Điều này có thể được thực hiện bằng cách nhân η với một số (ví dụ: 0.98) sau mỗi epoch huấn luyện, hoặc sử dụng **lịch trình tốc độ học** phức tạp hơn.

## Các Kiến Trúc Mạng Khác Nhau

Chọn kiến trúc mạng phù hợp cho vấn đề của bạn có thể là một thách thức. Thông thường, chúng ta sẽ chọn một kiến trúc đã được chứng minh là hoạt động tốt cho nhiệm vụ cụ thể của chúng ta (hoặc nhiệm vụ tương tự). Đây là [một tổng quan tốt](https://www.topbots.com/a-brief-history-of-neural-network-architectures/) về các kiến trúc mạng nơ-ron cho thị giác máy tính.

> Điều quan trọng là chọn một kiến trúc đủ mạnh cho số lượng mẫu huấn luyện mà chúng ta có. Chọn mô hình quá mạnh có thể dẫn đến [overfitting](../../3-NeuralNetworks/05-Frameworks/Overfitting.md).

Một cách tốt khác là sử dụng một kiến trúc có thể tự động điều chỉnh theo độ phức tạp cần thiết. Ở một mức độ nào đó, kiến trúc **ResNet** và **Inception** có khả năng tự điều chỉnh. [Tìm hiểu thêm về các kiến trúc thị giác máy tính](../07-ConvNets/CNN_Architectures.md).

---

**Tuyên bố miễn trừ trách nhiệm**:  
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng các bản dịch tự động có thể chứa lỗi hoặc không chính xác. Tài liệu gốc bằng ngôn ngữ bản địa nên được coi là nguồn tham khảo chính thức. Đối với các thông tin quan trọng, nên sử dụng dịch vụ dịch thuật chuyên nghiệp từ con người. Chúng tôi không chịu trách nhiệm cho bất kỳ sự hiểu lầm hoặc diễn giải sai nào phát sinh từ việc sử dụng bản dịch này.