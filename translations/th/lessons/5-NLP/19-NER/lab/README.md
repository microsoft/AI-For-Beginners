# การรู้จำชื่อเฉพาะ (NER)

การบ้านจาก [AI for Beginners Curriculum](https://github.com/microsoft/ai-for-beginners)

## งานที่ต้องทำ

ในแลปนี้ คุณจะต้องฝึกโมเดลการรู้จำชื่อเฉพาะ (NER) สำหรับคำศัพท์ทางการแพทย์

## ชุดข้อมูล

เพื่อฝึกโมเดล NER เราจำเป็นต้องมีชุดข้อมูลที่มีการติดป้ายกำกับคำศัพท์ทางการแพทย์อย่างเหมาะสม [ชุดข้อมูล BC5CDR](https://biocreative.bioinformatics.udel.edu/tasks/biocreative-v/track-3-cdr/) มีการติดป้ายกำกับคำศัพท์เกี่ยวกับโรคและสารเคมีจากเอกสารมากกว่า 1,500 ฉบับ คุณสามารถดาวน์โหลดชุดข้อมูลนี้ได้หลังจากลงทะเบียนที่เว็บไซต์ของพวกเขา

ชุดข้อมูล BC5CDR มีลักษณะดังนี้:

```
6794356|t|Tricuspid valve regurgitation and lithium carbonate toxicity in a newborn infant.
6794356|a|A newborn with massive tricuspid regurgitation, atrial flutter, congestive heart failure, and a high serum lithium level is described. This is the first patient to initially manifest tricuspid regurgitation and atrial flutter, and the 11th described patient with cardiac disease among infants exposed to lithium compounds in the first trimester of pregnancy. Sixty-three percent of these infants had tricuspid valve involvement. Lithium carbonate may be a factor in the increasing incidence of congenital heart disease when taken during early pregnancy. It also causes neurologic depression, cyanosis, and cardiac arrhythmia when consumed prior to delivery.
6794356	0	29	Tricuspid valve regurgitation	Disease	D014262
6794356	34	51	lithium carbonate	Chemical	D016651
6794356	52	60	toxicity	Disease	D064420
...
```

ในชุดข้อมูลนี้ จะมีชื่อเรื่องและบทคัดย่อของเอกสารในสองบรรทัดแรก จากนั้นจะมีคำศัพท์แต่ละคำ พร้อมตำแหน่งเริ่มต้นและสิ้นสุดภายในบล็อกชื่อเรื่อง+บทคัดย่อ นอกจากนี้ยังมีประเภทของคำศัพท์และรหัส ontology ของคำศัพท์นั้นใน ontology ทางการแพทย์บางตัว

คุณจะต้องเขียนโค้ด Python เพื่อแปลงข้อมูลนี้ให้อยู่ในรูปแบบการเข้ารหัสแบบ BIO

## เครือข่ายประสาทเทียม

ความพยายามแรกในการทำ NER สามารถทำได้โดยใช้เครือข่าย LSTM ดังที่คุณได้เห็นในตัวอย่างระหว่างบทเรียน อย่างไรก็ตาม ในงาน NLP สถาปัตยกรรม [transformer](https://en.wikipedia.org/wiki/Transformer_(machine_learning_model)) โดยเฉพาะโมเดลภาษา [BERT](https://en.wikipedia.org/wiki/BERT_(language_model)) ให้ผลลัพธ์ที่ดีกว่ามาก โมเดล BERT ที่ผ่านการฝึกฝนล่วงหน้าสามารถเข้าใจโครงสร้างทั่วไปของภาษา และสามารถปรับแต่งเพิ่มเติมสำหรับงานเฉพาะได้ด้วยชุดข้อมูลและต้นทุนการคำนวณที่ค่อนข้างต่ำ

เนื่องจากเราวางแผนที่จะใช้ NER ในบริบททางการแพทย์ จึงสมเหตุสมผลที่จะใช้โมเดล BERT ที่ผ่านการฝึกฝนด้วยข้อความทางการแพทย์ Microsoft Research ได้เผยแพร่โมเดลที่ผ่านการฝึกฝนล่วงหน้าชื่อ [PubMedBERT][PubMedBERT] ([บทความ][PubMedBERT-Pub]) ซึ่งได้รับการปรับแต่งโดยใช้ข้อความจากคลังข้อมูล [PubMed](https://pubmed.ncbi.nlm.nih.gov/)

มาตรฐาน *de facto* สำหรับการฝึกโมเดล transformer คือไลบรารี [Hugging Face Transformers](https://huggingface.co/) ซึ่งยังมีคลังโมเดลที่ผ่านการฝึกฝนล่วงหน้าที่ดูแลโดยชุมชน รวมถึง PubMedBERT ด้วย การโหลดและใช้งานโมเดลนี้ต้องใช้โค้ดเพียงไม่กี่บรรทัด:

```python
model_name = "microsoft/BiomedNLP-PubMedBERT-base-uncased-abstract"
classes = ... # number of classes: 2*entities+1
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = BertForTokenClassification.from_pretrained(model_name, classes)
```

โค้ดนี้จะให้ `model` ซึ่งถูกสร้างขึ้นสำหรับงานการจัดประเภทโทเค็นโดยใช้จำนวน `classes` ที่กำหนด รวมถึงออบเจ็กต์ `tokenizer` ที่สามารถแยกข้อความอินพุตออกเป็นโทเค็น คุณจะต้องแปลงชุดข้อมูลให้อยู่ในรูปแบบ BIO โดยคำนึงถึงการแยกโทเค็นของ PubMedBERT คุณสามารถใช้ [โค้ด Python ส่วนนี้](https://gist.github.com/shwars/580b55684be3328eb39ecf01b9cbbd88) เป็นแรงบันดาลใจได้

## สิ่งที่ได้เรียนรู้

งานนี้ใกล้เคียงกับงานจริงที่คุณอาจต้องทำหากคุณต้องการทำความเข้าใจข้อมูลจำนวนมากในข้อความภาษาธรรมชาติ ในกรณีของเรา เราสามารถนำโมเดลที่ฝึกแล้วไปใช้กับ [ชุดข้อมูลเอกสารที่เกี่ยวข้องกับ COVID](https://www.kaggle.com/allen-institute-for-ai/CORD-19-research-challenge) และดูว่าเราจะสามารถดึงข้อมูลเชิงลึกอะไรออกมาได้บ้าง [บทความในบล็อกนี้](https://soshnikov.com/science/analyzing-medical-papers-with-azure-and-text-analytics-for-health/) และ [งานวิจัยนี้](https://www.mdpi.com/2504-2289/6/1/4) อธิบายถึงการวิจัยที่สามารถทำได้บนคลังเอกสารนี้โดยใช้ NER

---

**ข้อจำกัดความรับผิดชอบ**:  
เอกสารนี้ได้รับการแปลโดยใช้บริการแปลภาษา AI [Co-op Translator](https://github.com/Azure/co-op-translator) แม้ว่าเราจะพยายามให้การแปลมีความถูกต้องมากที่สุด แต่โปรดทราบว่าการแปลโดยระบบอัตโนมัติอาจมีข้อผิดพลาดหรือความไม่ถูกต้อง เอกสารต้นฉบับในภาษาดั้งเดิมควรถือเป็นแหล่งข้อมูลที่เชื่อถือได้ สำหรับข้อมูลที่สำคัญ ขอแนะนำให้ใช้บริการแปลภาษาจากผู้เชี่ยวชาญ เราไม่รับผิดชอบต่อความเข้าใจผิดหรือการตีความที่ผิดพลาดซึ่งเกิดจากการใช้การแปลนี้