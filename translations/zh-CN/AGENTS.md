# AGENTS.md

## 项目概述

AI for Beginners 是一个为期 12 周、共 24 节课的全面课程，涵盖人工智能基础知识。该教育资源库包括使用 Jupyter Notebooks 的实践课程、测验和动手实验。课程内容包括：

- 符号 AI：知识表示与专家系统
- 使用 TensorFlow 和 PyTorch 的神经网络与深度学习
- 计算机视觉技术与架构
- 自然语言处理（NLP），包括 transformers 和 BERT
- 专题内容：遗传算法、强化学习、多智能体系统
- AI 伦理与负责任的 AI 原则

**关键技术：** Python 3、Jupyter Notebooks、TensorFlow、PyTorch、Keras、OpenCV、Vue.js（用于测验应用）

**架构：** 教育内容资源库，按主题区域组织的 Jupyter Notebooks，辅以基于 Vue.js 的测验应用和广泛的多语言支持。

## 设置命令

### 主要开发环境（Python/Jupyter）

课程设计基于 Python 和 Jupyter Notebooks 运行。推荐使用 miniconda：

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

### 替代方案：使用 devcontainer

```bash
# Open in VS Code and select "Reopen in Container" when prompted
# The devcontainer will automatically set up the environment
```

### 测验应用设置

测验应用是一个独立的 Vue.js 应用，位于 `etc/quiz-app/`：

```bash
cd etc/quiz-app
npm install
npm run serve  # Development server
npm run build  # Production build
npm run lint   # Lint and fix files
```

## 开发工作流

### 使用 Jupyter Notebooks

1. **本地开发：**
   - 激活 conda 环境：`conda activate ai4beg`
   - 启动 Jupyter：`jupyter notebook` 或 `jupyter lab`
   - 导航到课程文件夹并打开 `.ipynb` 文件
   - 交互式运行单元格以跟随课程内容

2. **使用 VS Code 和 Python 扩展：**
   - 在 VS Code 中打开资源库
   - 安装 Python 扩展
   - VS Code 会自动检测并使用 conda 环境
   - 直接在 VS Code 中打开 `.ipynb` 文件

3. **云端开发：**
   - **GitHub Codespaces：** 点击“Code” → “Codespaces” → “Create codespace on main”
   - **Binder：** 使用 README 中的 Binder 徽章在浏览器中启动
   - 注意：Binder 资源有限且有部分网络访问限制

### 高级课程的 GPU 支持

后续课程显著受益于 GPU 加速：

- **Azure Data Science VM：** 使用支持 GPU 的 NC 系列虚拟机
- **Azure Machine Learning：** 使用带 GPU 计算的 notebook 功能
- **Google Colab：** 单独上传 notebooks（提供免费 GPU 支持）

### 测验应用开发

```bash
cd etc/quiz-app
npm run serve  # Hot-reload development server at http://localhost:8080
```

## 测试说明

这是一个以学习内容为重点的教育资源库，而非软件测试，因此没有传统的测试套件。

### 验证方法：

1. **Jupyter Notebooks：** 按顺序执行单元格以验证代码示例是否正常运行
2. **测验应用测试：** 通过开发服务器进行手动测试
3. **翻译验证：** 检查 `translations/` 文件夹中的翻译内容
4. **测验应用代码检查：** 在 `etc/quiz-app/` 中运行 `npm run lint`

### 运行代码示例：

```bash
# Activate environment first
conda activate ai4beg

# Run Python scripts directly
python lessons/4-ComputerVision/07-ConvNets/pytorchcv.py

# Or execute notebooks
jupyter notebook lessons/3-NeuralNetworks/03-Perceptron/Perceptron.ipynb
```

## 代码风格

### Python 代码风格

- 遵循教育代码的标准 Python 约定
- 代码清晰易读，优先考虑学习而非优化
- 注释解释关键概念
- 适配 Jupyter Notebook：尽量使单元格自包含
- 对课程内容没有严格的代码检查要求

### JavaScript/Vue.js（测验应用）

- ESLint 配置位于 `etc/quiz-app/package.json`
- 运行 `npm run lint` 检查并自动修复问题
- 遵循 Vue 2.x 约定
- 基于组件的架构

### 文件组织

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

## 构建与部署

### Jupyter 内容

无需构建过程 - Jupyter Notebooks 可直接执行。

### 测验应用

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

### 文档站点

