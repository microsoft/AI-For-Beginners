# Cách Chạy Mã Lệnh

Chương trình học này chứa nhiều ví dụ và bài thực hành có thể chạy được mà bạn sẽ muốn thử. Để làm điều này, bạn cần khả năng thực thi mã Python trong Jupyter Notebooks được cung cấp như một phần của chương trình học này. Bạn có một số lựa chọn để chạy mã:

## Chạy trên máy tính cá nhân

Để chạy mã trên máy tính cá nhân, bạn cần cài đặt Python. Một gợi ý là cài **[miniconda](https://conda.io/en/latest/miniconda.html)** - đây là một bản cài đặt nhẹ hỗ trợ trình quản lý gói `conda` cho các **môi trường ảo** Python khác nhau.

Sau khi cài miniconda, bạn clone kho và tạo môi trường ảo để dùng cho khóa học này:

```bash
git clone http://github.com/microsoft/ai-for-beginners
cd ai-for-beginners
conda env create --name ai4beg --file .devcontainer/environment.yml
conda activate ai4beg
```

### Sử dụng Visual Studio Code với Phần mở rộng Python

Chương trình học này sẽ sử dụng hiệu quả nhất khi mở trong [Visual Studio Code](http://code.visualstudio.com/?WT.mc_id=academic-77998-cacaste) với [Phần mở rộng Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python&WT.mc_id=academic-77998-cacaste).

> **Lưu ý**: Khi bạn clone và mở thư mục trong VS Code, nó sẽ tự động gợi ý bạn cài đặt phần mở rộng Python. Bạn cũng cần phải cài miniconda như mô tả ở trên.

> **Lưu ý**: Nếu VS Code gợi ý bạn mở lại kho trong container, bạn nên từ chối để sử dụng cài đặt Python cục bộ.

### Sử dụng Jupyter trên trình duyệt

Bạn cũng có thể sử dụng môi trường Jupyter từ trình duyệt trên máy cá nhân. Cả Jupyter truyền thống và JupyterHub đều cung cấp môi trường phát triển tiện lợi với tự động hoàn thành, tô sáng mã, v.v.

Để khởi động Jupyter trên máy, hãy chuyển đến thư mục của khóa học, và chạy:

```bash
jupyter notebook
```
hoặc
```bash
jupyterhub
```
Bạn sau đó có thể mở bất kỳ tập tin `.ipynb` nào để bắt đầu làm việc.

### Chạy trong container

Một lựa chọn thay thế cho việc cài đặt Python là chạy mã trong container. Vì kho của chúng tôi cung cấp thư mục `.devcontainer` đặc biệt hướng dẫn cách xây dựng container cho kho này, VS Code sẽ cung cấp tùy chọn mở lại mã trong container. Điều này yêu cầu cài Docker, và cũng phức tạp hơn, nên chúng tôi khuyến nghị cho người dùng có kinh nghiệm hơn.

## Chạy trên điện toán đám mây

Nếu bạn không muốn cài Python trên máy và có quyền truy cập một số tài nguyên đám mây - lựa chọn tốt là chạy mã trên đám mây. Có một số cách bạn có thể làm điều này:

* Sử dụng **[GitHub Codespaces](https://github.com/features/codespaces)**, một môi trường ảo được tạo trên GitHub cho bạn, truy cập qua giao diện trình duyệt VS Code. Nếu bạn có quyền truy cập Codespaces, bạn chỉ cần bấm nút **Code** trong repo, khởi tạo một codespace và bắt đầu ngay lập tức.
* Sử dụng **[Binder](https://mybinder.org/v2/gh/microsoft/ai-for-beginners/HEAD)**. [Binder](https://mybinder.org) cung cấp tài nguyên tính toán miễn phí trên đám mây cho người dùng như bạn để thử mã trên GitHub. Có một nút ở trang đầu để mở kho trong Binder - điều này sẽ nhanh chóng đưa bạn đến trang Binder, nơi xây dựng một container bên dưới và khởi động giao diện web Jupyter cho bạn một cách liền mạch.

> **Lưu ý**: Để ngăn ngừa sử dụng sai mục đích, Binder chặn truy cập một số tài nguyên web. Điều này có thể làm một số mã không hoạt động vì phải lấy mô hình và/hoặc bộ dữ liệu từ Internet công cộng. Bạn có thể cần tìm cách giải quyết. Ngoài ra, tài nguyên tính toán do Binder cung cấp khá cơ bản, nên việc huấn luyện sẽ chậm, đặc biệt trong các bài học phức tạp hơn sau này.

## Chạy trên đám mây với GPU

Một số bài học sau trong chương trình sẽ rất cần GPU. Việc huấn luyện mô hình, ví dụ, có thể rất chậm nếu không có GPU. Có vài tùy chọn bạn có thể theo, nhất là nếu bạn có quyền truy cập đám mây thông qua [Azure for Students](https://azure.microsoft.com/free/students/?WT.mc_id=academic-77998-cacaste), hoặc qua tổ chức của bạn:

* Tạo [Máy ảo Khoa học Dữ liệu](https://docs.microsoft.com/learn/modules/intro-to-azure-data-science-virtual-machine/?WT.mc_id=academic-77998-cacaste) và kết nối đến nó qua Jupyter. Bạn có thể clone repo ngay lên máy và bắt đầu học. Máy ảo dòng NC có hỗ trợ GPU.

> **Lưu ý**: Một số gói đăng ký, bao gồm Azure for Students, không cung cấp GPU mặc định. Bạn có thể cần gửi yêu cầu hỗ trợ kỹ thuật để nhận thêm lõi GPU.

* Tạo [Azure Machine Learning Workspace](https://azure.microsoft.com/services/machine-learning/?WT.mc_id=academic-77998-cacaste) và sử dụng tính năng Notebook ở đó. [Video này](https://azure-for-academics.github.io/quickstart/azureml-papers/) hướng dẫn cách clone repo vào notebook Azure ML và bắt đầu sử dụng.

Bạn cũng có thể sử dụng Google Colab, có hỗ trợ GPU miễn phí, và tải các Jupyter Notebooks lên đó để thực thi từng notebook một.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Tuyên bố từ chối trách nhiệm**:
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng các bản dịch tự động có thể chứa lỗi hoặc không chính xác. Tài liệu gốc bằng ngôn ngữ gốc nên được xem là nguồn tham khảo chính thức. Đối với những thông tin quan trọng, nên sử dụng dịch vụ dịch thuật chuyên nghiệp do con người thực hiện. Chúng tôi không chịu trách nhiệm về bất kỳ sự hiểu lầm hay giải thích sai nào phát sinh từ việc sử dụng bản dịch này.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->