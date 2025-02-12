# IA Ética e Responsável

Você quase terminou este curso, e espero que agora veja claramente que a IA é baseada em uma série de métodos matemáticos formais que nos permitem encontrar relações nos dados e treinar modelos para replicar alguns aspectos do comportamento humano. Neste momento da história, consideramos a IA uma ferramenta muito poderosa para extrair padrões dos dados e aplicar esses padrões para resolver novos problemas.

## [Quiz pré-aula](https://white-water-09ec41f0f.azurestaticapps.net/quiz/5/)

No entanto, na ficção científica, muitas vezes vemos histórias onde a IA apresenta um perigo para a humanidade. Geralmente, essas histórias giram em torno de algum tipo de rebelião da IA, quando a IA decide confrontar os seres humanos. Isso implica que a IA possui algum tipo de emoção ou pode tomar decisões imprevistas por seus desenvolvedores.

O tipo de IA que aprendemos neste curso não é nada mais do que aritmética de matrizes grandes. É uma ferramenta muito poderosa para nos ajudar a resolver nossos problemas, e como qualquer outra ferramenta poderosa - pode ser usada para fins bons e ruins. Importante, ela pode ser *mal utilizada*.

## Princípios da IA Responsável

Para evitar esse uso acidental ou intencional da IA, a Microsoft afirma os importantes [Princípios da IA Responsável](https://www.microsoft.com/ai/responsible-ai?WT.mc_id=academic-77998-cacaste). Os seguintes conceitos sustentam esses princípios:

* **Justiça** está relacionada ao importante problema de *viés de modelo*, que pode ser causado pelo uso de dados tendenciosos para treinamento. Por exemplo, quando tentamos prever a probabilidade de uma pessoa conseguir um emprego como desenvolvedor de software, o modelo provavelmente dará uma preferência maior aos homens - apenas porque o conjunto de dados de treinamento provavelmente estava tendencioso em relação a um público masculino. Precisamos equilibrar cuidadosamente os dados de treinamento e investigar o modelo para evitar viéses, e garantir que o modelo leve em conta características mais relevantes.
* **Confiabilidade e Segurança**. Por sua natureza, os modelos de IA podem cometer erros. Uma rede neural retorna probabilidades, e precisamos levar isso em conta ao tomar decisões. Todo modelo possui alguma precisão e revocação, e precisamos entender isso para prevenir danos que um conselho errado pode causar.
* **Privacidade e Segurança** têm algumas implicações específicas para a IA. Por exemplo, quando usamos alguns dados para treinar um modelo, esses dados se tornam de alguma forma "integrados" ao modelo. Por um lado, isso aumenta a segurança e a privacidade, por outro - precisamos lembrar quais dados o modelo foi treinado.
* **Inclusividade** significa que não estamos construindo IA para substituir pessoas, mas sim para aumentar as capacidades humanas e tornar nosso trabalho mais criativo. Isso também está relacionado à justiça, porque ao lidar com comunidades sub-representadas, a maioria dos conjuntos de dados que coletamos tende a ser tendenciosa, e precisamos garantir que essas comunidades sejam incluídas e tratadas corretamente pela IA.
* **Transparência**. Isso inclui garantir que estamos sempre claros sobre a IA sendo utilizada. Além disso, sempre que possível, queremos usar sistemas de IA que sejam *interpretáveis*.
* **Responsabilidade**. Quando modelos de IA tomam algumas decisões, nem sempre é claro quem é responsável por essas decisões. Precisamos garantir que entendemos onde reside a responsabilidade pelas decisões da IA. Na maioria dos casos, queremos incluir seres humanos no processo de tomada de decisões importantes, para que pessoas reais sejam responsabilizadas.

## Ferramentas para IA Responsável

A Microsoft desenvolveu a [Caixa de Ferramentas de IA Responsável](https://github.com/microsoft/responsible-ai-toolbox), que contém um conjunto de ferramentas:

* Painel de Interpretabilidade (InterpretML)
* Painel de Justiça (FairLearn)
* Painel de Análise de Erros
* Painel de IA Responsável que inclui

   - EconML - ferramenta para Análise Causal, que foca em perguntas do tipo "e se"
   - DiCE - ferramenta para Análise Contrafactual que permite ver quais características precisam ser alteradas para afetar a decisão do modelo

Para mais informações sobre Ética em IA, visite [esta lição](https://github.com/microsoft/ML-For-Beginners/tree/main/1-Introduction/3-fairness?WT.mc_id=academic-77998-cacaste) no Currículo de Aprendizado de Máquina, que inclui tarefas.

## Revisão e Autoestudo

Faça este [Caminho de Aprendizado](https://docs.microsoft.com/learn/modules/responsible-ai-principles/?WT.mc_id=academic-77998-cacaste) para aprender mais sobre IA responsável.

## [Quiz pós-aula](https://white-water-09ec41f0f.azurestaticapps.net/quiz/6/)

**Isenção de responsabilidade**:  
Este documento foi traduzido utilizando serviços de tradução automática baseados em IA. Embora nos esforcemos para garantir a precisão, esteja ciente de que traduções automatizadas podem conter erros ou imprecisões. O documento original em seu idioma nativo deve ser considerado a fonte autoritária. Para informações críticas, recomenda-se a tradução profissional realizada por humanos. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações errôneas decorrentes do uso desta tradução.