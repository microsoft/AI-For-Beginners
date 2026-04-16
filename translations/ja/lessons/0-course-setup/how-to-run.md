# コードの実行方法

このカリキュラムには、多くの実行可能な例とラボが含まれており、それらを実行したいと思うでしょう。そのためには、このカリキュラムの一部として提供されるJupyterノートブックでPythonコードを実行する能力が必要です。コードを実行する方法はいくつかあります：

## お使いのコンピューターでローカルに実行する

お使いのコンピューターでコードをローカルに実行するには、Pythonのインストールが必要です。おすすめの一つは**[miniconda](https://conda.io/en/latest/miniconda.html)**のインストールです。これは比較的軽量なインストールで、異なるPythonの**仮想環境**用の`conda`パッケージマネージャーをサポートします。

minicondaをインストールした後に、リポジトリをクローンし、このコース用に仮想環境を作成します：

```bash
git clone http://github.com/microsoft/ai-for-beginners
cd ai-for-beginners
conda env create --name ai4beg --file .devcontainer/environment.yml
conda activate ai4beg
```

### Python拡張機能を使ったVisual Studio Codeの利用

このカリキュラムは、[Visual Studio Code](http://code.visualstudio.com/?WT.mc_id=academic-77998-cacaste)で[Python拡張機能](https://marketplace.visualstudio.com/items?itemName=ms-python.python&WT.mc_id=academic-77998-cacaste)を開いて使うのが最適です。

> **注意**: リポジトリをクローンしてVS Codeでディレクトリを開くと、自動的にPython拡張機能のインストールを提案されます。また、上記のようにminicondaもインストールしておく必要があります。

> **注意**: VS Codeがリポジトリをコンテナで再オープンするよう提案してきた場合は、ローカルのPythonインストールを利用するためにこれを拒否してください。

### ブラウザーでのJupyterの使用

ご自身のコンピューターのブラウザーからJupyter環境を使うこともできます。従来のJupyterとJupyterHubの両方が、コード補完やコードのハイライトなど便利な開発環境を提供します。

ローカルでJupyterを開始するには、コースのディレクトリに移動して、以下を実行します：

```bash
jupyter notebook
```
 または
```bash
jupyterhub
```
`.ipynb`ファイルに移動して開き、作業を始めることができます。

### コンテナでの実行

Pythonのインストールの代替案として、コードをコンテナで実行する方法があります。本リポジトリは、このリポジトリ用のコンテナ作成方法を指示する特別な`.devcontainer`フォルダーを提供しており、VS Codeはコードをコンテナで再オープンする機能を提供しています。これはDockerのインストールが必要で、より複雑になるため、経験豊富なユーザー向けをお勧めします。

## クラウドでの実行

Pythonをローカルにインストールしたくない場合やクラウドリソースにアクセスできる場合、クラウドでコードを実行する良い代替手段があります。いくつかの方法を紹介します：

* **[GitHub Codespaces](https://github.com/features/codespaces)**を利用する。これはGitHub上に用意された仮想環境で、VS Codeのブラウザーインターフェースからアクセス可能です。Codespacesにアクセスできる場合、リポジトリの**Code**ボタンをクリックしてCodespaceを開始し、すぐに作業を始められます。
* **[Binder](https://mybinder.org/v2/gh/microsoft/ai-for-beginners/HEAD)**を利用する。[Binder](https://mybinder.org)は、GitHub上のコードを試すために無料でクラウドの計算資源を提供します。リポジトリのフロントページにあるボタンからBinderに移動でき、即座に基盤となるコンテナを構築してJupyterのウェブインターフェースをシームレスに開始します。

> **注意**: 不正使用防止のため、Binderは一部のウェブリソースへのアクセスをブロックしています。これにより、モデルやデータセットをパブリックインターネットから取得するコードの一部が動作しない場合があります。回避策を検討する必要があるかもしれません。また、Binderの提供する計算資源はかなり基本的なものなので、特に複雑な後のレッスンのトレーニングは遅くなります。

## GPU付きクラウドでの実行

このカリキュラムの後半のレッスンではGPUサポートがあると大いに役立ちます。例えばモデルのトレーニングは、そうでないと非常に遅くなります。特に[Azure for Students](https://azure.microsoft.com/free/students/?WT.mc_id=academic-77998-cacaste)や所属機関を通じてクラウドにアクセスできる場合、次のような選択肢があります：

* [Data Science Virtual Machine](https://docs.microsoft.com/learn/modules/intro-to-azure-data-science-virtual-machine/?WT.mc_id=academic-77998-cacaste)を作成し、Jupyterを通じて接続します。マシンにリポジトリをクローンして学習を始められます。NCシリーズVMはGPUサポートがあります。

> **注意**: Azure for Studentsを含む一部のサブスクリプションはGPUサポートを標準で提供していません。追加のGPUコアを技術サポートにリクエストする必要がある場合があります。

* [Azure Machine Learning Workspace](https://azure.microsoft.com/services/machine-learning/?WT.mc_id=academic-77998-cacaste)を作成し、そこでノートブック機能を使用します。[このビデオ](https://azure-for-academics.github.io/quickstart/azureml-papers/)は、Azure MLノートブックにリポジトリをクローンして使い始める方法を示しています。

またGoogle Colabも、無料のGPUサポートが付いており、Jupyterノートブックを一つずつアップロードして実行できます。

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責事項**：
本書類はAI翻訳サービス「Co-op Translator」（https://github.com/Azure/co-op-translator）を使用して翻訳されています。正確性には努めておりますが、自動翻訳は誤りや不正確な部分を含む可能性があります。原文の言語による原文書が正式な情報源とみなされるべきです。重要な情報については、専門の人間翻訳を推奨します。本翻訳の利用によって生じたいかなる誤解や誤訳についても、当方は一切責任を負いかねます。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->