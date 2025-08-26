<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f3d2cee9cb3c52160419e560c57a690e",
  "translation_date": "2025-08-25T20:55:46+00:00",
  "source_file": "lessons/4-ComputerVision/07-ConvNets/lab/README.md",
  "language_code": "sw"
}
-->
# Uainishaji wa Nyuso za Wanyama wa Kipenzi

Kazi ya Maabara kutoka [Mtaala wa AI kwa Kompyuta](https://github.com/microsoft/ai-for-beginners).

## Kazi

Fikiria unahitaji kuunda programu kwa ajili ya kitalu cha wanyama wa kipenzi ili kuorodhesha wanyama wote. Moja ya vipengele bora vya programu kama hiyo itakuwa kugundua moja kwa moja aina ya mnyama kutoka kwenye picha. Hili linaweza kufanikiwa kwa kutumia mitandao ya neva.

Unahitaji kufundisha mtandao wa neva wa convolutional ili kuainisha aina tofauti za paka na mbwa kwa kutumia seti ya data ya **Pet Faces**.

## Seti ya Data

Tutatumia seti ya data ya **Pet Faces**, inayotokana na seti ya data ya wanyama wa kipenzi ya [Oxford-IIIT](https://www.robots.ox.ac.uk/~vgg/data/pets/). Inayo aina 35 tofauti za mbwa na paka.

![Seti ya data tutakayoshughulikia](../../../../../../translated_images/data.50b2a9d5484bdbf0f52f5765b381cec9efe2bd296a98f007f90bedb6ac67f2a8.sw.png)

Ili kupakua seti ya data, tumia kipande hiki cha msimbo:

```python
!wget https://mslearntensorflowlp.blob.core.windows.net/data/petfaces.tar.gz
!tar xfz petfaces.tar.gz
!rm petfaces.tar.gz
```

## Kuanzisha Daftari

Anza maabara kwa kufungua [PetFaces.ipynb](../../../../../../lessons/4-ComputerVision/07-ConvNets/lab/PetFaces.ipynb)

## Jambo la Kujifunza

Umesuluhisha tatizo changamani la uainishaji wa picha kutoka mwanzo! Kulikuwa na madarasa mengi, na bado uliweza kupata usahihi wa kuridhisha! Pia inafaa kupima usahihi wa top-k, kwa sababu ni rahisi kuchanganya baadhi ya madarasa ambayo hata kwa wanadamu si rahisi kuyatofautisha wazi.

**Kanusho**:  
Hati hii imetafsiriwa kwa kutumia huduma ya kutafsiri ya AI [Co-op Translator](https://github.com/Azure/co-op-translator). Ingawa tunajitahidi kuhakikisha usahihi, tafadhali fahamu kuwa tafsiri za kiotomatiki zinaweza kuwa na makosa au kutokuwa sahihi. Hati ya asili katika lugha yake ya awali inapaswa kuzingatiwa kama chanzo cha mamlaka. Kwa taarifa muhimu, tafsiri ya kitaalamu ya binadamu inapendekezwa. Hatutawajibika kwa kutoelewana au tafsiri zisizo sahihi zinazotokana na matumizi ya tafsiri hii.