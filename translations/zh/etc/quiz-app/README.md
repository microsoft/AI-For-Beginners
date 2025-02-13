# 测验

这些测验是 https://aka.ms/ai-beginners 上 AI 课程的课前和课后测验。

## 添加翻译的测验集

通过在 `assets/translations` 文件夹中创建匹配的测验结构来添加测验翻译。规范测验位于 `assets/translations/en`。测验按课程分为几个组。确保将编号与正确的测验部分对齐。本课程总共有 40 个测验，编号从 0 开始。

编辑完翻译后，编辑翻译文件夹中的 index.js 文件，以按照 `en` 中的约定导入所有文件。

在 `assets/translations` 中编辑 `index.js` 文件，以导入新的翻译文件。

然后，在此应用程序中的 `App.vue` 下拉菜单中添加您的语言。将本地化缩写与您的语言文件夹名称匹配。

最后，如果存在，编辑翻译课程中的所有测验链接，以包括此本地化作为查询参数，例如：`?loc=fr`。

## 项目设置

```
npm install
```

### 为开发编译和热重载

```
npm run serve
```

### 为生产编译和压缩

```
npm run build
```

### 检查并修复文件

```
npm run lint
```

### 自定义配置

请参阅 [配置参考](https://cli.vuejs.org/config/)。

致谢：感谢这个测验应用程序的原始版本： https://github.com/arpan45/simple-quiz-vue

## 部署到 Azure

以下是帮助您入门的逐步指南：

1. 叉一个 GitHub 仓库
确保您的静态 Web 应用代码在您的 GitHub 仓库中。叉这个仓库。

2. 创建 Azure 静态 Web 应用
- 创建一个 [Azure 账户](http://azure.microsoft.com)
- 访问 [Azure 门户](https://portal.azure.com) 
- 点击“创建资源”，搜索“静态 Web 应用”。
- 点击“创建”。

3. 配置静态 Web 应用
- 基本信息：订阅：选择您的 Azure 订阅。
- 资源组：创建一个新的资源组或使用现有的。
- 名称：为您的静态 Web 应用提供一个名称。
- 区域：选择离您的用户最近的区域。

- #### 部署详情：
- 来源：选择“GitHub”。
- GitHub 账户：授权 Azure 访问您的 GitHub 账户。
- 组织：选择您的 GitHub 组织。
- 仓库：选择包含您静态 Web 应用的仓库。
- 分支：选择您想要部署的分支。

- #### 构建详情：
- 构建预设：选择您的应用构建所用的框架（例如，React、Angular、Vue 等）。
- 应用位置：指定包含您应用代码的文件夹（例如，如果在根目录，则为 /）。
- API 位置：如果您有 API，请指定其位置（可选）。
- 输出位置：指定生成输出的文件夹（例如，build 或 dist）。

4. 审核并创建
审核您的设置并点击“创建”。Azure 将设置所需的资源并在您的仓库中创建 GitHub Actions 工作流。

5. GitHub Actions 工作流
Azure 将自动在您的仓库中创建一个 GitHub Actions 工作流文件（.github/workflows/azure-static-web-apps-<name>.yml）。该工作流将处理构建和部署过程。

6. 监控部署
转到您的 GitHub 仓库中的“操作”选项卡。
您应该看到一个正在运行的工作流。此工作流将构建并将您的静态 Web 应用部署到 Azure。
一旦工作流完成，您的应用将在提供的 Azure URL 上上线。

### 示例工作流文件

以下是 GitHub Actions 工作流文件可能的示例：
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
本文件使用基于机器的人工智能翻译服务进行翻译。虽然我们努力追求准确性，但请注意，自动翻译可能包含错误或不准确之处。原文件的母语版本应视为权威来源。对于关键信息，建议进行专业人工翻译。我们对因使用此翻译而产生的任何误解或错误解释不承担责任。