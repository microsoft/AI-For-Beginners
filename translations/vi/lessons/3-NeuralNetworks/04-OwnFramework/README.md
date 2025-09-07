<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "186bf7eeab776b36f557357ea56d4751",
  "translation_date": "2025-08-29T12:34:28+00:00",
  "source_file": "lessons/3-NeuralNetworks/04-OwnFramework/README.md",
  "language_code": "vi"
}
-->
# Giới thiệu về Mạng Nơ-ron. Perceptron Nhiều Lớp

Trong phần trước, bạn đã tìm hiểu về mô hình mạng nơ-ron đơn giản nhất - perceptron một lớp, một mô hình phân loại tuyến tính hai lớp.

Trong phần này, chúng ta sẽ mở rộng mô hình này thành một khung linh hoạt hơn, cho phép chúng ta:

* thực hiện **phân loại đa lớp** ngoài phân loại hai lớp  
* giải quyết các **bài toán hồi quy** ngoài phân loại  
* phân tách các lớp không thể phân tách tuyến tính  

Chúng ta cũng sẽ phát triển khung mô-đun của riêng mình bằng Python để xây dựng các kiến trúc mạng nơ-ron khác nhau.

## [Câu hỏi trước bài giảng](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/104)

## Chính thức hóa Học Máy

Hãy bắt đầu bằng cách chính thức hóa bài toán Học Máy. Giả sử chúng ta có một tập dữ liệu huấn luyện **X** với nhãn **Y**, và chúng ta cần xây dựng một mô hình *f* để đưa ra dự đoán chính xác nhất. Chất lượng của dự đoán được đo lường bằng **Hàm mất mát** ℒ. Các hàm mất mát sau thường được sử dụng:

* Đối với bài toán hồi quy, khi cần dự đoán một con số, chúng ta có thể sử dụng **lỗi tuyệt đối** ∑<sub>i</sub>|f(x<sup>(i)</sup>)-y<sup>(i)</sup>|, hoặc **lỗi bình phương** ∑<sub>i</sub>(f(x<sup>(i)</sup>)-y<sup>(i)</sup>)<sup>2</sup>  
* Đối với phân loại, chúng ta sử dụng **mất mát 0-1** (thực chất là **độ chính xác** của mô hình), hoặc **mất mát logistic**.

Đối với perceptron một lớp, hàm *f* được định nghĩa là một hàm tuyến tính *f(x)=wx+b* (ở đây *w* là ma trận trọng số, *x* là vector các đặc trưng đầu vào, và *b* là vector độ chệch). Đối với các kiến trúc mạng nơ-ron khác nhau, hàm này có thể có dạng phức tạp hơn.

> Trong trường hợp phân loại, thường mong muốn đầu ra của mạng là xác suất của các lớp tương ứng. Để chuyển đổi các số bất kỳ thành xác suất (ví dụ, để chuẩn hóa đầu ra), chúng ta thường sử dụng hàm **softmax** σ, và hàm *f* trở thành *f(x)=σ(wx+b)*.

Trong định nghĩa của *f* ở trên, *w* và *b* được gọi là **tham số** θ=⟨*w,b*⟩. Với tập dữ liệu ⟨**X**,**Y**⟩, chúng ta có thể tính toán lỗi tổng thể trên toàn bộ tập dữ liệu như một hàm của các tham số θ.

> ✅ **Mục tiêu của việc huấn luyện mạng nơ-ron là giảm thiểu lỗi bằng cách thay đổi các tham số θ**

## Tối ưu hóa Gradient Descent

Có một phương pháp tối ưu hóa hàm nổi tiếng gọi là **gradient descent**. Ý tưởng là chúng ta có thể tính đạo hàm (trong trường hợp đa chiều gọi là **gradient**) của hàm mất mát đối với các tham số, và thay đổi các tham số sao cho lỗi giảm đi. Điều này có thể được chính thức hóa như sau:

* Khởi tạo các tham số bằng một số giá trị ngẫu nhiên w<sup>(0)</sup>, b<sup>(0)</sup>  
* Lặp lại bước sau nhiều lần:  
    - w<sup>(i+1)</sup> = w<sup>(i)</sup>-η∂ℒ/∂w  
    - b<sup>(i+1)</sup> = b<sup>(i)</sup>-η∂ℒ/∂b  

