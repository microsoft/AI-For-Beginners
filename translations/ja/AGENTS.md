# AGENTS.md

## プロジェクト概要

AI for Beginnersは、人工知能の基礎を網羅した12週間、24レッスンのカリキュラムです。この教育用リポジトリには、Jupyter Notebookを使用した実践的なレッスン、クイズ、ハンズオンラボが含まれています。カリキュラムの内容は以下の通りです：

- 知識表現とエキスパートシステムを用いた記号的AI
- TensorFlowとPyTorchを使用したニューラルネットワークと深層学習
- コンピュータビジョンの技術とアーキテクチャ
- トランスフォーマーやBERTを含む自然言語処理（NLP）
- 専門的なトピック：遺伝的アルゴリズム、強化学習、マルチエージェントシステム
- AI倫理と責任あるAIの原則

**主要技術:** Python 3、Jupyter Notebook、TensorFlow、PyTorch、Keras、OpenCV、Vue.js（クイズアプリ用）

**アーキテクチャ:** トピック別に整理されたJupyter Notebookを含む教育コンテンツリポジトリ、Vue.jsベースのクイズアプリケーション、多言語対応を充実させた構成。

## セットアップコマンド

### 主な開発環境（Python/Jupyter）

このカリキュラムはPythonとJupyter Notebookで動作するよう設計されています。推奨される方法はminicondaの使用です：

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

### 代替案: devcontainerの使用

```bash
# Open in VS Code and select "Reopen in Container" when prompted
# The devcontainer will automatically set up the environment
```

### クイズアプリのセットアップ

クイズアプリは`etc/quiz-app/`にあるVue.jsアプリケーションです：

```bash
cd etc/quiz-app
npm install
npm run serve  # Development server
npm run build  # Production build
npm run lint   # Lint and fix files
```

## 開発ワークフロー

### Jupyter Notebookの操作

1. **ローカル開発:**
   - conda環境をアクティブ化: `conda activate ai4beg`
   - Jupyterを起動: `jupyter notebook` または `jupyter lab`
   - レッスンフォルダに移動し、`.ipynb`ファイルを開く
   - セルをインタラクティブに実行してレッスンを進める

2. **VS CodeとPython拡張機能:**
   - リポジトリをVS Codeで開く
   - Python拡張機能をインストール
   - VS Codeが自動的にconda環境を検出して使用
   - `.ipynb`ファイルを直接VS Codeで開く

3. **クラウド開発:**
   - **GitHub Codespaces:** 「Code」→「Codespaces」→「Create codespace on main」をクリック
   - **Binder:** READMEのBinderバッジを使用してブラウザで起動
   - 注意: Binderはリソースが限られており、ウェブアクセスに制限がある場合があります

### 高度なレッスン向けGPUサポート

後半のレッスンではGPUアクセラレーションが大いに役立ちます：

- **Azure Data Science VM:** GPUサポート付きのNCシリーズVMを使用
- **Azure Machine Learning:** GPUコンピュートを使用したノートブック機能
- **Google Colab:** ノートブックを個別にアップロード（無料のGPUサポートあり）

### クイズアプリの開発

```bash
cd etc/quiz-app
npm run serve  # Hot-reload development server at http://localhost:8080
```

## テスト手順

このリポジトリは学習コンテンツに焦点を当てており、ソフトウェアテストのための従来型のテストスイートはありません。

### 検証方法:

1. **Jupyter Notebook:** セルを順番に実行してコード例が動作することを確認
2. **クイズアプリのテスト:** 開発サーバーを使用した手動テスト
3. **翻訳の検証:** `translations/`フォルダ内の翻訳コンテンツを確認
4. **クイズアプリのLinting:** `npm run lint`を`etc/quiz-app/`で実行

### コード例の実行:

```bash
# Activate environment first
conda activate ai4beg

# Run Python scripts directly
python lessons/4-ComputerVision/07-ConvNets/pytorchcv.py

# Or execute notebooks
jupyter notebook lessons/3-NeuralNetworks/03-Perceptron/Perceptron.ipynb
```

## コードスタイル

### Pythonコードスタイル

- 教育用コードにおける標準的なPythonの慣例
- 学習を優先した明確で読みやすいコード
- 重要な概念を説明するコメント
- Jupyter Notebookに適した形式: セルは可能な限り自己完結型にする
- レッスンコンテンツには厳密なLinting要件はなし

### JavaScript/Vue.js（クイズアプリ）

- `etc/quiz-app/package.json`にESLint設定
- `npm run lint`を実行して問題をチェックし自動修正
- Vue 2.xの慣例
- コンポーネントベースのアーキテクチャ

### ファイル構成

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

## ビルドとデプロイ

### Jupyterコンテンツ

ビルドプロセスは不要 - Jupyter Notebookは直接実行されます。

### クイズアプリ

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

### ドキュメントサイト

このリポジトリはDocsifyを使用してドキュメントを提供しています：
- `index.html`がエントリーポイントとして機能
- ビルド不要 - GitHub Pagesで直接提供
- アクセス先: https://microsoft.github.io/AI-For-Beginners/

