# Các mẹo huấn luyện học sâu

Khi các mạng nơ-ron ngày càng sâu hơn, quá trình huấn luyện chúng trở nên ngày càng khó khăn. Một vấn đề lớn là cái gọi là [biên độ gradient biến mất](https://en.wikipedia.org/wiki/Vanishing_gradient_problem) hoặc [biên độ gradient bùng nổ](https://deepai.org/machine-learning-glossary-and-terms/exploding-gradient-problem#:~:text=Exploding%20gradients%20are%20a%20problem,updates%20are%20small%20and%20controlled.). [Bài viết này](https://towardsdatascience.com/the-vanishing-exploding-gradient-problem-in-deep-neural-networks-191358470c11) cung cấp một giới thiệu tốt về các vấn đề đó.

Để làm cho việc huấn luyện các mạng sâu hiệu quả hơn, có một vài kỹ thuật có thể được sử dụng.

## Giữ các giá trị trong khoảng hợp lý

Để làm cho các phép tính số học ổn định hơn, chúng ta muốn đảm bảo rằng tất cả các giá trị trong mạng nơ-ron của chúng ta nằm trong phạm vi hợp lý, thường là [-1..1] hoặc [0..1]. Đây không phải là một yêu cầu quá khắt khe, nhưng bản chất của các phép tính dấu phẩy động là các giá trị có độ lớn khác nhau không thể được xử lý chính xác cùng nhau. Ví dụ, nếu ta cộng 10<sup>-10</sup> và 10<sup>10</sup>, ta có khả năng nhận được kết quả bằng 10<sup>10</sup>, vì giá trị nhỏ hơn sẽ bị "chuyển đổi" về cùng bậc với giá trị lớn hơn, và do đó phần mantissa sẽ bị mất.

Phần lớn các hàm kích hoạt có phi tuyến quanh khoảng [-1..1], và do đó hợp lý khi ta chuẩn hóa toàn bộ dữ liệu đầu vào về khoảng [-1..1] hoặc [0..1].

## Khởi tạo trọng số ban đầu

Lý tưởng là chúng ta muốn các giá trị nằm trong cùng một phạm vi sau khi đi qua các lớp mạng. Do đó, quan trọng là khởi tạo trọng số sao cho giữ được phân phối của các giá trị.

Phân phối chuẩn **N(0,1)** không phải là một ý tưởng tốt, vì nếu ta có *n* đầu vào, độ lệch chuẩn của đầu ra sẽ là *&radic;n*, và các giá trị có khả năng bị nhảy ra khỏi khoảng [0..1].

Các khởi tạo sau đây thường được sử dụng:

 * Phân phối đều -- `uniform`
 * **N(0,1/n)** -- `gaussian`
 * **N(0,1/&radic;n_in)** đảm bảo rằng với đầu vào có trung bình bằng 0 và độ lệch chuẩn là 1, trung bình/độ lệch chuẩn đó sẽ được giữ nguyên
 * **N(0,&radic;2/(n_in+n_out))** -- gọi là **khởi tạo Xavier** (`glorot`), giúp giữ tín hiệu trong phạm vi trong cả quá trình lan truyền tiến và lan truyền ngược

## Chuẩn hóa batch

Ngay cả với khởi tạo trọng số đúng, trọng số có thể trở nên cực lớn hoặc nhỏ trong quá trình huấn luyện, và chúng sẽ làm tín hiệu ra khỏi phạm vi đúng. Ta có thể đưa tín hiệu về lại bằng cách sử dụng một trong các kỹ thuật **chuẩn hóa**. Trong khi có nhiều kỹ thuật (Chuẩn hóa trọng số, Chuẩn hóa lớp), cái được sử dụng nhiều nhất là Chuẩn hóa batch.

Ý tưởng của **chuẩn hóa batch** là xem xét tất cả các giá trị trong minibatch, và thực hiện chuẩn hóa (tức là trừ trung bình và chia độ lệch chuẩn) dựa trên các giá trị đó. Nó được triển khai như một lớp mạng thực hiện chuẩn hóa này sau khi áp dụng trọng số, nhưng trước hàm kích hoạt. Kết quả là, ta có khả năng thấy độ chính xác cuối cao hơn và quá trình huấn luyện nhanh hơn.

Đây là [bài báo gốc](https://arxiv.org/pdf/1502.03167.pdf) về chuẩn hóa batch, [giải thích trên Wikipedia](https://en.wikipedia.org/wiki/Batch_normalization), và [một bài viết nhập môn hay](https://towardsdatascience.com/batch-normalization-in-3-levels-of-understanding-14c2da90a338) (và một bài [bằng tiếng Nga](https://habrahabr.ru/post/309302/)).

## Dropout

**Dropout** là một kỹ thuật thú vị loại bỏ một tỷ lệ phần trăm ngẫu nhiên các nơ-ron trong quá trình huấn luyện. Nó cũng được triển khai như một lớp với một tham số (tỷ lệ phần trăm nơ-ron cần loại bỏ, thường là 10%-50%), và trong suốt quá trình huấn luyện, nó đặt ngẫu nhiên các phần tử trong vector đầu vào về 0 trước khi truyền đến lớp tiếp theo.

Dù điều này có thể nghe có vẻ kỳ lạ, bạn có thể thấy hiệu ứng của dropout trên huấn luyện bộ phân loại chữ số MNIST trong notebook [`Dropout.ipynb`](Dropout.ipynb). Nó làm tăng tốc huấn luyện và cho phép chúng ta đạt độ chính xác cao hơn trong ít epoch huấn luyện hơn.

Hiệu ứng này có thể được giải thích theo nhiều cách khác nhau:

 * Nó có thể được xem như một yếu tố sốc ngẫu nhiên tác động lên mô hình, khiến việc tối ưu hóa thoát khỏi điểm cực tiểu cục bộ
 * Nó có thể được xem như *trung bình mô hình ngầm định*, vì ta có thể nói rằng trong quá trình dropout, ta đang huấn luyện một mô hình hơi khác

> *Một số người nói rằng khi một người say cố gắng học điều gì đó, anh ta sẽ nhớ nó tốt hơn vào sáng hôm sau so với người tỉnh táo, vì một bộ não với một số nơ-ron hoạt động lỗi cố gắng thích nghi tốt hơn để nắm bắt ý nghĩa. Chúng tôi chưa bao giờ tự kiểm tra liệu điều này có đúng không*

## Ngăn ngừa hiện tượng overfitting

Một trong những khía cạnh rất quan trọng của học sâu là có thể ngăn ngừa [overfitting](../../3-NeuralNetworks/05-Frameworks/Overfitting.md). Dù có thể hấp dẫn khi dùng một mô hình mạng rất mạnh, chúng ta luôn cần cân bằng số lượng tham số mô hình với số mẫu huấn luyện.

> Hãy chắc chắn bạn hiểu khái niệm [overfitting](../../3-NeuralNetworks/05-Frameworks/Overfitting.md) mà chúng ta đã giới thiệu trước đó!

Có một vài cách để ngăn ngừa overfitting:

 * Dừng sớm -- liên tục theo dõi lỗi trên tập xác nhận và dừng huấn luyện khi lỗi xác nhận bắt đầu tăng.
 * Giảm trọng số/Regularization rõ ràng -- thêm một hình phạt vào hàm mất mát cho các giá trị tuyệt đối lớn của trọng số, giúp ngăn mô hình cho ra kết quả rất không ổn định
 * Trung bình mô hình -- huấn luyện nhiều mô hình rồi sau đó lấy trung bình kết quả. Điều này giúp giảm phương sai.
 * Dropout (Trung bình mô hình ngầm định)

## Bộ tối ưu / Thuật toán huấn luyện

Một khía cạnh quan trọng khác của huấn luyện là lựa chọn thuật toán huấn luyện tốt. Trong khi **gradient descent** cổ điển là một lựa chọn hợp lý, đôi khi nó quá chậm hoặc dẫn đến các vấn đề khác.

Trong học sâu, ta sử dụng **Stochastic Gradient Descent** (SGD), là thuật toán gradient descent áp dụng cho các minibatch được chọn ngẫu nhiên từ tập huấn luyện. Trọng số được điều chỉnh theo công thức:

w<sup>t+1</sup> = w<sup>t</sup> - &eta;&nabla;&lagran;

### Momentum

Trong **momentum SGD**, ta giữ lại một phần gradient của các bước trước. Nó giống như khi ta di chuyển với quán tính, và nhận một cú đấm vào hướng khác, quỹ đạo không thay đổi ngay lập tức mà giữ lại một phần chuyển động ban đầu. Ở đây ta giới thiệu một vector khác v để biểu diễn *tốc độ*:

* v<sup>t+1</sup> = &gamma; v<sup>t</sup> - &eta;&nabla;&lagran;
* w<sup>t+1</sup> = w<sup>t</sup>+v<sup>t+1</sup>

Ở đây tham số &gamma; chỉ mức độ ta tính đến quán tính: &gamma;=0 tương ứng với SGD cổ điển; &gamma;=1 là phương trình chuyển động thuần túy.

### Adam, Adagrad, v.v.

Vì ở mỗi lớp ta nhân tín hiệu với ma trận W<sub>i</sub>, tùy thuộc vào ||W<sub>i</sub>||, gradient có thể giảm dần về gần 0, hoặc tăng lên vô hạn. Đây là bản chất của vấn đề Biên độ gradient bùng nổ/biến mất.

Một giải pháp cho vấn đề này là chỉ sử dụng hướng của gradient trong phương trình, và bỏ qua giá trị tuyệt đối, tức là

w<sup>t+1</sup> = w<sup>t</sup> - &eta;(&nabla;&lagran;/||&nabla;&lagran;||), với ||&nabla;&lagran;|| = &radic;&sum;(&nabla;&lagran;)<sup>2</sup>

Thuật toán này gọi là **Adagrad**. Các thuật toán khác cùng sử dụng ý tưởng này là: **RMSProp**, **Adam**

> **Adam** được coi là thuật toán rất hiệu quả cho nhiều ứng dụng, vì vậy nếu bạn chưa chắc chọn cái nào - hãy dùng Adam.

### Cắt gradient

Cắt gradient là phần mở rộng của ý tưởng trên. Khi ||&nabla;&lagran;|| &le; &theta;, ta dùng gradient gốc để tối ưu hóa trọng số, và khi ||&nabla;&lagran;|| > &theta; - ta chia gradient cho chuẩn của nó. Ở đây &theta; là tham số, trong đa số trường hợp ta chọn &theta;=1 hoặc &theta;=10.

### Giảm tốc độ học

Thành công của việc huấn luyện thường phụ thuộc vào tham số tốc độ học &eta;. Lý luận hợp lý là giá trị lớn của &eta; giúp huấn luyện nhanh hơn, điều ta thường muốn ở đầu quá trình huấn luyện, và sau đó giá trị nhỏ hơn của &eta; cho phép ta tinh chỉnh mạng. Do vậy, trong hầu hết các trường hợp ta muốn giảm &eta; trong quá trình huấn luyện.

Việc này có thể làm bằng cách nhân &eta; với một số (ví dụ 0.98) sau mỗi epoch huấn luyện, hoặc bằng cách sử dụng **lịch trình tốc độ học** phức tạp hơn.

## Các kiến trúc mạng khác nhau

Việc lựa chọn kiến trúc mạng phù hợp cho bài toán của bạn có thể khá khó. Thông thường ta sẽ chọn kiến trúc đã được chứng minh là hiệu quả cho nhiệm vụ cụ thể (hoặc tương tự). Đây là một [tổng quan tốt](https://www.topbots.com/a-brief-history-of-neural-network-architectures/) về các kiến trúc mạng nơ-ron cho thị giác máy tính.

> Quan trọng là chọn kiến trúc đủ mạnh cho số lượng mẫu huấn luyện ta có. Chọn mô hình quá mạnh có thể dẫn đến [overfitting](../../3-NeuralNetworks/05-Frameworks/Overfitting.md)

Một cách tốt khác là sử dụng kiến trúc có khả năng tự điều chỉnh độ phức tạp cần thiết. Ở mức độ nào đó, kiến trúc **ResNet** và **Inception** là tự điều chỉnh. [Xem thêm về các kiến trúc thị giác máy tính](../07-ConvNets/CNN_Architectures.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Tuyên bố miễn trừ trách nhiệm**:
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng bản dịch tự động có thể chứa lỗi hoặc sai sót. Tài liệu gốc bằng ngôn ngữ gốc nên được coi là nguồn tin chính thức. Đối với thông tin quan trọng, nên sử dụng dịch vụ dịch thuật chuyên nghiệp bởi con người. Chúng tôi không chịu trách nhiệm về bất kỳ hiểu lầm hoặc giải thích sai nào phát sinh từ việc sử dụng bản dịch này.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->