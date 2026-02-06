# AGENTS.md

## Tổng quan dự án

AI for Beginners là một chương trình học kéo dài 12 tuần với 24 bài học, bao gồm các kiến thức cơ bản về Trí tuệ Nhân tạo. Kho tài liệu giáo dục này bao gồm các bài học thực hành sử dụng Jupyter Notebooks, bài kiểm tra và các phòng thí nghiệm thực hành. Chương trình học bao gồm:

- AI biểu tượng với Đại diện Kiến thức và Hệ thống Chuyên gia
- Mạng Neural và Học sâu với TensorFlow và PyTorch
- Kỹ thuật và kiến trúc Thị giác Máy tính
- Xử lý Ngôn ngữ Tự nhiên (NLP) bao gồm transformers và BERT
- Các chủ đề chuyên biệt: Thuật toán Di truyền, Học Tăng cường, Hệ thống Đa Tác nhân
- Đạo đức AI và nguyên tắc AI có trách nhiệm

**Công nghệ chính:** Python 3, Jupyter Notebooks, TensorFlow, PyTorch, Keras, OpenCV, Vue.js (cho ứng dụng kiểm tra)

**Kiến trúc:** Kho tài liệu giáo dục với Jupyter Notebooks được tổ chức theo các lĩnh vực chủ đề, bổ sung bởi một ứng dụng kiểm tra dựa trên Vue.js và hỗ trợ đa ngôn ngữ rộng rãi.

## Lệnh thiết lập

### Môi trường phát triển chính (Python/Jupyter)

Chương trình học được thiết kế để chạy với Python và Jupyter Notebooks. Cách tiếp cận được khuyến nghị là sử dụng miniconda:

```bash
# Clone the repository
git clone https://github.com/microsoft/ai-for-beginners
cd ai-for-beginners

# Create and activate conda environment
conda env create --name ai4beg --file environment.yml
conda activate ai4beg

# Start Jupyter Notebook
jupyter notebook
# OR
jupyter lab
```

### Lựa chọn thay thế: Sử dụng devcontainer

```bash
# Open in VS Code and select "Reopen in Container" when prompted
# The devcontainer will automatically set up the environment
```

### Thiết lập ứng dụng kiểm tra

Ứng dụng kiểm tra là một ứng dụng Vue.js riêng biệt nằm trong `etc/quiz-app/`:

```bash
cd etc/quiz-app
npm install
npm run serve  # Development server
npm run build  # Production build
npm run lint   # Lint and fix files
```

## Quy trình phát triển

### Làm việc với Jupyter Notebooks

1. **Phát triển cục bộ:**
   - Kích hoạt môi trường conda: `conda activate ai4beg`
   - Khởi động Jupyter: `jupyter notebook` hoặc `jupyter lab`
   - Điều hướng đến các thư mục bài học và mở các tệp `.ipynb`
   - Chạy các ô tương tác để theo dõi bài học

2. **VS Code với tiện ích mở rộng Python:**
   - Mở kho tài liệu trong VS Code
   - Cài đặt tiện ích mở rộng Python
   - VS Code tự động phát hiện và sử dụng môi trường conda
   - Mở trực tiếp các tệp `.ipynb` trong VS Code

3. **Phát triển trên đám mây:**
   - **GitHub Codespaces:** Nhấp vào "Code" → "Codespaces" → "Create codespace on main"
   - **Binder:** Sử dụng huy hiệu Binder trên README để khởi chạy trong trình duyệt
   - Lưu ý: Binder có tài nguyên hạn chế và một số hạn chế truy cập web

### Hỗ trợ GPU cho các bài học nâng cao

Các bài học sau này hưởng lợi đáng kể từ tăng tốc GPU:

- **Azure Data Science VM:** Sử dụng các VM NC-series với hỗ trợ GPU
- **Azure Machine Learning:** Sử dụng các tính năng notebook với tính toán GPU
- **Google Colab:** Tải lên các notebook riêng lẻ (có hỗ trợ GPU miễn phí)

### Phát triển ứng dụng kiểm tra

```bash
cd etc/quiz-app
npm run serve  # Hot-reload development server at http://localhost:8080
```

## Hướng dẫn kiểm tra

Đây là một kho tài liệu giáo dục tập trung vào nội dung học tập hơn là kiểm tra phần mềm. Không có bộ kiểm tra truyền thống.

### Các phương pháp xác thực:

1. **Jupyter Notebooks:** Thực thi các ô theo thứ tự để xác minh các ví dụ mã hoạt động
2. **Kiểm tra ứng dụng kiểm tra:** Kiểm tra thủ công qua máy chủ phát triển
3. **Xác thực bản dịch:** Kiểm tra nội dung đã dịch trong thư mục `translations/`
4. **Linting ứng dụng kiểm tra:** `npm run lint` trong `etc/quiz-app/`

