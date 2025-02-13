# ニューラルネットワークの紹介

![ニューラルネットワークの内容を示すスケッチ](../../../../translated_images/ai-neuralnetworks.1c687ae40bc86e834f497844866a26d3e0886650a67a4bbe29442e2f157d3b18.ja.png)

前述のように、知性を達成する方法の一つは、**コンピュータモデル**または**人工脳**を訓練することです。20世紀中頃から、研究者たちはさまざまな数学的モデルを試みてきましたが、近年、この方向性が非常に成功したことが証明されました。このような脳の数学的モデルを**ニューラルネットワーク**と呼びます。

> ニューラルネットワークは、モデルについて話していることを示すために、*人工ニューラルネットワーク*（ANN）とも呼ばれることがあります。

## 機械学習

ニューラルネットワークは、データを使用して問題を解決できるコンピュータモデルを訓練することを目的とした**機械学習**と呼ばれるより大きな分野の一部です。機械学習は人工知能の大部分を構成していますが、このカリキュラムでは古典的な機械学習は扱いません。

> 古典的な機械学習について詳しく学ぶには、別の**[初心者のための機械学習](http://github.com/microsoft/ml-for-beginners)**カリキュラムをご覧ください。

機械学習では、いくつかの例のデータセット**X**と、それに対応する出力値**Y**があると仮定します。例は、**特徴**で構成されるN次元ベクトルであり、出力は**ラベル**と呼ばれます。

私たちは、最も一般的な機械学習の問題を二つ考えます：

* **分類**：入力オブジェクトを二つ以上のクラスに分類する必要があります。
* **回帰**：入力サンプルごとに数値を予測する必要があります。

> 入力と出力をテンソルとして表現する場合、入力データセットはサイズM×Nの行列であり、Mはサンプル数、Nは特徴の数です。出力ラベルYはサイズMのベクトルです。

このカリキュラムでは、ニューラルネットワークモデルにのみ焦点を当てます。

## ニューロンのモデル

生物学から、私たちの脳は神経細胞で構成されており、それぞれが複数の「入力」（軸索）と出力（樹状突起）を持つことがわかっています。軸索と樹状突起は電気信号を伝導でき、軸索と樹状突起の間の接続は異なる導電性を示すことがあります（神経伝達物質によって制御されます）。

![ニューロンのモデル](../../../../translated_images/synapse-wikipedia.ed20a9e4726ea1c6a3ce8fec51c0b9bec6181946dca0fe4e829bc12fa3bacf01.ja.jpg) | ![ニューロンのモデル](../../../../translated_images/artneuron.1a5daa88d20ebe6f5824ddb89fba0bdaaf49f67e8230c1afbec42909df1fc17e.ja.png)
----|----
実際のニューロン *([画像](https://en.wikipedia.org/wiki/Synapse#/media/File:SynapseSchematic_lines.svg) 出典: Wikipedia)* | 人工ニューロン *(著者による画像)*

したがって、ニューロンの最も単純な数学モデルは、いくつかの入力X<sub>1</sub>, ..., X<sub>N</sub>と出力Y、そして一連の重みW<sub>1</sub>, ..., W<sub>N</sub>を含みます。出力は次のように計算されます：

<img src="images/netout.png" alt="Y = f\left(\sum_{i=1}^N X_iW_i\right)" width="131" height="53" align="center"/>

ここで、fは非線形の**活性化関数**です。

> ニューロンの初期モデルは、1943年にウォーレン・マカロックとウォルター・ピッツによる古典的な論文[A logical calculus of the ideas immanent in nervous activity](https://www.cs.cmu.edu/~./epxing/Class/10715/reading/McCulloch.and.Pitts.pdf)で説明されました。ドナルド・ヘッブは、彼の著書"[The Organization of Behavior: A Neuropsychological Theory](https://books.google.com/books?id=VNetYrB8EBoC)"で、これらのネットワークをどのように訓練できるかを提案しました。

## このセクションでは

このセクションでは、以下について学びます：
* [パーセプトロン](03-Perceptron/README.md)：二クラス分類のための最も初期のニューラルネットワークモデルの一つ
* [多層ネットワーク](04-OwnFramework/README.md)：私たちのフレームワークを構築する方法に関するペアノートブック[04-OwnFramework/OwnFramework.ipynb]
* [ニューラルネットワークフレームワーク](05-Frameworks/README.md)：これらのノートブック：[PyTorch](../../../../lessons/3-NeuralNetworks/05-Frameworks/IntroPyTorch.ipynb)と[Keras/Tensorflow](../../../../lessons/3-NeuralNetworks/05-Frameworks/IntroKerasTF.ipynb)
* [過剰適合](../../../../lessons/3-NeuralNetworks/05-Frameworks)

**免責事項**:  
この文書は、機械ベースのAI翻訳サービスを使用して翻訳されました。正確性を追求していますが、自動翻訳には誤りや不正確さが含まれる可能性があることにご留意ください。原文はその言語での権威ある情報源と見なされるべきです。重要な情報については、専門の人間翻訳を推奨します。この翻訳の使用に起因する誤解や誤訳について、当社は一切の責任を負いません。