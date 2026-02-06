# IA Ética e Responsável

Está quase a terminar este curso, e espero que, até agora, tenha percebido claramente que a IA é baseada em vários métodos matemáticos formais que nos permitem encontrar relações nos dados e treinar modelos para replicar alguns aspetos do comportamento humano. Neste momento da história, consideramos a IA uma ferramenta muito poderosa para extrair padrões dos dados e aplicar esses padrões para resolver novos problemas.

## [Pre-lecture quiz](https://white-water-09ec41f0f.azurestaticapps.net/quiz/5/)

No entanto, na ficção científica, vemos frequentemente histórias onde a IA representa um perigo para a humanidade. Normalmente, essas histórias giram em torno de algum tipo de rebelião da IA, quando esta decide confrontar os seres humanos. Isso implica que a IA tem algum tipo de emoção ou pode tomar decisões imprevistas pelos seus desenvolvedores.

O tipo de IA que aprendemos neste curso não é mais do que operações matriciais em grande escala. É uma ferramenta muito poderosa para nos ajudar a resolver os nossos problemas e, como qualquer outra ferramenta poderosa, pode ser usada para fins bons ou maus. É importante destacar que pode ser *mal utilizada*.

## Princípios de IA Responsável

Para evitar esta utilização acidental ou intencional da IA, a Microsoft define os importantes [Princípios de IA Responsável](https://www.microsoft.com/ai/responsible-ai?WT.mc_id=academic-77998-cacaste). Os seguintes conceitos sustentam estes princípios:

* **Justiça** está relacionada com o importante problema de *viés nos modelos*, que pode ser causado pelo uso de dados enviesados para o treino. Por exemplo, quando tentamos prever a probabilidade de uma pessoa conseguir um emprego como programador, o modelo tende a dar maior preferência aos homens - apenas porque o conjunto de dados de treino provavelmente estava enviesado para um público masculino. Precisamos de equilibrar cuidadosamente os dados de treino e investigar o modelo para evitar vieses, garantindo que o modelo considera características mais relevantes.
* **Fiabilidade e Segurança**. Por natureza, os modelos de IA podem cometer erros. Uma rede neural retorna probabilidades, e precisamos de ter isso em conta ao tomar decisões. Cada modelo tem uma precisão e um recall, e precisamos de compreender isso para evitar danos que conselhos errados possam causar.
* **Privacidade e Segurança** têm algumas implicações específicas para a IA. Por exemplo, quando usamos alguns dados para treinar um modelo, esses dados tornam-se de certa forma "integrados" no modelo. Por um lado, isso aumenta a segurança e a privacidade, por outro - precisamos de lembrar quais os dados que foram usados para treinar o modelo.
* **Inclusão** significa que não estamos a construir IA para substituir pessoas, mas sim para as complementar e tornar o nosso trabalho mais criativo. Está também relacionado com a justiça, porque ao lidar com comunidades sub-representadas, a maioria dos conjuntos de dados que recolhemos tende a ser enviesada, e precisamos de garantir que essas comunidades são incluídas e tratadas corretamente pela IA.
* **Transparência**. Isto inclui garantir que somos sempre claros sobre o uso de IA. Além disso, sempre que possível, queremos usar sistemas de IA que sejam *interpretáveis*.
* **Responsabilidade**. Quando os modelos de IA tomam algumas decisões, nem sempre é claro quem é responsável por essas decisões. Precisamos de garantir que compreendemos onde reside a responsabilidade pelas decisões da IA. Na maioria dos casos, queremos incluir seres humanos no processo de tomada de decisões importantes, para que pessoas reais sejam responsabilizadas.

## Ferramentas para IA Responsável

A Microsoft desenvolveu o [Responsible AI Toolbox](https://github.com/microsoft/responsible-ai-toolbox), que contém um conjunto de ferramentas:

* Interpretability Dashboard (InterpretML)
* Fairness Dashboard (FairLearn)
* Error Analysis Dashboard
* Responsible AI Dashboard que inclui:

   - EconML - ferramenta para Análise Causal, que se foca em questões hipotéticas
   - DiCE - ferramenta para Análise Contrafactual que permite ver quais as características que precisam de ser alteradas para influenciar a decisão do modelo

Para mais informações sobre Ética na IA, visite [esta lição](https://github.com/microsoft/ML-For-Beginners/tree/main/1-Introduction/3-fairness?WT.mc_id=academic-77998-cacaste) no currículo de Machine Learning, que inclui tarefas.

## Revisão e Estudo Individual

Faça este [Learn Path](https://docs.microsoft.com/learn/modules/responsible-ai-principles/?WT.mc_id=academic-77998-cacaste) para aprender mais sobre IA responsável.

## [Post-lecture quiz](https://white-water-09ec41f0f.azurestaticapps.net/quiz/6/)

**Aviso Legal**:  
Este documento foi traduzido utilizando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos para garantir a precisão, esteja ciente de que traduções automáticas podem conter erros ou imprecisões. O documento original na sua língua nativa deve ser considerado a fonte autoritária. Para informações críticas, recomenda-se a tradução profissional realizada por humanos. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas decorrentes do uso desta tradução.