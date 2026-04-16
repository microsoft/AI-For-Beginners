# IA Ética e Responsável

Você está quase terminando este curso, e espero que até agora esteja claro que a IA é baseada em uma série de métodos matemáticos formais que nos permitem encontrar relações nos dados e treinar modelos para replicar alguns aspectos do comportamento humano. Neste momento da história, consideramos a IA uma ferramenta muito poderosa para extrair padrões dos dados e aplicar esses padrões para resolver novos problemas.

## [Quiz pré-aula](https://white-water-09ec41f0f.azurestaticapps.net/quiz/5/)

No entanto, na ficção científica, frequentemente vemos histórias onde a IA apresenta um perigo para a humanidade. Geralmente, essas histórias giram em torno de algum tipo de rebelião da IA, quando ela decide confrontar os seres humanos. Isso implica que a IA possui algum tipo de emoção ou pode tomar decisões inesperadas por seus desenvolvedores.

O tipo de IA que aprendemos neste curso nada mais é do que uma grande aritmética de matrizes. É uma ferramenta muito poderosa para nos ajudar a resolver nossos problemas e, como qualquer outra ferramenta poderosa, pode ser usada para fins bons ou ruins. É importante destacar que ela pode ser *mal utilizada*.

## Princípios de IA Responsável

Para evitar o uso acidental ou intencional inadequado da IA, a Microsoft estabelece os importantes [Princípios de IA Responsável](https://www.microsoft.com/ai/responsible-ai?WT.mc_id=academic-77998-cacaste). Os seguintes conceitos fundamentam esses princípios:

* **Justiça** está relacionada ao importante problema de *viés nos modelos*, que pode ser causado pelo uso de dados tendenciosos no treinamento. Por exemplo, quando tentamos prever a probabilidade de uma pessoa conseguir um emprego como desenvolvedor de software, o modelo provavelmente dará preferência maior aos homens - simplesmente porque o conjunto de dados de treinamento provavelmente foi tendencioso em relação ao público masculino. Precisamos equilibrar cuidadosamente os dados de treinamento e investigar o modelo para evitar vieses, garantindo que ele leve em conta características mais relevantes.
* **Confiabilidade e Segurança**. Por sua natureza, os modelos de IA podem cometer erros. Uma rede neural retorna probabilidades, e precisamos levar isso em consideração ao tomar decisões. Todo modelo possui alguma precisão e recall, e precisamos entender isso para evitar danos que conselhos errados podem causar.
* **Privacidade e Segurança** têm algumas implicações específicas para IA. Por exemplo, quando usamos alguns dados para treinar um modelo, esses dados se tornam de certa forma "integrados" ao modelo. Por um lado, isso aumenta a segurança e a privacidade, por outro - precisamos lembrar quais dados foram usados no treinamento do modelo.
* **Inclusão** significa que não estamos construindo IA para substituir pessoas, mas sim para aumentar a capacidade humana e tornar nosso trabalho mais criativo. Isso também está relacionado à justiça, porque ao lidar com comunidades sub-representadas, a maioria dos conjuntos de dados que coletamos provavelmente será tendenciosa, e precisamos garantir que essas comunidades sejam incluídas e tratadas corretamente pela IA.
* **Transparência**. Isso inclui garantir que sejamos sempre claros sobre o uso de IA. Além disso, sempre que possível, queremos usar sistemas de IA que sejam *interpretáveis*.
* **Responsabilidade**. Quando os modelos de IA tomam decisões, nem sempre é claro quem é responsável por essas decisões. Precisamos garantir que entendemos onde está a responsabilidade pelas decisões da IA. Na maioria dos casos, queremos incluir seres humanos no processo de tomada de decisões importantes, para que pessoas reais sejam responsabilizadas.

## Ferramentas para IA Responsável

A Microsoft desenvolveu o [Responsible AI Toolbox](https://github.com/microsoft/responsible-ai-toolbox), que contém um conjunto de ferramentas:

* Interpretability Dashboard (InterpretML)
* Fairness Dashboard (FairLearn)
* Error Analysis Dashboard
* Responsible AI Dashboard, que inclui:

   - EconML - ferramenta para Análise Causal, que foca em questões de "e se"
   - DiCE - ferramenta para Análise Contrafactual que permite ver quais características precisam ser alteradas para influenciar a decisão do modelo

Para mais informações sobre Ética em IA, visite [esta lição](https://github.com/microsoft/ML-For-Beginners/tree/main/1-Introduction/3-fairness?WT.mc_id=academic-77998-cacaste) no currículo de Machine Learning, que inclui tarefas.

## Revisão e Autoestudo

Faça este [Caminho de Aprendizado](https://docs.microsoft.com/learn/modules/responsible-ai-principles/?WT.mc_id=academic-77998-cacaste) para aprender mais sobre IA responsável.

## [Quiz pós-aula](https://white-water-09ec41f0f.azurestaticapps.net/quiz/6/)

**Aviso Legal**:  
Este documento foi traduzido utilizando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos para garantir a precisão, esteja ciente de que traduções automáticas podem conter erros ou imprecisões. O documento original em seu idioma nativo deve ser considerado a fonte oficial. Para informações críticas, recomenda-se a tradução profissional feita por humanos. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações equivocadas decorrentes do uso desta tradução.