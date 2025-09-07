<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "7df19702b8d2d3f7c4238c51bec2c8fc",
  "translation_date": "2025-08-24T21:19:32+00:00",
  "source_file": "lessons/0-course-setup/how-to-run.md",
  "language_code": "ja"
}
-->
# コードを実行する方法

このカリキュラムには、実行可能な例やラボが多数含まれており、それらを実行したいと思うでしょう。そのためには、このカリキュラムの一部として提供されるJupyter NotebookでPythonコードを実行する環境が必要です。コードを実行するには、いくつかの選択肢があります。

## ローカル環境で実行する

コードをローカル環境で実行するには、何らかのバージョンのPythonをインストールする必要があります。個人的には、**[miniconda](https://conda.io/en/latest/miniconda.html)** のインストールをお勧めします。これは軽量なインストールで、`conda`パッケージマネージャを使用してさまざまなPythonの**仮想環境**をサポートします。

minicondaをインストールした後、このコース用の仮想環境を作成するためにリポジトリをクローンし、以下を実行します：

```bash
git clone http://github.com/microsoft/ai-for-beginners
cd ai-for-beginners
conda env create --name ai4beg --file .devcontainer/environment.yml
conda activate ai4beg
```

### Python拡張機能を使ったVisual Studio Codeの利用

おそらく、このカリキュラムを利用する最良の方法は、[Visual Studio Code](http://code.visualstudio.com/?WT.mc_id=academic-77998-cacaste)と[Python Extension](https://marketplace.visualstudio.com/items?itemName=ms-python.python&WT.mc_id=academic-77998-cacaste)を使って開くことです。

> **Note**: リポジトリをクローンしてVS Codeでディレクトリを開くと、Python拡張機能のインストールを自動的に提案されます。また、上記のようにminicondaをインストールする必要があります。

> **Note**: VS Codeがリポジトリをコンテナで再オープンすることを提案した場合、ローカルのPythonインストールを使用するためにこれを拒否してください。

### ブラウザでJupyterを使用する

ブラウザ上でJupyter環境を直接使用することもできます。実際、クラシックなJupyterやJupyter Hubは、オートコンプリートやコードのハイライトなど、非常に便利な開発環境を提供します。

ローカルでJupyterを起動するには、コースのディレクトリに移動し、以下を実行します：

```bash
jupyter notebook
```  
または  
```bash
jupyterhub
```  
その後、任意の`.ipynb`ファイルに移動して開き、作業を開始できます。

### コンテナで実行する

Pythonをインストールする代わりの方法として、コンテナ内でコードを実行することもできます。このリポジトリには、`.devcontainer`フォルダが含まれており、このリポジトリ用のコンテナを構築する方法が記載されています。そのため、VS Codeはコードをコンテナで再オープンすることを提案します。ただし、これにはDockerのインストールが必要で、より複雑になるため、経験豊富なユーザーにお勧めします。

## クラウドで実行する

Pythonをローカルにインストールしたくない場合や、クラウドリソースにアクセスできる場合は、クラウドでコードを実行するのも良い選択肢です。以下の方法があります：

* **[GitHub Codespaces](https://github.com/features/codespaces)** を使用する方法。これはGitHub上で作成される仮想環境で、VS Codeのブラウザインターフェースを通じてアクセスできます。Codespacesにアクセスできる場合は、リポジトリの**Code**ボタンをクリックし、Codespaceを開始するだけで、すぐに実行を開始できます。
* **[Binder](https://mybinder.org/v2/gh/microsoft/ai-for-beginners/HEAD)** を使用する方法。[Binder](https://mybinder.org)は、GitHub上のコードを試すために提供される無料のクラウドコンピューティングリソースです。リポジトリのフロントページにあるボタンをクリックすると、Binderサイトに移動し、基盤となるコンテナを構築してJupyterのウェブインターフェースをシームレスに開始できます。

> **Note**: 不正利用を防ぐため、Binderでは一部のウェブリソースへのアクセスが制限されています。これにより、モデルやデータセットをインターネットから取得するコードが動作しない場合があります。回避策を見つける必要があるかもしれません。また、Binderが提供する計算リソースは非常に基本的なものなので、特に後半の複雑なレッスンではトレーニングが遅くなる可能性があります。

## GPUを使用したクラウドでの実行

このカリキュラムの後半のレッスンでは、GPUサポートがあると非常に便利です。GPUがないとトレーニングが非常に遅くなるためです。クラウドにアクセスできる場合（[Azure for Students](https://azure.microsoft.com/free/students/?WT.mc_id=academic-77998-cacaste)や所属機関を通じて）、以下のオプションを検討できます：

* [Data Science Virtual Machine](https://docs.microsoft.com/learn/modules/intro-to-azure-data-science-virtual-machine/?WT.mc_id=academic-77998-cacaste)を作成し、Jupyterを通じて接続します。その後、リポジトリをマシン上にクローンして学習を開始できます。NCシリーズのVMはGPUサポートがあります。

> **Note**: 一部のサブスクリプション（Azure for Studentsを含む）では、デフォルトでGPUサポートが提供されていません。追加のGPUコアをリクエストするために技術サポートに問い合わせる必要がある場合があります。

* [Azure Machine Learning Workspace](https://azure.microsoft.com/services/machine-learning/?WT.mc_id=academic-77998-cacaste)を作成し、そこでNotebook機能を使用します。[このビデオ](https://azure-for-academics.github.io/quickstart/azureml-papers/)では、Azure MLノートブックにリポジトリをクローンして使用を開始する方法を示しています。

また、Google Colabを使用することもできます。Google Colabは無料のGPUサポートを提供しており、Jupyter Notebookをアップロードして1つずつ実行することができます。

**免責事項**:  
この文書は、AI翻訳サービス [Co-op Translator](https://github.com/Azure/co-op-translator) を使用して翻訳されています。正確性を追求しておりますが、自動翻訳には誤りや不正確な部分が含まれる可能性があることをご承知おきください。元の言語で記載された文書が公式な情報源とみなされるべきです。重要な情報については、専門の人間による翻訳をお勧めします。本翻訳の使用に起因する誤解や誤認について、当方は一切の責任を負いません。