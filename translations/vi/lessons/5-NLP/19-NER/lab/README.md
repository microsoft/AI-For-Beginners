# NER

Bài tập thực hành từ [AI for Beginners Curriculum](https://github.com/microsoft/ai-for-beginners).

## Nhiệm vụ

Trong bài thực hành này, bạn cần huấn luyện mô hình nhận dạng thực thể có tên (NER) cho các thuật ngữ y khoa.

## Bộ dữ liệu

Để huấn luyện mô hình NER, chúng ta cần một bộ dữ liệu được gắn nhãn đúng với các thực thể y khoa. [Bộ dữ liệu BC5CDR](https://biocreative.bioinformatics.udel.edu/tasks/biocreative-v/track-3-cdr/) chứa các thực thể bệnh và hóa chất được gắn nhãn từ hơn 1500 bài báo. Bạn có thể tải bộ dữ liệu này sau khi đăng ký tại trang web của họ.

Bộ dữ liệu BC5CDR trông như sau:

```
6794356|t|Tricuspid valve regurgitation and lithium carbonate toxicity in a newborn infant.
6794356|a|A newborn with massive tricuspid regurgitation, atrial flutter, congestive heart failure, and a high serum lithium level is described. This is the first patient to initially manifest tricuspid regurgitation and atrial flutter, and the 11th described patient with cardiac disease among infants exposed to lithium compounds in the first trimester of pregnancy. Sixty-three percent of these infants had tricuspid valve involvement. Lithium carbonate may be a factor in the increasing incidence of congenital heart disease when taken during early pregnancy. It also causes neurologic depression, cyanosis, and cardiac arrhythmia when consumed prior to delivery.
6794356	0	29	Tricuspid valve regurgitation	Disease	D014262
6794356	34	51	lithium carbonate	Chemical	D016651
6794356	52	60	toxicity	Disease	D064420
...
```

Trong bộ dữ liệu này, tiêu đề bài báo và phần tóm tắt nằm ở hai dòng đầu tiên, sau đó là các thực thể riêng lẻ, với vị trí bắt đầu và kết thúc trong khối tiêu đề + tóm tắt. Ngoài loại thực thể, bạn còn nhận được ID của thực thể này trong một số hệ thống phân loại y khoa.

Bạn sẽ cần viết một số mã Python để chuyển đổi dữ liệu này sang định dạng BIO.

## Mạng lưới

Lần thử đầu tiên với NER có thể được thực hiện bằng cách sử dụng mạng LSTM, như trong ví dụ bạn đã thấy trong bài học. Tuy nhiên, trong các nhiệm vụ NLP, [kiến trúc transformer](https://en.wikipedia.org/wiki/Transformer_(machine_learning_model)), và đặc biệt là [mô hình ngôn ngữ BERT](https://en.wikipedia.org/wiki/BERT_(language_model)) cho kết quả tốt hơn nhiều. Các mô hình BERT được huấn luyện trước hiểu cấu trúc chung của ngôn ngữ và có thể được tinh chỉnh cho các nhiệm vụ cụ thể với bộ dữ liệu tương đối nhỏ và chi phí tính toán thấp.

Vì chúng ta dự định áp dụng NER vào kịch bản y khoa, nên việc sử dụng mô hình BERT được huấn luyện trên các văn bản y khoa là hợp lý. Microsoft Research đã phát hành một mô hình được huấn luyện trước gọi là [PubMedBERT][PubMedBERT] ([bài báo][PubMedBERT-Pub]), được tinh chỉnh bằng các văn bản từ kho [PubMed](https://pubmed.ncbi.nlm.nih.gov/).

Tiêu chuẩn *de facto* để huấn luyện các mô hình transformer là thư viện [Hugging Face Transformers](https://huggingface.co/). Thư viện này cũng chứa một kho các mô hình được huấn luyện trước do cộng đồng duy trì, bao gồm PubMedBERT. Để tải và sử dụng mô hình này, chúng ta chỉ cần vài dòng mã:

```python
model_name = "microsoft/BiomedNLP-PubMedBERT-base-uncased-abstract"
classes = ... # number of classes: 2*entities+1
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = BertForTokenClassification.from_pretrained(model_name, classes)
```

Điều này cung cấp cho chúng ta `model` được xây dựng cho nhiệm vụ phân loại token với số lượng `classes` lớp, cũng như đối tượng `tokenizer` có thể chia văn bản đầu vào thành các token. Bạn sẽ cần chuyển đổi bộ dữ liệu sang định dạng BIO, đồng thời tính đến việc token hóa của PubMedBERT. Bạn có thể sử dụng [đoạn mã Python này](https://gist.github.com/shwars/580b55684be3328eb39ecf01b9cbbd88) làm nguồn cảm hứng.

## Kết luận

Nhiệm vụ này rất gần với nhiệm vụ thực tế mà bạn có thể gặp phải nếu muốn tìm hiểu sâu hơn về khối lượng lớn văn bản ngôn ngữ tự nhiên. Trong trường hợp của chúng ta, bạn có thể áp dụng mô hình đã huấn luyện vào [bộ dữ liệu các bài báo liên quan đến COVID](https://www.kaggle.com/allen-institute-for-ai/CORD-19-research-challenge) và xem những thông tin chi tiết nào có thể thu được. [Bài viết blog này](https://soshnikov.com/science/analyzing-medical-papers-with-azure-and-text-analytics-for-health/) và [bài báo này](https://www.mdpi.com/2504-2289/6/1/4) mô tả nghiên cứu có thể được thực hiện trên tập hợp các bài báo này bằng cách sử dụng NER.

---

**Tuyên bố miễn trừ trách nhiệm**:  
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng các bản dịch tự động có thể chứa lỗi hoặc không chính xác. Tài liệu gốc bằng ngôn ngữ bản địa nên được coi là nguồn thông tin chính thức. Đối với các thông tin quan trọng, khuyến nghị sử dụng dịch vụ dịch thuật chuyên nghiệp bởi con người. Chúng tôi không chịu trách nhiệm cho bất kỳ sự hiểu lầm hoặc diễn giải sai nào phát sinh từ việc sử dụng bản dịch này.