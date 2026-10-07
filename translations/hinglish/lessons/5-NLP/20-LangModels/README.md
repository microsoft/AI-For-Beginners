# Pre-Trained Large Language Models

Hamare pichhle saare tasks mein, humne ek neural network ko ek certain task karne ke liye train kiya tha, jisme labeled dataset use hua tha. Bade transformer models, jaise BERT, mein hum language modeling ko self-supervised tareeke se use karte hain taaki ek language model banaya ja sake, jise baad mein specific downstream task ke liye domain-specific training ke saath adapt kiya jaata hai. Halaanki, yeh prove ho chuka hai ki large language models kai tasks bina kisi domain-specific training ke bhi solve kar sakte hain. Aise models ke group ko **GPT**: Generative Pre-Trained Transformer kehte hain.

## [Pre-lecture quiz](https://ff-quizzes.netlify.app/en/ai/quiz/39)

## Text Generation aur Perplexity

Ek neural network ki general tasks bina downstream training ke karne ki ability [Language Models are Unsupervised Multitask Learners](https://cdn.openai.com/better-language-models/language_models_are_unsupervised_multitask_learners.pdf) paper mein present ki gayi hai. Main idea yeh hai ki kai doosre tasks ko **text generation** use karke model kiya ja sakta hai, kyunki text ko samajhne ka matlab hai ki use generate kar paane mein capable hona. Kyunki model ko insaani knowledge ko samete hue vishaal matra mein text par train kiya gaya hai, yeh alag-alag topics ke baare mein bhi knowledgeable ban jaata hai.

> Text ko samajhna aur generate kar paana duniya ke baare mein kuch jaanne ka bhi signal deta hai. Log bhi bade paimane par padhkar seekhte hain, aur GPT networks is approach mein similar hain.

Text generation networks agle word ki probability $$P(w_N)$$ predict karke kaam karte hain. Halaanki, agle word ki unconditional probability text corpus mein is word ki frequency ke barabar hoti hai. GPT humein pichhle words ko dhyan mein rakhte hue agle word ki **conditional probability** deta hai: $$P(w_N | w_{n-1}, ..., w_0)$$

> Aap hamare [Data Science for Beginners curriculum](https://github.com/microsoft/Data-Science-For-Beginners/tree/main/1-Introduction/04-stats-and-probability) mein probabilities ke baare mein aur padh sakte hain.

Language generate karne wale model ki quality ko **perplexity** use karke define kiya ja sakta hai. Yeh ek intrinsic metric hai jo humein kisi task-specific dataset ke bina model ki quality measure karne deta hai. Yeh *sentence ki probability* ke concept par based hai - model un sentences ko high probability deta hai jinke real hone ki sambhavna hoti hai (yaani model unse **perplexed** nahi hota), aur un sentences ko kam probability deta hai jo kam sense banate hain (jaise *Can it does what?*). Jab hum apne model ko real text corpus se sentences dete hain, toh hum ummeed karte hain ki woh high probability aur low **perplexity** dikhayenge. Mathematically, ise test set ki normalized inverse probability ke roop mein define kiya gaya hai:
$$
\mathrm{Perplexity}(W) = \sqrt[N]{1\over P(W_1,...,W_N)}
$$ 

**Aap [Hugging Face ke GPT-powered text editor](https://transformer.huggingface.co/doc/gpt2-large)** ko use karke text generation ke saath experiment kar sakte hain. Is editor mein, aap apna text likhna shuru karte hain, aur **[TAB]** dabane par aapko kai completion options milte hain. Agar woh bahut chhote hain, ya aap unse satisfied nahi hain - dobara [TAB] dabaiye, aur aapko aur options milenge, jisme lambe text ke pieces bhi shaamil hain.

## GPT ek Family hai

GPT ek single model nahi hai, balki [OpenAI](https://openai.com) dwara develop aur train kiye gaye models ka ek collection hai.

GPT models mein shaamil hain:

| [GPT-2](https://huggingface.co/docs/transformers/model_doc/gpt2#openai-gpt2) | [GPT 3](https://openai.com/research/language-models-are-few-shot-learners) | [GPT-4](https://openai.com/gpt-4) |
| -- | -- | -- |
| Language model jisme 1.5 billion tak parameters hain. | Language model jisme 175 billion tak parameters hain. | 100T parameters aur yeh text aur image inputs accept karta hai aur text output deta hai. |

GPT-3 aur GPT-4 models [Microsoft Azure se ek Cognitive Service](https://azure.microsoft.com/en-us/services/cognitive-services/openai-service/#overview?WT.mc_id=academic-77998-cacaste) ke roop mein aur [OpenAI API](https://openai.com/api/) ke roop mein available hain.

## Prompt Engineering

Kyunki GPT ko language aur code samajhne ke liye vishaal matra mein data par train kiya gaya hai, yeh inputs (prompts) ke response mein outputs deta hai. Prompts GPT inputs ya queries hote hain, jinme ek person model ko un tasks par instructions deta hai jo use complete karne hain. Desired result paane ke liye, aapko sabse effective prompt chahiye, jisme sahi words, format, phrases ya symbols tak ka selection shaamil hota hai. Is approach ko [Prompt Engineering](https://learn.microsoft.com/en-us/shows/ai-show/the-basics-of-prompt-engineering-with-azure-openai-service?WT.mc_id=academic-77998-bethanycheum) kehte hain.

[Yeh documentation](https://learn.microsoft.com/en-us/semantic-kernel/prompt-engineering/?WT.mc_id=academic-77998-bethanycheum) aapko prompt engineering ke baare mein aur jaankari deti hai.

## ✍️ Example Notebook: [OpenAI-GPT ke saath khelna](GPT-PyTorch.ipynb)

Agle notebooks mein apni learning jaari rakhiye:

* [OpenAI-GPT aur Hugging Face Transformers ke saath Text Generation](GPT-PyTorch.ipynb)

## Conclusion

Naye general pre-trained language models sirf language structure ko model nahi karte, balki natural language ki vishaal matra ko bhi apne andar samete hue hain. Isliye, inhe kuch NLP tasks ko zero-shot ya few-shot settings mein effectively solve karne ke liye use kiya ja sakta hai.

## [Post-lecture quiz](https://ff-quizzes.netlify.app/en/ai/quiz/40)

---

