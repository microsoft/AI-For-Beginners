# クイズ

これらのクイズは、https://aka.ms/ai-beginners のAIカリキュラムの講義前後のクイズです。

## 翻訳されたクイズセットの追加

`assets/translations` フォルダー内に一致するクイズ構造を作成することで、クイズの翻訳を追加します。標準のクイズは `assets/translations/en` にあります。クイズはレッスンごとにいくつかのグループに分けられています。適切なクイズセクションに番号を合わせるようにしてください。このカリキュラムには合計40のクイズがあり、カウントは0から始まります。

翻訳を編集した後、`en` の規約に従ってすべてのファイルをインポートするために、翻訳フォルダー内の index.js ファイルを編集します。

`assets/translations` 内の `index.js` ファイルを編集して、新しい翻訳ファイルをインポートします。

次に、このアプリの `App.vue` 内のドロップダウンを編集して、あなたの言語を追加します。ローカライズされた略語をあなたの言語のフォルダー名に一致させてください。

最後に、翻訳されたレッスン内のすべてのクイズリンクを、存在する場合は、次のようなクエリパラメータを含むように編集します: `?loc=fr` など。

## プロジェクトのセットアップ

```
npm install
```

### 開発用にコンパイルとホットリロード

```
npm run serve
```

### 本番用にコンパイルとミニファイ

```
npm run build
```

### ファイルのリンティングと修正

```
npm run lint
```

### 設定のカスタマイズ

[設定リファレンス](https://cli.vuejs.org/config/)を参照してください。

クレジット: このクイズアプリのオリジナルバージョンに感謝します: https://github.com/arpan45/simple-quiz-vue

## Azureへのデプロイ

ここでは、始めるためのステップバイステップガイドを紹介します。

1. GitHubリポジトリをフォークする
静的WebアプリのコードがGitHubリポジトリにあることを確認します。このリポジトリをフォークしてください。

2. Azure Static Web Appを作成する
- [Azureアカウント](http://azure.microsoft.com)を作成します。
- [Azureポータル](https://portal.azure.com)にアクセスします。
- 「リソースの作成」をクリックし、「Static Web App」を検索します。
- 「作成」をクリックします。

3. Static Web Appを構成する
- 基本: サブスクリプション: あなたのAzureサブスクリプションを選択します。
- リソースグループ: 新しいリソースグループを作成するか、既存のものを使用します。
- 名前: 静的Webアプリの名前を提供します。
- リージョン: ユーザーに最も近いリージョンを選択します。

- #### デプロイメントの詳細:
- ソース: 「GitHub」を選択します。
- GitHubアカウント: AzureがあなたのGitHubアカウントにアクセスすることを許可します。
- 組織: あなたのGitHub組織を選択します。
- リポジトリ: 静的Webアプリを含むリポジトリを選択します。
- ブランチ: デプロイ元のブランチを選択します。

- #### ビルドの詳細:
- ビルドプリセット: アプリが構築されているフレームワークを選択します（例: React, Angular, Vueなど）。
- アプリの場所: アプリコードが含まれているフォルダーを指定します（例: ルートにある場合は /）。
- APIの場所: APIがある場合、その場所を指定します（オプション）。
- 出力の場所: ビルド出力が生成されるフォルダーを指定します（例: build または dist）。

4. レビューして作成
設定を確認し、「作成」をクリックします。Azureは必要なリソースをセットアップし、あなたのリポジトリにGitHub Actionsワークフローを作成します。

5. GitHub Actionsワークフロー
Azureは自動的にあなたのリポジトリにGitHub Actionsワークフローファイルを作成します (.github/workflows/azure-static-web-apps-<name>.yml)。このワークフローはビルドとデプロイのプロセスを処理します。

6. デプロイの監視
あなたのGitHubリポジトリの「Actions」タブに移動します。
ワークフローが実行中であることが表示されるはずです。このワークフローは静的WebアプリをAzureにビルドしてデプロイします。
ワークフローが完了すると、あなたのアプリは提供されたAzure URLでライブになります。

### 例: ワークフローファイル

以下は、GitHub Actionsワークフローファイルの例です:
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

### 追加リソース
- [Azure Static Web Apps ドキュメント](https://learn.microsoft.com/azure/static-web-apps/getting-started)
- [GitHub Actions ドキュメント](https://docs.github.com/actions/use-cases-and-examples/deploying/deploying-to-azure-static-web-app)

**免責事項**:  
この文書は、機械翻訳AIサービスを使用して翻訳されています。正確性を追求していますが、自動翻訳には誤りや不正確さが含まれる可能性があることをご理解ください。元の文書は、その母国語での権威ある情報源と見なされるべきです。重要な情報については、専門の人間翻訳を推奨します。この翻訳の使用から生じる誤解や誤訳については、一切の責任を負いません。