# Deep Learning Training Tricks

Jaise-jaise neural networks deep hote jaate hain, unki training aur zyada challenging ho jaati hai. Ek bada problem hai jise [vanishing gradients](https://en.wikipedia.org/wiki/Vanishing_gradient_problem) ya [exploding gradients](https://deepai.org/machine-learning-glossary-and-terms/exploding-gradient-problem#:~:text=Exploding%20gradients%20are%20a%20problem,updates%20are%20small%20and%20controlled.) kehte hain. [Yeh post](https://towardsdatascience.com/the-vanishing-exploding-gradient-problem-in-deep-neural-networks-191358470c11) in problems ka accha introduction deti hai.

Deep networks ki training ko zyada efficient banane ke liye kuch techniques use ki ja sakti hain.

## Values ko reasonable range mein rakhna

Numerical computations ko zyada stable banane ke liye, humein dhyan rakhna chahiye ki hamare neural network ki saari values reasonable scale mein hon, aam taur par [-1..1] ya [0..1]. Yeh koi bahut strict requirement nahi hai, lekin floating point computations ki nature aisi hai ki alag-alag magnitude ki values ko ek saath accurately handle nahi kiya ja sakta. Jaise, agar hum 10<sup>-10</sup> aur 10<sup>10</sup> ko add karein, toh hamein shayad 10<sup>10</sup> hi milega, kyunki chhoti value ko badi value ke same order mein "convert" kiya jayega, aur is tarah mantissa kho jayega.

Zyadatar activation functions mein [-1..1] ke aaspaas non-linearity hoti hai, isliye saare input data ko [-1..1] ya [0..1] interval mein scale karna samajhdaari ki baat hai.

## Initial Weight Initialization

Ideal taur par, hum chahte hain ki network layers se guzarne ke baad bhi values same range mein rahein. Isliye weights ko is tarah initialize karna zaroori hai ki values ka distribution preserve rahe.

Normal distribution **N(0,1)** accha idea nahi hai, kyunki agar hamare paas *n* inputs hain, toh output ka standard deviation *n* hoga, aur values [0..1] interval se bahar ja sakti hain.

Neeche diye gaye initializations aksar use kiye jaate hain:

- Uniform distribution -- `uniform`
- **N(0,1/n)** -- `gaussian`
- **N(0,1/√n_in)** yeh guarantee deta hai ki zero mean aur standard deviation 1 wale inputs ke liye wahi mean/standard deviation bana rahega.
- **N(0,√2/(n_in+n_out))** -- jise **Xavier initialization** (`glorot`) kehte hain, yeh forward aur backward propagation dono ke dauran signals ko range mein rakhne mein help karta hai.

## Batch Normalization

Sahi weight initialization ke bawajood, training ke dauran weights bahut bade ya chhote ho sakte hain, aur woh signals ko proper range se bahar le ja sakte hain. Hum **normalization** techniques use karke signals ko wapas la sakte hain. Kai techniques hain (weight normalization, layer normalization), lekin sabse zyada use hone wali technique batch normalization hai.

**Batch normalization** ka idea yeh hai ki minibatch ki saari values ko dhyan mein rakha jaye, aur un values ke basis par normalization (jaise mean ghataana aur standard deviation se divide karna) kiya jaye. Ise ek network layer ke roop mein implement kiya jaata hai, jo weights apply karne ke baad, lekin activation function se pehle yeh normalization karti hai. Result mein, hamein higher final accuracy aur faster training dekhne ko milti hai.

Batch normalization par yeh [original paper](https://arxiv.org/pdf/1502.03167.pdf), [Wikipedia par explanation](https://en.wikipedia.org/wiki/Batch_normalization), aur [ek accha introductory blog post](https://towardsdatascience.com/batch-normalization-in-3-levels-of-understanding-14c2da90a338) (aur [Russian mein](https://habrahabr.ru/post/309302/)) available hai.

## Dropout

**Dropout** ek interesting technique hai jo training ke dauran random neurons ka ek certain percentage hata deti hai. Ise ek layer ke roop mein implement kiya jaata hai jisme ek parameter hota hai (hataye jaane wale neurons ka percentage, aam taur par 10%-50%), aur training ke dauran yeh input vector ke random elements ko zero kar deta hai, uske baad hi use agli layer mein bheja jaata hai.

Halaanki yeh idea ajeeb lag sakta hai, aap [`Dropout.ipynb`](../../../../../lessons/4-ComputerVision/08-TransferLearning/Dropout.ipynb) notebook mein MNIST digit classifier ki training par dropout ka effect dekh sakte hain. Yeh training ko tez karta hai aur kam training epochs mein higher accuracy paane deta hai.

Is effect ko kai tareekon se samjhaya ja sakta hai:

- Ise model ke liye ek random shock factor maana ja sakta hai, jo optimization ko local minimum se bahar nikaalta hai.
- Ise *implicit model averaging* maana ja sakta hai, kyunki hum keh sakte hain ki dropout ke dauran hum thoda alag model train kar rahe hote hain.

> *Kuch log kehte hain ki jab koi nashe mein vyakti kuch seekhne ki koshish karta hai, toh woh agle din subah use ek aam vyakti ke mukaable behtar yaad rakhta hai, kyunki kuch kharaab neurons wala dimaag meaning samajhne ke liye behtar adjust ho jaata hai. Humne kabhi yeh test nahi kiya ki yeh sach hai ya nahi.*

## Overfitting ko rokna

Deep learning ka ek bahut important pehlu hai [overfitting](../../3-NeuralNetworks/05-Frameworks/Overfitting.md) ko rok paana. Halaanki ek bahut powerful neural network model use karne ka mann kar sakta hai, humein hamesha model parameters ki sankhya aur training samples ki sankhya ke beech balance banaye rakhna chahiye.

> Dhyan rakhiye ki aap [overfitting](../../3-NeuralNetworks/05-Frameworks/Overfitting.md) ka concept samajhte hain jo humne pehle introduce kiya tha!

Overfitting ko rokne ke kai tareeke hain:

- Early stopping -- validation set par error ko lagaataar monitor karna aur jab validation error badhne lage toh training rok dena.
- Explicit weight decay / regularization -- loss function mein weights ki high values ke liye ek extra penalty jodna, jo model ko bahut unstable results dene se rokta hai.
- Model averaging -- kai models train karna aur phir results ka average nikaalna. Yeh variance ko kam karne mein help karta hai.
- Dropout (implicit model averaging)

## Optimizers / Training algorithms

Training ka ek aur important pehlu ek accha training algorithm chunna hai. Jabki traditional **gradient descent** ek reasonable choice hai, yeh kabhi-kabhi bahut slow ho sakta hai, ya doosre problems paida kar sakta hai.

Deep learning mein, hum **Stochastic Gradient Descent** (SGD) use karte hain, jo training set se randomly chune gaye minibatch par apply kiya gaya gradient descent hai. Weights ko is formula se adjust kiya jaata hai:

w<sup>t+1</sup> = w<sup>t</sup> - η∇ℒ

### Momentum

**Momentum SGD** mein, hum pichhle steps ke gradient ka ek hissa bana kar rakhte hain. Yeh waisa hi hai jaise hum inertia ke saath kahin ja rahe hon, aur humein ek alag direction mein dhakka mile, toh hamari trajectory turant nahi badalti, balki original motion ka kuch hissa bana rehta hai. Yahan hum *speed* ko represent karne ke liye ek aur vector v introduce karte hain:

- v<sup>t+1</sup> = γ v<sup>t</sup> - η∇ℒ
- w<sup>t+1</sup> = w<sup>t</sup> + v<sup>t+1</sup>

Yahan parameter γ batata hai ki hum inertia ko kitna dhyan mein lete hain: γ=0 traditional SGD ke barabar hai; γ=1 ek pure motion equation hai.

### Adam, Adagrad, aadi

Kyunki har layer mein hum signals ko kisi matrix W<sub>i</sub> se multiply karte hain, ||W<sub>i</sub>|| ke basis par, gradient ya toh ghat kar 0 ke kareeb ho sakta hai, ya indefinitely badh sakta hai. Yahi Exploding/Vanishing Gradients problem ka saar hai.

Is problem ka ek solution yeh hai ki equation mein sirf gradient ki direction use ki jaye, aur uski magnitude ko ignore kiya jaye, yaani:

w<sup>t+1</sup> = w<sup>t</sup> - η(∇ℒ/||∇ℒ||), jahan ||∇ℒ|| = √∑(∇ℒ)<sup>2</sup>

Is algorithm ko **Adagrad** kehte hain. Isi idea ko use karne wale doosre algorithms: **RMSProp**, **Adam**

> **Adam** ko kai applications ke liye ek bahut efficient algorithm maana jaata hai, isliye agar aap sure nahi hain ki kaunsa use karein - Adam use kijiye.

### Gradient clipping

Gradient clipping upar wale idea ka ek extension hai. Jab ||∇ℒ|| ≤ θ, toh hum weight optimization mein original gradient consider karte hain, aur jab ||∇ℒ|| > θ - toh hum gradient ko uske norm se divide karte hain. Yahan θ ek parameter hai, zyadatar cases mein hum θ=1 ya θ=10 le sakte hain.

### Learning rate decay

Training ki success aksar learning rate parameter η par depend karti hai. Yeh maanna logical hai ki η ki badi values faster training deti hain, jo hum aam taur par training ki shuruaat mein chahte hain, aur phir η ki chhoti values humein network ko fine-tune karne deti hain. Isliye, zyadatar cases mein hum training ke process mein η ko kam karna chahte hain.

Yeh har training epoch ke baad η ko kisi number (jaise 0.98) se multiply karke kiya ja sakta hai, ya zyada complex **learning rate schedule** use karke.

## Alag-alag network architectures

Aapki problem ke liye sahi network architecture chunna mushkil ho sakta hai. Aam taur par, hum woh architecture chunenge jo hamare specific task (ya similar task) ke liye kaam karta hua prove ho chuka ho. Yahan computer vision ke liye neural network architectures ka [ek accha overview](https://www.topbots.com/a-brief-history-of-neural-network-architectures/) hai.

> Yeh important hai ki hum aisa architecture chunein jo hamare paas available training samples ki sankhya ke liye kaafi powerful ho. Bahut powerful model chunne se [overfitting](../../3-NeuralNetworks/05-Frameworks/Overfitting.md) ho sakti hai.

Ek aur accha tareeka yeh hoga ki aisa architecture use kiya jaye jo required complexity ke hisaab se automatically adjust ho jaye. Kuch had tak, **ResNet** architecture aur **Inception** self-adjusting hain. [Computer vision architectures ke baare mein aur jaankari](../07-ConvNets/CNN_Architectures.md).

---

<!-- HINGLISH NOTE START -->
**Note**:
Yeh document Hindi translation ko Hinglish (Roman script) mein convert karke banaya gaya hai, taaki padhna aur samajhna aasaan ho.
Isme kuch galtiyan ya anuvaad ki kamiyan ho sakti hain. Sabse sahi jaankari ke liye original English document ko hi authoritative source maanein.
<!-- HINGLISH NOTE END -->
