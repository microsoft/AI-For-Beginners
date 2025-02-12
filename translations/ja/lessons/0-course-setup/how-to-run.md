# コードの実行方法

このカリキュラムには、多くの実行可能な例やラボが含まれており、実行したいと思うでしょう。これを行うには、このカリキュラムの一部として提供されているJupyter NotebookでPythonコードを実行する能力が必要です。コードを実行するためのいくつかのオプションがあります。

## コンピュータ上でローカルに実行する

コンピュータ上でローカルにコードを実行するには、Pythonの何らかのバージョンをインストールする必要があります。個人的には、**[miniconda](https://conda.io/en/latest/miniconda.html)**のインストールをお勧めします。これは、異なるPythonの**仮想環境**用の`conda`パッケージマネージャをサポートする、比較的軽量なインストールです。

minicondaをインストールしたら、リポジトリをクローンし、このコースで使用する仮想環境を作成する必要があります：

```bash
git clone http://github.com/microsoft/ai-for-beginners
cd ai-for-beginners
conda env create --name ai4beg --file .devcontainer/environment.yml
conda activate ai4beg
```

### Python拡張機能を使用したVisual Studio Codeの利用

カリキュラムを使用する最良の方法は、[Visual Studio Code](http://code.visualstudio.com/?WT.mc_id=academic-77998-cacaste)を[Python拡張機能](https://marketplace.visualstudio.com/items?itemName=ms-python.python&WT.mc_id=academic-77998-cacaste)で開くことです。

> **注意**: リポジトリをクローンしてVS Codeでディレクトリを開くと、自動的にPython拡張機能のインストールを提案されます。また、上記のようにminicondaもインストールする必要があります。

> **注意**: VS Codeがリポジトリをコンテナ内で再オープンするよう提案した場合、ローカルのPythonインストールを使用するためにこれを拒否する必要があります。

### ブラウザでのJupyterの使用

ブラウザから直接Jupyter環境を使用することもできます。実際、従来のJupyterとJupyter Hubの両方は、自動補完やコードハイライトなどを備えた非常に便利な開発環境を提供します。

ローカルでJupyterを開始するには、コースのディレクトリに移動し、次のコマンドを実行します：

```bash
jupyter notebook
```
または
```bash
jupyterhub
```
その後、`.ipynb` files, open them and start working.

### Running in container

One alternative to Python installation would be to run the code in container. Since our repository contains special `.devcontainer`フォルダに移動し、このリポジトリのコンテナを構築する方法を指示します。VS Codeはコンテナ内でコードを再オープンすることを提案します。これにはDockerのインストールが必要で、またより複雑になるため、経験豊富なユーザーにお勧めします。

## クラウドでの実行

ローカルにPythonをインストールしたくない場合や、クラウドリソースにアクセスできる場合は、クラウドでコードを実行する良い代替手段があります。これを行う方法はいくつかあります：

* **[GitHub Codespaces](https://github.com/features/codespaces)**を使用する。これは、GitHub上であなたのために作成された仮想環境で、VS Codeのブラウザインターフェースを通じてアクセスできます。Codespacesにアクセスできる場合は、リポジトリの**Code**ボタンをクリックし、コードスペースを開始すれば、すぐに実行できます。
* **[Binder](https://mybinder.org/v2/gh/microsoft/ai-for-beginners/HEAD)**を使用する。[Binder](https://mybinder.org)は、GitHub上のコードを試すために提供される無料の計算リソースです。フロントページにあるボタンをクリックすると、リポジトリがBinderで開かれ、すぐに基盤となるコンテナが構築され、Jupyterのウェブインターフェースがシームレスに開始されます。

> **注意**: 悪用を防ぐために、Binderは一部のウェブリソースへのアクセスをブロックしています。これにより、公共のインターネットからモデルやデータセットを取得するコードが正常に動作しない場合があります。何らかの回避策を見つける必要があるかもしれません。また、Binderが提供する計算リソースは非常に基本的なものであるため、特に後のより複雑なレッスンではトレーニングが遅くなります。

## GPUを使用したクラウドでの実行

このカリキュラムの後半のレッスンのいくつかは、GPUサポートから大きな恩恵を受けるでしょう。そうしないと、トレーニングが非常に遅くなります。特に、[Azure for Students](https://azure.microsoft.com/free/students/?WT.mc_id=academic-77998-cacaste)やあなたの機関を通じてクラウドにアクセスできる場合、いくつかのオプションがあります：

* [データサイエンス仮想マシン](https://docs.microsoft.com/learn/modules/intro-to-azure-data-science-virtual-machine/?WT.mc_id=academic-77998-cacaste)を作成し、Jupyterを通じて接続します。その後、リポジトリをマシンにクローンし、学習を開始できます。NCシリーズのVMはGPUサポートがあります。

> **注意**: 一部のサブスクリプション、特にAzure for Studentsは、デフォルトでGPUサポートを提供していません。追加のGPUコアを技術サポートにリクエストする必要があるかもしれません。

* [Azure Machine Learning Workspace](https://azure.microsoft.com/services/machine-learning/?WT.mc_id=academic-77998-cacaste)を作成し、そこでノートブック機能を使用します。[このビデオ](https://azure-for-academics.github.io/quickstart/azureml-papers/)では、リポジトリをAzure MLノートブックにクローンし、使用を開始する方法が示されています。

また、Google Colabを使用することもでき、こちらには無料のGPUサポートがあり、Jupyter Notebookをアップロードして一つずつ実行することができます。

**免責事項**:  
この文書は、機械ベースのAI翻訳サービスを使用して翻訳されています。正確さを追求していますが、自動翻訳には誤りや不正確さが含まれる可能性があることをご理解ください。原文のネイティブ言語の文書を権威ある情報源として考慮するべきです。重要な情報については、専門の人間による翻訳を推奨します。この翻訳の使用に起因する誤解や誤訳について、当社は責任を負いません。