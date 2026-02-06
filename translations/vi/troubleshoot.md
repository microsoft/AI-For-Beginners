# Hướng Dẫn Khắc Phục Sự Cố AI-For-Beginners

Hướng dẫn này giúp bạn giải quyết các vấn đề thường gặp khi sử dụng hoặc đóng góp vào kho lưu trữ [AI-For-Beginners](https://github.com/microsoft/AI-For-Beginners). Mỗi vấn đề bao gồm thông tin nền, triệu chứng, giải thích và các bước giải quyết cụ thể.

---

## Mục Lục

- [Các Vấn Đề Chung](../..)
- [Vấn Đề Cài Đặt](../..)
- [Vấn Đề Cấu Hình](../..)
- [Chạy Notebooks](../..)
- [Vấn Đề Hiệu Suất](../..)
- [Vấn Đề Trang Web Giáo Trình](../..)
- [Vấn Đề Đóng Góp](../..)
- [Câu Hỏi Thường Gặp](../..)
- [Nhận Hỗ Trợ](../..)

---

## Các Vấn Đề Chung

### 1. Không Thể Clone Repository

**Thông tin nền:** Clone cho phép bạn sao chép kho lưu trữ về máy của mình.

**Triệu chứng:**
- Lỗi: `fatal: repository not found`
- Lỗi: `Permission denied (publickey)`

**Nguyên nhân có thể:**
- URL kho lưu trữ không chính xác
- Quyền truy cập không đủ
- Chưa cấu hình SSH keys

**Giải pháp:**
1. **Kiểm tra URL kho lưu trữ.**  
   Sử dụng URL HTTPS:  
   ```
   git clone https://github.com/microsoft/AI-For-Beginners.git
   ```
2. **Chuyển sang HTTPS nếu SSH không hoạt động.**  
   Nếu bạn thấy lỗi `Permission denied (publickey)`, hãy sử dụng liên kết HTTPS ở trên thay vì SSH.
3. **Cấu hình SSH keys (tùy chọn).**  
   Nếu bạn muốn sử dụng SSH, hãy làm theo [hướng dẫn SSH của GitHub](https://docs.github.com/en/authentication/connecting-to-github-with-ssh).

---

## Vấn Đề Cài Đặt

### 2. Vấn Đề Môi Trường Python

**Thông tin nền:** Kho lưu trữ dựa vào Python và các thư viện khác nhau.

**Triệu chứng:**
- Lỗi: `ModuleNotFoundError: No module named '<package>'`
- Lỗi import khi chạy script hoặc notebook

**Nguyên nhân có thể:**
- Chưa cài đặt các phụ thuộc
- Phiên bản Python không đúng

**Giải pháp:**
1. **Thiết lập môi trường ảo.**  
   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
   ```
2. **Cài đặt các phụ thuộc.**  
   ```bash
   pip install -r requirements.txt
   ```
3. **Kiểm tra phiên bản Python.**  
   Sử dụng Python 3.7 hoặc mới hơn.  
   ```bash
   python --version
   ```

### 3. Jupyter Chưa Được Cài Đặt

**Thông tin nền:** Notebooks là tài nguyên học tập cốt lõi.

**Triệu chứng:**
- Lỗi: `jupyter: command not found`
- Không thể mở notebook

**Nguyên nhân có thể:**
- Jupyter chưa được cài đặt

**Giải pháp:**
1. **Cài đặt Jupyter Notebook.**  
   ```bash
   pip install notebook
   ```
   hoặc, nếu sử dụng Anaconda:
   ```bash
   conda install notebook
   ```
2. **Khởi động Jupyter Notebook.**  
   ```bash
   jupyter notebook
   ```

### 4. Xung Đột Phiên Bản Phụ Thuộc

**Thông tin nền:** Dự án có thể bị lỗi nếu phiên bản gói không khớp.

**Triệu chứng:**
- Lỗi hoặc cảnh báo về phiên bản không tương thích

**Nguyên nhân có thể:**
- Các gói Python cũ hoặc xung đột

**Giải pháp:**
1. **Cài đặt trong môi trường sạch.**  
   Xóa venv/conda env cũ và tạo một môi trường mới.
2. **Sử dụng phiên bản chính xác.**  
   Luôn chạy:
   ```bash
   pip install -r requirements.txt
   ```
   Nếu thất bại, cài đặt thủ công các gói bị thiếu như được mô tả trong README.

---

## Vấn Đề Cấu Hình

### 5. Biến Môi Trường Chưa Được Thiết Lập

**Thông tin nền:** Một số module có thể yêu cầu khóa, token hoặc cài đặt cấu hình.

**Triệu chứng:**
- Lỗi: `KeyError` hoặc cảnh báo về cấu hình bị thiếu

**Nguyên nhân có thể:**
- Biến môi trường cần thiết chưa được thiết lập

**Giải pháp:**
1. **Kiểm tra tệp `.env.example` hoặc các tệp tương tự.**
2. **Tạo tệp `.env` và điền các giá trị cần thiết.**
3. **Tải lại terminal hoặc IDE sau khi thiết lập biến môi trường.**

---

## Chạy Notebooks

### 6. Notebook Không Mở Hoặc Chạy Được

**Thông tin nền:** Jupyter notebooks cần được thiết lập đúng cách.

**Triệu chứng:**
- Notebook không thể khởi chạy
- Trình duyệt không tự động mở

**Nguyên nhân có thể:**
- Jupyter chưa được cài đặt
- Vấn đề cấu hình trình duyệt

**Giải pháp:**
1. **Cài đặt Jupyter (xem Vấn Đề Cài Đặt ở trên).**
2. **Mở notebook thủ công.**
   - Sao chép URL từ terminal (ví dụ: `http://localhost:8888/?token=...`) và dán vào trình duyệt.

### 7. Kernel Bị Crash Hoặc Đóng Băng

**Thông tin nền:** Kernel của notebook có thể bị crash do giới hạn tài nguyên hoặc lỗi mã.

**Triệu chứng:**
- Kernel chết hoặc khởi động lại liên tục
- Lỗi hết bộ nhớ

**Nguyên nhân có thể:**
- Dữ liệu lớn
- Mã hoặc gói không tương thích

**Giải pháp:**
1. **Khởi động lại kernel.**  
   Sử dụng nút "Restart Kernel" trong Jupyter.
2. **Kiểm tra mức sử dụng bộ nhớ.**  
   Đóng các ứng dụng không sử dụng.
3. **Chạy notebook trên nền tảng đám mây.**  
   Sử dụng [Google Colab](https://colab.research.google.com/) hoặc [Azure Notebooks](https://notebooks.azure.com/).

---

## Vấn Đề Hiệu Suất

### 8. Notebook Chạy Chậm

**Thông tin nền:** Một số tác vụ AI yêu cầu bộ nhớ và CPU lớn.

**Triệu chứng:**
- Thực thi chậm
- Quạt laptop chạy ồn

**Nguyên nhân có thể:**
- Dữ liệu hoặc mô hình lớn
- Tài nguyên hệ thống hạn chế

**Giải pháp:**
1. **Sử dụng nền tảng đám mây.**
   - Tải notebook lên Colab hoặc Azure Notebooks.
2. **Giảm kích thước dữ liệu.**
   - Sử dụng dữ liệu mẫu để thực hành.
3. **Đóng các chương trình không cần thiết.**
   - Giải phóng RAM hệ thống.

---

## Vấn Đề Trang Web Giáo Trình

### 9. Chương Không Tải Được

**Thông tin nền:** Giáo trình trực tuyến hiển thị các bài học và chương.

**Triệu chứng:**
- Một chương (ví dụ: Transformers/BERT) bị thiếu hoặc không mở được

**Vấn đề đã biết:**  
- [Vấn đề #303](https://github.com/microsoft/AI-For-Beginners/issues/303): “18 Transformers. BERT. không thể mở trên trang web giáo trình.” Do lỗi tên tệp (`READMEtransformers.md` thay vì `README.md`).

**Giải pháp:**
1. **Kiểm tra lỗi đổi tên tệp.**  
   Nếu bạn là người đóng góp, đảm bảo các tệp chương được đặt tên là `README.md`.
2. **Báo cáo tệp bị thiếu.**  
   Mở một vấn đề trên GitHub với tên chương và chi tiết lỗi.

---

## Vấn Đề Đóng Góp

### 10. PR Không Được Chấp Nhận Hoặc Build Bị Lỗi

**Thông tin nền:** Các đóng góp phải vượt qua kiểm tra và tuân theo hướng dẫn.

**Triệu chứng:**
- Pull request bị từ chối
- Lỗi pipeline CI/CD

**Nguyên nhân có thể:**
- Kiểm tra thất bại
- Không tuân thủ tiêu chuẩn mã hóa

**Giải pháp:**
1. **Đọc hướng dẫn đóng góp.**
   - Tuân theo [CONTRIBUTING.md](https://github.com/microsoft/AI-For-Beginners/blob/main/CONTRIBUTING.md) của kho lưu trữ.
2. **Chạy kiểm tra cục bộ trước khi đẩy lên.**
3. **Kiểm tra quy tắc linting hoặc yêu cầu định dạng.**

---

## Câu Hỏi Thường Gặp

### Tôi có thể tìm trợ giúp cho các module cụ thể ở đâu?
- Mỗi module thường có README riêng. Bắt đầu từ đó để biết cách thiết lập và sử dụng.

### Làm thế nào để báo cáo lỗi hoặc yêu cầu tính năng?
- [Mở một vấn đề trên GitHub](https://github.com/microsoft/AI-For-Beginners/issues/new) với mô tả rõ ràng và các bước để tái hiện.

### Tôi có thể yêu cầu trợ giúp nếu vấn đề của tôi không được liệt kê?
- Có! Tìm kiếm các vấn đề hiện có trước, và nếu không tìm thấy vấn đề của bạn, hãy tạo một vấn đề mới.

---

## Nhận Hỗ Trợ

- **Kiểm tra Vấn Đề:** [GitHub Issues](https://github.com/microsoft/AI-For-Beginners/issues)
- **Đặt Câu Hỏi:** Sử dụng GitHub Discussions hoặc mở một vấn đề.
- **Cộng Đồng:** Xem các liên kết trong kho lưu trữ để tham gia chat/diễn đàn.

---

_Cập nhật lần cuối: 20-09-2025_

---

**Tuyên bố miễn trừ trách nhiệm**:  
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng các bản dịch tự động có thể chứa lỗi hoặc không chính xác. Tài liệu gốc bằng ngôn ngữ bản địa nên được coi là nguồn thông tin chính thức. Đối với các thông tin quan trọng, khuyến nghị sử dụng dịch vụ dịch thuật chuyên nghiệp bởi con người. Chúng tôi không chịu trách nhiệm cho bất kỳ sự hiểu lầm hoặc diễn giải sai nào phát sinh từ việc sử dụng bản dịch này.