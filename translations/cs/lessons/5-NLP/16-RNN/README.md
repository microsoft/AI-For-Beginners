<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "58bf4adb210aab53e8f78c8082040e7c",
  "translation_date": "2025-08-25T21:32:06+00:00",
  "source_file": "lessons/5-NLP/16-RNN/README.md",
  "language_code": "cs"
}
-->
# Rekurentní neuronové sítě

## [Kvíz před přednáškou](https://ff-quizzes.netlify.app/en/ai/quiz/31)

V předchozích sekcích jsme používali bohaté sémantické reprezentace textu a jednoduchý lineární klasifikátor nad embeddingy. Tato architektura zachycuje agregovaný význam slov ve větě, ale nezohledňuje **pořadí** slov, protože operace agregace nad embeddingy tuto informaci z původního textu odstranila. Protože tyto modely nedokážou modelovat pořadí slov, nemohou řešit složitější nebo nejednoznačné úkoly, jako je generování textu nebo odpovídání na otázky.

Abychom zachytili význam sekvence textu, musíme použít jinou architekturu neuronové sítě, která se nazývá **rekurentní neuronová síť** (RNN). V RNN procházíme větou sítí po jednom symbolu a síť produkuje určitý **stav**, který následně předáváme zpět do sítě spolu s dalším symbolem.

![RNN](../../../../../translated_images/rnn.27f5c29c53d727b546ad3961637a267f0fe9ec5ab01f2a26a853c92fcefbb574.cs.png)

> Obrázek od autora

Pro danou vstupní sekvenci tokenů X<sub>0</sub>,...,X<sub>n</sub> vytvoří RNN sekvenci bloků neuronové sítě a trénuje tuto sekvenci end-to-end pomocí zpětné propagace. Každý blok sítě přijímá dvojici (X<sub>i</sub>,S<sub>i</sub>) jako vstup a produkuje S<sub>i+1</sub> jako výsledek. Konečný stav S<sub>n</sub> (nebo výstup Y<sub>n</sub>) jde do lineárního klasifikátoru, který produkuje výsledek. Všechny bloky sítě sdílejí stejné váhy a jsou trénovány end-to-end během jedné zpětné propagace.

Protože stavové vektory S<sub>0</sub>,...,S<sub>n</sub> procházejí sítí, je schopna se naučit sekvenční závislosti mezi slovy. Například když se někde v sekvenci objeví slovo *not*, může se naučit negovat určité prvky ve stavovém vektoru, což vede k negaci.

> ✅ Protože váhy všech bloků RNN na obrázku výše jsou sdílené, stejný obrázek lze reprezentovat jako jeden blok (vpravo) s rekurentní zpětnou vazbou, která předává výstupní stav sítě zpět na vstup.

## Anatomie RNN buňky

Podívejme se, jak je organizována jednoduchá RNN buňka. Přijímá předchozí stav S<sub>i-1</sub> a aktuální symbol X<sub>i</sub> jako vstupy a musí produkovat výstupní stav S<sub>i</sub> (a někdy nás také zajímá jiný výstup Y<sub>i</sub>, jako v případě generativních sítí).

Jednoduchá RNN buňka obsahuje dvě váhové matice: jedna transformuje vstupní symbol (nazvěme ji W) a druhá transformuje vstupní stav (H). V tomto případě je výstup sítě vypočítán jako σ(W×X<sub>i</sub>+H×S<sub>i-1</sub>+b), kde σ je aktivační funkce a b je dodatečný bias.

<img alt="Anatomie RNN buňky" src="images/rnn-anatomy.png" width="50%"/>

> Obrázek od autora

V mnoha případech jsou vstupní tokeny před vstupem do RNN prohnány embedding vrstvou, aby se snížila dimenzionalita. V tomto případě, pokud je dimenze vstupních vektorů *emb_size* a stavového vektoru *hid_size*, velikost W je *emb_size*×*hid_size* a velikost H je *hid_size*×*hid_size*.

## Long Short Term Memory (LSTM)

Jedním z hlavních problémů klasických RNN je tzv. problém **mizících gradientů**. Protože RNN jsou trénovány end-to-end během jedné zpětné propagace, mají potíže s propagací chyby do prvních vrstev sítě, a tím pádem se síť nemůže naučit vztahy mezi vzdálenými tokeny. Jedním ze způsobů, jak tento problém obejít, je zavedení **explicitního řízení stavu** pomocí tzv. **bran**. Existují dvě známé architektury tohoto typu: **Long Short Term Memory** (LSTM) a **Gated Relay Unit** (GRU).

![Obrázek ukazující příklad buňky LSTM](../../../../../lessons/5-NLP/16-RNN/images/long-short-term-memory-cell.svg)

> Zdroj obrázku TBD

