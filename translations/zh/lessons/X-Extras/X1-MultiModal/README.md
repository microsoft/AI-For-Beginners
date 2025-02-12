# 多模态网络

在变换器模型成功解决自然语言处理任务后，相同或类似的架构已被应用于计算机视觉任务。人们对构建能够*结合*视觉和自然语言能力的模型越来越感兴趣。OpenAI 就是这样的尝试之一，名为 CLIP 和 DALL.E。

## 对比图像预训练 (CLIP)

CLIP 的主要思想是能够将文本提示与图像进行比较，并确定图像与提示的对应程度。

![CLIP 架构](../../../../../translated_images/clip-arch.b3dbf20b4e8ed8be1c38e2bc6100fd3cc257c33cda4692b301be91f791b13ea7.zh.png)

> *图片来自 [这篇博客文章](https://openai.com/blog/clip/)*

该模型在从互联网上获取的图像及其说明上进行训练。对于每个批次，我们获取 N 对 (图像, 文本)，并将它们转换为某种向量表示 I 和 T。这些表示随后被匹配在一起。损失函数的定义是最大化对应于一对 (例如 I 和 T) 的向量之间的余弦相似度，并最小化所有其他对之间的余弦相似度。这就是这个方法被称为 **对比** 的原因。

CLIP 模型/库可以从 [OpenAI GitHub](https://github.com/openai/CLIP) 获取。该方法在 [这篇博客文章](https://openai.com/blog/clip/) 中进行了描述，并在 [这篇论文](https://arxiv.org/pdf/2103.00020.pdf) 中进行了更详细的阐述。

一旦该模型经过预训练，我们可以给它一批图像和一批文本提示，它将返回一个包含概率的张量。CLIP 可用于多个任务：

**图像分类**

假设我们需要对图像进行分类，例如，猫、狗和人。在这种情况下，我们可以给模型一张图像，以及一系列文本提示：“*一张猫的图片*”，“*一张狗的图片*”，“*一张人类的图片*”。在结果的 3 个概率向量中，我们只需选择具有最高值的索引。

![CLIP 用于图像分类](../../../../../translated_images/clip-class.3af42ef0b2b19369a633df5f20ddf4f5a01d6c8ffa181e9d3a0572c19f919f72.zh.png)

> *图片来自 [这篇博客文章](https://openai.com/blog/clip/)*

**基于文本的图像搜索**

我们也可以做相反的事情。如果我们有一组图像，我们可以将这组图像传递给模型，以及一个文本提示——这将为我们提供与给定提示最相似的图像。

## ✍️ 示例: [使用 CLIP 进行图像分类和图像搜索](../../../../../lessons/X-Extras/X1-MultiModal/Clip.ipynb)

打开 [Clip.ipynb](../../../../../lessons/X-Extras/X1-MultiModal/Clip.ipynb) 笔记本以查看 CLIP 的实际应用。

## 使用 VQGAN+CLIP 进行图像生成

CLIP 还可以用于从文本提示中**生成图像**。为此，我们需要一个**生成器模型**，能够根据某些向量输入生成图像。其中一个这样的模型被称为 [VQGAN](https://compvis.github.io/taming-transformers/)（向量量化 GAN）。

VQGAN 与普通 [GAN](../../4-ComputerVision/10-GANs/README.md) 的主要区别如下：
* 使用自回归变换器架构生成组成图像的上下文丰富的视觉部分序列。这些视觉部分又通过 [CNN](../../4-ComputerVision/07-ConvNets/README.md) 学习得到。
* 使用子图像判别器，检测图像的部分是否为“真实”或“虚假”（与传统 GAN 的“全有或全无”方法不同）。

在 [Taming Transformers](https://compvis.github.io/taming-transformers/) 网站上了解更多关于 VQGAN 的信息。

VQGAN 与传统 GAN 之间的重要区别之一是，后者可以从任何输入向量生成不错的图像，而 VQGAN 生成的图像可能不连贯。因此，我们需要进一步指导图像创建过程，这可以通过 CLIP 来实现。

![VQGAN+CLIP 架构](../../../../../translated_images/vqgan.5027fe05051dfa3101950cfa930303f66e6478b9bd273e83766731796e462d9b.zh.png)

为了生成与文本提示对应的图像，我们从一些随机编码向量开始，并将其传递给 VQGAN 以生成图像。然后使用 CLIP 生成一个损失函数，显示图像与文本提示的对应程度。目标是最小化这个损失，使用反向传播来调整输入向量参数。

一个实现 VQGAN+CLIP 的优秀库是 [Pixray](http://github.com/pixray/pixray)。

![Pixray 生成的图片](../../../../../translated_images/a_closeup_watercolor_portrait_of_young_male_teacher_of_literature_with_a_book.2384968e9db8a0d09dc96de938b9f95bde8a7e1c721f48f286a7795bf16d56c7.zh.png) |  ![Pixray 生成的图片](../../../../../translated_images/a_closeup_oil_portrait_of_young_female_teacher_of_computer_science_with_a_computer.e0b6495f210a439077e1c32cc8afdf714e634fe24dc78dc5aa45fd2f560b0ed5.zh.png) | ![Pixray 生成的图片](../../../../../translated_images/a_closeup_oil_portrait_of_old_male_teacher_of_math.5362e67aa7fc2683b9d36a613b364deb7454760cd39205623fc1e3938fa133c0.zh.png)
----|----|----
根据提示 *一张年轻男性文学教师手持书籍的水彩特写肖像* 生成的图片 | 根据提示 *一张年轻女性计算机科学教师手持电脑的油画特写肖像* 生成的图片 | 根据提示 *一张老年男性数学教师在黑板前的油画特写肖像* 生成的图片

> 图片来自 **人工教师** 系列，由 [Dmitry Soshnikov](http://soshnikov.com) 提供

## DALL-E
### [DALL-E 1](https://openai.com/research/dall-e)
DALL-E 是一种经过训练的 GPT-3 版本，旨在根据提示生成图像。它的训练参数达到了 120 亿。

与 CLIP 不同，DALL-E 将文本和图像作为一系列令牌的单一流输入。因此，从多个提示中，您可以基于文本生成图像。

### [DALL-E 2](https://openai.com/dall-e-2)
DALL-E 1 和 DALL-E 2 之间的主要区别在于，后者生成的图像和艺术作品更加真实。

DALL-E 生成的图像示例：
![Pixray 生成的图片](../../../../../translated_images/DALL·E%202023-06-20%2015.56.56%20-%20a%20closeup%20watercolor%20portrait%20of%20young%20male%20teacher%20of%20literature%20with%20a%20book.6c235e8271d9ed10ce985d86aeb241a58518958647973af136912116b9518fce.zh.png) |  ![Pixray 生成的图片](../../../../../translated_images/DALL·E%202023-06-20%2015.57.43%20-%20a%20closeup%20oil%20portrait%20of%20young%20female%20teacher%20of%20computer%20science%20with%20a%20computer.f21dc4166340b6c8b4d1cb57efd1e22127407f9b28c9ac7afe11344065369e64.zh.png) | ![Pixray 生成的图片](../../../../../translated_images/DALL·E%202023-06-20%2015.58.42%20-%20%20a%20closeup%20oil%20portrait%20of%20old%20male%20teacher%20of%20mathematics%20in%20front%20of%20blackboard.d331c2dfbdc3f7c46aa65c0809066f5e7ed4b49609cd259852e760df21051e4a.zh.png)
----|----|----
根据提示 *一张年轻男性文学教师手持书籍的水彩特写肖像* 生成的图片 | 根据提示 *一张年轻女性计算机科学教师手持电脑的油画特写肖像* 生成的图片 | 根据提示 *一张老年男性数学教师在黑板前的油画特写肖像* 生成的图片

## 参考文献

* VQGAN 论文: [高分辨率图像合成的变换器驯化](https://compvis.github.io/taming-transformers/paper/paper.pdf)
* CLIP 论文: [从自然语言监督学习可转移的视觉模型](https://arxiv.org/pdf/2103.00020.pdf)

**免责声明**：  
本文件使用基于机器的人工智能翻译服务进行翻译。尽管我们努力追求准确性，但请注意，自动翻译可能包含错误或不准确之处。原始文件的母语版本应视为权威来源。对于关键信息，建议进行专业人工翻译。我们对因使用此翻译而导致的任何误解或误释不承担任何责任。