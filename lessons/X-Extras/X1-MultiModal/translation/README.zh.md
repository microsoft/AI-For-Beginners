# 多模态网络

在transformer模型在解决自然语言处理任务方面取得成功之后，相似的架构也被应用于计算机视觉任务中。人们越来越关注构建能够*结合*视觉和自然语言能力的模型。OpenAI进行了这样一种尝试，称为CLIP和DALL.E。

## 对比图像预训练（CLIP）

CLIP的主要思想是能够将文本提示与图像进行比较，并确定图像与提示的匹配程度。

![CLIP架构](../images/clip-arch.png)> *图片来自[这篇博客文章](https://openai.com/blog/clip/)*

该模型是通过从互联网上获取的图像和其标题进行训练的。对于每个批次，我们取N对(image, text)，将它们转换为一些向量表示：I<sub>1</sub>,..., I<sub>N</sub> / T<sub>1</sub>, ..., T<sub>N</sub>。然后，将这些表示进行匹配。损失函数定义为最大化一对向量的余弦相似度（例如，I<sub>i</sub>和T<sub>i</sub>之间的相似度），并最小化所有其他对之间的余弦相似度。这就是为什么这种方法被称为**对比学习**的原因。

CLIP模型/库可以从[OpenAI GitHub](https://github.com/openai/CLIP)获取。这个方法在[这篇博客文章](https://openai.com/blog/clip/)中进行了描述，并且在[这篇论文](https://arxiv.org/pdf/2103.00020.pdf)中有更详细的说明。

一旦这个模型被预训练，我们可以给它一批图像和一批文本提示，它将返回一个包含概率的张量。CLIP可以用于多个任务：

**图像分类**假设我们需要对图片进行分类，比如猫、狗和人类。在这种情况下，我们可以为模型提供一张图片以及一系列文本提示：“*一张猫的图片*”，“*一张狗的图片*”，“*一张人的图片*”。在得到的3个概率值的向量中，我们只需要选择具有最高值的索引。

![CLIP for Image Classification](../images/clip-class.png)

> *图片来自于[这篇博客文章](https://openai.com/blog/clip/)*

**基于文本的图片搜索**

我们也可以做相反的事情。如果我们有一系列图片，我们可以将这个集合传递给模型，再加上一个文本提示，这样就可以得到与给定提示最相似的图片。## ✍️ 示例：[使用CLIP进行图像分类和图像搜索](../Clip.ipynb)

打开[Clip.ipynb](../Clip.ipynb)笔记本以查看CLIP的实际应用。

## 使用VQGAN+CLIP进行图像生成

CLIP也可以用于根据文本提示生成图像。为了做到这一点，我们需要一个能够根据一些向量输入生成图像的**生成模型**。其中一个这样的模型被称为[VQGAN](https://compvis.github.io/taming-transformers/)（矢量量化GAN）。

VQGAN与普通的[GAN](../../../4-ComputerVision/10-GANs/translation/README.zh.md)的主要区别在于以下几点：
* 使用自回归变压器架构生成图像的上下文丰富的可视部分序列。这些可视部分是通过[CNN](../../../4-ComputerVision/07-ConvNets/translation/README.zh.md)学习的。* 使用子图鉴别器来检测图像的部分是“真实”的还是“假的”（与传统GAN中的“全有全无”方法不同）。

在[Taming Transformers](https://compvis.github.io/taming-transformers/)网站上了解更多关于VQGAN的信息。

VQGAN和传统的GAN之间的一个重要区别是，后者可以从任何输入向量生成一个体面的图像，而VQGAN可能会生成一个不连贯的图像。因此，我们需要进一步引导图像的创建过程，这可以使用CLIP来完成。

![VQGAN+CLIP架构](../images/vqgan.png)

要生成与文本提示相对应的图像，我们首先从一些随机编码向量开始，然后通过VQGAN生成一个图像。然后使用CLIP生成一个损失函数，显示图像与文本提示的匹配程度。然后，目标是通过反向传播来最小化这个损失，以调整输入向量参数。一个实现了VQGAN+CLIP的优秀库是[Pixray](http://github.com/pixray/pixray)

![由Pixray生成的图片](../images/a_closeup_watercolor_portrait_of_young_male_teacher_of_literature_with_a_book.png) |  ![由Pixray生成的图片](../images/a_closeup_oil_portrait_of_young_female_teacher_of_computer_science_with_a_computer.png) | ![由Pixray生成的图片](../images/a_closeup_oil_portrait_of_old_male_teacher_of_math.png)
----|----|----
从提示*一个拿着书的年轻男性文学教师的水彩近景肖像*生成的图片 | 从提示*一个拿着电脑的年轻女性计算机科学教师的油画近景肖像*生成的图片 | 从提示*一个站在黑板前的年老数学教师的油画近景肖像*生成的图片

> 来自[Dmitry Soshnikov](http://soshnikov.com)的**Artificial Teachers**系列的图片

## DALL-E
### [DALL-E 1](https://openai.com/research/dall-e)DALL-E是GPT-3的一个版本，用于根据提示生成图像。它使用了120亿个参数进行训练。

与CLIP不同，DALL-E对于图像和文本，都将其作为单个令牌流进行处理。因此，你可以根据文本生成多个提示的图像。

### [DALL-E 2](https://openai.com/dall-e-2)
DALL-E 1和2之间的主要区别是，DALL-E 2可以生成更加逼真的图像和艺术作品。

以下是使用DALL-E生成的图像示例：
![由Pixray生成的图片](../images/DALL·E%202023-06-20%2015.56.56%20-%20a%20closeup%20watercolor%20portrait%20of%20young%20male%20teacher%20of%20literature%20with%20a%20book.png) |  ![由Pixray生成的图片](../images/DALL·E%202023-06-20%2015.57.43%20-%20a%20closeup%20oil%20portrait%20of%20young%20female%20teacher%20of%20computer%20science%20with%20a%20computer.png) | ![由Pixray生成的图片](../images/DALL·E%202023-06-20%2015.58.42%20-%20%20a%20closeup%20oil%20portrait%20of%20old%20male%20teacher%20of%20mathematics%20in%20front%20of%20blackboard.png)
----|----|----

## 引用

* VQGAN论文：[驯服变形器用于高分辨率图像合成](https://compvis.github.io/taming-transformers/paper/paper.pdf)
* CLIP论文：[从自然语言监督中学习可迁移的视觉模型](https://arxiv.org/pdf/2103.00020.pdf)