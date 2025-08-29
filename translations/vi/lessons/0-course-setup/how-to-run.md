<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "7df19702b8d2d3f7c4238c51bec2c8fc",
  "translation_date": "2025-08-29T12:16:25+00:00",
  "source_file": "lessons/0-course-setup/how-to-run.md",
  "language_code": "vi"
}
-->
# Cách Chạy Mã

Chương trình học này chứa rất nhiều ví dụ và bài thực hành có thể chạy được mà bạn sẽ muốn thử nghiệm. Để làm điều này, bạn cần khả năng thực thi mã Python trong Jupyter Notebooks được cung cấp như một phần của chương trình học. Bạn có một số lựa chọn để chạy mã:

## Chạy trên máy tính cá nhân

Để chạy mã trên máy tính cá nhân, bạn cần cài đặt một phiên bản Python nào đó. Cá nhân tôi khuyên bạn nên cài đặt **[miniconda](https://conda.io/en/latest/miniconda.html)** - đây là một cài đặt nhẹ hỗ trợ trình quản lý gói `conda` cho các **môi trường ảo** Python khác nhau.

Sau khi cài đặt miniconda, bạn cần sao chép kho lưu trữ và tạo một môi trường ảo để sử dụng cho khóa học này:

```bash
git clone http://github.com/microsoft/ai-for-beginners
cd ai-for-beginners
conda env create --name ai4beg --file .devcontainer/environment.yml
conda activate ai4beg
```

### Sử dụng Visual Studio Code với Python Extension

Có lẽ cách tốt nhất để sử dụng chương trình học là mở nó trong [Visual Studio Code](http://code.visualstudio.com/?WT.mc_id=academic-77998-cacaste) với [Python Extension](https://marketplace.visualstudio.com/items?itemName=ms-python.python&WT.mc_id=academic-77998-cacaste).

> **Lưu ý**: Khi bạn sao chép và mở thư mục trong VS Code, nó sẽ tự động gợi ý bạn cài đặt các tiện ích mở rộng Python. Bạn cũng cần cài đặt miniconda như đã mô tả ở trên.

> **Lưu ý**: Nếu VS Code gợi ý bạn mở lại kho lưu trữ trong container, bạn cần từ chối để sử dụng cài đặt Python cục bộ.

### Sử dụng Jupyter trong Trình duyệt

Bạn cũng có thể sử dụng môi trường Jupyter trực tiếp từ trình duyệt trên máy tính của mình. Thực tế, cả Jupyter cổ điển và Jupyter Hub đều cung cấp môi trường phát triển khá tiện lợi với tính năng tự động hoàn thành, tô sáng mã, v.v.

Để khởi động Jupyter cục bộ, hãy vào thư mục của khóa học và thực thi:

```bash
jupyter notebook
```
hoặc
```bash
jupyterhub
```
Sau đó, bạn có thể điều hướng đến bất kỳ tệp `.ipynb` nào, mở chúng và bắt đầu làm việc.

### Chạy trong container

Một lựa chọn thay thế cho việc cài đặt Python là chạy mã trong container. Vì kho lưu trữ của chúng tôi chứa thư mục `.devcontainer` đặc biệt hướng dẫn cách xây dựng container cho kho này, VS Code sẽ đề xuất bạn mở lại mã trong container. Điều này sẽ yêu cầu cài đặt Docker và cũng phức tạp hơn, vì vậy chúng tôi khuyến nghị điều này cho những người dùng có kinh nghiệm hơn.

## Chạy trên Đám mây

Nếu bạn không muốn cài đặt Python cục bộ và có quyền truy cập vào một số tài nguyên đám mây - một lựa chọn tốt là chạy mã trên đám mây. Có một số cách bạn có thể làm điều này:

* Sử dụng **[GitHub Codespaces](https://github.com/features/codespaces)**, đây là một môi trường ảo được tạo cho bạn trên GitHub, có thể truy cập thông qua giao diện trình duyệt của VS Code. Nếu bạn có quyền truy cập vào Codespaces, bạn chỉ cần nhấp vào nút **Code** trong kho, bắt đầu một codespace và chạy ngay lập tức.
* Sử dụng **[Binder](https://mybinder.org/v2/gh/microsoft/ai-for-beginners/HEAD)**. [Binder](https://mybinder.org) là tài nguyên tính toán miễn phí được cung cấp trên đám mây cho những người như bạn để thử nghiệm một số mã trên GitHub. Có một nút ở trang đầu để mở kho lưu trữ trong Binder - điều này sẽ nhanh chóng đưa bạn đến trang Binder, nơi sẽ xây dựng container cơ bản và khởi động giao diện web Jupyter cho bạn một cách liền mạch.

> **Lưu ý**: Để ngăn chặn việc sử dụng sai mục đích, Binder đã chặn quyền truy cập vào một số tài nguyên web. Điều này có thể ngăn một số mã hoạt động, đặc biệt là mã tải mô hình và/hoặc tập dữ liệu từ Internet công cộng. Bạn có thể cần tìm một số giải pháp thay thế. Ngoài ra, tài nguyên tính toán được cung cấp bởi Binder khá cơ bản, vì vậy việc huấn luyện sẽ chậm, đặc biệt trong các bài học phức tạp hơn sau này.

## Chạy trên Đám mây với GPU

Một số bài học sau trong chương trình học này sẽ được hưởng lợi rất nhiều từ việc hỗ trợ GPU, vì nếu không, việc huấn luyện sẽ rất chậm. Có một vài lựa chọn bạn có thể thực hiện, đặc biệt nếu bạn có quyền truy cập vào đám mây thông qua [Azure for Students](https://azure.microsoft.com/free/students/?WT.mc_id=academic-77998-cacaste) hoặc thông qua tổ chức của bạn:

* Tạo [Máy Ảo Khoa Học Dữ Liệu](https://docs.microsoft.com/learn/modules/intro-to-azure-data-science-virtual-machine/?WT.mc_id=academic-77998-cacaste) và kết nối với nó thông qua Jupyter. Sau đó, bạn có thể sao chép kho lưu trữ trực tiếp vào máy và bắt đầu học. Các máy ảo dòng NC có hỗ trợ GPU.

> **Lưu ý**: Một số gói đăng ký, bao gồm Azure for Students, không cung cấp hỗ trợ GPU ngay lập tức. Bạn có thể cần yêu cầu thêm lõi GPU thông qua yêu cầu hỗ trợ kỹ thuật.

* Tạo [Azure Machine Learning Workspace](https://azure.microsoft.com/services/machine-learning/?WT.mc_id=academic-77998-cacaste) và sau đó sử dụng tính năng Notebook ở đó. [Video này](https://azure-for-academics.github.io/quickstart/azureml-papers/) hướng dẫn cách sao chép một kho lưu trữ vào notebook Azure ML và bắt đầu sử dụng.

Bạn cũng có thể sử dụng Google Colab, nơi cung cấp một số hỗ trợ GPU miễn phí, và tải lên các Jupyter Notebooks để thực thi từng cái một.

---

**Tuyên bố miễn trừ trách nhiệm**:  
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng các bản dịch tự động có thể chứa lỗi hoặc không chính xác. Tài liệu gốc bằng ngôn ngữ bản địa nên được coi là nguồn tham khảo chính thức. Đối với các thông tin quan trọng, chúng tôi khuyến nghị sử dụng dịch vụ dịch thuật chuyên nghiệp từ con người. Chúng tôi không chịu trách nhiệm cho bất kỳ sự hiểu lầm hoặc diễn giải sai nào phát sinh từ việc sử dụng bản dịch này.