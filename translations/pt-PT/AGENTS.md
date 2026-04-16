# AGENTS.md

## Visão Geral do Projeto

AI for Beginners é um currículo abrangente de 12 semanas e 24 aulas que cobre os fundamentos da Inteligência Artificial. Este repositório educacional inclui lições práticas usando Jupyter Notebooks, questionários e laboratórios práticos. O currículo aborda:

- IA Simbólica com Representação de Conhecimento e Sistemas Especialistas
- Redes Neurais e Aprendizagem Profunda com TensorFlow e PyTorch
- Técnicas e arquiteturas de Visão Computacional
- Processamento de Linguagem Natural (NLP), incluindo transformers e BERT
- Tópicos especializados: Algoritmos Genéticos, Aprendizagem por Reforço, Sistemas Multiagentes
- Ética em IA e princípios de IA Responsável

**Principais Tecnologias:** Python 3, Jupyter Notebooks, TensorFlow, PyTorch, Keras, OpenCV, Vue.js (para aplicação de questionários)

**Arquitetura:** Repositório de conteúdo educacional com Jupyter Notebooks organizados por áreas temáticas, complementado por uma aplicação de questionários baseada em Vue.js e suporte extensivo a múltiplos idiomas.

## Comandos de Configuração

### Ambiente de Desenvolvimento Principal (Python/Jupyter)

O currículo foi projetado para ser executado com Python e Jupyter Notebooks. A abordagem recomendada é usar miniconda:

```bash
# Clone the repository
git clone https://github.com/microsoft/ai-for-beginners
cd ai-for-beginners

# Create and activate conda environment
conda env create --name ai4beg --file environment.yml
conda activate ai4beg

# Start Jupyter Notebook
jupyter notebook
# OR
jupyter lab
```

### Alternativa: Usar devcontainer

```bash
# Open in VS Code and select "Reopen in Container" when prompted
# The devcontainer will automatically set up the environment
```

### Configuração da Aplicação de Questionários

A aplicação de questionários é uma aplicação Vue.js separada localizada em `etc/quiz-app/`:

```bash
cd etc/quiz-app
npm install
npm run serve  # Development server
npm run build  # Production build
npm run lint   # Lint and fix files
```

## Fluxo de Trabalho de Desenvolvimento

### Trabalhar com Jupyter Notebooks

1. **Desenvolvimento Local:**
   - Ativar o ambiente conda: `conda activate ai4beg`
   - Iniciar o Jupyter: `jupyter notebook` ou `jupyter lab`
   - Navegar pelas pastas das lições e abrir os ficheiros `.ipynb`
   - Executar as células interativamente para acompanhar as lições

2. **VS Code com Extensão Python:**
   - Abrir o repositório no VS Code
   - Instalar a extensão Python
   - O VS Code deteta automaticamente e utiliza o ambiente conda
   - Abrir ficheiros `.ipynb` diretamente no VS Code

3. **Desenvolvimento na Nuvem:**
   - **GitHub Codespaces:** Clique em "Code" → "Codespaces" → "Create codespace on main"
   - **Binder:** Use o emblema Binder no README para iniciar no navegador
   - Nota: O Binder tem recursos limitados e algumas restrições de acesso à web

### Suporte a GPU para Lições Avançadas

As lições posteriores beneficiam significativamente da aceleração por GPU:

- **Azure Data Science VM:** Utilize VMs da série NC com suporte a GPU
- **Azure Machine Learning:** Utilize funcionalidades de notebooks com computação GPU
- **Google Colab:** Carregue os notebooks individualmente (tem suporte gratuito a GPU)

### Desenvolvimento da Aplicação de Questionários

```bash
cd etc/quiz-app
npm run serve  # Hot-reload development server at http://localhost:8080
```

## Instruções de Teste

Este é um repositório educacional focado em conteúdo de aprendizagem, em vez de testes de software. Não há um conjunto de testes tradicional.

### Abordagens de Validação:

