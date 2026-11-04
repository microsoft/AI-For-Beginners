# Cách Chạy Mã Lệnh

Chương trình học này chứa nhiều ví dụ và bài lab có thể thực thi mà bạn sẽ muốn chạy. Để làm điều này, bạn cần khả năng thực thi mã Python trong Jupyter Notebooks được cung cấp như một phần của chương trình học này. Bạn có nhiều lựa chọn để chạy mã:

## Chạy cục bộ trên máy tính của bạn

Để chạy mã cục bộ trên máy tính, bạn cần cài đặt Python. Một đề xuất là cài đặt **[miniconda](https://conda.io/en/latest/miniconda.html)** - đây là một bản cài đặt nhẹ hỗ trợ trình quản lý gói `conda` cho các **môi trường ảo** Python khác nhau.

Sau khi cài miniconda, hãy sao chép kho lưu trữ này và tạo một môi trường ảo để sử dụng cho khóa học:

```bash
git clone http://github.com/microsoft/ai-for-beginners
cd ai-for-beginners
conda env create --name ai4beg --file .devcontainer/environment.yml
conda activate ai4beg
```

> **Lưu ý Windows**: Nếu việc tạo môi trường thất bại khi cài đặt `gdk-pixbuf` với một `UnicodeDecodeError` báo lỗi codec `gbk`, hãy bật chế độ UTF-8 của Python trong terminal của bạn và thử lại. Sử dụng cú pháp phù hợp với terminal bạn đang dùng:
>
> **PowerShell:**
>
> ```powershell
> $env:PYTHONUTF8 = "1"
> conda env create --name ai4beg --file .devcontainer/environment.yml
> ```
>
> **Command Prompt (`cmd.exe`) hoặc Anaconda Prompt:**
>
> ```cmd
> set PYTHONUTF8=1
> conda env create --name ai4beg --file .devcontainer/environment.yml
> ```
>
> **Bash, bao gồm Git Bash:**
>
> ```bash
> export PYTHONUTF8=1
> conda env create --name ai4beg --file .devcontainer/environment.yml
> ```
>
> Nếu một lần thử thất bại để lại môi trường `ai4beg`, hãy hủy kích hoạt nó và xóa môi trường đó trước khi thử lại. Sử dụng `conda deactivate` trước khi môi trường đang được kích hoạt:
>
> ```text
> conda deactivate
> conda env remove --name ai4beg
> ```

### Sử dụng Visual Studio Code với Extension Python

Chương trình học này được sử dụng tốt nhất khi mở trong [Visual Studio Code](http://code.visualstudio.com/?WT.mc_id=academic-77998-cacaste) với [Python Extension](https://marketplace.visualstudio.com/items?itemName=ms-python.python&WT.mc_id=academic-77998-cacaste).

> **Lưu ý**: Khi bạn sao chép và mở thư mục trong VS Code, nó sẽ tự động đề xuất bạn cài đặt các extension Python. Bạn cũng cần cài miniconda như mô tả ở trên.

> **Lưu ý**: Nếu VS Code đề xuất bạn mở lại kho lưu trữ trong một container, bạn nên từ chối để sử dụng cài đặt Python cục bộ.

### Sử dụng Jupyter trong trình duyệt

Bạn cũng có thể sử dụng môi trường Jupyter từ trình duyệt trên máy tính của mình. Cả Jupyter cổ điển và JupyterHub đều cung cấp môi trường phát triển tiện lợi với tự động hoàn thành, tô sáng mã code, v.v.

Để khởi động Jupyter cục bộ, vào thư mục khóa học và thực thi:

```bash
jupyter notebook
```
hoặc
```bash
jupyterhub
```
Bạn có thể điều hướng đến bất kỳ tệp `.ipynb` nào, mở chúng và bắt đầu làm việc.

### Chạy trong container

Một lựa chọn thay thế cho việc cài Python là chạy mã trong container. Vì kho lưu trữ của chúng tôi cung cấp thư mục `.devcontainer` đặc biệt chỉ dẫn cách xây dựng container cho repo này, VS Code cung cấp tùy chọn mở lại mã trong container. Điều này yêu cầu cài Docker và phức tạp hơn, vì vậy chúng tôi khuyên những người dùng có kinh nghiệm nên sử dụng.

## Chạy trên Cloud

Nếu bạn không muốn cài Python cục bộ và có quyền truy cập tài nguyên đám mây - một lựa chọn tốt là chạy mã trên đám mây. Có vài cách bạn có thể làm điều này:

* Sử dụng **[GitHub Codespaces](https://github.com/features/codespaces)**, một môi trường ảo được tạo cho bạn trên GitHub, truy cập qua giao diện trình duyệt của VS Code. Nếu bạn có quyền truy cập Codespaces, bạn chỉ cần nhấn nút **Code** trong repo, bắt đầu codespace và chạy ngay lập tức.
* Sử dụng **[Binder](https://mybinder.org/v2/gh/microsoft/ai-for-beginners/HEAD)**. [Binder](https://mybinder.org) cung cấp tài nguyên tính toán miễn phí trên đám mây cho người dùng kiểm thử mã trên GitHub. Có nút trên trang đầu để mở repo bằng Binder - điều này sẽ nhanh chóng chuyển bạn đến trang Binder, nơi xây dựng container nền tảng và khởi động giao diện web Jupyter cho bạn.

> **Lưu ý**: Để tránh lạm dụng, Binder chặn quyền truy cập một số tài nguyên web. Điều này có thể làm một số đoạn mã không hoạt động, nhất là các mã tải mô hình và/hoặc bộ dữ liệu từ Internet công cộng. Bạn có thể cần tìm giải pháp thay thế. Ngoài ra, tài nguyên tính toán do Binder cung cấp khá cơ bản nên việc huấn luyện sẽ chậm, đặc biệt trong các bài học phức tạp sau.

## Chạy trên Cloud với GPU

Một số bài học sau trong chương trình sẽ được lợi rất nhiều từ hỗ trợ GPU. Việc huấn luyện mô hình, ví dụ, sẽ rất chậm nếu không có GPU. Có một vài lựa chọn bạn có thể làm, đặc biệt nếu bạn có quyền truy cập đám mây thông qua [Azure for Students](https://azure.microsoft.com/free/students/?WT.mc_id=academic-77998-cacaste), hoặc qua tổ chức của bạn:

* Tạo [Máy ảo Khoa học Dữ liệu](https://docs.microsoft.com/learn/modules/intro-to-azure-data-science-virtual-machine/?WT.mc_id=academic-77998-cacaste) và kết nối thông qua Jupyter. Bạn có thể sao chép repo trực tiếp lên máy và bắt đầu học. Máy ảo dòng NC có hỗ trợ GPU.

> **Lưu ý**: Một số gói đăng ký, bao gồm Azure for Students, không tự động hỗ trợ GPU. Bạn có thể phải yêu cầu thêm lõi GPU qua kênh hỗ trợ kỹ thuật.

* Tạo [Azure Machine Learning Workspace](https://azure.microsoft.com/services/machine-learning/?WT.mc_id=academic-77998-cacaste) sau đó dùng tính năng Notebook tại đó. [Video này](https://azure-for-academics.github.io/quickstart/azureml-papers/) hướng dẫn cách sao chép repo vào notebook Azure ML và bắt đầu sử dụng.

Bạn cũng có thể dùng Google Colab, cung cấp GPU miễn phí và tải lên Jupyter Notebooks để thực thi từng cái một.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Tuyên bố miễn trừ trách nhiệm**:
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng bản dịch tự động có thể chứa lỗi hoặc sai sót. Tài liệu gốc bằng ngôn ngữ gốc nên được coi là nguồn tin chính thức. Đối với thông tin quan trọng, nên sử dụng dịch vụ dịch thuật chuyên nghiệp bởi con người. Chúng tôi không chịu trách nhiệm về bất kỳ hiểu lầm hoặc giải thích sai nào phát sinh từ việc sử dụng bản dịch này.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->