### Chạy các ví dụ mã:

```bash
# Activate environment first
conda activate ai4beg

# Run Python scripts directly
python lessons/4-ComputerVision/07-ConvNets/pytorchcv.py

# Or execute notebooks
jupyter notebook lessons/3-NeuralNetworks/03-Perceptron/Perceptron.ipynb
```

## Phong cách mã

### Phong cách mã Python

- Quy ước Python tiêu chuẩn cho mã giáo dục
- Mã rõ ràng, dễ đọc ưu tiên học tập hơn tối ưu hóa
- Các chú thích giải thích các khái niệm chính
- Thân thiện với Jupyter Notebook: các ô nên tự chứa nếu có thể
- Không yêu cầu linting nghiêm ngặt cho nội dung bài học

### JavaScript/Vue.js (Ứng dụng kiểm tra)

- Cấu hình ESLint trong `etc/quiz-app/package.json`
- Chạy `npm run lint` để kiểm tra và tự động sửa lỗi
- Quy ước Vue 2.x
- Kiến trúc dựa trên thành phần

### Tổ chức tệp

```
lessons/
  ├── 0-course-setup/          # Setup instructions
  ├── 1-Intro/                 # Introduction to AI
  ├── 2-Symbolic/              # Symbolic AI
  ├── 3-NeuralNetworks/        # Neural Networks basics
  ├── 4-ComputerVision/        # Computer Vision
  ├── 5-NLP/                   # Natural Language Processing
  ├── 6-Other/                 # Other AI techniques
  ├── 7-Ethics/                # AI Ethics
  └── X-Extras/                # Additional content

etc/
  ├── quiz-app/                # Vue.js quiz application
  └── quiz-src/                # Quiz source files

translations/                  # Multi-language translations
```

## Xây dựng và triển khai

### Nội dung Jupyter

Không yêu cầu quy trình xây dựng - Jupyter Notebooks được thực thi trực tiếp.

### Ứng dụng kiểm tra

```bash
cd etc/quiz-app

# Development
npm run serve

# Production build
npm run build  # Outputs to etc/quiz-app/dist/

# Deploy to Azure Static Web Apps
# Azure automatically creates GitHub Actions workflow
# See etc/quiz-app/README.md for detailed deployment instructions
```

### Trang tài liệu

Kho tài liệu sử dụng Docsify cho tài liệu:
- `index.html` đóng vai trò là điểm vào
- Không yêu cầu xây dựng - được phục vụ trực tiếp qua GitHub Pages
- Truy cập tại: https://microsoft.github.io/AI-For-Beginners/

## Hướng dẫn đóng góp

### Quy trình Pull Request

1. **Định dạng tiêu đề:** Tiêu đề rõ ràng, mô tả thay đổi
2. **Yêu cầu CLA:** Microsoft CLA phải được ký (kiểm tra tự động)
3. **Hướng dẫn nội dung:**
   - Duy trì trọng tâm giáo dục và cách tiếp cận thân thiện với người mới bắt đầu
   - Kiểm tra tất cả các ví dụ mã trong notebook
   - Đảm bảo notebook chạy từ đầu đến cuối
   - Cập nhật bản dịch nếu chỉnh sửa nội dung tiếng Anh
4. **Thay đổi ứng dụng kiểm tra:** Chạy `npm run lint` trước khi commit

### Đóng góp bản dịch

- Bản dịch được tự động hóa qua GitHub Actions sử dụng co-op-translator
- Bản dịch thủ công nằm trong `translations/<language-code>/`
- Bản dịch kiểm tra nằm trong `etc/quiz-app/src/assets/translations/`
- Ngôn ngữ được hỗ trợ: Hơn 40 ngôn ngữ (xem README để biết danh sách đầy đủ)

### Các lĩnh vực đóng góp tích cực

Xem `etc/CONTRIBUTING.md` để biết các nhu cầu hiện tại:
- Các phần Học Tăng cường Sâu
- Cải tiến Phát hiện Đối tượng
- Ví dụ Nhận dạng Thực thể Được đặt tên
- Mẫu đào tạo nhúng tùy chỉnh

## Cấu hình môi trường

### Các phụ thuộc cần thiết

```bash
# Core Python packages (from requirements.txt)
tensorflow==2.17.0
torch (via conda)
torchvision (via conda)
keras==3.5.0
opencv (via conda)
scikit-learn
numpy==1.26
pandas==2.2.2
matplotlib==3.9
jupyter
```

