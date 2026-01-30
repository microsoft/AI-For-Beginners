# Questionários

Estes questionários são os questionários pré e pós-aula para o currículo de IA em https://aka.ms/ai-beginners

## Adicionar um conjunto de questionários traduzidos

Adicione uma tradução de questionário criando estruturas de questionários correspondentes nas pastas `assets/translations`. Os questionários originais estão em `assets/translations/en`. Os questionários estão divididos em vários grupos por lição. Certifique-se de alinhar a numeração com a secção correta do questionário. Existem 40 questionários no total neste currículo, começando a contagem em 0.

Depois de editar as traduções, edite o ficheiro index.js na pasta de tradução para importar todos os ficheiros seguindo as convenções em `en`.

Edite o ficheiro `index.js` em `assets/translations` para importar os novos ficheiros traduzidos.

De seguida, edite o menu suspenso em `App.vue` nesta aplicação para adicionar o seu idioma. Combine a abreviatura localizada com o nome da pasta do seu idioma.

Por fim, edite todos os links dos questionários nas lições traduzidas, se existirem, para incluir esta localização como um parâmetro de consulta: `?loc=fr`, por exemplo.

## Configuração do projeto

```
npm install
```

### Compilar e recarregar automaticamente para desenvolvimento

```
npm run serve
```

### Compilar e minimizar para produção

```
npm run build
```

### Verificar e corrigir ficheiros

```
npm run lint
```

### Personalizar configuração

Consulte [Referência de Configuração](https://cli.vuejs.org/config/).

Créditos: Agradecimentos à versão original desta aplicação de questionários: https://github.com/arpan45/simple-quiz-vue

## Implementar no Azure

Aqui está um guia passo a passo para o ajudar a começar:

1. Faça um fork do repositório GitHub  
Certifique-se de que o código da sua aplicação web estático está no seu repositório GitHub. Faça um fork deste repositório.

2. Crie uma Aplicação Web Estática no Azure  
- Crie uma [conta Azure](http://azure.microsoft.com)  
- Aceda ao [portal do Azure](https://portal.azure.com)  
- Clique em “Criar um recurso” e procure por “Aplicação Web Estática”.  
- Clique em “Criar”.  

3. Configure a Aplicação Web Estática  
- Básico:  
  - Subscrição: Selecione a sua subscrição do Azure.  
  - Grupo de Recursos: Crie um novo grupo de recursos ou utilize um existente.  
  - Nome: Forneça um nome para a sua aplicação web estática.  
  - Região: Escolha a região mais próxima dos seus utilizadores.  

- #### Detalhes de Implementação:  
  - Fonte: Selecione “GitHub”.  
  - Conta GitHub: Autorize o Azure a aceder à sua conta GitHub.  
  - Organização: Selecione a sua organização GitHub.  
  - Repositório: Escolha o repositório que contém a sua aplicação web estática.  
  - Ramo: Selecione o ramo a partir do qual deseja implementar.  

- #### Detalhes de Construção:  
  - Predefinições de Construção: Escolha o framework com o qual a sua aplicação foi construída (por exemplo, React, Angular, Vue, etc.).  
  - Localização da Aplicação: Especifique a pasta que contém o código da sua aplicação (por exemplo, / se estiver na raiz).  
  - Localização da API: Se tiver uma API, especifique a sua localização (opcional).  
  - Localização de Saída: Especifique a pasta onde a saída da construção é gerada (por exemplo, build ou dist).  

4. Rever e Criar  
Revise as suas definições e clique em “Criar”. O Azure configurará os recursos necessários e criará um ficheiro de workflow do GitHub Actions no seu repositório.

5. Workflow do GitHub Actions  
O Azure criará automaticamente um ficheiro de workflow do GitHub Actions no seu repositório (.github/workflows/azure-static-web-apps-<name>.yml). Este workflow irá gerir o processo de construção e implementação.

6. Monitorizar a Implementação  
Aceda ao separador “Actions” no seu repositório GitHub.  
Deverá ver um workflow em execução. Este workflow irá construir e implementar a sua aplicação web estática no Azure.  
Assim que o workflow for concluído, a sua aplicação estará ativa no URL fornecido pelo Azure.

### Exemplo de Ficheiro de Workflow

Aqui está um exemplo de como poderá ser o ficheiro de workflow do GitHub Actions:  
name: Azure Static Web Apps CI/CD  
```
on:
  push:
    branches:
      - main
  pull_request:
    types: [opened, synchronize, reopened, closed]
    branches:
      - main

jobs:
  build_and_deploy_job:
    runs-on: ubuntu-latest
    name: Build and Deploy Job
    steps:
      - uses: actions/checkout@v2
      - name: Build And Deploy
        id: builddeploy
        uses: Azure/static-web-apps-deploy@v1
        with:
          azure_static_web_apps_api_token: ${{ secrets.AZURE_STATIC_WEB_APPS_API_TOKEN }}
          repo_token: ${{ secrets.GITHUB_TOKEN }}
          action: "upload"
          app_location: "etc/quiz-app # App source code path"
          api_location: ""API source code path optional
          output_location: "dist" #Built app content directory - optional
```

### Recursos Adicionais  
- [Documentação de Aplicações Web Estáticas do Azure](https://learn.microsoft.com/azure/static-web-apps/getting-started)  
- [Documentação do GitHub Actions](https://docs.github.com/actions/use-cases-and-examples/deploying/deploying-to-azure-static-web-app)  

**Aviso Legal**:  
Este documento foi traduzido utilizando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos pela precisão, esteja ciente de que traduções automáticas podem conter erros ou imprecisões. O documento original na sua língua nativa deve ser considerado a fonte autoritária. Para informações críticas, recomenda-se a tradução profissional realizada por humanos. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas decorrentes do uso desta tradução.