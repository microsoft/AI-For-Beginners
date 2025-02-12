# ニューラルネットワーク入門: パーセプトロン

## [講義前クイズ](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/103)

現代のニューラルネットワークに類似したものを実装する最初の試みの一つは、1957年にコーネル航空宇宙研究所のフランク・ローゼンブラットによって行われました。これは「Mark-1」と呼ばれるハードウェア実装で、三角形、四角形、円などの原始的な幾何学的図形を認識するために設計されました。

|      |      |
|--------------|-----------|
|<img src='images/Rosenblatt-wikipedia.jpg' alt='フランク・ローゼンブラット'/> | <img src='images/Mark_I_perceptron_wikipedia.jpg' alt='Mark 1 パーセプトロン' />|

> 画像は [ウィキペディア](https://en.wikipedia.org/wiki/Perceptron) より引用

入力画像は20x20のフォトセルアレイによって表現され、ニューラルネットワークは400の入力と1つのバイナリ出力を持っていました。シンプルなネットワークには1つのニューロン、つまり**しきい値論理ユニット**が含まれていました。ニューラルネットワークの重みは、学習フェーズ中に手動で調整する必要があるポテンショメータのように機能しました。

> ✅ ポテンショメータは、回路の抵抗を調整することを可能にするデバイスです。

> ニューヨークタイムズは当時パーセプトロンについて次のように書きました: *[海軍]が期待する電子コンピュータの胚で、歩き、話し、見え、書き、自らを再生し、その存在を意識することができる。*

## パーセプトロンモデル

モデルにNの特徴があると仮定すると、入力ベクトルはサイズNのベクトルになります。パーセプトロンは**バイナリ分類**モデルであり、つまり2つのクラスの入力データを区別することができます。各入力ベクトルxに対して、パーセプトロンの出力はクラスに応じて+1または-1であると仮定します。出力は次の式を使って計算されます。

y(x) = f(w<sup>T</sup>x)

ここで、fはステップ活性化関数です。

<!-- img src="http://www.sciweavers.org/tex2img.php?eq=f%28x%29%20%3D%20%5Cbegin%7Bcases%7D%0A%20%20%20%20%20%20%20%20%20%2B1%20%26%20x%20%5Cgeq%200%20%5C%5C%0A%20%20%20%20%20%20%20%20%20-1%20%26%20x%20%3C%200%0A%20%20%20%20%20%20%20%5Cend%7Bcases%7D%20%5C%5C%0A&bc=White&fc=Black&im=jpg&fs=12&ff=arev&edit=0" align="center" border="0" alt="f(x) = \begin{cases} +1 & x \geq 0 \\ -1 & x < 0 \end{cases} \\" width="154" height="50" / -->
<img src="images/activation-func.png"/>

## パーセプトロンの訓練

パーセプトロンを訓練するには、ほとんどの値を正しく分類する重みベクトルwを見つける必要があります。つまり、最小の**誤差**を生じさせる必要があります。この誤差Eは、次のように**パーセプトロン基準**によって定義されます。

E(w) = -∑w<sup>T</sup>x<sub>i</sub>t<sub>i</sub>

ここで:

* 合計は誤分類を引き起こすトレーニングデータポイントiに対して取られます
* x<sub>i</sub>は入力データで、t<sub>i</sub>は負の例に対して-1、正の例に対して+1です。

この基準は重みwの関数と見なされ、最小化する必要があります。多くの場合、**勾配降下法**と呼ばれる手法が使用され、初期重みw<sup>(0)</sup>から始めて、各ステップで次の式に従って重みを更新します。

w<sup>(t+1)</sup> = w<sup>(t)</sup> - η∇E(w)

ここでηは**学習率**と呼ばれ、∇E(w)はEの**勾配**を示します。勾配を計算した後、次のようになります。

w<sup>(t+1)</sup> = w<sup>(t)</sup> + ∑ηx<sub>i</sub>t<sub>i</sub>

Pythonでのアルゴリズムは次のようになります。

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

このレッスンでは、バイナリ分類モデルであるパーセプトロンについて学び、重みベクトルを使用してそれを訓練する方法について学びました。

## 🚀 チャレンジ

自分自身のパーセプトロンを構築してみたい場合は、[Microsoft Learnのこのラボ](https://docs.microsoft.com/en-us/azure/machine-learning/component-reference/two-class-averaged-perceptron?WT.mc_id=academic-77998-cacaste)を試してみてください。これは[Azure MLデザイナー](https://docs.microsoft.com/en-us/azure/machine-learning/concept-designer?WT.mc_id=academic-77998-cacaste)を使用しています。

## [講義後クイズ](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/203)

## 復習と自己学習

パーセプトロンを使っておもちゃの問題や実際の問題を解決する方法を学び続けるには、[Perceptron](../../../../../lessons/3-NeuralNetworks/03-Perceptron/Perceptron.ipynb)ノートブックに進んでください。

また、興味深い[パーセプトロンに関する記事](https://towardsdatascience.com/what-is-a-perceptron-basics-of-neural-networks-c4cfea20c590)もあります。

## [課題](lab/README.md)

このレッスンでは、バイナリ分類タスクのためにパーセプトロンを実装し、2つの手書き数字を分類するために使用しました。このラボでは、与えられた画像に最も関連する数字を特定するという形で、数字分類の問題を完全に解決するよう求められます。

* [指示](lab/README.md)
* [ノートブック](../../../../../lessons/3-NeuralNetworks/03-Perceptron/lab/PerceptronMultiClass.ipynb)

**免責事項**:  
この文書は、機械ベースのAI翻訳サービスを使用して翻訳されています。正確性を追求していますが、自動翻訳にはエラーや不正確さが含まれる可能性があることにご留意ください。原文のネイティブ言語の文書が権威ある情報源と見なされるべきです。重要な情報については、専門の人間翻訳を推奨します。この翻訳の使用に起因する誤解や誤解釈について、当社は一切の責任を負いません。