1. **Jupyter Notebooks:** Execute as células sequencialmente para verificar se os exemplos de código funcionam
2. **Teste da Aplicação de Questionários:** Teste manual através do servidor de desenvolvimento
3. **Validação de Traduções:** Verifique o conteúdo traduzido na pasta `translations/`
4. **Linting da Aplicação de Questionários:** `npm run lint` em `etc/quiz-app/`

### Executar Exemplos de Código:

```bash
# Activate environment first
conda activate ai4beg

# Run Python scripts directly
python lessons/4-ComputerVision/07-ConvNets/pytorchcv.py

# Or execute notebooks
jupyter notebook lessons/3-NeuralNetworks/03-Perceptron/Perceptron.ipynb
```

## Estilo de Código

### Estilo de Código Python

- Convenções padrão de Python para código educacional
- Código claro e legível, priorizando o aprendizado em vez da otimização
- Comentários explicando conceitos-chave
- Compatível com Jupyter Notebook: as células devem ser autossuficientes sempre que possível
- Não há requisitos rigorosos de linting para o conteúdo das lições

### JavaScript/Vue.js (Aplicação de Questionários)

- Configuração ESLint em `etc/quiz-app/package.json`
- Execute `npm run lint` para verificar e corrigir automaticamente problemas
- Convenções do Vue 2.x
- Arquitetura baseada em componentes

### Organização de Ficheiros

```
lessons/
  ├── 0-course-setup/          # Setup instructions
  ├── 1-Intro/                 # Introduction to AI
  ├── 2-Symbolic/              # Symbolic AI
  ├── 3-NeuralNetworks/        # Neural Networks basics
  ├── 4-ComputerVision/        # Computer Vision
  ├── 5-NLP/                   # Natural Language Processing
  ├── 6-Other/                 # Other AI techniques
  ├── 7-Ethics/                # AI Ethics
  └── X-Extras/                # Additional content

etc/
  ├── quiz-app/                # Vue.js quiz application
  └── quiz-src/                # Quiz source files

translations/                  # Multi-language translations
```

## Construção e Implementação

### Conteúdo Jupyter

Não é necessário processo de construção - os Jupyter Notebooks são executados diretamente.

### Aplicação de Questionários

```bash
cd etc/quiz-app

# Development
npm run serve

# Production build
npm run build  # Outputs to etc/quiz-app/dist/

# Deploy to Azure Static Web Apps
# Azure automatically creates GitHub Actions workflow
# See etc/quiz-app/README.md for detailed deployment instructions
```

### Site de Documentação

O repositório utiliza Docsify para documentação:
- `index.html` serve como ponto de entrada
- Não é necessário construção - servido diretamente via GitHub Pages
- Acesso em: https://microsoft.github.io/AI-For-Beginners/

## Diretrizes de Contribuição

### Processo de Pull Request

1. **Formato do Título:** Títulos claros e descritivos que descrevam a alteração
2. **Requisito CLA:** O CLA da Microsoft deve ser assinado (verificação automatizada)
3. **Diretrizes de Conteúdo:**
   - Mantenha o foco educacional e abordagem amigável para iniciantes
   - Teste todos os exemplos de código nos notebooks
   - Certifique-se de que os notebooks são executados de ponta a ponta
   - Atualize traduções se modificar o conteúdo em inglês
4. **Alterações na Aplicação de Questionários:** Execute `npm run lint` antes de fazer commit

### Contribuições de Tradução

- As traduções são automatizadas via GitHub Actions usando co-op-translator
- Traduções manuais vão para `translations/<language-code>/`
- Traduções de questionários em `etc/quiz-app/src/assets/translations/`
- Idiomas suportados: mais de 40 idiomas (consulte o README para a lista completa)

### Áreas Ativas de Contribuição

Consulte `etc/CONTRIBUTING.md` para necessidades atuais:
- Secções de Aprendizagem por Reforço Profundo
- Melhorias na Detecção de Objetos
- Exemplos de Reconhecimento de Entidades Nomeadas
- Amostras de treino de embeddings personalizados

## Configuração do Ambiente

### Dependências Necessárias

