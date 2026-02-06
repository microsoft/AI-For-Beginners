# AI-For-Beginners 故障排查指南

本指南旨在帮助您解决使用或贡献 [AI-For-Beginners](https://github.com/microsoft/AI-For-Beginners) 仓库时遇到的常见问题。每个问题都包括背景信息、症状、原因解释以及逐步解决方案。

---

## 目录

- [常见问题](../..)
- [安装问题](../..)
- [配置问题](../..)
- [运行笔记本](../..)
- [性能问题](../..)
- [教材网站问题](../..)
- [贡献问题](../..)
- [常见问答](../..)
- [获取帮助](../..)

---

## 常见问题

### 1. 仓库无法正确克隆

**背景：** 克隆操作可以将仓库复制到您的机器上。

**症状：**
- 错误：`fatal: repository not found`
- 错误：`Permission denied (publickey)`

**可能原因：**
- 仓库 URL 不正确
- 权限不足
- SSH 密钥未配置

**解决方案：**
1. **检查仓库 URL。**  
   使用 HTTPS URL：  
   ```
   git clone https://github.com/microsoft/AI-For-Beginners.git
   ```
2. **如果 SSH 失败，切换到 HTTPS。**  
   如果出现 `Permission denied (publickey)` 错误，请使用上述 HTTPS 链接代替 SSH。
3. **配置 SSH 密钥（可选）。**  
   如果您希望使用 SSH，请参考 [GitHub 的 SSH 指南](https://docs.github.com/en/authentication/connecting-to-github-with-ssh)。

---

## 安装问题

### 2. Python 环境问题

**背景：** 仓库依赖于 Python 和各种库。

**症状：**
- 错误：`ModuleNotFoundError: No module named '<package>'`
- 运行脚本或笔记本时出现导入错误

**可能原因：**
- 依赖未安装
- Python 版本错误

**解决方案：**
1. **设置虚拟环境。**  
   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
   ```
2. **安装依赖项。**  
   ```bash
   pip install -r requirements.txt
   ```
3. **检查 Python 版本。**  
   使用 Python 3.7 或更高版本。  
   ```bash
   python --version
   ```

### 3. 未安装 Jupyter

**背景：** 笔记本是核心学习资源。

**症状：**
- 错误：`jupyter: command not found`
- 笔记本无法启动

**可能原因：**
- 未安装 Jupyter

**解决方案：**
1. **安装 Jupyter Notebook。**  
   ```bash
   pip install notebook
   ```
   或者，如果使用 Anaconda：
   ```bash
   conda install notebook
   ```
2. **启动 Jupyter Notebook。**  
   ```bash
   jupyter notebook
   ```

### 4. 依赖版本冲突

**背景：** 如果包版本不匹配，项目可能会出现问题。

**症状：**
- 关于版本不兼容的错误或警告

**可能原因：**
- 旧的或冲突的 Python 包

**解决方案：**
1. **在干净的环境中安装。**  
   删除旧的 venv/conda 环境并创建一个新的。
2. **使用指定版本。**  
   始终运行：
   ```bash
   pip install -r requirements.txt
   ```
   如果失败，请按照 README 手动安装缺失的包。

---

## 配置问题

### 5. 环境变量未设置

**背景：** 某些模块可能需要密钥、令牌或配置设置。

**症状：**
- 错误：`KeyError` 或关于缺少配置的警告

**可能原因：**
- 必需的环境变量未设置

**解决方案：**
1. **检查 `.env.example` 或类似文件。**
2. **创建 `.env` 文件并填写所需值。**
3. **设置环境变量后重新加载终端或 IDE。**

---

## 运行笔记本

### 6. 笔记本无法打开或运行

**背景：** Jupyter 笔记本需要正确的设置。

**症状：**
- 笔记本无法启动
- 浏览器未自动打开

**可能原因：**
- 未安装 Jupyter
- 浏览器配置问题

**解决方案：**
1. **安装 Jupyter（参见安装问题部分）。**
2. **手动打开笔记本。**
   - 从终端复制 URL（例如 `http://localhost:8888/?token=...`），并将其粘贴到浏览器中。

### 7. 内核崩溃或冻结

**背景：** 笔记本内核可能因资源限制或代码错误而崩溃。

**症状：**
- 内核反复崩溃或重启
- 内存不足错误

**可能原因：**
- 数据集过大
- 不兼容的代码或包

**解决方案：**
1. **重启内核。**  
   使用 Jupyter 中的“重启内核”按钮。
2. **检查内存使用情况。**  
   关闭未使用的应用程序。
3. **在云平台上运行笔记本。**  
   使用 [Google Colab](https://colab.research.google.com/) 或 [Azure Notebooks](https://notebooks.azure.com/)。

---

## 性能问题

### 8. 笔记本运行缓慢

**背景：** 某些 AI 任务需要大量内存和 CPU。

**症状：**
- 执行速度慢
- 笔记本电脑风扇声音很大

**可能原因：**
- 数据集或模型过大
- 系统资源有限

**解决方案：**
1. **使用云平台。**
   - 将笔记本上传到 Colab 或 Azure Notebooks。
2. **减少数据集大小。**
   - 使用样本数据进行练习。
3. **关闭不必要的程序。**
   - 释放系统内存。

---

## 教材网站问题

### 9. 章节无法加载

**背景：** 在线教材显示课程和章节内容。

**症状：**
- 某章节（例如 Transformers/BERT）缺失或无法打开

**已知问题：**  
- [问题 #303](https://github.com/microsoft/AI-For-Beginners/issues/303)：“第 18 章 Transformers. BERT 无法在教材网站上打开。” 原因是文件名错误（`READMEtransformers.md` 而不是 `README.md`）。

**解决方案：**
1. **检查文件重命名错误。**  
   如果您是贡献者，请确保章节文件命名为 `README.md`。
2. **报告缺失文件。**  
   在 GitHub 上提交问题，注明章节名称和错误详情。

---

## 贡献问题

### 10. PR 未被接受或构建失败

**背景：** 贡献必须通过测试并遵循指南。

**症状：**
- 拉取请求被拒绝
- CI/CD 管道错误

**可能原因：**
- 测试失败
- 未遵循编码标准

**解决方案：**
1. **阅读贡献指南。**
   - 遵循仓库的 [CONTRIBUTING.md](https://github.com/microsoft/AI-For-Beginners/blob/main/CONTRIBUTING.md)。
2. **在推送之前本地运行测试。**
3. **检查代码格式或 linting 规则。**

---

## 常见问答

### 哪里可以找到特定模块的帮助？
- 每个模块通常都有自己的 README。从那里开始了解设置和使用技巧。

### 如何报告错误或请求新功能？
- [提交 GitHub 问题](https://github.com/microsoft/AI-For-Beginners/issues/new)，并提供清晰的描述和复现步骤。

### 如果我的问题未列出，可以寻求帮助吗？
- 可以！先搜索现有问题，如果没有找到您的问题，请创建一个新问题。

---

## 获取帮助

- **检查问题：** [GitHub Issues](https://github.com/microsoft/AI-For-Beginners/issues)
- **提问：** 使用 GitHub Discussions 或提交问题。
- **社区：** 查看仓库链接以获取聊天/论坛选项。

---

_最后更新：2025-09-20_

---

**免责声明**：  
本文档使用AI翻译服务 [Co-op Translator](https://github.com/Azure/co-op-translator) 进行翻译。尽管我们努力确保翻译的准确性，但请注意，自动翻译可能包含错误或不准确之处。原始语言的文档应被视为权威来源。对于关键信息，建议使用专业人工翻译。我们对因使用此翻译而产生的任何误解或误读不承担责任。