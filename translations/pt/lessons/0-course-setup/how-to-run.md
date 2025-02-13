# Como Executar o Código

Este currículo contém muitos exemplos executáveis e laboratórios que você vai querer rodar. Para fazer isso, você precisa da capacidade de executar código Python em Jupyter Notebooks fornecidos como parte deste currículo. Você tem várias opções para executar o código:

## Executar localmente no seu computador

Para executar o código localmente no seu computador, você precisará ter alguma versão do Python instalada. Eu pessoalmente recomendo instalar o **[miniconda](https://conda.io/en/latest/miniconda.html)** - é uma instalação bastante leve que suporta o gerenciador de pacotes `conda` para diferentes **ambientes virtuais** Python.

Depois de instalar o miniconda, você precisa clonar o repositório e criar um ambiente virtual a ser usado para este curso:

```bash
git clone http://github.com/microsoft/ai-for-beginners
cd ai-for-beginners
conda env create --name ai4beg --file .devcontainer/environment.yml
conda activate ai4beg
```

### Usando o Visual Studio Code com a Extensão Python

Provavelmente a melhor maneira de usar o currículo é abri-lo no [Visual Studio Code](http://code.visualstudio.com/?WT.mc_id=academic-77998-cacaste) com a [Extensão Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python&WT.mc_id=academic-77998-cacaste).

> **Nota**: Assim que você clonar e abrir o diretório no VS Code, ele automaticamente sugerirá que você instale as extensões do Python. Você também terá que instalar o miniconda, conforme descrito acima.

> **Nota**: Se o VS Code sugerir que você reabra o repositório em um contêiner, você precisa recusar isso para usar a instalação local do Python.

### Usando Jupyter no Navegador

Você também pode usar o ambiente Jupyter diretamente do navegador no seu próprio computador. Na verdade, tanto o Jupyter clássico quanto o Jupyter Hub fornecem um ambiente de desenvolvimento bastante conveniente com autocompletar, destaque de código, etc.

Para iniciar o Jupyter localmente, vá para o diretório do curso e execute:

```bash
jupyter notebook
```
ou
```bash
jupyterhub
```
Você pode então navegar até qualquer uma das pastas `.ipynb` files, open them and start working.

### Running in container

One alternative to Python installation would be to run the code in container. Since our repository contains special `.devcontainer` que instruem como construir um contêiner para este repositório; o VS Code lhe oferecerá a opção de reabrir o código no contêiner. Isso exigirá a instalação do Docker e também será mais complexo, então recomendamos isso para usuários mais experientes.

## Executando na Nuvem

Se você não quiser instalar o Python localmente e tiver acesso a alguns recursos em nuvem, uma boa alternativa seria executar o código na nuvem. Existem várias maneiras de fazer isso:

* Usando **[GitHub Codespaces](https://github.com/features/codespaces)**, que é um ambiente virtual criado para você no GitHub, acessível através da interface do navegador do VS Code. Se você tiver acesso ao Codespaces, pode simplesmente clicar no botão **Code** no repositório, iniciar um codespace e começar a rodar em pouco tempo.
* Usando **[Binder](https://mybinder.org/v2/gh/microsoft/ai-for-beginners/HEAD)**. [Binder](https://mybinder.org) é um recurso de computação gratuito fornecido na nuvem para pessoas como você testarem algum código no GitHub. Há um botão na página inicial para abrir o repositório no Binder - isso deve levá-lo rapidamente ao site do binder, que construirá o contêiner subjacente e iniciará a interface web do Jupyter para você de forma contínua.

> **Nota**: Para prevenir abusos, o Binder tem acesso a alguns recursos da web bloqueados. Isso pode impedir que alguns códigos funcionem, que buscam modelos e/ou conjuntos de dados da Internet pública. Você pode precisar encontrar algumas soluções alternativas. Além disso, os recursos computacionais fornecidos pelo Binder são bastante básicos, então o treinamento será lento, especialmente nas lições mais complexas posteriores.

## Executando na Nuvem com GPU

Algumas das lições posteriores neste currículo se beneficiariam muito do suporte a GPU, pois, caso contrário, o treinamento será dolorosamente lento. Existem algumas opções que você pode seguir, especialmente se tiver acesso à nuvem, seja através do [Azure for Students](https://azure.microsoft.com/free/students/?WT.mc_id=academic-77998-cacaste) ou através da sua instituição:

* Criar uma [Máquina Virtual de Ciência de Dados](https://docs.microsoft.com/learn/modules/intro-to-azure-data-science-virtual-machine/?WT.mc_id=academic-77998-cacaste) e se conectar a ela através do Jupyter. Você pode então clonar o repositório diretamente na máquina e começar a aprender. As VMs da série NC têm suporte a GPU.

> **Nota**: Algumas assinaturas, incluindo o Azure for Students, não fornecem suporte a GPU de forma nativa. Você pode precisar solicitar núcleos de GPU adicionais através de um pedido de suporte técnico.

* Criar um [Espaço de Trabalho de Aprendizado de Máquina do Azure](https://azure.microsoft.com/services/machine-learning/?WT.mc_id=academic-77998-cacaste) e então usar o recurso de Notebook lá. [Este vídeo](https://azure-for-academics.github.io/quickstart/azureml-papers/) mostra como clonar um repositório em um notebook do Azure ML e começar a usá-lo.

Você também pode usar o Google Colab, que vem com algum suporte gratuito para GPU, e fazer o upload de Jupyter Notebooks lá para executá-los um por um.

**Isenção de responsabilidade**:  
Este documento foi traduzido utilizando serviços de tradução automática baseados em IA. Embora nos esforcemos pela precisão, esteja ciente de que traduções automáticas podem conter erros ou imprecisões. O documento original em seu idioma nativo deve ser considerado a fonte autoritativa. Para informações críticas, recomenda-se a tradução profissional por um humano. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações errôneas decorrentes do uso desta tradução.