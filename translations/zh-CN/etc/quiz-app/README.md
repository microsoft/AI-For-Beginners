# 测验

这些测验是 AI 课程（https://aka.ms/ai-beginners）的课前和课后测验。

## 添加翻译后的测验集

通过在 `assets/translations` 文件夹中创建相应的测验结构来添加测验翻译。原始测验位于 `assets/translations/en` 文件夹中。测验按照课程分为多个组别。请确保编号与正确的测验部分对齐。整个课程共有 40 个测验，编号从 0 开始。

编辑翻译内容后，修改翻译文件夹中的 `index.js` 文件，按照 `en` 文件夹中的约定导入所有文件。

接着，编辑 `assets/translations` 文件夹中的 `index.js` 文件，导入新翻译的文件。

然后，编辑此应用中的 `App.vue` 文件中的下拉菜单，添加您的语言。确保本地化缩写与您的语言文件夹名称匹配。

最后，编辑翻译课程中的所有测验链接（如果存在），将本地化作为查询参数添加，例如：`?loc=fr`。

## 项目设置

```
npm install
```

### 编译并热加载用于开发

```
npm run serve
```

### 编译并压缩用于生产

```
npm run build
```

### 检查并修复文件

```
npm run lint
```

### 自定义配置

请参阅 [配置参考](https://cli.vuejs.org/config/)。

致谢：感谢此测验应用的原始版本：https://github.com/arpan45/simple-quiz-vue

## 部署到 Azure

以下是帮助您入门的分步指南：

1. Fork GitHub 仓库  
确保您的静态 Web 应用代码在 GitHub 仓库中。Fork 此仓库。

2. 创建 Azure 静态 Web 应用  
- 创建一个 [Azure 账户](http://azure.microsoft.com)  
- 访问 [Azure 门户](https://portal.azure.com)  
- 点击“创建资源”，搜索“静态 Web 应用”。  
- 点击“创建”。

3. 配置静态 Web 应用  
- 基本信息：  
  - 订阅：选择您的 Azure 订阅。  
  - 资源组：创建一个新的资源组或使用现有的资源组。  
  - 名称：为您的静态 Web 应用提供一个名称。  
  - 区域：选择离您的用户最近的区域。

- #### 部署详情：  
  - 源：选择“GitHub”。  
  - GitHub 账户：授权 Azure 访问您的 GitHub 账户。  
  - 组织：选择您的 GitHub 组织。  
  - 仓库：选择包含静态 Web 应用的仓库。  
  - 分支：选择您要部署的分支。

- #### 构建详情：  
  - 构建预设：选择您的应用所使用的框架（例如 React、Angular、Vue 等）。  
  - 应用位置：指定包含应用代码的文件夹（例如，如果在根目录，则为 /）。  
  - API 位置：如果有 API，请指定其位置（可选）。  
  - 输出位置：指定生成的构建输出所在的文件夹（例如 build 或 dist）。

4. 审核并创建  
审核您的设置并点击“创建”。Azure 将设置必要的资源，并在您的仓库中创建一个 GitHub Actions 工作流。

5. GitHub Actions 工作流  
Azure 会自动在您的仓库中创建一个 GitHub Actions 工作流文件（.github/workflows/azure-static-web-apps-<name>.yml）。此工作流将处理构建和部署过程。

6. 监控部署  
前往 GitHub 仓库中的“Actions”标签页。  
您应该会看到一个正在运行的工作流。此工作流将构建并部署您的静态 Web 应用到 Azure。  
工作流完成后，您的应用将在提供的 Azure URL 上上线。

### 示例工作流文件

以下是 GitHub Actions 工作流文件的示例：  
name: Azure Static Web Apps CI/CD  
```
on:
  push:
    branches:
      - main
  pull_request:
    types: [opened, synchronize, reopened, closed]
    branches:
      - main

jobs:
  build_and_deploy_job:
    runs-on: ubuntu-latest
    name: Build and Deploy Job
    steps:
      - uses: actions/checkout@v2
      - name: Build And Deploy
        id: builddeploy
        uses: Azure/static-web-apps-deploy@v1
        with:
          azure_static_web_apps_api_token: ${{ secrets.AZURE_STATIC_WEB_APPS_API_TOKEN }}
          repo_token: ${{ secrets.GITHUB_TOKEN }}
          action: "upload"
          app_location: "etc/quiz-app # App source code path"
          api_location: ""API source code path optional
          output_location: "dist" #Built app content directory - optional
```

### 其他资源
- [Azure 静态 Web 应用文档](https://learn.microsoft.com/azure/static-web-apps/getting-started)  
- [GitHub Actions 文档](https://docs.github.com/actions/use-cases-and-examples/deploying/deploying-to-azure-static-web-app)  

**免责声明**：  
本文档使用AI翻译服务 [Co-op Translator](https://github.com/Azure/co-op-translator) 进行翻译。尽管我们努力确保翻译的准确性，但请注意，自动翻译可能包含错误或不准确之处。应以原始语言的文档作为权威来源。对于关键信息，建议使用专业人工翻译。因使用本翻译而引起的任何误解或误读，我们概不负责。