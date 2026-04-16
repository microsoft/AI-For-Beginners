# NER

[AI for Beginners Curriculum](https://github.com/microsoft/ai-for-beginners) నుండి ల్యాబ్ అసైన్‌మెంట్.

## పని

ఈ ల్యాబ్‌లో, మీరు వైద్య పదజాలం కోసం నేమ్డ్ ఎంటిటీ రికగ్నిషన్ మోడల్‌ను శిక్షణ ఇవ్వాలి.

## డేటాసెట్

NER మోడల్‌ను శిక్షణ ఇవ్వడానికి, వైద్య ఎంటిటీలతో సరైన లేబుల్ చేయబడిన డేటాసెట్ అవసరం. [BC5CDR dataset](https://biocreative.bioinformatics.udel.edu/tasks/biocreative-v/track-3-cdr/) 1500 కంటే ఎక్కువ పత్రాల నుండి లేబుల్ చేయబడిన రోగాలు మరియు రసాయన ఎంటిటీలను కలిగి ఉంది. మీరు వారి వెబ్‌సైట్‌లో రిజిస్టర్ అయిన తర్వాత డేటాసెట్‌ను డౌన్లోడ్ చేసుకోవచ్చు.

BC5CDR డేటాసెట్ ఇలా ఉంటుంది:

```
6794356|t|Tricuspid valve regurgitation and lithium carbonate toxicity in a newborn infant.
6794356|a|A newborn with massive tricuspid regurgitation, atrial flutter, congestive heart failure, and a high serum lithium level is described. This is the first patient to initially manifest tricuspid regurgitation and atrial flutter, and the 11th described patient with cardiac disease among infants exposed to lithium compounds in the first trimester of pregnancy. Sixty-three percent of these infants had tricuspid valve involvement. Lithium carbonate may be a factor in the increasing incidence of congenital heart disease when taken during early pregnancy. It also causes neurologic depression, cyanosis, and cardiac arrhythmia when consumed prior to delivery.
6794356	0	29	Tricuspid valve regurgitation	Disease	D014262
6794356	34	51	lithium carbonate	Chemical	D016651
6794356	52	60	toxicity	Disease	D064420
...
```

ఈ డేటాసెట్‌లో, మొదటి రెండు లైన్లలో పత్రం శీర్షిక మరియు సారాంశం ఉంటాయి, ఆ తర్వాత వ్యక్తిగత ఎంటిటీలను, శీర్షిక+సారాంశం బ్లాక్‌లో ప్రారంభం మరియు ముగింపు స్థానాలతో చూపిస్తారు. ఎంటిటీ రకం తో పాటు, మీరు ఈ ఎంటిటీకి సంబంధించిన వైద్య ఆంటాలజీ ID కూడా పొందుతారు.

దీనిని BIO ఎంకోడింగ్‌గా మార్చడానికి మీరు కొంత Python కోడ్ రాయాలి.

## నెట్‌వర్క్

NER కోసం మొదటి ప్రయత్నం LSTM నెట్‌వర్క్ ఉపయోగించి చేయవచ్చు, మన ఉదాహరణలో మీరు పాఠంలో చూసినట్లుగా. అయితే, NLP పనులలో, [ట్రాన్స్‌ఫార్మర్ ఆర్కిటెక్చర్](https://en.wikipedia.org/wiki/Transformer_(machine_learning_model)) మరియు ప్రత్యేకంగా [BERT భాషా మోడల్స్](https://en.wikipedia.org/wiki/BERT_(language_model)) చాలా మెరుగైన ఫలితాలు చూపిస్తాయి. ప్రీ-ట్రెయిన్డ్ BERT మోడల్స్ భాష యొక్క సాధారణ నిర్మాణాన్ని అర్థం చేసుకుంటాయి, మరియు తక్కువ డేటాసెట్ మరియు కంప్యూటేషనల్ ఖర్చులతో ప్రత్యేక పనుల కోసం ఫైన్-ట్యూన్ చేయవచ్చు.

మనం NER ను వైద్య సందర్భంలో ఉపయోగించబోతున్నందున, వైద్య పాఠ్యాలపై శిక్షణ పొందిన BERT మోడల్ ఉపయోగించడం మంచిది. Microsoft Research [PubMedBERT][PubMedBERT] అనే ప్రీ-ట్రెయిన్డ్ మోడల్ విడుదల చేసింది ([ప్రచురణ][PubMedBERT-Pub]), ఇది [PubMed](https://pubmed.ncbi.nlm.nih.gov/) రిపాజిటరీ నుండి పాఠ్యాలతో ఫైన్-ట్యూన్ చేయబడింది.

ట్రాన్స్‌ఫార్మర్ మోడల్స్ శిక్షణకు *de facto* స్టాండర్డ్ [Hugging Face Transformers](https://huggingface.co/) లైబ్రరీ. ఇది కమ్యూనిటీ నిర్వహించే ప్రీ-ట్రెయిన్డ్ మోడల్స్ రిపాజిటరీని కూడా కలిగి ఉంది, అందులో PubMedBERT కూడా ఉంది. ఈ మోడల్‌ను లోడ్ చేసి ఉపయోగించడానికి, మనకు కొన్ని కోడ్ లైన్లు మాత్రమే అవసరం:

```python
model_name = "microsoft/BiomedNLP-PubMedBERT-base-uncased-abstract"
classes = ... # తరగతుల సంఖ్య: 2*సంస్థలు+1
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = BertForTokenClassification.from_pretrained(model_name, classes)
```

ఇది `classes` సంఖ్య ఆధారంగా టోకెన్ క్లాసిఫికేషన్ టాస్క్ కోసం నిర్మించిన `model` ను మరియు ఇన్‌పుట్ టెక్స్ట్‌ను టోకెన్లుగా విడగొట్టగల `tokenizer` ఆబ్జెక్ట్‌ను ఇస్తుంది. మీరు డేటాసెట్‌ను BIO ఫార్మాట్‌లోకి మార్చాలి, PubMedBERT టోకెనైజేషన్‌ను పరిగణలోకి తీసుకుని. మీరు [ఈ Python కోడ్](https://gist.github.com/shwars/580b55684be3328eb39ecf01b9cbbd88) ను ప్రేరణగా ఉపయోగించవచ్చు.

## ముఖ్యాంశం

ఈ పని మీరు పెద్ద పరిమాణంలో సహజ భాషా పాఠ్యాలపై మరింత అవగాహన పొందాలనుకుంటే ఎదుర్కొనే అసలు పనికి చాలా దగ్గరగా ఉంటుంది. మన సందర్భంలో, శిక్షణ పొందిన మోడల్‌ను [COVID-సంబంధిత పత్రాల డేటాసెట్](https://www.kaggle.com/allen-institute-for-ai/CORD-19-research-challenge) పై వర్తింపజేసి, మనం ఏ అవగాహనలను పొందగలమో చూడవచ్చు. [ఈ బ్లాగ్ పోస్ట్](https://soshnikov.com/science/analyzing-medical-papers-with-azure-and-text-analytics-for-health/) మరియు [ఈ పత్రం](https://www.mdpi.com/2504-2289/6/1/4) NER ఉపయోగించి ఈ పత్రాల కార్పస్‌పై చేయగల పరిశోధనలను వివరించాయి.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**అస్పష్టత**:  
ఈ డాక్యుమెంట్‌ను AI అనువాద సేవ [Co-op Translator](https://github.com/Azure/co-op-translator) ఉపయోగించి అనువదించబడింది. మేము ఖచ్చితత్వానికి ప్రయత్నించినప్పటికీ, ఆటోమేటెడ్ అనువాదాల్లో పొరపాట్లు లేదా తప్పిదాలు ఉండవచ్చు. అసలు డాక్యుమెంట్ దాని స్వదేశీ భాషలోనే అధికారిక మూలంగా పరిగణించాలి. ముఖ్యమైన సమాచారానికి, ప్రొఫెషనల్ మానవ అనువాదం చేయించుకోవడం మంచిది. ఈ అనువాదం వలన కలిగే ఏవైనా అపార్థాలు లేదా తప్పుదారుల బాధ్యత మేము తీసుకోము.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->