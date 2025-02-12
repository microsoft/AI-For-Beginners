# Representação do Conhecimento e Sistemas Especialistas

![Resumo do conteúdo de IA Simbólica](../../../../translated_images/ai-symbolic.715a30cb610411a6964d2e2f23f24364cb338a07cb4844c1f97084d366e586c3.pt.png)

> Sketchnote por [Tomomi Imura](https://twitter.com/girlie_mac)

A busca pela inteligência artificial é baseada na procura por conhecimento, para compreender o mundo de forma semelhante a como os humanos fazem. Mas como você pode fazer isso?

## [Quiz pré-aula](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/102)

Nos primeiros dias da IA, a abordagem de cima para baixo para criar sistemas inteligentes (discutida na lição anterior) era popular. A ideia era extrair o conhecimento das pessoas para alguma forma legível por máquina e, em seguida, usá-lo para resolver problemas automaticamente. Essa abordagem baseava-se em duas grandes ideias:

* Representação do Conhecimento
* Raciocínio

## Representação do Conhecimento

Um dos conceitos importantes na IA Simbólica é o **conhecimento**. É importante diferenciar conhecimento de *informação* ou *dados*. Por exemplo, pode-se dizer que livros contêm conhecimento, porque alguém pode estudar livros e se tornar um especialista. No entanto, o que os livros contêm é, na verdade, chamado de *dados*, e ao ler livros e integrar esses dados em nosso modelo de mundo, convertemos esses dados em conhecimento.

> ✅ **Conhecimento** é algo que está contido em nossa mente e representa nossa compreensão do mundo. Ele é obtido por um processo ativo de **aprendizagem**, que integra pedaços de informação que recebemos em nosso modelo ativo do mundo.

Na maioria das vezes, não definimos estritamente conhecimento, mas o alinhamos com outros conceitos relacionados usando a [Pirâmide DIKW](https://en.wikipedia.org/wiki/DIKW_pyramid). Ela contém os seguintes conceitos:

* **Dados** são algo representado em mídias físicas, como texto escrito ou palavras faladas. Dados existem independentemente dos seres humanos e podem ser transmitidos entre as pessoas.
* **Informação** é como interpretamos dados em nossa mente. Por exemplo, quando ouvimos a palavra *computador*, temos alguma compreensão do que é.
* **Conhecimento** é a informação integrada em nosso modelo de mundo. Por exemplo, uma vez que aprendemos o que é um computador, começamos a ter algumas ideias sobre como ele funciona, quanto custa e para que pode ser usado. Essa rede de conceitos inter-relacionados forma nosso conhecimento.
* **Sabedoria** é mais um nível de nossa compreensão do mundo e representa *meta-conhecimento*, ou seja, alguma noção de como e quando o conhecimento deve ser usado.

<img src="images/DIKW_Pyramid.png" width="30%"/>

*Imagem [da Wikipedia](https://commons.wikimedia.org/w/index.php?curid=37705247), Por Longlivetheux - Trabalho próprio, CC BY-SA 4.0*

Assim, o problema da **representação do conhecimento** é encontrar uma maneira eficaz de representar o conhecimento dentro de um computador na forma de dados, para torná-lo automaticamente utilizável. Isso pode ser visto como um espectro:

![Espectro de representação do conhecimento](../../../../translated_images/knowledge-spectrum.b60df631852c0217e941485b79c9eee40ebd574f15f18609cec5758fcb384bf3.pt.png)

> Imagem por [Dmitry Soshnikov](http://soshnikov.com)

* À esquerda, existem tipos muito simples de representações de conhecimento que podem ser efetivamente utilizados por computadores. O mais simples é o algorítmico, quando o conhecimento é representado por um programa de computador. No entanto, essa não é a melhor maneira de representar conhecimento, pois não é flexível. O conhecimento dentro de nossa mente é frequentemente não algorítmico.
* À direita, existem representações como texto natural. É a mais poderosa, mas não pode ser usada para raciocínio automático.

> ✅ Pense por um minuto sobre como você representa conhecimento em sua mente e o converte em anotações. Existe um formato específico que funciona bem para você ajudar na retenção?

## Classificando Representações de Conhecimento Computacional

Podemos classificar diferentes métodos de representação de conhecimento computacional nas seguintes categorias:

* **Representações em rede** baseiam-se no fato de que temos uma rede de conceitos inter-relacionados em nossa mente. Podemos tentar reproduzir as mesmas redes como um gráfico dentro de um computador - uma chamada **rede semântica**.

1. **Triplas Objeto-Atributo-Valor** ou **pares atributo-valor**. Uma vez que um gráfico pode ser representado dentro de um computador como uma lista de nós e arestas, podemos representar uma rede semântica por uma lista de triplas, contendo objetos, atributos e valores. Por exemplo, construímos as seguintes triplas sobre linguagens de programação:

Objeto | Atributo | Valor
-------|-----------|------
Python | é | Linguagem-Destipada
Python | inventado-por | Guido van Rossum
Python | sintaxe-bloco | indentação
Linguagem-Destipada | não tem | definições de tipo

> ✅ Pense em como triplas podem ser usadas para representar outros tipos de conhecimento.

2. **Representações hierárquicas** enfatizam o fato de que frequentemente criamos uma hierarquia de objetos em nossa mente. Por exemplo, sabemos que um canário é um pássaro, e todos os pássaros têm asas. Também temos alguma ideia sobre qual é a cor de um canário normalmente, e qual é a sua velocidade de voo.

   - **Representação em quadro** baseia-se em representar cada objeto ou classe de objetos como um **quadro** que contém **slots**. Slots têm possíveis valores padrão, restrições de valor ou procedimentos armazenados que podem ser chamados para obter o valor de um slot. Todos os quadros formam uma hierarquia semelhante a uma hierarquia de objetos em linguagens de programação orientadas a objetos.
   - **Cenários** são um tipo especial de quadros que representam situações complexas que podem se desenrolar ao longo do tempo.

**Python**

Slot | Valor | Valor padrão | Intervalo |
-----|-------|---------------|----------|
Nome | Python | | |
É-Uma | Linguagem-Destipada | | |
Caso da Variável | | CamelCase | |
Comprimento do Programa | | | 5-5000 linhas |
Sintaxe do Bloco | Indente | | |

3. **Representações procedurais** baseiam-se em representar conhecimento por uma lista de ações que podem ser executadas quando uma certa condição ocorre.
   - Regras de produção são declarações do tipo se-então que nos permitem tirar conclusões. Por exemplo, um médico pode ter uma regra dizendo que **SE** um paciente tem febre alta **OU** um nível elevado de proteína C-reativa no exame de sangue **ENTÃO** ele tem uma inflamação. Uma vez que encontramos uma das condições, podemos chegar a uma conclusão sobre a inflamação e, em seguida, usá-la em um raciocínio posterior.
   - Algoritmos podem ser considerados outra forma de representação procedural, embora quase nunca sejam usados diretamente em sistemas baseados em conhecimento.

4. **Lógica** foi originalmente proposta por Aristóteles como uma maneira de representar o conhecimento humano universal.
   - A Lógica de Predicados, como uma teoria matemática, é rica demais para ser computável, portanto, normalmente usa-se algum subconjunto dela, como cláusulas Horn usadas em Prolog.
   - A Lógica Descritiva é uma família de sistemas lógicos usados para representar e raciocinar sobre hierarquias de objetos em representações de conhecimento distribuído, como a *web semântica*.

## Sistemas Especialistas

Um dos primeiros sucessos da IA simbólica foram os chamados **sistemas especialistas** - sistemas computacionais que foram projetados para atuar como um especialista em algum domínio de problema limitado. Eles eram baseados em uma **base de conhecimento** extraída de um ou mais especialistas humanos e continham um **motor de inferência** que realizava algum raciocínio sobre isso.

![Arquitetura Humana](../../../../translated_images/arch-human.5d4d35f1bba3ab1cdfda96af2f10b89574eb31e9796d0e3011cd9beda1c35112.pt.png) | ![Sistema Baseado em Conhecimento](../../../../translated_images/arch-kbs.3ec5c150b09fa8dadc2beb0931a4983c9e2b03913a89eebcc103b5bb841b0212.pt.png)
---------------------------------------------|------------------------------------------------
Estrutura simplificada de um sistema neural humano | Arquitetura de um sistema baseado em conhecimento

Os sistemas especialistas são construídos como o sistema de raciocínio humano, que contém **memória de curto prazo** e **memória de longo prazo**. Da mesma forma, em sistemas baseados em conhecimento, distinguimos os seguintes componentes:

* **Memória do problema**: contém o conhecimento sobre o problema que está sendo resolvido atualmente, ou seja, a temperatura ou pressão arterial de um paciente, se ele tem inflamação ou não, etc. Esse conhecimento também é chamado de **conhecimento estático**, porque contém uma instantânea do que sabemos atualmente sobre o problema - o chamado *estado do problema*.
* **Base de conhecimento**: representa o conhecimento de longo prazo sobre um domínio de problema. É extraído manualmente de especialistas humanos e não muda de consulta para consulta. Como permite navegar de um estado do problema para outro, também é chamado de **conhecimento dinâmico**.
* **Motor de inferência**: orquestra todo o processo de busca no espaço do estado do problema, fazendo perguntas ao usuário quando necessário. Também é responsável por encontrar as regras corretas a serem aplicadas a cada estado.

Como exemplo, vamos considerar o seguinte sistema especialista para determinar um animal com base em suas características físicas:

![Árvore AND-OR](../../../../translated_images/AND-OR-Tree.5592d2c70187f283703c8e9c0d69d6a786eb370f4ace67f9a7aae5ada3d260b0.pt.png)

> Imagem por [Dmitry Soshnikov](http://soshnikov.com)

Esse diagrama é chamado de **árvore AND-OR**, e é uma representação gráfica de um conjunto de regras de produção. Desenhar uma árvore é útil no início da extração de conhecimento do especialista. Para representar o conhecimento dentro do computador, é mais conveniente usar regras:

```
IF the animal eats meat
OR (animal has sharp teeth
    AND animal has claws
    AND animal has forward-looking eyes
) 
THEN the animal is a carnivore
```

Você pode notar que cada condição no lado esquerdo da regra e a ação são essencialmente triplas objeto-atributo-valor (OAV). **Memória de trabalho** contém o conjunto de triplas OAV que correspondem ao problema que está sendo resolvido atualmente. Um **motor de regras** procura regras para as quais uma condição é satisfeita e as aplica, adicionando outra tripla à memória de trabalho.

> ✅ Escreva sua própria árvore AND-OR sobre um tópico que você goste!

### Inferência Direta vs. Inferência Reversa

O processo descrito acima é chamado de **inferência direta**. Ele começa com alguns dados iniciais sobre o problema disponíveis na memória de trabalho e, em seguida, executa o seguinte loop de raciocínio:

1. Se o atributo alvo estiver presente na memória de trabalho - pare e forneça o resultado
2. Procure todas as regras cuja condição esteja atualmente satisfeita - obtenha o **conjunto de conflitos** de regras.
3. Realize a **resolução de conflitos** - selecione uma regra que será executada neste passo. Pode haver diferentes estratégias de resolução de conflitos:
   - Selecione a primeira regra aplicável na base de conhecimento
   - Selecione uma regra aleatória
   - Selecione uma regra *mais específica*, ou seja, aquela que atende ao maior número de condições no "lado esquerdo" (LHS)
4. Aplique a regra selecionada e insira um novo pedaço de conhecimento no estado do problema
5. Repita a partir do passo 1.

No entanto, em alguns casos, podemos querer começar com um conhecimento vazio sobre o problema e fazer perguntas que nos ajudem a chegar à conclusão. Por exemplo, ao fazer um diagnóstico médico, geralmente não realizamos todas as análises médicas antecipadamente antes de começar a diagnosticar o paciente. Preferimos realizar análises quando uma decisão precisa ser tomada.

Esse processo pode ser modelado usando **inferência reversa**. Ele é impulsionado pelo **objetivo** - o valor do atributo que estamos tentando encontrar:

1. Selecione todas as regras que podem nos dar o valor de um objetivo (ou seja, com o objetivo no RHS ("lado direito")) - um conjunto de conflitos
1. Se não houver regras para esse atributo, ou se houver uma regra dizendo que devemos perguntar o valor ao usuário - pergunte, caso contrário:
1. Use a estratégia de resolução de conflitos para selecionar uma regra que usaremos como *hipótese* - tentaremos prová-la
1. Repetidamente repita o processo para todos os atributos no LHS da regra, tentando prová-los como objetivos
1. Se em algum momento o processo falhar - use outra regra no passo 3.

> ✅ Em quais situações a inferência direta é mais apropriada? E a inferência reversa?

### Implementando Sistemas Especialistas

Os sistemas especialistas podem ser implementados usando diferentes ferramentas:

* Programando-os diretamente em alguma linguagem de programação de alto nível. Esta não é a melhor ideia, pois a principal vantagem de um sistema baseado em conhecimento é que o conhecimento é separado da inferência, e potencialmente um especialista em domínio de problema deve ser capaz de escrever regras sem entender os detalhes do processo de inferência.
* Usando **shell de sistemas especialistas**, ou seja, um sistema especificamente projetado para ser populado com conhecimento usando alguma linguagem de representação de conhecimento.

## ✍️ Exercício: Inferência Animal

Veja [Animals.ipynb](https://github.com/microsoft/AI-For-Beginners/blob/main/lessons/2-Symbolic/Animals.ipynb) para um exemplo de implementação de sistema especialista de inferência direta e reversa.

> **Nota**: Este exemplo é bastante simples e apenas dá a ideia de como um sistema especialista se parece. Uma vez que você comece a criar tal sistema, você só notará um comportamento *inteligente* a partir do momento em que atingir um certo número de regras, em torno de 200+. Em algum ponto, as regras se tornam complexas demais para manter todas elas em mente, e nesse momento você pode começar a se perguntar por que um sistema toma certas decisões. No entanto, a característica importante dos sistemas baseados em conhecimento é que você pode sempre *explicar* exatamente como qualquer uma das decisões foi tomada.

## Ontologias e a Web Semântica

No final do século 20, houve uma iniciativa para usar a representação do conhecimento para anotar recursos da Internet, de modo que fosse possível encontrar recursos que corresponderiam a consultas muito específicas. Esse movimento foi chamado de **Web Semântica**, e baseou-se em vários conceitos:

- Uma representação de conhecimento especial baseada em **[lógicas descritivas](https://en.wikipedia.org/wiki/Description_logic)** (DL). É semelhante à representação de conhecimento em quadros, porque constrói uma hierarquia de objetos com propriedades, mas possui semântica lógica formal e inferência. Há uma família inteira de DLs que equilibram expressividade e complexidade algorítmica de inferência.
- Representação de conhecimento distribuído, onde todos os conceitos são representados por um identificador URI global, tornando possível criar hierarquias de conhecimento que se estendem pela internet.
- Uma família de linguagens baseadas em XML para descrição de conhecimento: RDF (Resource Description Framework), RDFS (RDF Schema), OWL (Ontology Web Language).

Um conceito central na Web Semântica é o conceito de **Ontologia**. Refere-se a uma especificação explícita de um domínio de problema usando alguma representação formal de conhecimento. A ontologia mais simples pode ser apenas uma hierarquia de objetos em um domínio de problema, mas ontologias mais complexas incluirão regras que podem ser usadas para inferência.

Na web semântica, todas as representações são baseadas em triplas. Cada objeto e cada relação são identificados de forma única pelo URI. Por exemplo, se quisermos afirmar o fato de que este Currículo de IA foi desenvolvido por Dmitry Soshnikov em 1º de janeiro de 2022 - aqui estão as triplas que podemos usar:

<img src="images/triplet.png" width="30%"/>

```
http://github.com/microsoft/ai-for-beginners http://www.example.com/terms/creation-date “Jan 13, 2007”
http://github.com/microsoft/ai-for-beginners http://purl.org/dc/elements/1.1/creator http://soshnikov.com
```

> ✅ Aqui `http://www.example.com/terms/creation-date` and `http://purl.org/dc/elements/1.1/creator` são alguns URIs bem conhecidos e universalmente aceitos para expressar os conceitos de *criador* e *data de criação*.

Em um caso mais complexo, se quisermos definir uma lista de criadores, podemos usar algumas estruturas de dados definidas em RDF.

<img src="images/triplet-complex.png" width="40%"/>

> Diagramas acima por [Dmitry Soshnikov](http://soshnikov.com)

O progresso na construção da Web Semântica foi de certa forma desacelerado pelo sucesso dos motores de busca e técnicas de processamento de linguagem natural, que permitem extrair dados estruturados de texto. No entanto, em algumas áreas, ainda existem esforços significativos para manter ontologias e bases de conhecimento. Alguns projetos que valem a pena notar:

* [WikiData](https://wikidata.org/) é uma coleção de bases de conhecimento legíveis por máquina associadas ao Wikipedia. A maior parte dos dados é extraída das *InfoBoxes* do Wikipedia, pedaços de conteúdo estruturado dentro das páginas do Wikipedia. Você pode [consultar](https://query.wikidata.org/) wikidata em SPARQL, uma linguagem de consulta especial para a Web Semântica. Aqui está uma consulta de exemplo que exibe as cores de olhos mais populares entre os humanos:

```sparql
#defaultView:BubbleChart
SELECT ?eyeColorLabel (COUNT(?human) AS ?count)
WHERE
{
  ?human wdt:P31 wd:Q5.       # human instance-of homo sapiens
  ?human wdt:P1340 ?eyeColor. # human eye-color ?eyeColor
  SERVICE wikibase:label { bd:serviceParam wikibase:language "en". }
}
GROUP BY ?eyeColorLabel
```

* [DBpedia](https://www.dbpedia.org/) é outro esforço semelhante ao WikiData.

> ✅ Se você quiser experimentar a construção de suas próprias ontologias, ou abrir ontologias existentes, há um ótimo editor visual de ontologias chamado [Protégé](https://protege.stanford.edu/). Baixe-o ou use-o online.

<img src="images/protege.png" width="70%"/>

*Editor Web Protégé aberto com a ontologia da Família Romanov. Captura de tela por Dmitry Soshnikov*

## ✍️ Exercício: Uma Ontologia Familiar

Veja [FamilyOntology.ipynb](https://github.com/Ezana135/AI-For-Beginners/blob/main/lessons/2-Symbolic/FamilyOntology.ipynb) para um exemplo de uso de técnicas da Web Semântica para raciocinar sobre relacionamentos familiares. Nós pegaremos uma árvore genealógica representada no formato GEDCOM comum e uma ontologia de relacionamentos familiares e construiremos um gráfico de todos os relacionamentos familiares para um conjunto dado de indivíduos.

## Grafo de Conceitos da Microsoft

Na maioria dos casos, as ontologias são cuidadosamente criadas à mão. No entanto, também é possível **extrair** ontologias de dados não estruturados, por exemplo, de textos em linguagem natural.

Uma dessas tentativas foi feita pela Microsoft Research, resultando no [Grafo de Conceitos da Microsoft](https://blogs.microsoft.com/ai/microsoft-researchers-release-graph-that-helps-machines-conceptualize/?WT.mc_id=academic-77998-cacaste).

É uma grande coleção de entidades agrupadas usando a relação de herança `is-a`. Permite responder a perguntas como "O que é a Microsoft?" - a resposta sendo algo como "uma empresa com probabilidade de 0,87 e uma marca

**Isenção de responsabilidade**:  
Este documento foi traduzido utilizando serviços de tradução automática baseados em IA. Embora nos esforcemos pela precisão, esteja ciente de que traduções automatizadas podem conter erros ou imprecisões. O documento original em sua língua nativa deve ser considerado a fonte autoritativa. Para informações críticas, recomenda-se a tradução profissional realizada por humanos. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações equivocadas resultantes do uso desta tradução.