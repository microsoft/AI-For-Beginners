<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "0c37770bba4fff3c71dc00eb261ee61b",
  "translation_date": "2025-08-24T21:15:55+00:00",
  "source_file": "lessons/3-NeuralNetworks/03-Perceptron/README.md",
  "language_code": "ja"
}
-->
# ニューラルネットワーク入門: パーセプトロン

## [講義前クイズ](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/103)

現代のニューラルネットワークに似たものを初めて実装しようとした試みの一つは、1957年にコーネル航空研究所のフランク・ローゼンブラットによって行われました。それは「Mark-1」と呼ばれるハードウェア実装で、三角形、四角形、円などの基本的な幾何学的図形を認識するよう設計されていました。

|      |      |
|--------------|-----------|
|<img src='images/Rosenblatt-wikipedia.jpg' alt='Frank Rosenblatt'/> | <img src='images/Mark_I_perceptron_wikipedia.jpg' alt='The Mark 1 Perceptron' />|

> 画像は[Wikipedia](https://en.wikipedia.org/wiki/Perceptron)より

入力画像は20x20のフォトセル配列で表されており、ニューラルネットワークには400の入力と1つの二値出力がありました。単純なネットワークは1つのニューロン、つまり**閾値論理ユニット**と呼ばれるものを含んでいました。ニューラルネットワークの重みはポテンショメータのように機能し、トレーニング段階で手動で調整する必要がありました。

> ✅ ポテンショメータとは、回路の抵抗を調整できる装置のことです。

> 当時のニューヨーク・タイムズはパーセプトロンについて次のように書いています: *「[海軍が]歩き、話し、見て、書き、自らを再生し、自分の存在を意識することができると期待している電子計算機の胚芽」*

## パーセプトロンモデル

モデルにN個の特徴量があると仮定すると、入力ベクトルはサイズNのベクトルになります。パーセプトロンは**二値分類**モデル、つまり2つのクラスの入力データを区別するモデルです。各入力ベクトルxに対して、パーセプトロンの出力はクラスに応じて+1または-1のいずれかになると仮定します。出力は次の式を使って計算されます:

y(x) = f(w<sup>T</sup>x)

ここでfはステップ活性化関数です。

<!-- img src="http://www.sciweavers.org/tex2img.php?eq=f%28x%29%20%3D%20%5Cbegin%7Bcases%7D%0A%20%20%20%20%20%20%20%20%20%2B1%20%26%20x%20%5Cgeq%200%20%5C%5C%0A%20%20%20%20%20%20%20%20%20-1%20%26%20x%20%3C%200%0A%20%20%20%20%20%20%20%5Cend%7Bcases%7D%20%5C%5C%0A&bc=White&fc=Black&im=jpg&fs=12&ff=arev&edit=0" align="center" border="0" alt="f(x) = \begin{cases} +1 & x \geq 0 \\ -1 & x < 0 \end{cases} \\" width="154" height="50" / -->
<img src="images/activation-func.png"/>

## パーセプトロンのトレーニング

パーセプトロンをトレーニングするには、ほとんどの値を正しく分類する重みベクトルwを見つける必要があります。つまり、**誤差**を最小化する必要があります。この誤差Eは、次のように**パーセプトロン基準**によって定義されます:

E(w) = -∑w<sup>T</sup>x<sub>i</sub>t<sub>i</sub>

ここで:

* 和は誤分類されたトレーニングデータポイントiについて取られます
* x<sub>i</sub>は入力データ、t<sub>i</sub>は負の例と正の例に応じてそれぞれ-1または+1です。

この基準は重みwの関数と見なされ、これを最小化する必要があります。よく使われる方法として**勾配降下法**があります。この方法では、初期重みw<sup>(0)</sup>から始め、各ステップで次の式に従って重みを更新します:

w<sup>(t+1)</sup> = w<sup>(t)</sup> - η∇E(w)

ここでηは**学習率**と呼ばれ、∇E(w)はEの**勾配**を表します。勾配を計算した後、次のようになります:

w<sup>(t+1)</sup> = w<sup>(t)</sup> + ∑ηx<sub>i</sub>t<sub>i</sub>

Pythonでのアルゴリズムは次のようになります:

```python
def train(positive_examples, negative_examples, num_iterations = 100, eta = 1):

    weights = [0,0,0] # Initialize weights (almost randomly :)
        
    for i in range(num_iterations):
        pos = random.choice(positive_examples)
        neg = random.choice(negative_examples)

        z = np.dot(pos, weights) # compute perceptron output
        if z < 0: # positive example classified as negative
            weights = weights + eta*weights.shape

        z  = np.dot(neg, weights)
        if z >= 0: # negative example classified as positive
            weights = weights - eta*weights.shape

    return weights
```

## 結論

このレッスンでは、二値分類モデルであるパーセプトロンと、それを重みベクトルを使ってトレーニングする方法について学びました。

## 🚀 チャレンジ

自分でパーセプトロンを構築してみたい場合は、[Microsoft Learnのこのラボ](https://docs.microsoft.com/en-us/azure/machine-learning/component-reference/two-class-averaged-perceptron?WT.mc_id=academic-77998-cacaste)を試してみてください。このラボでは[Azure MLデザイナー](https://docs.microsoft.com/en-us/azure/machine-learning/concept-designer?WT.mc_id=academic-77998-cacaste)を使用します。

## [講義後クイズ](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/203)

## 復習と自己学習

パーセプトロンを使っておもちゃの問題や実際の問題を解く方法を確認し、学習を続けるには、[Perceptron](../../../../../lessons/3-NeuralNetworks/03-Perceptron/Perceptron.ipynb)ノートブックをご覧ください。

また、パーセプトロンに関する興味深い[記事](https://towardsdatascience.com/what-is-a-perceptron-basics-of-neural-networks-c4cfea20c590)もあります。

## [課題](lab/README.md)

このレッスンでは、二値分類タスクのためのパーセプトロンを実装し、それを使って2つの手書き数字を分類しました。このラボでは、数字分類の問題を完全に解決すること、つまり、与えられた画像に最も対応する数字を特定することが求められます。

* [指示](lab/README.md)
* [ノートブック](../../../../../lessons/3-NeuralNetworks/03-Perceptron/lab/PerceptronMultiClass.ipynb)

**免責事項**:  
この文書は、AI翻訳サービス [Co-op Translator](https://github.com/Azure/co-op-translator) を使用して翻訳されています。正確性を追求しておりますが、自動翻訳には誤りや不正確な部分が含まれる可能性があります。元の言語で記載された文書を正式な情報源としてお考えください。重要な情報については、専門の人間による翻訳を推奨します。この翻訳の使用に起因する誤解や誤解釈について、当社は責任を負いません。