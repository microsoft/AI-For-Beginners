<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "0c37770bba4fff3c71dc00eb261ee61b",
  "translation_date": "2025-08-29T12:35:32+00:00",
  "source_file": "lessons/3-NeuralNetworks/03-Perceptron/README.md",
  "language_code": "vi"
}
-->
# Giới thiệu về Mạng Nơ-ron: Perceptron

## [Câu hỏi trước bài giảng](https://ff-quizzes.netlify.app/en/ai/quiz/5)

Một trong những nỗ lực đầu tiên để triển khai một thứ gì đó tương tự như mạng nơ-ron hiện đại được thực hiện bởi Frank Rosenblatt từ Phòng thí nghiệm Hàng không Cornell vào năm 1957. Đây là một triển khai phần cứng có tên "Mark-1", được thiết kế để nhận diện các hình học cơ bản như tam giác, hình vuông và hình tròn.

|      |      |
|--------------|-----------|
|<img src='images/Rosenblatt-wikipedia.jpg' alt='Frank Rosenblatt'/> | <img src='images/Mark_I_perceptron_wikipedia.jpg' alt='The Mark 1 Perceptron' />|

> Hình ảnh [từ Wikipedia](https://en.wikipedia.org/wiki/Perceptron)

Hình ảnh đầu vào được biểu diễn bằng một mảng 20x20 tế bào quang, vì vậy mạng nơ-ron có 400 đầu vào và một đầu ra nhị phân. Một mạng đơn giản chứa một nơ-ron, còn được gọi là **đơn vị logic ngưỡng**. Các trọng số của mạng nơ-ron hoạt động như các biến trở cần được điều chỉnh thủ công trong giai đoạn huấn luyện.

> ✅ Biến trở là một thiết bị cho phép người dùng điều chỉnh điện trở của một mạch.

> Tờ New York Times đã viết về perceptron vào thời điểm đó: *phôi thai của một máy tính điện tử mà [Hải quân] kỳ vọng sẽ có thể đi lại, nói chuyện, nhìn, viết, tự tái tạo và nhận thức được sự tồn tại của chính nó.*

## Mô hình Perceptron

Giả sử chúng ta có N đặc trưng trong mô hình của mình, khi đó vector đầu vào sẽ là một vector kích thước N. Perceptron là một mô hình **phân loại nhị phân**, tức là nó có thể phân biệt giữa hai lớp dữ liệu đầu vào. Chúng ta sẽ giả định rằng đối với mỗi vector đầu vào x, đầu ra của perceptron sẽ là +1 hoặc -1, tùy thuộc vào lớp. Đầu ra được tính bằng công thức:

y(x) = f(w<sup>T</sup>x)

trong đó f là một hàm kích hoạt dạng bậc.

<!-- img src="http://www.sciweavers.org/tex2img.php?eq=f%28x%29%20%3D%20%5Cbegin%7Bcases%7D%0A%20%20%20%20%20%20%20%20%20%2B1%20%26%20x%20%5Cgeq%200%20%5C%5C%0A%20%20%20%20%20%20%20%20%20-1%20%26%20x%20%3C%200%0A%20%20%20%20%20%20%20%5Cend%7Bcases%7D%20%5C%5C%0A&bc=White&fc=Black&im=jpg&fs=12&ff=arev&edit=0" align="center" border="0" alt="f(x) = \begin{cases} +1 & x \geq 0 \\ -1 & x < 0 \end{cases} \\" width="154" height="50" / -->
<img src="images/activation-func.png"/>

## Huấn luyện Perceptron

Để huấn luyện một perceptron, chúng ta cần tìm một vector trọng số w sao cho phân loại đúng hầu hết các giá trị, tức là dẫn đến **lỗi** nhỏ nhất. Lỗi E này được định nghĩa bởi **tiêu chí perceptron** như sau:

E(w) = -∑w<sup>T</sup>x<sub>i</sub>t<sub>i</sub>

trong đó:

* tổng được thực hiện trên các điểm dữ liệu huấn luyện i dẫn đến phân loại sai
* x<sub>i</sub> là dữ liệu đầu vào, và t<sub>i</sub> là -1 hoặc +1 tương ứng với ví dụ âm và dương.

Tiêu chí này được coi là một hàm của trọng số w, và chúng ta cần tối thiểu hóa nó. Thông thường, một phương pháp gọi là **gradient descent** được sử dụng, trong đó chúng ta bắt đầu với một trọng số ban đầu w<sup>(0)</sup>, và sau đó tại mỗi bước cập nhật trọng số theo công thức:

w<sup>(t+1)</sup> = w<sup>(t)</sup> - η∇E(w)

Ở đây η được gọi là **tốc độ học**, và ∇E(w) biểu thị **gradient** của E. Sau khi tính gradient, chúng ta có:

w<sup>(t+1)</sup> = w<sup>(t)</sup> + ∑ηx<sub>i</sub>t<sub>i</sub>

Thuật toán trong Python trông như sau:

```python
def train(positive_examples, negative_examples, num_iterations = 100, eta = 1):

    weights = [0,0,0] # Initialize weights (almost randomly :)
        
    for i in range(num_iterations):
        pos = random.choice(positive_examples)
        neg = random.choice(negative_examples)

        z = np.dot(pos, weights) # compute perceptron output
        if z < 0: # positive example classified as negative
            weights = weights + eta*weights.shape

        z  = np.dot(neg, weights)
        if z >= 0: # negative example classified as positive
            weights = weights - eta*weights.shape

    return weights
```

## Kết luận

Trong bài học này, bạn đã tìm hiểu về perceptron, một mô hình phân loại nhị phân, và cách huấn luyện nó bằng cách sử dụng vector trọng số.

## 🚀 Thử thách

Nếu bạn muốn tự xây dựng perceptron của riêng mình, hãy thử [bài thực hành này trên Microsoft Learn](https://docs.microsoft.com/en-us/azure/machine-learning/component-reference/two-class-averaged-perceptron?WT.mc_id=academic-77998-cacaste) sử dụng [Azure ML designer](https://docs.microsoft.com/en-us/azure/machine-learning/concept-designer?WT.mc_id=academic-77998-cacaste).

## [Câu hỏi sau bài giảng](https://ff-quizzes.netlify.app/en/ai/quiz/6)

## Ôn tập & Tự học

Để xem cách chúng ta có thể sử dụng perceptron để giải quyết một bài toán đơn giản cũng như các bài toán thực tế, và để tiếp tục học - hãy truy cập notebook [Perceptron](Perceptron.ipynb).

Đây là một [bài viết thú vị về perceptron](https://towardsdatascience.com/what-is-a-perceptron-basics-of-neural-networks-c4cfea20c590) mà bạn có thể tham khảo.

## [Bài tập](lab/README.md)

Trong bài học này, chúng ta đã triển khai một perceptron cho nhiệm vụ phân loại nhị phân, và chúng ta đã sử dụng nó để phân loại giữa hai chữ số viết tay. Trong bài thực hành này, bạn được yêu cầu giải quyết hoàn toàn bài toán phân loại chữ số, tức là xác định chữ số nào có khả năng tương ứng nhất với một hình ảnh đã cho.

* [Hướng dẫn](lab/README.md)
* [Notebook](lab/PerceptronMultiClass.ipynb)

---

**Tuyên bố miễn trừ trách nhiệm**:  
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng các bản dịch tự động có thể chứa lỗi hoặc không chính xác. Tài liệu gốc bằng ngôn ngữ bản địa nên được coi là nguồn thông tin chính thức. Đối với các thông tin quan trọng, khuyến nghị sử dụng dịch vụ dịch thuật chuyên nghiệp bởi con người. Chúng tôi không chịu trách nhiệm cho bất kỳ sự hiểu lầm hoặc diễn giải sai nào phát sinh từ việc sử dụng bản dịch này.