```bash
# Core Python packages (from requirements.txt)
tensorflow==2.17.0
torch (via conda)
torchvision (via conda)
keras==3.5.0
opencv (via conda)
scikit-learn
numpy==1.26
pandas==2.2.2
matplotlib==3.9
jupyter
```

### Variáveis de Ambiente

Não são necessárias variáveis de ambiente especiais para uso básico.

Para implementações no Azure (aplicação de questionários):
- `AZURE_STATIC_WEB_APPS_API_TOKEN` (configurado automaticamente pelo Azure)

## Depuração e Resolução de Problemas

### Problemas Comuns

**Problema:** Falha na criação do ambiente conda
- **Solução:** Atualize o conda primeiro: `conda update conda -y`
- Certifique-se de que há espaço suficiente em disco (recomendado 50GB)

**Problema:** Kernel do Jupyter não encontrado
- **Solução:** 
  ```bash
  conda activate ai4beg
  python -m ipykernel install --user --name ai4beg
  ```

**Problema:** GPU não detetada nos notebooks
- **Solução:** 
  - Verifique a instalação do CUDA: `nvidia-smi`
  - Verifique GPU no PyTorch: `python -c "import torch; print(torch.cuda.is_available())"`
  - Verifique GPU no TensorFlow: `python -c "import tensorflow as tf; print(tf.config.list_physical_devices('GPU'))"`

**Problema:** Aplicação de questionários não inicia
- **Solução:**
  ```bash
  cd etc/quiz-app
  rm -rf node_modules package-lock.json
  npm install
  npm run serve
  ```

**Problema:** Binder expira ou bloqueia downloads
- **Solução:** Use GitHub Codespaces ou configuração local para melhor acesso a recursos

### Problemas de Memória

Algumas lições requerem RAM significativa (recomendado 8GB+):
- Utilize VMs na nuvem para lições que exigem muitos recursos
- Feche outras aplicações ao treinar modelos
- Reduza os tamanhos de batch nos notebooks se ficar sem memória

## Notas Adicionais

### Para Instrutores do Curso

- Consulte `lessons/0-course-setup/for-teachers.md` para orientações de ensino
- As lições são autossuficientes e podem ser ensinadas em sequência ou selecionadas individualmente
- Tempo estimado: 12 semanas com 2 lições por semana

### Recursos na Nuvem

- **Azure for Students:** Créditos gratuitos disponíveis para estudantes
- **Microsoft Learn:** Caminhos de aprendizagem suplementares ligados ao longo do curso
- **Binder:** Gratuito, mas com recursos limitados e algumas restrições de rede

### Opções de Execução de Código

1. **Local (Recomendado):** Controle total, melhor desempenho, suporte a GPU
2. **GitHub Codespaces:** VS Code baseado na nuvem, bom para acesso rápido
3. **Binder:** Jupyter baseado no navegador, gratuito mas limitado
4. **Azure ML Notebooks:** Opção empresarial com suporte a GPU
5. **Google Colab:** Carregue os notebooks individualmente, disponível nível gratuito de GPU

### Trabalhar com Notebooks

- Os notebooks foram projetados para serem executados célula por célula para aprendizagem
- Muitos notebooks fazem download de datasets na primeira execução (pode demorar)
- Alguns modelos requerem GPU para tempos de treino razoáveis
- Modelos pré-treinados são usados sempre que possível para reduzir requisitos de computação

### Considerações de Desempenho

- Lições posteriores de visão computacional (CNNs, GANs) beneficiam de GPU
- Lições de transformers em NLP podem exigir RAM significativa
- Treinar do zero é educativo, mas demorado
- Exemplos de aprendizagem por transferência minimizam o tempo de treino

---

**Aviso**:  
Este documento foi traduzido utilizando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos para garantir a precisão, esteja ciente de que traduções automáticas podem conter erros ou imprecisões. O documento original na sua língua nativa deve ser considerado a fonte autoritária. Para informações críticas, recomenda-se uma tradução profissional realizada por humanos. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas decorrentes do uso desta tradução.