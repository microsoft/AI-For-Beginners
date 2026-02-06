# Večrazredna klasifikacija s perceptronom

Laboratorijska naloga iz [Učnega načrta za začetnike v umetni inteligenci](https://github.com/microsoft/ai-for-beginners).

## Naloga

Z uporabo kode, ki smo jo razvili v tej lekciji za binarno klasifikacijo ročno napisanih številk MNIST, ustvarite večrazredni klasifikator, ki bo sposoben prepoznati katerokoli številko. Izračunajte natančnost klasifikacije na učnem in testnem naboru podatkov ter izpišite matriko zmede.

## Namigi

1. Za vsako številko ustvarite nabor podatkov za binarno klasifikacijo "ta številka proti vsem ostalim številkam".
1. Natrenirajte 10 različnih perceptronov za binarno klasifikacijo (enega za vsako številko).
1. Definirajte funkcijo, ki bo klasificirala vhodno številko.

> **Namig**: Če združimo uteži vseh 10 perceptronov v eno matriko, bi morali biti sposobni uporabiti vseh 10 perceptronov na vhodne številke z eno matrično množitvijo. Najverjetnejšo številko lahko nato najdemo z uporabo operacije `argmax` na izhodu.

## Začetni zvezek

Začnite laboratorijsko nalogo z odpiranjem [PerceptronMultiClass.ipynb](PerceptronMultiClass.ipynb)

---

**Omejitev odgovornosti**:  
Ta dokument je bil preveden z uporabo storitve za strojno prevajanje [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas prosimo, da upoštevate, da lahko avtomatizirani prevodi vsebujejo napake ali netočnosti. Izvirni dokument v njegovem izvirnem jeziku je treba obravnavati kot avtoritativni vir. Za ključne informacije priporočamo strokovno človeško prevajanje. Ne prevzemamo odgovornosti za morebitna nesporazumevanja ali napačne razlage, ki izhajajo iz uporabe tega prevoda.