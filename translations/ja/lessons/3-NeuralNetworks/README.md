# ニューラルネットワーク入門

![ニューラルネットワーク入門の内容をまとめたイラスト](../../../../translated_images/ja/ai-neuralnetworks.1c687ae40bc86e83.webp)

序章で述べたように、知能を実現する方法の一つは、**コンピュータモデル**や**人工の脳**を訓練することです。20世紀中頃から研究者たちはさまざまな数学的モデルを試みてきましたが、近年になってこの方向性が非常に成功を収めることが証明されました。このような脳の数学的モデルは**ニューラルネットワーク**と呼ばれます。

> ニューラルネットワークは時折、*人工ニューラルネットワーク*（Artificial Neural Networks、ANNs）と呼ばれることがあります。これは、実際のニューロンのネットワークではなく、モデルについて話していることを示すためです。

## 機械学習

ニューラルネットワークは、**機械学習**と呼ばれるより大きな分野の一部です。この分野の目的は、データを使用して問題を解決できるコンピュータモデルを訓練することです。機械学習は人工知能の大部分を構成していますが、このカリキュラムでは古典的な機械学習については扱いません。

> 古典的な機械学習について学びたい場合は、別の**[Machine Learning for Beginners](http://github.com/microsoft/ml-for-beginners)**カリキュラムをご覧ください。

機械学習では、例のデータセット**X**と対応する出力値**Y**があると仮定します。例は通常、**特徴**からなるN次元ベクトルであり、出力は**ラベル**と呼ばれます。

機械学習の最も一般的な問題を2つ考えます：

* **分類**：入力オブジェクトを2つ以上のクラスに分類する必要がある場合。
* **回帰**：各入力サンプルに対して数値を予測する必要がある場合。

> 入力と出力をテンソルとして表現する場合、入力データセットはM&times;Nのサイズの行列であり、Mはサンプル数、Nは特徴数です。出力ラベルYはサイズMのベクトルです。

このカリキュラムでは、ニューラルネットワークモデルにのみ焦点を当てます。

## ニューロンのモデル

生物学から、私たちの脳はニューロン（神経細胞）で構成されており、それぞれが複数の「入力」（樹状突起）と1つの「出力」（軸索）を持っていることがわかっています。樹状突起と軸索は電気信号を伝達することができ、これらの間の接続—シナプスとして知られる—は、神経伝達物質によって調節されるさまざまな伝導度を示すことができます。

![ニューロンのモデル](../../../../translated_images/ja/synapse-wikipedia.ed20a9e4726ea1c6.webp) | ![ニューロンのモデル](../../../../translated_images/ja/artneuron.1a5daa88d20ebe6f.webp)
----|----
実際のニューロン *([画像](https://en.wikipedia.org/wiki/Synapse#/media/File:SynapseSchematic_lines.svg) Wikipediaより)* | 人工ニューロン *(著者による画像)*

したがって、ニューロンの最も単純な数学的モデルは、いくつかの入力X<sub>1</sub>, ..., X<sub>N</sub>と出力Y、および一連の重みW<sub>1</sub>, ..., W<sub>N</sub>を含みます。出力は次のように計算されます：

<img src="../../../../translated_images/ja/netout.1eb15eb76fd76731.webp" alt="Y = f\left(\sum_{i=1}^N X_iW_i\right)" width="131" height="53" align="center"/>

ここで、fは非線形の**活性化関数**です。

> ニューロンの初期モデルは、1943年にWarren McCullockとWalter Pittsによる古典的な論文[A logical calculus of the ideas immanent in nervous activity](https://www.cs.cmu.edu/~./epxing/Class/10715/reading/McCulloch.and.Pitts.pdf)で記述されました。Donald Hebbは著書"[The Organization of Behavior: A Neuropsychological Theory](https://books.google.com/books?id=VNetYrB8EBoC)"で、これらのネットワークを訓練する方法を提案しました。

## このセクションで学ぶこと

このセクションでは以下について学びます：
* [パーセプトロン](03-Perceptron/README.md)：2クラス分類のための初期のニューラルネットワークモデル
* [多層ネットワーク](04-OwnFramework/README.md)：対応するノートブック[独自のフレームワークを構築する方法](04-OwnFramework/OwnFramework.ipynb)付き
* [ニューラルネットワークフレームワーク](05-Frameworks/README.md)：以下のノートブック付き：[PyTorch](05-Frameworks/IntroPyTorch.ipynb)と[Keras/Tensorflow](05-Frameworks/IntroKerasTF.ipynb)
* [過学習](../../../../lessons/3-NeuralNetworks/05-Frameworks)

---

**免責事項**:  
この文書は、AI翻訳サービス [Co-op Translator](https://github.com/Azure/co-op-translator) を使用して翻訳されています。正確性を追求しておりますが、自動翻訳には誤りや不正確な部分が含まれる可能性があることをご承知ください。元の言語で記載された文書が正式な情報源とみなされるべきです。重要な情報については、専門の人間による翻訳を推奨します。この翻訳の使用に起因する誤解や誤解釈について、当方は責任を負いません。