该资源库使用 Docsify 进行文档管理：
- `index.html` 作为入口点
- 无需构建 - 直接通过 GitHub Pages 提供服务
- 访问地址：https://microsoft.github.io/AI-For-Beginners/

## 贡献指南

### 拉取请求流程

1. **标题格式：** 清晰、描述性的标题，说明更改内容
2. **CLA 要求：** 必须签署 Microsoft CLA（自动检查）
3. **内容指南：**
   - 保持教育重点和面向初学者的风格
   - 测试 notebooks 中的所有代码示例
   - 确保 notebooks 能从头到尾运行
   - 如果修改英文内容，请更新翻译
4. **测验应用更改：** 提交前运行 `npm run lint`

### 翻译贡献

- 翻译通过 GitHub Actions 使用 co-op-translator 自动完成
- 手动翻译存放在 `translations/<language-code>/`
- 测验翻译存放在 `etc/quiz-app/src/assets/translations/`
- 支持语言：40+ 种语言（完整列表见 README）

### 活跃贡献领域

请参阅 `etc/CONTRIBUTING.md` 了解当前需求：
- 深度强化学习部分
- 目标检测改进
- 命名实体识别示例
- 自定义嵌入训练样本

## 环境配置

### 所需依赖项

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

### 环境变量

基本使用无需特殊环境变量。

对于 Azure 部署（测验应用）：
- `AZURE_STATIC_WEB_APPS_API_TOKEN`（由 Azure 自动设置）

## 调试与故障排除

### 常见问题

**问题：** Conda 环境创建失败  
- **解决方案：** 先更新 conda：`conda update conda -y`  
- 确保磁盘空间充足（建议 50GB）

**问题：** 找不到 Jupyter 内核  
- **解决方案：**  
  ```bash
  conda activate ai4beg
  python -m ipykernel install --user --name ai4beg
  ```

**问题：** Notebooks 中未检测到 GPU  
- **解决方案：**  
  - 验证 CUDA 安装：`nvidia-smi`  
  - 检查 PyTorch GPU：`python -c "import torch; print(torch.cuda.is_available())"`  
  - 检查 TensorFlow GPU：`python -c "import tensorflow as tf; print(tf.config.list_physical_devices('GPU'))"`

**问题：** 测验应用无法启动  
- **解决方案：**  
  ```bash
  cd etc/quiz-app
  rm -rf node_modules package-lock.json
  npm install
  npm run serve
  ```

**问题：** Binder 超时或阻止下载  
- **解决方案：** 使用 GitHub Codespaces 或本地设置以获得更好的资源访问

### 内存问题

某些课程需要大量内存（建议 8GB+）：  
- 对于资源密集型课程，使用云端虚拟机  
- 训练模型时关闭其他应用  
- 如果内存不足，可在 notebooks 中减少批量大小

## 附加说明

### 课程讲师须知

- 请参阅 `lessons/0-course-setup/for-teachers.md` 获取教学指导
- 课程内容是自包含的，可按顺序教学或单独选择
- 预计时间：每周 2 节课，共 12 周

### 云资源

- **Azure for Students：** 学生可获得免费额度
- **Microsoft Learn：** 提供补充学习路径
- **Binder：** 免费但资源有限，且有部分网络限制

### 代码执行选项

1. **本地（推荐）：** 完全控制，最佳性能，支持 GPU
2. **GitHub Codespaces：** 基于云的 VS Code，快速访问
3. **Binder：** 基于浏览器的 Jupyter，免费但有限
4. **Azure ML Notebooks：** 企业级选项，支持 GPU
5. **Google Colab：** 单独上传 notebooks，提供免费 GPU 层

### 使用 Notebooks

- Notebooks 设计为逐个单元格运行以便学习
- 许多 notebooks 在首次运行时会下载数据集（可能需要一些时间）
- 某些模型训练需要 GPU 才能达到合理的时间
- 尽可能使用预训练模型以减少计算需求

### 性能注意事项

- 后期的计算机视觉课程（CNNs、GANs）受益于 GPU
- NLP transformer 课程可能需要大量内存
- 从头训练是教育性的，但耗时较长
- 迁移学习示例可最大限度减少训练时间

---

**免责声明**：  
本文档使用AI翻译服务 [Co-op Translator](https://github.com/Azure/co-op-translator) 进行翻译。尽管我们努力确保翻译的准确性，但请注意，自动翻译可能包含错误或不准确之处。原始语言的文档应被视为权威来源。对于关键信息，建议使用专业人工翻译。我们不对因使用此翻译而产生的任何误解或误读承担责任。