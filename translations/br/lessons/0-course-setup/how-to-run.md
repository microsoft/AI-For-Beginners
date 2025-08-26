<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "7df19702b8d2d3f7c4238c51bec2c8fc",
  "translation_date": "2025-08-26T11:11:13+00:00",
  "source_file": "lessons/0-course-setup/how-to-run.md",
  "language_code": "br"
}
-->
# Como Executar o Código

Este curso contém muitos exemplos executáveis e laboratórios que você provavelmente vai querer rodar. Para isso, é necessário ter a capacidade de executar código Python em Jupyter Notebooks fornecidos como parte deste curso. Você tem várias opções para executar o código:

## Executar localmente no seu computador

Para executar o código localmente no seu computador, você precisará ter alguma versão do Python instalada. Eu recomendo instalar o **[miniconda](https://conda.io/en/latest/miniconda.html)** - é uma instalação leve que suporta o gerenciador de pacotes `conda` para diferentes **ambientes virtuais** Python.

Depois de instalar o miniconda, você precisará clonar o repositório e criar um ambiente virtual para ser usado neste curso:

```bash
git clone http://github.com/microsoft/ai-for-beginners
cd ai-for-beginners
conda env create --name ai4beg --file .devcontainer/environment.yml
conda activate ai4beg
```

### Usando o Visual Studio Code com a Extensão Python

Provavelmente, a melhor maneira de usar o curso é abri-lo no [Visual Studio Code](http://code.visualstudio.com/?WT.mc_id=academic-77998-cacaste) com a [Extensão Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python&WT.mc_id=academic-77998-cacaste).

> **Nota**: Assim que você clonar e abrir o diretório no VS Code, ele automaticamente sugerirá a instalação das extensões Python. Você também precisará instalar o miniconda conforme descrito acima.

> **Nota**: Se o VS Code sugerir reabrir o repositório em um container, recuse para usar a instalação local do Python.

### Usando o Jupyter no Navegador

Você também pode usar o ambiente Jupyter diretamente do navegador no seu próprio computador. Na verdade, tanto o Jupyter clássico quanto o Jupyter Hub oferecem um ambiente de desenvolvimento bastante conveniente com autocompletar, destaque de código, etc.

Para iniciar o Jupyter localmente, vá até o diretório do curso e execute:

```bash
jupyter notebook
```
ou
```bash
jupyterhub
```
Depois, você pode navegar até qualquer um dos arquivos `.ipynb`, abri-los e começar a trabalhar.

### Executando em um Container

Uma alternativa à instalação do Python seria executar o código em um container. Como nosso repositório contém uma pasta especial `.devcontainer` que instrui como construir um container para este repositório, o VS Code oferecerá a opção de reabrir o código em um container. Isso exigirá a instalação do Docker e será mais complexo, então recomendamos essa opção para usuários mais experientes.

## Executando na Nuvem

Se você não quiser instalar o Python localmente e tiver acesso a alguns recursos na nuvem, uma boa alternativa seria executar o código na nuvem. Existem várias maneiras de fazer isso:

* Usando o **[GitHub Codespaces](https://github.com/features/codespaces)**, que é um ambiente virtual criado para você no GitHub, acessível através da interface do navegador do VS Code. Se você tiver acesso ao Codespaces, basta clicar no botão **Code** no repositório, iniciar um codespace e começar a trabalhar rapidamente.
* Usando o **[Binder](https://mybinder.org/v2/gh/microsoft/ai-for-beginners/HEAD)**. O [Binder](https://mybinder.org) oferece recursos computacionais gratuitos na nuvem para pessoas como você testarem algum código no GitHub. Há um botão na página inicial para abrir o repositório no Binder - isso deve levá-lo rapidamente ao site do Binder, que construirá o container subjacente e iniciará a interface web do Jupyter para você de forma transparente.

> **Nota**: Para evitar uso indevido, o Binder bloqueia o acesso a alguns recursos da web. Isso pode impedir que alguns códigos funcionem, especialmente aqueles que baixam modelos e/ou conjuntos de dados da Internet pública. Você pode precisar encontrar alternativas. Além disso, os recursos computacionais fornecidos pelo Binder são bastante básicos, então o treinamento será lento, especialmente nas lições mais complexas.

## Executando na Nuvem com GPU

Algumas das lições mais avançadas deste curso se beneficiariam muito do suporte a GPU, pois, caso contrário, o treinamento será extremamente lento. Existem algumas opções que você pode seguir, especialmente se tiver acesso à nuvem, seja através do [Azure for Students](https://azure.microsoft.com/free/students/?WT.mc_id=academic-77998-cacaste) ou da sua instituição:

* Criar uma [Máquina Virtual de Ciência de Dados](https://docs.microsoft.com/learn/modules/intro-to-azure-data-science-virtual-machine/?WT.mc_id=academic-77998-cacaste) e conectá-la via Jupyter. Você pode então clonar o repositório diretamente na máquina e começar a aprender. As VMs da série NC possuem suporte a GPU.

> **Nota**: Algumas assinaturas, incluindo o Azure for Students, não oferecem suporte a GPU por padrão. Pode ser necessário solicitar núcleos de GPU adicionais através de um pedido de suporte técnico.

* Criar um [Workspace do Azure Machine Learning](https://azure.microsoft.com/services/machine-learning/?WT.mc_id=academic-77998-cacaste) e usar o recurso de Notebook lá. [Este vídeo](https://azure-for-academics.github.io/quickstart/azureml-papers/) mostra como clonar um repositório em um notebook do Azure ML e começar a usá-lo.

Você também pode usar o Google Colab, que oferece algum suporte gratuito a GPU, e carregar os Jupyter Notebooks lá para executá-los um por um.

**Aviso Legal**:  
Este documento foi traduzido utilizando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos para garantir a precisão, esteja ciente de que traduções automáticas podem conter erros ou imprecisões. O documento original em seu idioma nativo deve ser considerado a fonte oficial. Para informações críticas, recomenda-se a tradução profissional feita por humanos. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações equivocadas decorrentes do uso desta tradução.