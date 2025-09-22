<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "1ddf651d7681b4449f9d09ea3b17911e",
  "translation_date": "2025-08-24T09:02:01+00:00",
  "source_file": "lessons/6-Other/23-MultiagentSystems/README.md",
  "language_code": "pt"
}
-->
# Sistemas Multi-Agente

Uma das formas possíveis de alcançar inteligência é a chamada abordagem **emergente** (ou **sinergética**), que se baseia no facto de que o comportamento combinado de muitos agentes relativamente simples pode resultar num comportamento geral mais complexo (ou inteligente) do sistema como um todo. Teoricamente, isto baseia-se nos princípios de [Inteligência Coletiva](https://en.wikipedia.org/wiki/Collective_intelligence), [Emergentismo](https://en.wikipedia.org/wiki/Global_brain) e [Cibernética Evolutiva](https://en.wikipedia.org/wiki/Global_brain), que afirmam que sistemas de nível superior ganham algum tipo de valor acrescentado quando são devidamente combinados a partir de sistemas de nível inferior (o chamado *princípio da transição de metassistema*).

## [Questionário pré-aula](https://ff-quizzes.netlify.app/en/ai/quiz/45)

A direção dos **Sistemas Multi-Agente** surgiu na IA nos anos 1990 como uma resposta ao crescimento da Internet e dos sistemas distribuídos. Um dos manuais clássicos de IA, [Artificial Intelligence: A Modern Approach](https://en.wikipedia.org/wiki/Artificial_Intelligence:_A_Modern_Approach), foca-se na visão da IA clássica do ponto de vista dos sistemas multi-agente.

Central à abordagem multi-agente está a noção de **Agente** - uma entidade que vive num determinado **ambiente**, que pode perceber e sobre o qual pode agir. Esta é uma definição muito ampla, e podem existir muitos tipos e classificações diferentes de agentes:

* Pela sua capacidade de raciocinar:
   - Agentes **Reativos** geralmente têm um comportamento simples de pedido-resposta
   - Agentes **Deliberativos** utilizam algum tipo de raciocínio lógico e/ou capacidades de planeamento
* Pelo local onde o agente executa o seu código:
   - Agentes **Estáticos** trabalham num nó de rede dedicado
   - Agentes **Móveis** podem mover o seu código entre nós de rede
* Pelo seu comportamento:
   - Agentes **Passivos** não têm objetivos específicos. Estes agentes podem reagir a estímulos externos, mas não iniciam ações por si mesmos.
   - Agentes **Ativos** têm objetivos que procuram alcançar
   - Agentes **Cognitivos** envolvem planeamento e raciocínio complexos

Atualmente, os sistemas multi-agente são utilizados em várias aplicações:

* Em jogos, muitas personagens não jogáveis utilizam algum tipo de IA e podem ser consideradas agentes inteligentes
* Na produção de vídeo, a renderização de cenas 3D complexas que envolvem multidões é geralmente feita usando simulação multi-agente
* Na modelação de sistemas, a abordagem multi-agente é usada para simular o comportamento de um modelo complexo. Por exemplo, a abordagem multi-agente foi usada com sucesso para prever a propagação da doença COVID-19 em todo o mundo. Uma abordagem semelhante pode ser usada para modelar o tráfego numa cidade e ver como reage a mudanças nas regras de trânsito.
* Em sistemas de automação complexos, cada dispositivo pode atuar como um agente independente, tornando o sistema como um todo menos monolítico e mais robusto.

Não vamos gastar muito tempo a aprofundar os sistemas multi-agente, mas vamos considerar um exemplo de **Modelação Multi-Agente**.

## NetLogo

[NetLogo](https://ccl.northwestern.edu/netlogo/) é um ambiente de modelação multi-agente baseado numa versão modificada da linguagem de programação [Logo](https://en.wikipedia.org/wiki/Logo_(programming_language)). Esta linguagem foi desenvolvida para ensinar conceitos de programação a crianças e permite controlar um agente chamado **tartaruga**, que pode mover-se, deixando um rastro atrás de si. Isto permite criar figuras geométricas complexas, sendo uma forma muito visual de compreender o comportamento de um agente.

No NetLogo, podemos criar muitas tartarugas usando o comando `create-turtles`. Podemos então comandar todas as tartarugas a realizar algumas ações (no exemplo abaixo - avançar 10 pontos):

```
create-turtles 10
ask turtles [
  forward 10
]
```

Claro que não é interessante quando todas as tartarugas fazem a mesma coisa, por isso podemos `ask` grupos de tartarugas, por exemplo, aquelas que estão nas proximidades de um determinado ponto. Também podemos criar tartarugas de diferentes *raças* usando o comando `breed [cats cat]`. Aqui, `cat` é o nome de uma raça, e precisamos especificar tanto a palavra no singular como no plural, porque diferentes comandos utilizam formas diferentes para maior clareza.

> ✅ Não vamos aprender a linguagem NetLogo em si - pode visitar o excelente recurso [Beginner's Interactive NetLogo Dictionary](https://ccl.northwestern.edu/netlogo/bind/) se estiver interessado em aprender mais.

Pode [descarregar](https://ccl.northwestern.edu/netlogo/download.shtml) e instalar o NetLogo para experimentá-lo.

### Biblioteca de Modelos

Uma grande vantagem do NetLogo é que contém uma biblioteca de modelos funcionais que pode experimentar. Vá a **File → Models Library**, e terá muitas categorias de modelos para escolher.

<img alt="NetLogo Models Library" src="images/NetLogo-ModelLib.png" width="60%"/>

> Uma captura de ecrã da biblioteca de modelos por Dmitry Soshnikov

Pode abrir um dos modelos, por exemplo **Biology → Flocking**.

### Princípios Principais

Depois de abrir o modelo, será levado para o ecrã principal do NetLogo. Aqui está um modelo de exemplo que descreve a população de lobos e ovelhas, dado recursos finitos (relva).

![NetLogo Main Screen](../../../../../lessons/6-Other/23-MultiagentSystems/images/NetLogo-Main.png)

> Captura de ecrã por Dmitry Soshnikov

Neste ecrã, pode ver:

* A secção **Interface**, que contém:
  - O campo principal, onde todos os agentes vivem
  - Diferentes controlos: botões, sliders, etc.
  - Gráficos que pode usar para exibir parâmetros da simulação
* O separador **Code**, que contém o editor onde pode escrever o programa NetLogo

Na maioria dos casos, a interface terá um botão **Setup**, que inicializa o estado da simulação, e um botão **Go**, que inicia a execução. Estes são tratados por manipuladores correspondentes no código que se parecem com isto:

```
to go [
...
]
```

O mundo do NetLogo consiste nos seguintes objetos:

* **Agentes** (tartarugas) que podem mover-se pelo campo e fazer algo. Comanda os agentes usando a sintaxe `ask turtles [...]`, e o código entre parênteses é executado por todos os agentes no *modo tartaruga*.
* **Patches** são áreas quadradas do campo onde os agentes vivem. Pode referir-se a todos os agentes no mesmo patch ou pode alterar as cores dos patches e algumas outras propriedades. Também pode `ask patches` para fazer algo.
* **Observador** é um agente único que controla o mundo. Todos os manipuladores de botões são executados no *modo observador*.

> ✅ A beleza de um ambiente multi-agente é que o código que corre no modo tartaruga ou no modo patch é executado ao mesmo tempo por todos os agentes em paralelo. Assim, ao escrever pouco código e programar o comportamento de um agente individual, pode criar um comportamento complexo do sistema de simulação como um todo.

### Flocking

Como exemplo de comportamento multi-agente, vamos considerar o **[Flocking](https://en.wikipedia.org/wiki/Flocking_(behavior))**. Flocking é um padrão complexo muito semelhante à forma como bandos de pássaros voam. Ao observá-los, pode pensar que seguem algum tipo de algoritmo coletivo ou que possuem alguma forma de *inteligência coletiva*. No entanto, este comportamento complexo surge quando cada agente individual (neste caso, um *pássaro*) apenas observa alguns outros agentes a uma curta distância e segue três regras simples:

* **Alinhamento** - direciona-se para a direção média dos agentes vizinhos
* **Coesão** - tenta direcionar-se para a posição média dos vizinhos (*atração de longo alcance*)
* **Separação** - ao aproximar-se demasiado de outros pássaros, tenta afastar-se (*repulsão de curto alcance*)

Pode executar o exemplo de flocking e observar o comportamento. Também pode ajustar parâmetros, como o *grau de separação* ou o *alcance de visão*, que define até onde cada pássaro pode ver. Note que, se reduzir o alcance de visão para 0, todos os pássaros ficam cegos e o flocking para. Se reduzir a separação para 0, todos os pássaros agrupam-se numa linha reta.

> ✅ Mude para o separador **Code** e veja onde as três regras de flocking (alinhamento, coesão e separação) estão implementadas no código. Note como nos referimos apenas aos agentes que estão à vista.

### Outros Modelos para Ver

Existem mais alguns modelos interessantes que pode experimentar:

* **Art → Fireworks** mostra como um fogo de artifício pode ser considerado um comportamento coletivo de fluxos de fogo individuais
* **Social Science → Traffic Basic** e **Social Science → Traffic Grid** mostram o modelo de tráfego urbano em 1D e numa grelha 2D com ou sem semáforos. Cada carro na simulação segue as seguintes regras:
   - Se o espaço à sua frente estiver vazio - acelera (até uma certa velocidade máxima)
   - Se vir um obstáculo à frente - trava (e pode ajustar até onde o condutor consegue ver)
* **Social Science → Party** mostra como as pessoas se agrupam durante uma festa de cocktail. Pode encontrar a combinação de parâmetros que leva ao aumento mais rápido da felicidade do grupo.

Como pode ver nestes exemplos, as simulações multi-agente podem ser uma forma bastante útil de compreender o comportamento de um sistema complexo composto por indivíduos que seguem a mesma ou lógica semelhante. Também pode ser usado para controlar agentes virtuais, como [NPCs](https://en.wikipedia.org/wiki/NPC) em jogos de computador ou agentes em mundos animados 3D.

## Agentes Deliberativos

Os agentes descritos acima são muito simples, reagindo a mudanças no ambiente usando algum tipo de algoritmo. Como tal, são **agentes reativos**. No entanto, às vezes os agentes podem raciocinar e planear as suas ações, caso em que são chamados de **deliberativos**.

Um exemplo típico seria um agente pessoal que recebe uma instrução de um humano para reservar uma viagem de férias. Suponha que existem muitos agentes na internet que podem ajudá-lo. Ele deve então contactar outros agentes para ver quais voos estão disponíveis, quais são os preços dos hotéis para diferentes datas e tentar negociar o melhor preço. Quando o plano de férias estiver completo e confirmado pelo proprietário, pode proceder à reserva.

Para isso, os agentes precisam de **comunicar**. Para uma comunicação bem-sucedida, eles precisam de:

* Algumas **linguagens padrão para trocar conhecimento**, como [Knowledge Interchange Format](https://en.wikipedia.org/wiki/Knowledge_Interchange_Format) (KIF) e [Knowledge Query and Manipulation Language](https://en.wikipedia.org/wiki/Knowledge_Query_and_Manipulation_Language) (KQML). Essas linguagens são projetadas com base na [Teoria dos Atos de Fala](https://en.wikipedia.org/wiki/Speech_act).
* Essas linguagens também devem incluir alguns **protocolos para negociações**, baseados em diferentes **tipos de leilão**.
* Uma **ontologia comum** a ser usada, para que se refiram aos mesmos conceitos conhecendo os seus significados
* Uma forma de **descobrir** o que diferentes agentes podem fazer, também baseada em algum tipo de ontologia

Os agentes deliberativos são muito mais complexos do que os reativos, porque não apenas reagem a mudanças no ambiente, mas também devem ser capazes de *iniciar* ações. Uma das arquiteturas propostas para agentes deliberativos é o chamado agente de Crença-Desejo-Intenção (BDI):

* **Crenças** formam um conjunto de conhecimentos sobre o ambiente do agente. Pode ser estruturado como uma base de conhecimento ou conjunto de regras que um agente pode aplicar a uma situação específica no ambiente.
* **Desejos** definem o que um agente quer fazer, ou seja, os seus objetivos. Por exemplo, o objetivo do agente assistente pessoal acima é reservar uma viagem, e o objetivo de um agente de hotel é maximizar o lucro.
* **Intenções** são ações específicas que um agente planeia para alcançar os seus objetivos. As ações geralmente mudam o ambiente e causam comunicação com outros agentes.

Existem algumas plataformas disponíveis para construir sistemas multi-agente, como [JADE](https://jade.tilab.com/). [Este artigo](https://arxiv.org/ftp/arxiv/papers/2007/2007.08961.pdf) contém uma revisão de plataformas multi-agente, juntamente com uma breve história dos sistemas multi-agente e os seus diferentes cenários de uso.

## Conclusão

Os sistemas Multi-Agente podem assumir formas muito diferentes e ser usados em muitas aplicações diferentes. 
Todos tendem a focar-se no comportamento mais simples de um agente individual e alcançar um comportamento mais complexo do sistema geral devido ao **efeito sinergético**.

## 🚀 Desafio

Leve esta lição para o mundo real e tente conceptualizar um sistema multi-agente que possa resolver um problema. O que, por exemplo, um sistema multi-agente precisaria fazer para otimizar a rota de um autocarro escolar? Como poderia funcionar numa padaria?

## [Questionário pós-aula](https://ff-quizzes.netlify.app/en/ai/quiz/46)

## Revisão e Autoestudo

Revise o uso deste tipo de sistema na indústria. Escolha um domínio, como a manufatura ou a indústria de videojogos, e descubra como os sistemas multi-agente podem ser usados para resolver problemas únicos.

## [Tarefa NetLogo](assignment.md)

**Aviso Legal**:  
Este documento foi traduzido utilizando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos para garantir a precisão, esteja ciente de que traduções automáticas podem conter erros ou imprecisões. O documento original no seu idioma nativo deve ser considerado a fonte autoritária. Para informações críticas, recomenda-se uma tradução profissional realizada por humanos. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas resultantes do uso desta tradução.