### Biến môi trường

Không yêu cầu biến môi trường đặc biệt cho việc sử dụng cơ bản.

Đối với triển khai Azure (ứng dụng kiểm tra):
- `AZURE_STATIC_WEB_APPS_API_TOKEN` (được thiết lập tự động bởi Azure)

## Gỡ lỗi và khắc phục sự cố

### Các vấn đề phổ biến

**Vấn đề:** Tạo môi trường conda thất bại
- **Giải pháp:** Cập nhật conda trước: `conda update conda -y`
- Đảm bảo đủ dung lượng đĩa (khuyến nghị 50GB)

**Vấn đề:** Kernel Jupyter không được tìm thấy
- **Giải pháp:** 
  ```bash
  conda activate ai4beg
  python -m ipykernel install --user --name ai4beg
  ```

**Vấn đề:** GPU không được phát hiện trong notebook
- **Giải pháp:** 
  - Xác minh cài đặt CUDA: `nvidia-smi`
  - Kiểm tra GPU PyTorch: `python -c "import torch; print(torch.cuda.is_available())"`
  - Kiểm tra GPU TensorFlow: `python -c "import tensorflow as tf; print(tf.config.list_physical_devices('GPU'))"`

**Vấn đề:** Ứng dụng kiểm tra không khởi động
- **Giải pháp:**
  ```bash
  cd etc/quiz-app
  rm -rf node_modules package-lock.json
  npm install
  npm run serve
  ```

**Vấn đề:** Binder hết thời gian hoặc chặn tải xuống
- **Giải pháp:** Sử dụng GitHub Codespaces hoặc thiết lập cục bộ để truy cập tài nguyên tốt hơn

### Vấn đề về bộ nhớ

Một số bài học yêu cầu RAM lớn (khuyến nghị 8GB+):
- Sử dụng VM đám mây cho các bài học yêu cầu tài nguyên cao
- Đóng các ứng dụng khác khi huấn luyện mô hình
- Giảm kích thước batch trong notebook nếu hết bộ nhớ

## Ghi chú bổ sung

### Dành cho giảng viên khóa học

- Xem `lessons/0-course-setup/for-teachers.md` để biết hướng dẫn giảng dạy
- Các bài học được thiết kế tự chứa và có thể được dạy theo trình tự hoặc chọn riêng lẻ
- Thời gian ước tính: 12 tuần với 2 bài học mỗi tuần

### Tài nguyên đám mây

- **Azure for Students:** Tín dụng miễn phí dành cho sinh viên
- **Microsoft Learn:** Các lộ trình học bổ sung được liên kết xuyên suốt
- **Binder:** Miễn phí nhưng tài nguyên hạn chế và một số hạn chế mạng

### Tùy chọn thực thi mã

1. **Cục bộ (Khuyến nghị):** Kiểm soát đầy đủ, hiệu suất tốt nhất, hỗ trợ GPU
2. **GitHub Codespaces:** VS Code trên đám mây, tốt cho truy cập nhanh
3. **Binder:** Jupyter trên trình duyệt, miễn phí nhưng hạn chế
4. **Azure ML Notebooks:** Tùy chọn doanh nghiệp với hỗ trợ GPU
5. **Google Colab:** Tải lên notebook riêng lẻ, có tầng GPU miễn phí

### Làm việc với Notebooks

- Các notebook được thiết kế để chạy từng ô một để học tập
- Nhiều notebook tải xuống tập dữ liệu khi chạy lần đầu (có thể mất thời gian)
- Một số mô hình yêu cầu GPU để thời gian huấn luyện hợp lý
- Các mô hình đã được huấn luyện trước được sử dụng khi có thể để giảm yêu cầu tính toán

### Cân nhắc về hiệu suất

- Các bài học thị giác máy tính sau này (CNNs, GANs) hưởng lợi từ GPU
- Các bài học NLP transformer có thể yêu cầu RAM lớn
- Huấn luyện từ đầu mang tính giáo dục nhưng tốn thời gian
- Các ví dụ học chuyển tiếp giảm thiểu thời gian huấn luyện

---

**Tuyên bố miễn trừ trách nhiệm**:  
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng các bản dịch tự động có thể chứa lỗi hoặc không chính xác. Tài liệu gốc bằng ngôn ngữ bản địa nên được coi là nguồn thông tin chính thức. Đối với các thông tin quan trọng, khuyến nghị sử dụng dịch vụ dịch thuật chuyên nghiệp bởi con người. Chúng tôi không chịu trách nhiệm cho bất kỳ sự hiểu lầm hoặc diễn giải sai nào phát sinh từ việc sử dụng bản dịch này.