Trong quá trình huấn luyện, các bước tối ưu hóa được tính toán dựa trên toàn bộ tập dữ liệu (nhớ rằng hàm mất mát được tính như tổng qua tất cả các mẫu huấn luyện). Tuy nhiên, trong thực tế, chúng ta lấy các phần nhỏ của tập dữ liệu gọi là **minibatches**, và tính gradient dựa trên một tập con dữ liệu. Vì tập con được lấy ngẫu nhiên mỗi lần, phương pháp này được gọi là **stochastic gradient descent** (SGD).

## Perceptron Nhiều Lớp và Backpropagation

Mạng một lớp, như chúng ta đã thấy ở trên, có khả năng phân loại các lớp có thể phân tách tuyến tính. Để xây dựng một mô hình phong phú hơn, chúng ta có thể kết hợp nhiều lớp của mạng. Về mặt toán học, điều này có nghĩa là hàm *f* sẽ có dạng phức tạp hơn và được tính toán qua nhiều bước:
* z<sub>1</sub>=w<sub>1</sub>x+b<sub>1</sub>  
* z<sub>2</sub>=w<sub>2</sub>α(z<sub>1</sub>)+b<sub>2</sub>  
* f = σ(z<sub>2</sub>)  

Ở đây, α là một **hàm kích hoạt phi tuyến**, σ là hàm softmax, và các tham số θ=<*w<sub>1</sub>,b<sub>1</sub>,w<sub>2</sub>,b<sub>2</sub>*>.

Thuật toán gradient descent vẫn giữ nguyên, nhưng việc tính toán gradient sẽ phức tạp hơn. Dựa trên quy tắc đạo hàm chuỗi, chúng ta có thể tính các đạo hàm như sau:

* ∂ℒ/∂w<sub>2</sub> = (∂ℒ/∂σ)(∂σ/∂z<sub>2</sub>)(∂z<sub>2</sub>/∂w<sub>2</sub>)  
* ∂ℒ/∂w<sub>1</sub> = (∂ℒ/∂σ)(∂σ/∂z<sub>2</sub>)(∂z<sub>2</sub>/∂α)(∂α/∂z<sub>1</sub>)(∂z<sub>1</sub>/∂w<sub>1</sub>)  

> ✅ Quy tắc đạo hàm chuỗi được sử dụng để tính đạo hàm của hàm mất mát đối với các tham số.

Lưu ý rằng phần bên trái nhất của tất cả các biểu thức này là giống nhau, do đó chúng ta có thể tính toán hiệu quả các đạo hàm bắt đầu từ hàm mất mát và đi "ngược lại" qua đồ thị tính toán. Vì vậy, phương pháp huấn luyện perceptron nhiều lớp được gọi là **backpropagation**, hoặc 'backprop'.

<img alt="compute graph" src="images/ComputeGraphGrad.png"/>

> TODO: trích dẫn hình ảnh

> ✅ Chúng ta sẽ tìm hiểu chi tiết hơn về backprop trong ví dụ notebook của chúng ta.

## Kết luận

Trong bài học này, chúng ta đã xây dựng thư viện mạng nơ-ron của riêng mình và sử dụng nó cho một bài toán phân loại hai chiều đơn giản.

## 🚀 Thử thách

Trong notebook đi kèm, bạn sẽ triển khai khung của riêng mình để xây dựng và huấn luyện perceptron nhiều lớp. Bạn sẽ có thể thấy chi tiết cách các mạng nơ-ron hiện đại hoạt động.

Hãy tiếp tục với notebook [OwnFramework](OwnFramework.ipynb) và làm việc qua nó.

## [Câu hỏi sau bài giảng](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/204)

## Ôn tập & Tự học

Backpropagation là một thuật toán phổ biến được sử dụng trong AI và ML, đáng để nghiên cứu [chi tiết hơn](https://wikipedia.org/wiki/Backpropagation).

## [Bài tập](lab/README.md)

Trong bài thực hành này, bạn được yêu cầu sử dụng khung mà bạn đã xây dựng trong bài học này để giải bài toán phân loại chữ số viết tay MNIST.

* [Hướng dẫn](lab/README.md)  
* [Notebook](lab/MyFW_MNIST.ipynb)  

---

**Tuyên bố miễn trừ trách nhiệm**:  
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng các bản dịch tự động có thể chứa lỗi hoặc không chính xác. Tài liệu gốc bằng ngôn ngữ bản địa nên được coi là nguồn thông tin chính thức. Đối với các thông tin quan trọng, khuyến nghị sử dụng dịch vụ dịch thuật chuyên nghiệp bởi con người. Chúng tôi không chịu trách nhiệm cho bất kỳ sự hiểu lầm hoặc diễn giải sai nào phát sinh từ việc sử dụng bản dịch này.