## コントリビューションガイドライン

### プルリクエストプロセス

1. **タイトル形式:** 変更内容を明確に説明するタイトル
2. **CLA要件:** Microsoft CLAを署名する必要あり（自動チェック）
3. **コンテンツガイドライン:**
   - 教育的な焦点と初心者向けのアプローチを維持
   - ノートブック内のすべてのコード例をテスト
   - ノートブックがエンドツーエンドで動作することを確認
   - 英語コンテンツを変更する場合は翻訳を更新
4. **クイズアプリの変更:** コミット前に`npm run lint`を実行

### 翻訳のコントリビューション

- 翻訳はGitHub Actionsを使用してco-op-translatorで自動化
- 手動翻訳は`translations/<language-code>/`に配置
- クイズ翻訳は`etc/quiz-app/src/assets/translations/`に配置
- 対応言語: 40以上の言語（詳細はREADME参照）

### 積極的なコントリビューション分野

現在のニーズについては`etc/CONTRIBUTING.md`を参照：
- 深層強化学習セクション
- オブジェクト検出の改善
- 固有表現認識の例
- カスタム埋め込みトレーニングサンプル

## 環境構成

### 必要な依存関係

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

### 環境変数

基本的な使用には特別な環境変数は不要。

Azureデプロイメント（クイズアプリ）用：
- `AZURE_STATIC_WEB_APPS_API_TOKEN`（Azureによって自動設定）

## デバッグとトラブルシューティング

### よくある問題

**問題:** Conda環境の作成が失敗する
- **解決策:** まずcondaを更新: `conda update conda -y`
- 十分なディスク容量を確保（推奨50GB）

**問題:** Jupyterカーネルが見つからない
- **解決策:** 
  ```bash
  conda activate ai4beg
  python -m ipykernel install --user --name ai4beg
  ```

**問題:** ノートブックでGPUが検出されない
- **解決策:** 
  - CUDAインストールを確認: `nvidia-smi`
  - PyTorch GPUを確認: `python -c "import torch; print(torch.cuda.is_available())"`
  - TensorFlow GPUを確認: `python -c "import tensorflow as tf; print(tf.config.list_physical_devices('GPU'))"`

**問題:** クイズアプリが起動しない
- **解決策:**
  ```bash
  cd etc/quiz-app
  rm -rf node_modules package-lock.json
  npm install
  npm run serve
  ```

**問題:** Binderがタイムアウトする、またはダウンロードをブロックする
- **解決策:** GitHub Codespacesまたはローカルセットアップを使用してリソースアクセスを改善

### メモリ問題

一部のレッスンでは大量のRAM（推奨8GB以上）が必要：
- リソース集約型のレッスンにはクラウドVMを使用
- モデルをトレーニングする際は他のアプリケーションを閉じる
- メモリ不足の場合はノートブック内のバッチサイズを減らす

## 追加の注意事項

### コースインストラクター向け

- 教師向けガイダンスは`lessons/0-course-setup/for-teachers.md`を参照
- レッスンは自己完結型で、順番に教えることも個別に選択することも可能
- 推定期間: 12週間（週2レッスン）

### クラウドリソース

- **Azure for Students:** 学生向け無料クレジットあり
- **Microsoft Learn:** 補足的な学習パスが随所にリンク
- **Binder:** 無料だがリソースが限られ、ネットワーク制限がある場合あり

### コード実行オプション

1. **ローカル（推奨）:** 完全な制御、最高のパフォーマンス、GPUサポート
2. **GitHub Codespaces:** クラウドベースのVS Code、迅速なアクセスに適している
3. **Binder:** ブラウザベースのJupyter、無料だが制限あり
4. **Azure MLノートブック:** GPUサポート付きのエンタープライズオプション
5. **Google Colab:** ノートブックを個別にアップロード、無料GPU層利用可能

### ノートブックの操作

- ノートブックは学習のためにセルごとに実行するよう設計
- 多くのノートブックは初回実行時にデータセットをダウンロード（時間がかかる場合あり）
- 一部のモデルは合理的なトレーニング時間のためにGPUが必要
- 計算要件を減らすために事前学習済みモデルを使用

### パフォーマンスの考慮事項

- 後半のコンピュータビジョンレッスン（CNN、GAN）はGPUが有効
- NLPトランスフォーマーレッスンは大量のRAMを必要とする場合あり
- ゼロからのトレーニングは教育的だが時間がかかる
- 転移学習の例はトレーニング時間を最小化

---

**免責事項**:  
この文書は、AI翻訳サービス [Co-op Translator](https://github.com/Azure/co-op-translator) を使用して翻訳されています。正確性を追求しておりますが、自動翻訳には誤りや不正確な部分が含まれる可能性があります。元の言語で記載された文書を正式な情報源としてお考えください。重要な情報については、専門の人間による翻訳を推奨します。この翻訳の使用に起因する誤解や誤解釈について、当方は一切の責任を負いません。