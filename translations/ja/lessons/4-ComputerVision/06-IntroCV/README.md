<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "4bedc8e702db17260cfe824d58b6cfd4",
  "translation_date": "2025-08-24T21:10:53+00:00",
  "source_file": "lessons/4-ComputerVision/06-IntroCV/README.md",
  "language_code": "ja"
}
-->
# コンピュータビジョン入門

[コンピュータビジョン](https://wikipedia.org/wiki/Computer_vision)は、コンピュータがデジタル画像を高レベルで理解できるようにすることを目的とした分野です。この定義は非常に広範であり、「理解する」ということは、画像内の物体を見つける（**物体検出**）、何が起きているかを理解する（**イベント検出**）、画像をテキストで説明する、または3Dでシーンを再構築するなど、さまざまな意味を持ちます。人間の画像に関連する特別なタスクもあり、例えば年齢や感情の推定、顔の検出と識別、3Dポーズ推定などがあります。

## [講義前クイズ](https://ff-quizzes.netlify.app/en/ai/quiz/11)

コンピュータビジョンの最も基本的なタスクの一つは、**画像分類**です。

コンピュータビジョンはしばしばAIの一分野と見なされます。現在では、ほとんどのコンピュータビジョンのタスクはニューラルネットワークを使用して解決されています。このセクションでは、コンピュータビジョンに使用される特別なタイプのニューラルネットワーク、[畳み込みニューラルネットワーク](../07-ConvNets/README.md)について学びます。

ただし、画像をニューラルネットワークに渡す前に、多くの場合、画像を強化するためのアルゴリズム的な技術を使用することが理にかなっています。

画像処理に利用できるPythonライブラリはいくつかあります：

* **[imageio](https://imageio.readthedocs.io/en/stable/)** は、さまざまな画像形式の読み書きに使用できます。また、ffmpegをサポートしており、ビデオフレームを画像に変換する便利なツールです。
* **[Pillow](https://pillow.readthedocs.io/en/stable/index.html)**（PILとも呼ばれる）は、より強力で、モーフィングやパレット調整などの画像操作もサポートしています。
* **[OpenCV](https://opencv.org/)** は、C++で書かれた強力な画像処理ライブラリで、画像処理の*事実上の標準*となっています。Pythonインターフェースも便利です。
* **[dlib](http://dlib.net/)** は、多くの機械学習アルゴリズムを実装したC++ライブラリで、コンピュータビジョンアルゴリズムも含まれています。Pythonインターフェースもあり、顔や顔のランドマーク検出などの難しいタスクに使用できます。

## OpenCV

[OpenCV](https://opencv.org/)は、画像処理の*事実上の標準*とされています。C++で実装された多くの便利なアルゴリズムが含まれています。PythonからもOpenCVを呼び出すことができます。

OpenCVを学ぶのに良い場所は[このLearn OpenCVコース](https://learnopencv.com/getting-started-with-opencv/)です。このカリキュラムでは、OpenCVを学ぶことが目的ではなく、使用例やその方法を示すことが目的です。

### 画像の読み込み

Pythonでは、画像をNumPy配列で便利に表現できます。例えば、320x200ピクセルのグレースケール画像は200x320の配列に格納され、同じサイズのカラー画像は200x320x3（3つのカラーチャンネル）という形状になります。画像を読み込むには、以下のコードを使用できます：

```python
import cv2
import matplotlib.pyplot as plt

im = cv2.imread('image.jpeg')
plt.imshow(im)
```

伝統的に、OpenCVはカラー画像にBGR（青-緑-赤）エンコーディングを使用しますが、Pythonの他のツールはより一般的なRGB（赤-緑-青）を使用します。画像を正しく表示するには、NumPy配列の次元を入れ替えるか、OpenCV関数を呼び出してRGBカラースペースに変換する必要があります：

```python
im = cv2.cvtColor(im,cv2.COLOR_BGR2RGB)
```

同じ`cvtColor`関数を使用して、画像をグレースケールやHSV（色相-彩度-明度）カラースペースに変換するなど、他のカラースペース変換を行うこともできます。

OpenCVを使用してビデオをフレームごとに読み込むことも可能です。例は演習[OpenCV Notebook](../../../../../lessons/4-ComputerVision/06-IntroCV/OpenCV.ipynb)に記載されています。

### 画像処理

画像をニューラルネットワークに渡す前に、いくつかの前処理ステップを適用することができます。OpenCVは以下のようなことが可能です：

* `im = cv2.resize(im, (320,200),interpolation=cv2.INTER_LANCZOS)`を使用して画像を**リサイズ**する
* `im = cv2.medianBlur(im,3)`や`im = cv2.GaussianBlur(im, (3,3), 0)`を使用して画像を**ぼかす**
* 画像の**明るさとコントラスト**を変更するには、NumPy配列操作を使用します。[このStackoverflowのノート](https://stackoverflow.com/questions/39308030/how-do-i-increase-the-contrast-of-an-image-in-python-opencv)に記載されています。
* `cv2.threshold`や`cv2.adaptiveThreshold`関数を呼び出して[閾値処理](https://docs.opencv.org/4.x/d7/d4d/tutorial_py_thresholding.html)を使用することは、明るさやコントラストを調整するよりも好ましい場合があります。
* 画像に対してさまざまな[変換](https://docs.opencv.org/4.5.5/da/d6e/tutorial_py_geometric_transformations.html)を適用する：
    - **[アフィン変換](https://docs.opencv.org/4.5.5/d4/d61/tutorial_warp_affine.html)** は、画像の回転、リサイズ、傾きを組み合わせる必要があり、画像内の3点のソースと目的地の位置が分かっている場合に便利です。アフィン変換は平行線を平行に保ちます。
    - **[透視変換](https://medium.com/analytics-vidhya/opencv-perspective-transformation-9edffefb2143)** は、画像内の4点のソースと目的地の位置が分かっている場合に便利です。例えば、スマートフォンのカメラで角度をつけて長方形の文書を撮影し、その文書自体の長方形画像を作成したい場合などです。
* **[オプティカルフロー](https://docs.opencv.org/4.5.5/d4/dee/tutorial_optical_flow.html)** を使用して画像内の動きを理解する。

## コンピュータビジョンの使用例

[OpenCV Notebook](../../../../../lessons/4-ComputerVision/06-IntroCV/OpenCV.ipynb)では、コンピュータビジョンを使用して特定のタスクを実行する例をいくつか紹介しています：

* **点字の本の写真を前処理する**。閾値処理、特徴検出、透視変換、NumPy操作を使用して、個々の点字記号を分離し、ニューラルネットワークによる分類に備える方法に焦点を当てています。

![点字画像](../../../../../translated_images/braille.341962ff76b1bd7044409371d3de09ced5028132aef97344ea4b7468c1208126.ja.jpeg) | ![前処理された点字画像](../../../../../translated_images/braille-result.46530fea020b03c76aac532d7d6eeef7f6fb35b55b1001cd21627907dabef3ed.ja.png) | ![点字記号](../../../../../translated_images/braille-symbols.0159185ab69d533909dc4d7d26a1971b51401c6a80eb3a5584f250ea880af88b.ja.png)
----|-----|-----

> 画像は[OpenCV.ipynb](../../../../../lessons/4-ComputerVision/06-IntroCV/OpenCV.ipynb)より

* **フレーム差分を使用してビデオ内の動きを検出する**。カメラが固定されている場合、カメラフィードのフレームは互いに非常に似ているはずです。フレームが配列として表現されているため、2つの連続するフレームの配列を引き算するだけでピクセル差分が得られます。静的なフレームでは差分は低くなり、画像に大きな動きがあると差分が高くなります。

![ビデオフレームとフレーム差分の画像](../../../../../translated_images/frame-difference.706f805491a0883c938e16447bf5eb2f7d69e812c7f743cbe7d7c7645168f81f.ja.png)

> 画像は[OpenCV.ipynb](../../../../../lessons/4-ComputerVision/06-IntroCV/OpenCV.ipynb)より

* **オプティカルフローを使用して動きを検出する**。[オプティカルフロー](https://docs.opencv.org/3.4/d4/dee/tutorial_optical_flow.html)を使用すると、ビデオフレーム上の個々のピクセルがどのように移動するかを理解できます。オプティカルフローには2種類あります：

   - **密なオプティカルフロー**は、各ピクセルがどこに移動しているかを示すベクトルフィールドを計算します。
   - **疎なオプティカルフロー**は、画像内の特徴的な部分（例：エッジ）を基にして、それらのフレーム間の軌跡を構築します。

![オプティカルフローの画像](../../../../../translated_images/optical.1f4a94464579a83a10784f3c07fe7228514714b96782edf50e70ccd59d2d8c4f.ja.png)

> 画像は[OpenCV.ipynb](../../../../../lessons/4-ComputerVision/06-IntroCV/OpenCV.ipynb)より

## ✍️ サンプルノートブック: OpenCV [OpenCV in Actionを試す](../../../../../lessons/4-ComputerVision/06-IntroCV/OpenCV.ipynb)

[OpenCV Notebook](../../../../../lessons/4-ComputerVision/06-IntroCV/OpenCV.ipynb)を探索して、OpenCVを使った実験をしてみましょう。

## 結論

動きの検出や指先の検出など、比較的複雑なタスクがコンピュータビジョンだけで解決できる場合があります。そのため、コンピュータビジョンの基本的な技術やOpenCVのようなライブラリが何をできるかを知っておくことは非常に役立ちます。

## 🚀 チャレンジ

AIショーの[このビデオ](https://docs.microsoft.com/shows/ai-show/ai-show--2021-opencv-ai-competition--grand-prize-winners--cortic-tigers--episode-32?WT.mc_id=academic-77998-cacaste)を視聴して、Cortic Tigersプロジェクトについて学び、彼らがロボットを通じてコンピュータビジョンタスクを民主化するブロックベースのソリューションをどのように構築したかを確認してください。この分野への新しい学習者を導入するのに役立つ他のプロジェクトについても調査してみてください。

## [講義後クイズ](https://ff-quizzes.netlify.app/en/ai/quiz/12)

## 復習と自己学習

[この素晴らしいチュートリアル](https://learnopencv.com/optical-flow-in-opencv/)でオプティカルフローについてさらに学びましょう。

## [課題](lab/README.md)

このラボでは、簡単なジェスチャーを含むビデオを撮影し、オプティカルフローを使用して上下左右の動きを抽出することが目標です。

<img src="images/palm-movement.png" width="30%" alt="手の動きフレーム"/>

**免責事項**:  
この文書は、AI翻訳サービス [Co-op Translator](https://github.com/Azure/co-op-translator) を使用して翻訳されています。正確性を追求しておりますが、自動翻訳には誤りや不正確な部分が含まれる可能性があることをご承知ください。元の言語で記載された文書が正式な情報源とみなされるべきです。重要な情報については、専門の人間による翻訳を推奨します。この翻訳の使用に起因する誤解や誤認について、当方は一切の責任を負いません。