LSTM síť je organizována podobně jako RNN, ale existují dva stavy, které se předávají z vrstvy do vrstvy: aktuální stav C a skrytý vektor H. V každé jednotce je skrytý vektor H<sub>i</sub> spojen s vstupem X<sub>i</sub> a společně kontrolují, co se stane se stavem C prostřednictvím **bran**. Každá brána je neuronová síť se sigmoidní aktivací (výstup v rozmezí [0,1]), kterou lze chápat jako bitovou masku při násobení stavovým vektorem. Existují následující brány (zleva doprava na obrázku výše):

* **Zapomínací brána** bere skrytý vektor a určuje, které komponenty vektoru C je třeba zapomenout a které předat dál.
* **Vstupní brána** bere určité informace ze vstupního a skrytého vektoru a vkládá je do stavu.
* **Výstupní brána** transformuje stav přes lineární vrstvu s *tanh* aktivací a poté vybírá některé jeho komponenty pomocí skrytého vektoru H<sub>i</sub>, aby vytvořila nový stav C<sub>i+1</sub>.

Komponenty stavu C lze chápat jako určité příznaky, které lze zapínat a vypínat. Například když v sekvenci narazíme na jméno *Alice*, můžeme předpokládat, že se jedná o ženskou postavu, a nastavit příznak ve stavu, že máme ve větě ženské podstatné jméno. Když dále narazíme na frázi *and Tom*, nastavíme příznak, že máme množné číslo. Manipulací se stavem tak můžeme údajně sledovat gramatické vlastnosti částí věty.

> ✅ Skvělým zdrojem pro pochopení vnitřního fungování LSTM je tento výborný článek [Understanding LSTM Networks](https://colah.github.io/posts/2015-08-Understanding-LSTMs/) od Christophera Olaha.

## Bidirekcionální a vícevrstvé RNN

Diskutovali jsme o rekurentních sítích, které fungují jedním směrem, od začátku sekvence do konce. To vypadá přirozeně, protože to připomíná způsob, jakým čteme a posloucháme řeč. Nicméně, protože v mnoha praktických případech máme náhodný přístup ke vstupní sekvenci, může mít smysl spustit rekurentní výpočet v obou směrech. Takové sítě se nazývají **bidirekcionální** RNN. Při práci s bidirekcionální sítí bychom potřebovali dva skryté stavové vektory, jeden pro každý směr.

Rekurentní síť, ať už jednosměrná nebo bidirekcionální, zachycuje určité vzory v sekvenci a může je uložit do stavového vektoru nebo předat do výstupu. Stejně jako u konvolučních sítí můžeme na první vrstvu postavit další rekurentní vrstvu, která zachytí vzory vyšší úrovně a staví na vzorech nižší úrovně extrahovaných první vrstvou. To nás přivádí k pojmu **vícevrstvé RNN**, která se skládá ze dvou nebo více rekurentních sítí, kde výstup předchozí vrstvy je předán jako vstup do další vrstvy.

![Obrázek ukazující vícevrstvou LSTM RNN](../../../../../translated_images/multi-layer-lstm.dd975e29bb2a59fe58b429db833932d734c81f211cad2783797a9608984acb8c.cs.jpg)

*Obrázek z [tohoto skvělého článku](https://towardsdatascience.com/from-a-lstm-cell-to-a-multilayer-lstm-network-with-pytorch-2899eb5696f3) od Fernanda Lópeze*

## ✍️ Cvičení: Embeddingy

Pokračujte ve studiu v následujících noteboocích:

* [RNNs s PyTorch](../../../../../lessons/5-NLP/16-RNN/RNNPyTorch.ipynb)
* [RNNs s TensorFlow](../../../../../lessons/5-NLP/16-RNN/RNNTF.ipynb)

## Závěr

V této jednotce jsme viděli, že RNN lze použít pro klasifikaci sekvencí, ale ve skutečnosti zvládnou mnohem více úkolů, jako je generování textu, strojový překlad a další. Těmto úkolům se budeme věnovat v další jednotce.

## 🚀 Výzva

Projděte si literaturu o LSTM a zvažte jejich aplikace:

- [Grid Long Short-Term Memory](https://arxiv.org/pdf/1507.01526v1.pdf)
- [Show, Attend and Tell: Neural Image Caption
Generation with Visual Attention](https://arxiv.org/pdf/1502.03044v2.pdf)

## [Kvíz po přednášce](https://ff-quizzes.netlify.app/en/ai/quiz/32)

## Recenze a samostudium

- [Understanding LSTM Networks](https://colah.github.io/posts/2015-08-Understanding-LSTMs/) od Christophera Olaha.

## [Úkol: Notebooks](assignment.md)

**Prohlášení:**  
Tento dokument byl přeložen pomocí služby pro automatický překlad [Co-op Translator](https://github.com/Azure/co-op-translator). Ačkoli se snažíme o přesnost, mějte prosím na paměti, že automatické překlady mohou obsahovat chyby nebo nepřesnosti. Původní dokument v jeho původním jazyce by měl být považován za autoritativní zdroj. Pro důležité informace se doporučuje profesionální lidský překlad. Neodpovídáme za žádná nedorozumění nebo nesprávné interpretace vyplývající z použití tohoto překladu.