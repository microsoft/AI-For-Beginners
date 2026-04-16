# 多模态网络

在Transformer模型成功解决NLP任务后，相同或类似的架构也被应用于计算机视觉任务。越来越多的人开始关注构建能够*结合*视觉和自然语言能力的模型。其中一个尝试是由OpenAI完成的，称为CLIP和DALL.E。

## 对比图像预训练（CLIP）

CLIP的核心思想是能够比较文本提示与图像，并确定图像与提示的匹配程度。

![CLIP架构](../../../../../translated_images/zh-CN/clip-arch.b3dbf20b4e8ed8be.webp)

> *图片来源于[这篇博客](https://openai.com/blog/clip/)*

该模型通过从互联网获取的图像及其标题进行训练。对于每个批次，我们获取N对（图像，文本），并将它们转换为一些向量表示I，..., I / T，..., T。这些表示随后进行匹配。损失函数的定义是最大化对应一对（例如I和T）的向量之间的余弦相似度，同时最小化所有其他对之间的余弦相似度。这就是为什么这种方法被称为**对比学习**。

CLIP模型/库可以从[OpenAI GitHub](https://github.com/openai/CLIP)获取。该方法在[这篇博客](https://openai.com/blog/clip/)中有所描述，并在[这篇论文](https://arxiv.org/pdf/2103.00020.pdf)中有更详细的说明。

一旦该模型被预训练，我们可以给它一批图像和一批文本提示，它将返回一个概率张量。CLIP可以用于以下任务：

**图像分类**

假设我们需要将图像分类为猫、狗和人类。在这种情况下，我们可以给模型一个图像，以及一系列文本提示：“*一张猫的图片*”、“*一张狗的图片*”、“*一张人类的图片*”。在结果的3个概率向量中，我们只需选择值最高的索引。

![CLIP用于图像分类](../../../../../translated_images/zh-CN/clip-class.3af42ef0b2b19369.webp)

> *图片来源于[这篇博客](https://openai.com/blog/clip/)*

**基于文本的图像搜索**

我们也可以反过来操作。如果我们有一组图像，我们可以将这组图像传递给模型，并提供一个文本提示——这将返回与给定提示最相似的图像。

## ✍️ 示例：[使用CLIP进行图像分类和图像搜索](../../../../../lessons/X-Extras/X1-MultiModal/Clip.ipynb)

打开[Clip.ipynb](../../../../../lessons/X-Extras/X1-MultiModal/Clip.ipynb)笔记本，查看CLIP的实际应用。

## 使用VQGAN+CLIP进行图像生成

CLIP还可以用于从文本提示生成**图像**。为了实现这一点，我们需要一个**生成器模型**，能够根据某些向量输入生成图像。其中一个这样的模型称为[VQGAN](https://compvis.github.io/taming-transformers/)（向量量化GAN）。

VQGAN与普通[GAN](../../4-ComputerVision/10-GANs/README.md)的主要区别在于以下几点：
* 使用自回归Transformer架构生成一系列上下文丰富的视觉部分，这些部分组成图像。这些视觉部分由[卷积神经网络（CNN）](../../4-ComputerVision/07-ConvNets/README.md)学习。
* 使用子图像判别器来检测图像的部分是“真实”还是“伪造”（与传统GAN的“全或无”方法不同）。

可以在[Taming Transformers](https://compvis.github.io/taming-transformers/)网站上了解更多关于VQGAN的信息。

VQGAN与传统GAN的一个重要区别在于，后者可以从任何输入向量生成一个不错的图像，而VQGAN可能生成一个不连贯的图像。因此，我们需要进一步引导图像创建过程，这可以通过CLIP来实现。

![VQGAN+CLIP架构](../../../../../translated_images/zh-CN/vqgan.5027fe05051dfa31.webp)

为了生成与文本提示相对应的图像，我们从一些随机编码向量开始，将其传递给VQGAN以生成图像。然后使用CLIP生成一个损失函数，显示图像与文本提示的匹配程度。目标是通过反向传播调整输入向量参数以最小化该损失。

一个实现VQGAN+CLIP的优秀库是[Pixray](http://github.com/pixray/pixray)。

![Pixray生成的图片](../../../../../translated_images/zh-CN/a_closeup_watercolor_portrait_of_young_male_teacher_of_literature_with_a_book.2384968e9db8a0d0.webp) |  ![Pixray生成的图片](../../../../../translated_images/zh-CN/a_closeup_oil_portrait_of_young_female_teacher_of_computer_science_with_a_computer.e0b6495f210a4390.webp) | ![Pixray生成的图片](../../../../../translated_images/zh-CN/a_closeup_oil_portrait_of_old_male_teacher_of_math.5362e67aa7fc2683.webp)
----|----|----
从提示*一张年轻男性文学教师拿着书的水彩特写肖像*生成的图片 | 从提示*一张年轻女性计算机科学教师拿着电脑的油画特写肖像*生成的图片 | 从提示*一张老年男性数学教师站在黑板前的油画特写肖像*生成的图片

> 图片来自**人工教师**系列，由[Dmitry Soshnikov](http://soshnikov.com)创作

## DALL-E
### [DALL-E 1](https://openai.com/research/dall-e)
DALL-E是一个基于GPT-3的版本，能够根据提示生成图像。它使用了120亿参数进行训练。

与CLIP不同，DALL-E将文本和图像作为一个单一的令牌流输入。因此，可以根据多个提示生成图像。

### [DALL-E 2](https://openai.com/dall-e-2)
DALL-E 1和2的主要区别在于，后者能够生成更真实的图像和艺术作品。

以下是使用DALL-E生成图像的示例：
![DALL-E生成的图片](../../../../../translated_images/zh-CN/DALL·E%202023-06-20%2015.56.56%20-%20a%20closeup%20watercolor%20portrait%20of%20young%20male%20teacher%20of%20literature%20with%20a%20book.6c235e8271d9ed10ce985d86aeb241a58518958647973af136912116b9518fce.png) |  ![DALL-E生成的图片](../../../../../translated_images/zh-CN/DALL·E%202023-06-20%2015.57.43%20-%20a%20closeup%20oil%20portrait%20of%20young%20female%20teacher%20of%20computer%20science%20with%20a%20computer.f21dc4166340b6c8b4d1cb57efd1e22127407f9b28c9ac7afe11344065369e64.png) | ![DALL-E生成的图片](../../../../../translated_images/zh-CN/DALL·E%202023-06-20%2015.58.42%20-%20%20a%20closeup%20oil%20portrait%20of%20old%20male%20teacher%20of%20mathematics%20in%20front%20of%20blackboard.d331c2dfbdc3f7c46aa65c0809066f5e7ed4b49609cd259852e760df21051e4a.png)
----|----|----
从提示*一张年轻男性文学教师拿着书的水彩特写肖像*生成的图片 | 从提示*一张年轻女性计算机科学教师拿着电脑的油画特写肖像*生成的图片 | 从提示*一张老年男性数学教师站在黑板前的油画特写肖像*生成的图片

## 参考文献

* VQGAN论文：[Taming Transformers for High-Resolution Image Synthesis](https://compvis.github.io/taming-transformers/paper/paper.pdf)
* CLIP论文：[Learning Transferable Visual Models From Natural Language Supervision](https://arxiv.org/pdf/2103.00020.pdf)

**免责声明**：  
本文档使用AI翻译服务 [Co-op Translator](https://github.com/Azure/co-op-translator) 进行翻译。尽管我们努力确保翻译的准确性，但请注意，自动翻译可能包含错误或不准确之处。应以原始语言的文档作为权威来源。对于关键信息，建议使用专业人工翻译。我们对因使用此翻译而引起的任何误解或误读不承担责任。