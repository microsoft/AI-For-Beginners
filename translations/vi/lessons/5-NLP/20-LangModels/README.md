# Các Mô Hình Ngôn Ngữ Lớn Được Huấn Luyện Trước

Trong tất cả các nhiệm vụ trước đây, chúng ta đã huấn luyện một mạng nơ-ron để thực hiện một nhiệm vụ cụ thể bằng cách sử dụng tập dữ liệu có nhãn. Với các mô hình transformer lớn, như BERT, chúng ta sử dụng mô hình ngôn ngữ theo cách tự giám sát để xây dựng một mô hình ngôn ngữ, sau đó được chuyên biệt hóa cho các nhiệm vụ cụ thể với việc huấn luyện thêm theo từng lĩnh vực. Tuy nhiên, đã có minh chứng rằng các mô hình ngôn ngữ lớn cũng có thể giải quyết nhiều nhiệm vụ mà KHÔNG cần huấn luyện theo từng lĩnh vực. Một nhóm các mô hình có khả năng làm điều này được gọi là **GPT**: Generative Pre-Trained Transformer.

## [Câu hỏi trước bài giảng](https://ff-quizzes.netlify.app/en/ai/quiz/39)

## Sinh Văn Bản và Độ Phức Tạp

Ý tưởng về một mạng nơ-ron có thể thực hiện các nhiệm vụ chung mà không cần huấn luyện thêm được trình bày trong bài báo [Language Models are Unsupervised Multitask Learners](https://cdn.openai.com/better-language-models/language_models_are_unsupervised_multitask_learners.pdf). Ý tưởng chính là nhiều nhiệm vụ khác có thể được mô hình hóa bằng **sinh văn bản**, bởi vì hiểu văn bản về cơ bản có nghĩa là có khả năng tạo ra nó. Vì mô hình được huấn luyện trên một lượng lớn văn bản bao gồm kiến thức của con người, nó cũng trở nên hiểu biết về nhiều chủ đề khác nhau.

> Hiểu và có khả năng tạo ra văn bản cũng đồng nghĩa với việc biết một chút về thế giới xung quanh chúng ta. Con người cũng học rất nhiều thông qua việc đọc, và mạng GPT cũng tương tự theo khía cạnh này.

Các mạng sinh văn bản hoạt động bằng cách dự đoán xác suất của từ tiếp theo $$P(w_N)$$. Tuy nhiên, xác suất không điều kiện của từ tiếp theo bằng với tần suất của từ đó trong tập văn bản. GPT có khả năng cung cấp **xác suất có điều kiện** của từ tiếp theo, dựa trên các từ trước đó: $$P(w_N | w_{n-1}, ..., w_0)$$.

> Bạn có thể đọc thêm về xác suất trong [Chương trình học Khoa học Dữ liệu cho Người Mới Bắt Đầu](https://github.com/microsoft/Data-Science-For-Beginners/tree/main/1-Introduction/04-stats-and-probability).

Chất lượng của mô hình sinh ngôn ngữ có thể được định nghĩa bằng **độ phức tạp**. Đây là một thước đo nội tại cho phép chúng ta đánh giá chất lượng mô hình mà không cần bất kỳ tập dữ liệu cụ thể nào. Nó dựa trên khái niệm *xác suất của một câu* - mô hình gán xác suất cao cho một câu có khả năng là thực (tức là mô hình không **bối rối** bởi câu đó), và xác suất thấp cho các câu ít hợp lý hơn (ví dụ: *Can it does what?*). Khi chúng ta đưa cho mô hình các câu từ tập văn bản thực, chúng ta mong đợi chúng có xác suất cao và **độ phức tạp** thấp. Về mặt toán học, nó được định nghĩa là nghịch đảo chuẩn hóa của xác suất tập kiểm tra:
$$
\mathrm{Perplexity}(W) = \sqrt[N]{1\over P(W_1,...,W_N)}
$$ 

**Bạn có thể thử nghiệm sinh văn bản bằng [trình soạn thảo văn bản sử dụng GPT từ Hugging Face](https://transformer.huggingface.co/doc/gpt2-large)**. Trong trình soạn thảo này, bạn bắt đầu viết văn bản của mình, và nhấn **[TAB]** sẽ cung cấp cho bạn một số tùy chọn hoàn thành. Nếu chúng quá ngắn, hoặc bạn không hài lòng với chúng - nhấn [TAB] lần nữa, và bạn sẽ có thêm các tùy chọn, bao gồm các đoạn văn bản dài hơn.

## GPT là Một Gia Đình

GPT không phải là một mô hình duy nhất, mà là một tập hợp các mô hình được phát triển và huấn luyện bởi [OpenAI](https://openai.com).

Trong các mô hình GPT, chúng ta có:

| [GPT-2](https://huggingface.co/docs/transformers/model_doc/gpt2#openai-gpt2) | [GPT 3](https://openai.com/research/language-models-are-few-shot-learners) | [GPT-4](https://openai.com/gpt-4) |
| -- | -- | -- |
|Mô hình ngôn ngữ với tối đa 1.5 tỷ tham số. | Mô hình ngôn ngữ với tối đa 175 tỷ tham số. | 100T tham số và chấp nhận cả đầu vào hình ảnh và văn bản, đầu ra là văn bản. |

Các mô hình GPT-3 và GPT-4 có sẵn [như một dịch vụ nhận thức từ Microsoft Azure](https://azure.microsoft.com/en-us/services/cognitive-services/openai-service/#overview?WT.mc_id=academic-77998-cacaste), và dưới dạng [API của OpenAI](https://openai.com/api/).

## Kỹ Thuật Tạo Prompt

Vì GPT đã được huấn luyện trên một lượng lớn dữ liệu để hiểu ngôn ngữ và mã, chúng cung cấp đầu ra để đáp ứng các đầu vào (prompt). Prompt là các đầu vào hoặc truy vấn cho GPT, trong đó người dùng cung cấp hướng dẫn cho mô hình về các nhiệm vụ cần hoàn thành tiếp theo. Để đạt được kết quả mong muốn, bạn cần một prompt hiệu quả nhất, bao gồm việc chọn từ ngữ, định dạng, cụm từ hoặc thậm chí ký hiệu phù hợp. Phương pháp này được gọi là [Kỹ Thuật Tạo Prompt](https://learn.microsoft.com/en-us/shows/ai-show/the-basics-of-prompt-engineering-with-azure-openai-service?WT.mc_id=academic-77998-bethanycheum).

[Tài liệu này](https://learn.microsoft.com/en-us/semantic-kernel/prompt-engineering/?WT.mc_id=academic-77998-bethanycheum) cung cấp cho bạn thêm thông tin về kỹ thuật tạo prompt.

## ✍️ Notebook Ví Dụ: [Khám Phá OpenAI-GPT](GPT-PyTorch.ipynb)

Tiếp tục học tập trong các notebook sau:

* [Sinh văn bản với OpenAI-GPT và Hugging Face Transformers](GPT-PyTorch.ipynb)

## Kết Luận

Các mô hình ngôn ngữ được huấn luyện trước mới không chỉ mô hình hóa cấu trúc ngôn ngữ, mà còn chứa một lượng lớn ngôn ngữ tự nhiên. Do đó, chúng có thể được sử dụng hiệu quả để giải quyết một số nhiệm vụ NLP trong các tình huống không cần huấn luyện hoặc huấn luyện ít.

## [Câu hỏi sau bài giảng](https://ff-quizzes.netlify.app/en/ai/quiz/40)

---

