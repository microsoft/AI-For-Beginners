# コンピュータビジョン入門

[コンピュータビジョン](https://wikipedia.org/wiki/Computer_vision)は、コンピュータがデジタル画像を高レベルで理解できるようにすることを目的とした分野です。これは非常に広い定義であり、*理解*は多くの異なる意味を持つことができます。例えば、画像内の物体を見つけること（**物体検出**）、何が起こっているかを理解すること（**イベント検出**）、画像をテキストで説明すること、またはシーンを3Dで再構築することなどが含まれます。また、人間の画像に関連する特別なタスクもあります。例えば、年齢や感情の推定、顔の検出と識別、3Dポーズ推定などです。

## [講義前クイズ](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/106)

コンピュータビジョンの最も簡単なタスクの一つは**画像分類**です。

コンピュータビジョンは、しばしばAIの一分野と考えられています。現在、コンピュータビジョンのタスクのほとんどはニューラルネットワークを使用して解決されています。このセクションでは、コンピュータビジョンに使用される特別なタイプのニューラルネットワークである[畳み込みニューラルネットワーク](../07-ConvNets/README.md)について詳しく学んでいきます。

しかし、画像をニューラルネットワークに渡す前に、多くの場合、画像を強化するためにいくつかのアルゴリズム的手法を使用することが理にかなっています。

画像処理に利用できるPythonライブラリはいくつかあります：

* **[imageio](https://imageio.readthedocs.io/en/stable/)** は、さまざまな画像フォーマットの読み書きに使用できます。また、動画フレームを画像に変換するための便利なツールであるffmpegもサポートしています。
* **[Pillow](https://pillow.readthedocs.io/en/stable/index.html)**（PILとしても知られています）は、もう少し強力で、モーフィングやパレット調整などの画像操作もサポートしています。
* **[OpenCV](https://opencv.org/)** は、C++で書かれた強力な画像処理ライブラリで、画像処理の*事実上の*標準となっています。便利なPythonインターフェースもあります。
* **[dlib](http://dlib.net/)** は、多くの機械学習アルゴリズムを実装したC++ライブラリで、コンピュータビジョンアルゴリズムのいくつかも含まれています。Pythonインターフェースもあり、顔や顔のランドマーク検出などの難しいタスクにも使用できます。

## OpenCV

[OpenCV](https://opencv.org/)は、画像処理の*事実上の*標準と見なされています。多くの便利なアルゴリズムがC++で実装されています。PythonからもOpenCVを呼び出すことができます。

OpenCVを学ぶのに良い場所は[このLearn OpenCVコース](https://learnopencv.com/getting-started-with-opencv/)です。私たちのカリキュラムでは、OpenCVを学ぶことが目的ではなく、どのように使用できるかのいくつかの例を示すことが目標です。

### 画像の読み込み

Pythonでは、画像をNumPy配列で便利に表現できます。例えば、320x200ピクセルのグレースケール画像は200x320の配列に格納され、同じ寸法のカラ―画像は200x320x3の形状を持ちます（3つのカラーチャンネル用）。画像を読み込むには、次のコードを使用できます：

```python
import cv2
import matplotlib.pyplot as plt

im = cv2.imread('image.jpeg')
plt.imshow(im)
```

伝統的に、OpenCVはカラ―画像にBGR（青-緑-赤）エンコーディングを使用していますが、他のPythonツールはより伝統的なRGB（赤-緑-青）を使用します。画像を正しく表示するためには、NumPy配列内の次元を入れ替えるか、OpenCVの関数を呼び出してRGBカラースペースに変換する必要があります：

```python
im = cv2.cvtColor(im,cv2.COLOR_BGR2RGB)
```

同じ `cvtColor` function can be used to perform other color space transformations such as converting an image to grayscale or to the HSV (Hue-Saturation-Value) color space.

You can also use OpenCV to load video frame-by-frame - an example is given in the exercise [OpenCV Notebook](../../../../../lessons/4-ComputerVision/06-IntroCV/OpenCV.ipynb).

### Image Processing

Before feeding an image to a neural network, you may want to apply several pre-processing steps. OpenCV can do many things, including:

* **Resizing** the image using `im = cv2.resize(im, (320,200),interpolation=cv2.INTER_LANCZOS)`
* **Blurring** the image using `im = cv2.medianBlur(im,3)` or `im = cv2.GaussianBlur(im, (3,3), 0)`
* Changing the **brightness and contrast** of the image can be done by NumPy array manipulations, as described [in this Stackoverflow note](https://stackoverflow.com/questions/39308030/how-do-i-increase-the-contrast-of-an-image-in-python-opencv).
* Using [thresholding](https://docs.opencv.org/4.x/d7/d4d/tutorial_py_thresholding.html) by calling `cv2.threshold`/`cv2.adaptiveThreshold` 関数は、明るさやコントラストを調整するよりも好まれることがよくあります。
* 画像にさまざまな[変換](https://docs.opencv.org/4.5.5/da/d6e/tutorial_py_geometric_transformations.html)を適用する：
    - **[アフィン変換](https://docs.opencv.org/4.5.5/d4/d61/tutorial_warp_affine.html)** は、画像に回転、リサイズ、歪みを組み合わせる必要があり、画像内の3点のソースとデスティネーションの位置を知っている場合に便利です。アフィン変換は平行線を平行に保ちます。
    - **[透視変換](https://medium.com/analytics-vidhya/opencv-perspective-transformation-9edffefb2143)** は、画像内の4点のソースとデスティネーションの位置を知っている場合に便利です。たとえば、スマートフォンカメラで角度をつけて長方形の文書の写真を撮り、その文書自体の長方形の画像を作成したい場合などです。
* **[光学フロー](https://docs.opencv.org/4.5.5/d4/dee/tutorial_optical_flow.html)** を使用して画像内の動きを理解すること。

## コンピュータビジョンの使用例

私たちの[OpenCVノートブック](../../../../../lessons/4-ComputerVision/06-IntroCV/OpenCV.ipynb)では、コンピュータビジョンが特定のタスクを実行するためにどのように使用できるかのいくつかの例を示します：

* **点字本の写真の前処理**。私たちは、しきい値処理、特徴検出、透視変換、NumPy操作を使用して、ニューラルネットワークによるさらなる分類のために個々の点字記号を分離する方法に焦点を当てています。

![Braille Image](../../../../../translated_images/braille.341962ff76b1bd7044409371d3de09ced5028132aef97344ea4b7468c1208126.ja.jpeg) | ![Braille Image Pre-processed](../../../../../translated_images/braille-result.46530fea020b03c76aac532d7d6eeef7f6fb35b55b1001cd21627907dabef3ed.ja.png) | ![Braille Symbols](../../../../../translated_images/braille-symbols.0159185ab69d533909dc4d7d26a1971b51401c6a80eb3a5584f250ea880af88b.ja.png)
----|-----|-----

> 画像は[OpenCV.ipynb](../../../../../lessons/4-ComputerVision/06-IntroCV/OpenCV.ipynb)からのものです。

* **フレーム差を使用した動画の動きの検出**。カメラが固定されている場合、カメラフィードからのフレームはお互いに非常に似ているはずです。フレームは配列として表されるため、2つの連続するフレームの配列を単純に引き算することで、ピクセルの差分が得られます。静止フレームではこの差分は低く、画像に substantial な動きがあると高くなります。

![Image of video frames and frame differences](../../../../../translated_images/frame-difference.706f805491a0883c938e16447bf5eb2f7d69e812c7f743cbe7d7c7645168f81f.ja.png)

> 画像は[OpenCV.ipynb](../../../../../lessons/4-ComputerVision/06-IntroCV/OpenCV.ipynb)からのものです。

* **光学フローを使用した動きの検出**。[光学フロー](https://docs.opencv.org/3.4/d4/dee/tutorial_optical_flow.html)を使用すると、動画フレーム上の個々のピクセルがどのように動くかを理解できます。光学フローには2つのタイプがあります：

   - **密な光学フロー**は、各ピクセルがどこに移動しているかを示すベクトルフィールドを計算します。
   - **疎な光学フロー**は、画像内のいくつかの特徴（例えば、エッジ）を取り、それらの軌跡をフレームからフレームへと構築することに基づいています。

![Image of Optical Flow](../../../../../translated_images/optical.1f4a94464579a83a10784f3c07fe7228514714b96782edf50e70ccd59d2d8c4f.ja.png)

> 画像は[OpenCV.ipynb](../../../../../lessons/4-ComputerVision/06-IntroCV/OpenCV.ipynb)からのものです。

## ✍️ 例ノートブック：OpenCV [OpenCVを実際に試してみる](../../../../../lessons/4-ComputerVision/06-IntroCV/OpenCV.ipynb)

[OpenCVノートブック](../../../../../lessons/4-ComputerVision/06-IntroCV/OpenCV.ipynb)を探求して、OpenCVを使った実験を行いましょう。

## 結論

時には、動きの検出や指先の検出といった比較的複雑なタスクが純粋にコンピュータビジョンによって解決できることがあります。そのため、コンピュータビジョンの基本的な技術や、OpenCVのようなライブラリができることを知っておくことは非常に役立ちます。

## 🚀 チャレンジ

AIショーの[このビデオ](https://docs.microsoft.com/shows/ai-show/ai-show--2021-opencv-ai-competition--grand-prize-winners--cortic-tigers--episode-32?WT.mc_id=academic-77998-cacaste)を見て、Cortic Tigersプロジェクトについて学び、ロボットを通じてコンピュータビジョンタスクを民主化するためのブロックベースのソリューションをどのように構築したかを学んでください。この分野に新しい学習者を迎え入れるのを助ける他のプロジェクトについて調査してみてください。

## [講義後クイズ](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/206)

## レビューと自己学習

光学フローについては、[この素晴らしいチュートリアル](https://learnopencv.com/optical-flow-in-opencv/)でさらに学んでください。

## [課題](lab/README.md)

このラボでは、シンプルなジェスチャーでビデオを撮影し、光学フローを使用して上下左右の動きを抽出することが目標です。

<img src="images/palm-movement.png" width="30%" alt="Palm Movement Frame"/>

**免責事項**:  
この文書は、機械ベースのAI翻訳サービスを使用して翻訳されています。正確性を追求していますが、自動翻訳には誤りや不正確さが含まれる可能性があることをご承知おきください。元の文書は、その母国語での権威ある情報源と見なされるべきです。重要な情報については、専門の人間翻訳を推奨します。この翻訳の使用から生じる誤解や誤訳について、当社は責任を負いません。