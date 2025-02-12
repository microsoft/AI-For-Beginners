# Sistemas Multi-Agente

Uma das possíveis maneiras de alcançar inteligência é a chamada abordagem **emergente** (ou **sinergética**), que se baseia no fato de que o comportamento combinado de muitos agentes relativamente simples pode resultar em um comportamento mais complexo (ou inteligente) do sistema como um todo. Teoricamente, isso se baseia nos princípios da [Inteligência Coletiva](https://en.wikipedia.org/wiki/Collective_intelligence), [Emergentismo](https://en.wikipedia.org/wiki/Global_brain) e [Cibernética Evolutiva](https://en.wikipedia.org/wiki/Global_brain), que afirmam que sistemas de nível superior ganham algum tipo de valor agregado quando são devidamente combinados a partir de sistemas de nível inferior (o chamado *princípio da transição de metasistema*).

## [Quiz pré-aula](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/123)

A direção dos **Sistemas Multi-Agente** surgiu na IA na década de 1990 como uma resposta ao crescimento da Internet e de sistemas distribuídos. Um dos clássicos livros didáticos de IA, [Inteligência Artificial: Uma Abordagem Moderna](https://en.wikipedia.org/wiki/Artificial_Intelligence:_A_Modern_Approach), foca na visão da IA clássica sob a perspectiva dos sistemas multi-agente.

Central para a abordagem multi-agente é a noção de **Agente** - uma entidade que vive em algum **ambiente**, que pode perceber e agir sobre. Esta é uma definição muito ampla, e pode haver muitos tipos e classificações de agentes:

* Pela sua capacidade de raciocínio:
   - Agentes **Reativos** geralmente têm um comportamento simples do tipo solicitação-resposta
   - Agentes **Deliberativos** empregam algum tipo de raciocínio lógico e/ou capacidades de planejamento
* Pelo local onde o agente executa seu código:
   - Agentes **Estáticos** trabalham em um nó de rede dedicado
   - Agentes **Móveis** podem mover seu código entre nós de rede
* Pelo seu comportamento:
   - Agentes **Passivos** não têm objetivos específicos. Esses agentes podem reagir a estímulos externos, mas não iniciarão ações por conta própria.
   - Agentes **Ativos** têm alguns objetivos que perseguem
   - Agentes **Cognitivos** envolvem planejamento e raciocínio complexos

Os sistemas multi-agente são hoje utilizados em uma série de aplicações:

* Em jogos, muitos personagens não jogáveis empregam algum tipo de IA e podem ser considerados agentes inteligentes
* Na produção de vídeo, a renderização de cenas 3D complexas que envolvem multidões é tipicamente feita usando simulação multi-agente
* Na modelagem de sistemas, a abordagem multi-agente é utilizada para simular o comportamento de um modelo complexo. Por exemplo, a abordagem multi-agente foi usada com sucesso para prever a disseminação da doença COVID-19 em todo o mundo. Uma abordagem semelhante pode ser usada para modelar o tráfego na cidade e ver como ele reage a mudanças nas regras de trânsito.
* Em sistemas de automação complexos, cada dispositivo pode agir como um agente independente, o que torna todo o sistema menos monolítico e mais robusto.

Não vamos gastar muito tempo aprofundando em sistemas multi-agente, mas consideraremos um exemplo de **Modelagem Multi-Agente**.

## NetLogo

[NetLogo](https://ccl.northwestern.edu/netlogo/) é um ambiente de modelagem multi-agente baseado em uma versão modificada da linguagem de programação [Logo](https://en.wikipedia.org/wiki/Logo_(programming_language)). Esta linguagem foi desenvolvida para ensinar conceitos de programação para crianças, e permite que você controle um agente chamado **tartaruga**, que pode se mover, deixando um rastro para trás. Isso permite a criação de figuras geométricas complexas, que é uma maneira muito visual de entender o comportamento de um agente.

No NetLogo, podemos criar muitas tartarugas usando o comando `create-turtles`. Podemos então comandar todas as tartarugas a realizar algumas ações (no exemplo abaixo - mais 10 pontos para frente):

```
create-turtles 10
ask turtles [
  forward 10
]
```

Claro, não é interessante quando todas as tartarugas fazem a mesma coisa, então podemos `ask ` groups of turtles, eg. those who are in the vicinity of a certain point. We can also create turtles of different *breeds* using `breed [cats cat]` command. Here `cat` é o nome de uma raça, e precisamos especificar tanto a forma singular quanto a plural, porque diferentes comandos usam diferentes formas para clareza.

> ✅ Não vamos nos aprofundar no aprendizado da linguagem NetLogo em si - você pode visitar o brilhante [Dicionário Interativo para Iniciantes do NetLogo](https://ccl.northwestern.edu/netlogo/bind/) se estiver interessado em aprender mais.

Você pode [baixar](https://ccl.northwestern.edu/netlogo/download.shtml) e instalar o NetLogo para experimentar.

### Biblioteca de Modelos

Uma grande coisa sobre o NetLogo é que ele contém uma biblioteca de modelos funcionais que você pode experimentar. Vá para **Arquivo → Biblioteca de Modelos**, e você terá muitas categorias de modelos para escolher.

<img alt="Biblioteca de Modelos do NetLogo" src="images/NetLogo-ModelLib.png" width="60%"/>

> Uma captura de tela da biblioteca de modelos por Dmitry Soshnikov

Você pode abrir um dos modelos, por exemplo **Biologia → Flocking**.

### Princípios Principais

Após abrir o modelo, você é levado à tela principal do NetLogo. Aqui está um modelo de exemplo que descreve a população de lobos e ovelhas, dado recursos finitos (grama).

![Tela Principal do NetLogo](../../../../../translated_images/NetLogo-Main.32653711ec1a01b3cab22ec0b148e64193d0b979b055285bef329d5e3d6958c5.pt.png)

> Captura de tela por Dmitry Soshnikov

Nesta tela, você pode ver:

* A seção **Interface** que contém:
  - O campo principal, onde todos os agentes vivem
  - Diferentes controles: botões, deslizadores, etc.
  - Gráficos que você pode usar para exibir parâmetros da simulação
* A aba **Código** que contém o editor, onde você pode digitar o programa NetLogo

Na maioria dos casos, a interface teria um botão **Configurar**, que inicializa o estado da simulação, e um botão **Executar** que inicia a execução. Esses são gerenciados pelos manipuladores correspondentes no código que se parecem com isso:

```
to go [
...
]
```

O mundo do NetLogo consiste nos seguintes objetos:

* **Agentes** (tartarugas) que podem se mover pelo campo e fazer algo. Você comanda os agentes usando `ask turtles [...]` syntax, and the code in brackets is executed by all agents in *turtle mode*.
* **Patches** are square areas of the field, on which agents live. You can refer to all agents on the same patch, or you can change patch colors and some other properties. You can also `ask patches` para fazer algo.
* **Observador** é um agente único que controla o mundo. Todos os manipuladores de botões são executados no *modo observador*.

> ✅ A beleza de um ambiente multi-agente é que o código que é executado no modo tartaruga ou no modo patch é executado ao mesmo tempo por todos os agentes em paralelo. Assim, ao escrever um pouco de código e programar o comportamento de um agente individual, você pode criar um comportamento complexo do sistema de simulação como um todo.

### Flocking

Como um exemplo de comportamento multi-agente, vamos considerar **[Flocking](https://en.wikipedia.org/wiki/Flocking_(behavior))**. O Flocking é um padrão complexo que é muito semelhante a como bandos de pássaros voam. Ao observá-los voar, você pode pensar que eles seguem algum tipo de algoritmo coletivo ou que possuem alguma forma de *inteligência coletiva*. No entanto, esse comportamento complexo surge quando cada agente individual (neste caso, um *pássaro*) apenas observa alguns outros agentes a uma curta distância dele e segue três regras simples:

* **Alinhamento** - ele se dirige para a média da direção dos agentes vizinhos
* **Coesão** - ele tenta se dirigir para a posição média dos vizinhos (*atração de longo alcance*)
* **Separação** - ao se aproximar demais de outros pássaros, ele tenta se afastar (*repulsão de curto alcance*)

Você pode executar o exemplo de flocking e observar o comportamento. Você também pode ajustar parâmetros, como *grau de separação* ou *alcance de visão*, que define quão longe cada pássaro pode ver. Observe que, se você diminuir o alcance de visão para 0, todos os pássaros ficam cegos, e o flocking para. Se você diminuir a separação para 0, todos os pássaros se reúnem em uma linha reta.

> ✅ Mude para a aba **Código** e veja onde as três regras de flocking (alinhamento, coesão e separação) estão implementadas no código. Observe como nos referimos apenas àqueles agentes que estão à vista.

### Outros Modelos para Ver

Existem mais alguns modelos interessantes que você pode experimentar:

* **Arte → Fogos de Artifício** mostra como um fogo de artifício pode ser considerado um comportamento coletivo de fluxos individuais de fogo
* **Ciência Social → Tráfego Básico** e **Ciência Social → Grade de Tráfego** mostram o modelo de tráfego urbano em Grade 1D e 2D com ou sem semáforos. Cada carro na simulação segue as seguintes regras:
   - Se o espaço à sua frente estiver vazio - acelere (até uma certa velocidade máxima)
   - Se ele vê um obstáculo à frente - freie (e você pode ajustar quão longe um motorista pode ver)
* **Ciência Social → Festa** mostra como as pessoas se agrupam durante uma festa de coquetel. Você pode encontrar a combinação de parâmetros que leva ao aumento mais rápido da felicidade do grupo.

Como você pode ver por esses exemplos, simulações multi-agente podem ser uma maneira bastante útil de entender o comportamento de um sistema complexo composto por indivíduos que seguem a mesma lógica ou lógica semelhante. Também pode ser usado para controlar agentes virtuais, como [NPCs](https://en.wikipedia.org/wiki/NPC) em jogos de computador, ou agentes em mundos animados em 3D.

## Agentes Deliberativos

Os agentes descritos acima são muito simples, reagindo a mudanças no ambiente usando algum tipo de algoritmo. Como tal, eles são **agentes reativos**. No entanto, às vezes os agentes podem raciocinar e planejar suas ações, caso em que são chamados de **deliberativos**.

Um exemplo típico seria um agente pessoal que recebe uma instrução de um humano para reservar uma viagem de férias. Suponha que existam muitos agentes que vivem na internet, que podem ajudá-lo. Ele deve então entrar em contato com outros agentes para ver quais voos estão disponíveis, quais são os preços dos hotéis para diferentes datas e tentar negociar o melhor preço. Quando o plano de férias estiver completo e confirmado pelo proprietário, ele pode prosseguir com a reserva.

Para fazer isso, os agentes precisam **se comunicar**. Para uma comunicação bem-sucedida, eles precisam de:

* Algumas **línguas padrão para trocar conhecimento**, como [Formato de Intercâmbio de Conhecimento](https://en.wikipedia.org/wiki/Knowledge_Interchange_Format) (KIF) e [Linguagem de Consulta e Manipulação de Conhecimento](https://en.wikipedia.org/wiki/Knowledge_Query_and_Manipulation_Language) (KQML). Essas linguagens são projetadas com base na [Teoria do Ato de Fala](https://en.wikipedia.org/wiki/Speech_act).
* Essas linguagens também devem incluir alguns **protocolos para negociações**, baseados em diferentes **tipos de leilão**.
* Uma **ontologia comum** para usar, para que eles se refiram aos mesmos conceitos conhecendo sua semântica
* Uma maneira de **descobrir** o que diferentes agentes podem fazer, também baseada em algum tipo de ontologia

Agentes deliberativos são muito mais complexos do que reativos, porque eles não apenas reagem a mudanças no ambiente, mas também devem ser capazes de *iniciar* ações. Uma das arquiteturas propostas para agentes deliberativos é a chamada agente de Crença-Desejo-Intenção (BDI):

* **Crenças** formam um conjunto de conhecimentos sobre o ambiente de um agente. Pode ser estruturado como uma base de conhecimento ou um conjunto de regras que um agente pode aplicar a uma situação específica no ambiente.
* **Desejos** definem o que um agente quer fazer, ou seja, seus objetivos. Por exemplo, o objetivo do agente assistente pessoal acima é reservar uma viagem, e o objetivo de um agente de hotel é maximizar o lucro.
* **Intenções** são ações específicas que um agente planeja realizar para alcançar seus objetivos. As ações normalmente mudam o ambiente e causam comunicação com outros agentes.

Existem algumas plataformas disponíveis para construir sistemas multi-agente, como [JADE](https://jade.tilab.com/). [Este artigo](https://arxiv.org/ftp/arxiv/papers/2007/2007.08961.pdf) contém uma revisão das plataformas multi-agente, juntamente com uma breve história dos sistemas multi-agente e seus diferentes cenários de uso.

## Conclusão

Os sistemas multi-agente podem assumir formas muito diferentes e ser usados em muitas aplicações diferentes. 
Todos tendem a focar no comportamento mais simples de um agente individual e alcançar um comportamento mais complexo do sistema geral devido ao **efeito sinérgico**.

## 🚀 Desafio

Leve esta lição para o mundo real e tente conceituar um sistema multi-agente que possa resolver um problema. O que, por exemplo, um sistema multi-agente precisaria fazer para otimizar a rota de um ônibus escolar? Como ele poderia funcionar em uma padaria?

## [Quiz pós-aula](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/223)

## Revisão e Autoestudo

Revise o uso desse tipo de sistema na indústria. Escolha um domínio como fabricação ou a indústria de videogames e descubra como os sistemas multi-agente podem ser usados para resolver problemas únicos.

## [Tarefa NetLogo](assignment.md)

**Isenção de responsabilidade**:  
Este documento foi traduzido utilizando serviços de tradução automática baseados em IA. Embora nos esforcemos pela precisão, esteja ciente de que traduções automatizadas podem conter erros ou imprecisões. O documento original em seu idioma nativo deve ser considerado a fonte autoritativa. Para informações críticas, recomenda-se a tradução profissional por um humano. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações errôneas decorrentes do uso desta tradução.