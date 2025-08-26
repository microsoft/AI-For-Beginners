<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "7336583e4630220c835335da640016db",
  "translation_date": "2025-08-26T00:01:19+00:00",
  "source_file": "lessons/3-NeuralNetworks/03-Perceptron/lab/README.md",
  "language_code": "sl"
}
-->
# Večrazredna klasifikacija s perceptronom

Laboratorijska naloga iz [Učnega načrta za začetnike v umetni inteligenci](https://github.com/microsoft/ai-for-beginners).

## Naloga

Z uporabo kode, ki smo jo razvili v tej lekciji za binarno klasifikacijo ročno napisanih številk MNIST, ustvarite večrazredni klasifikator, ki bo sposoben prepoznati katerokoli številko. Izračunajte natančnost klasifikacije na učnem in testnem naboru podatkov ter izpišite matriko zmede.

## Namigi

1. Za vsako številko ustvarite nabor podatkov za binarno klasifikacijo "ta številka proti vsem ostalim številkam".
1. Natrenirajte 10 različnih perceptronov za binarno klasifikacijo (enega za vsako številko).
1. Definirajte funkcijo, ki bo razvrstila vhodno številko.

> **Namig**: Če združimo uteži vseh 10 perceptronov v eno matriko, lahko vseh 10 perceptronov uporabimo na vhodnih številkah z eno matriko množenja. Najverjetnejšo številko lahko nato najdemo z uporabo operacije `argmax` na izhodu.

## Začetni zvezek

Začnite nalogo z odpiranjem [PerceptronMultiClass.ipynb](../../../../../../lessons/3-NeuralNetworks/03-Perceptron/lab/PerceptronMultiClass.ipynb)

**Omejitev odgovornosti**:  
Ta dokument je bil preveden z uporabo storitve AI za prevajanje [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas prosimo, da upoštevate, da lahko avtomatizirani prevodi vsebujejo napake ali netočnosti. Izvirni dokument v njegovem maternem jeziku je treba obravnavati kot avtoritativni vir. Za ključne informacije priporočamo profesionalni človeški prevod. Ne prevzemamo odgovornosti za morebitna nesporazumevanja ali napačne razlage, ki bi nastale zaradi uporabe tega prevoda.