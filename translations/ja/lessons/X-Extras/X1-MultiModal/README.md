# マルチモーダルネットワーク

トランスフォーマーモデルがNLPタスクを解決する上で成功を収めた後、同様のアーキテクチャがコンピュータビジョンタスクにも適用されてきました。視覚と自然言語の機能を*組み合わせる*モデルの構築に対する関心が高まっています。そのような試みの一つがOpenAIによって行われ、CLIPおよびDALL.Eと呼ばれています。

## 対照的画像事前学習 (CLIP)

CLIPの主なアイデアは、テキストプロンプトと画像を比較し、画像がプロンプトにどれだけ一致するかを判断できることです。

![CLIPアーキテクチャ](../../../../../translated_images/clip-arch.b3dbf20b4e8ed8be1c38e2bc6100fd3cc257c33cda4692b301be91f791b13ea7.ja.png)

> *このブログ記事からの画像です [this blog post](https://openai.com/blog/clip/)*

モデルは、インターネットから取得した画像とそのキャプションでトレーニングされています。各バッチについて、N対の（画像、テキスト）を取得し、それらをいくつかのベクトル表現に変換します。これらの表現は互いにマッチングされます。損失関数は、1対（例：IとT）に対応するベクトル間のコサイン類似度を最大化し、他のすべてのペア間のコサイン類似度を最小化するように定義されています。これがこのアプローチが**対照的**と呼ばれる理由です。

CLIPモデル/ライブラリは[OpenAI GitHub](https://github.com/openai/CLIP)から入手できます。このアプローチは[このブログ記事](https://openai.com/blog/clip/)で説明されており、[この論文](https://arxiv.org/pdf/2103.00020.pdf)でより詳細に記載されています。

このモデルが事前学習されると、画像のバッチとテキストプロンプトのバッチを与えることができ、確率を持つテンソルを返します。CLIPは以下のいくつかのタスクに使用できます。

**画像分類**

たとえば、画像を猫、犬、人間に分類する必要があるとします。この場合、モデルに画像と一連のテキストプロンプト（"*猫の写真*", "*犬の写真*", "*人間の写真*"）を与えます。得られた3つの確率のベクトルの中から、最も高い値を持つインデックスを選択するだけです。

![CLIPによる画像分類](../../../../../translated_images/clip-class.3af42ef0b2b19369a633df5f20ddf4f5a01d6c8ffa181e9d3a0572c19f919f72.ja.png)

> *このブログ記事からの画像です [this blog post](https://openai.com/blog/clip/)*

**テキストベースの画像検索**

逆に、画像のコレクションを持っている場合、このコレクションをモデルに渡し、テキストプロンプトを与えることで、与えられたプロンプトに最も類似した画像を取得できます。

## ✍️ 例: [CLIPを使用した画像分類と画像検索](../../../../../lessons/X-Extras/X1-MultiModal/Clip.ipynb)

CLIPの実行を確認するには、[Clip.ipynb](../../../../../lessons/X-Extras/X1-MultiModal/Clip.ipynb)ノートブックを開いてください。

## VQGAN+ CLIPによる画像生成

CLIPは、テキストプロンプトから**画像生成**にも使用できます。これを行うには、いくつかのベクトル入力に基づいて画像を生成できる**生成モデル**が必要です。そのようなモデルの一つが[VQGAN](https://compvis.github.io/taming-transformers/)（ベクトル量子化GAN）と呼ばれています。

VQGANが通常の[GAN](../../4-ComputerVision/10-GANs/README.md)と異なる主なアイデアは次の通りです：
* 自己回帰トランスフォーマーアーキテクチャを使用して、画像を構成する文脈に富んだ視覚部分のシーケンスを生成します。これらの視覚部分は、[CNN](../../4-ComputerVision/07-ConvNets/README.md)によって学習されます。
* 画像の部分が「本物」か「偽物」であるかを検出する部分画像判別器を使用します（従来のGANの「全か無か」アプローチとは異なります）。

VQGANについて詳しくは、[Taming Transformers](https://compvis.github.io/taming-transformers/)のウェブサイトで学ぶことができます。

VQGANと従来のGANの重要な違いの一つは、後者が任意の入力ベクトルから適切な画像を生成できるのに対し、VQGANは一貫性のない画像を生成する可能性が高いことです。したがって、画像生成プロセスをさらにガイドする必要があり、それはCLIPを使用して行うことができます。

![VQGAN+CLIPアーキテクチャ](../../../../../translated_images/vqgan.5027fe05051dfa3101950cfa930303f66e6478b9bd273e83766731796e462d9b.ja.png)

テキストプロンプトに対応する画像を生成するために、まずランダムなエンコーディングベクトルを用意し、それをVQGANに通して画像を生成します。次に、CLIPを使用して、画像がテキストプロンプトにどれだけ一致するかを示す損失関数を生成します。目標は、この損失を最小化し、バックプロパゲーションを使用して入力ベクトルのパラメータを調整することです。

VQGAN+CLIPを実装した優れたライブラリは[Pixray](http://github.com/pixray/pixray)です。

![Pixrayによって生成された画像](../../../../../translated_images/a_closeup_watercolor_portrait_of_young_male_teacher_of_literature_with_a_book.2384968e9db8a0d09dc96de938b9f95bde8a7e1c721f48f286a7795bf16d56c7.ja.png) |  ![Pixrayによって生成された画像](../../../../../translated_images/a_closeup_oil_portrait_of_young_female_teacher_of_computer_science_with_a_computer.e0b6495f210a439077e1c32cc8afdf714e634fe24dc78dc5aa45fd2f560b0ed5.ja.png) | ![Pixrayによって生成された画像](../../../../../translated_images/a_closeup_oil_portrait_of_old_male_teacher_of_math.5362e67aa7fc2683b9d36a613b364deb7454760cd39205623fc1e3938fa133c0.ja.png)
----|----|----
プロンプト"*若い男性の文学教師が本を持っている水彩画のクローズアップポートレート*"から生成された画像 | プロンプト"*若い女性のコンピュータサイエンス教師がコンピュータを持っている油彩画のクローズアップポートレート*"から生成された画像 | プロンプト"*黒板の前にいる老年男性数学教師の油彩画のクローズアップポートレート*"から生成された画像

> 画像は[Dmitry Soshnikov](http://soshnikov.com)による**人工教師**コレクションからのものです。

## DALL-E
### [DALL-E 1](https://openai.com/research/dall-e)
DALL-Eは、プロンプトから画像を生成するように訓練されたGPT-3のバージョンです。120億のパラメータで訓練されています。

CLIPとは異なり、DALL-Eはテキストと画像をトークンの単一ストリームとして受け取ります。そのため、複数のプロンプトから、テキストに基づいて画像を生成することができます。

### [DALL-E 2](https://openai.com/dall-e-2)
DALL-E 1と2の主な違いは、よりリアルな画像とアートを生成することです。

DALL-Eによる画像生成の例：
![Pixrayによって生成された画像](../../../../../translated_images/DALL·E%202023-06-20%2015.56.56%20-%20a%20closeup%20watercolor%20portrait%20of%20young%20male%20teacher%20of%20literature%20with%20a%20book.6c235e8271d9ed10ce985d86aeb241a58518958647973af136912116b9518fce.ja.png) |  ![Pixrayによって生成された画像](../../../../../translated_images/DALL·E%202023-06-20%2015.57.43%20-%20a%20closeup%20oil%20portrait%20of%20young%20female%20teacher%20of%20computer%20science%20with%20a%20computer.f21dc4166340b6c8b4d1cb57efd1e22127407f9b28c9ac7afe11344065369e64.ja.png) | ![Pixrayによって生成された画像](../../../../../translated_images/DALL·E%202023-06-20%2015.58.42%20-%20%20a%20closeup%20oil%20portrait%20of%20old%20male%20teacher%20of%20mathematics%20in%20front%20of%20blackboard.d331c2dfbdc3f7c46aa65c0809066f5e7ed4b49609cd259852e760df21051e4a.ja.png)
----|----|----
プロンプト"*若い男性の文学教師が本を持っている水彩画のクローズアップポートレート*"から生成された画像 | プロンプト"*若い女性のコンピュータサイエンス教師がコンピュータを持っている油彩画のクローズアップポートレート*"から生成された画像 | プロンプト"*黒板の前にいる老年男性数学教師の油彩画のクローズアップポートレート*"から生成された画像

## 参考文献

* VQGAN論文: [高解像度画像合成のためのトランスフォーマーの調整](https://compvis.github.io/taming-transformers/paper/paper.pdf)
* CLIP論文: [自然言語監視からの転送可能な視覚モデルの学習](https://arxiv.org/pdf/2103.00020.pdf)

**免責事項**:  
この文書は、機械ベースのAI翻訳サービスを使用して翻訳されました。正確性を追求していますが、自動翻訳には誤りや不正確さが含まれる可能性があることをご承知おきください。原文の母国語の文書が権威ある情報源と見なされるべきです。重要な情報については、専門の人間による翻訳を推奨します。この翻訳の使用によって生じる誤解や誤訳について、当社は責任を負いません。