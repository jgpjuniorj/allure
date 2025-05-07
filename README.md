# 🧪 Allure Reports com Histórico por Ambiente (QC, UAT, PRD)

Este projeto automatiza a execução de testes com **pytest** e **Allure**, mantendo o histórico de execuções e publicando relatórios em um bucket **AWS S3** com hospedagem estática. Ele suporta múltiplos ambientes (QC, UAT, PRD) e fornece um painel centralizado para acesso aos relatórios.

---

## 📁 Estrutura do Projeto

.
├── tests/ # Diretório com os testes
├── conftest.py # Configuração do pytest
├── requirements.txt # Dependências do projeto
├── .github/
│ └── workflows/
│ └── allure-report.yml # Workflow do GitHub Actions
├── index.html # Painel central com links para os relatórios
└── README.md # Este arquivo

yaml
Copiar
Editar

---

## 🌐 Estrutura no AWS S3

Configure seu bucket S3 com a seguinte estrutura:

s3://estatico-jj/
├── index.html # Painel central
├── QC/
│ ├── index.html # Relatório do ambiente QC
│ └── history/ # Histórico do ambiente QC
├── UAT/
│ ├── index.html # Relatório do ambiente UAT
│ └── history/ # Histórico do ambiente UAT
└── PRD/
├── index.html # Relatório do ambiente PRD
└── history/ # Histórico do ambiente PRD

yaml
Copiar
Editar

---

## ⚙️ Configuração do Ambiente

### 1. Instalar Dependências

Instale as dependências necessárias:

```bash
pip install -r requirements.txt
2. Instalar o Allure Commandline
Siga as instruções oficiais para instalar o Allure CLI: Allure Installation Guide

🧪 Executando Testes Localmente
Para executar os testes e gerar o relatório Allure com histórico:

bash
Copiar
Editar
# Executar os testes
pytest tests/ --alluredir=allure-results --env QC

# Copiar o histórico anterior (se existir)
cp -r allure-report/history allure-results/history

# Gerar o relatório Allure
allure generate allure-results --clean -o allure-report

# Abrir o relatório no navegador
allure open allure-report
🤖 Integração com GitHub Actions
O workflow do GitHub Actions (.github/workflows/allure-report.yml) automatiza:

Execução dos testes para cada ambiente (QC, UAT, PRD)

Manutenção do histórico de execuções

Geração do relatório Allure

Publicação do relatório e histórico no AWS S3

Variáveis de Ambiente Necessárias
Configure as seguintes variáveis de ambiente no GitHub Secrets:

AWS_ACCESS_KEY_ID

AWS_SECRET_ACCESS_KEY

AWS_DEFAULT_REGION

📊 Visualizando o Histórico
No relatório Allure:

Acesse a aba "History" para visualizar o histórico de execuções de cada teste.

Acesse a aba "Overview" para visualizar gráficos de tendências, como o número de testes passados, falhados e com erro ao longo do tempo.

🖥️ Painel Central
O arquivo index.html na raiz do bucket S3 fornece um painel centralizado com links para os relatórios de cada ambiente:

html
Copiar
Editar
<!DOCTYPE html>
<html lang="pt-BR">
<head>
  <meta charset="UTF-8">
  <title>Painel de Relatórios Allure</title>
</head>
<body>
  <h1>Painel de Relatórios Allure</h1>
  <ul>
    <li><a href="/QC/index.html">Relatório QC</a></li>
    <li><a href="/UAT/index.html">Relatório UAT</a></li>
    <li><a href="/PRD/index.html">Relatório PRD</a></li>
  </ul>
</body>
</html>
🧹 Manutenção do Histórico
O Allure mantém até 20 execuções anteriores no histórico. Certifique-se de:

Copiar a pasta history do relatório anterior para allure-results/history antes de gerar um novo relatório.

Sincronizar a pasta history atualizada de volta para o S3 após a geração do relatório.

📄 Referências
Documentação Oficial do Allure

Allure Report com Histórico no AWS S3

Integração do Allure com GitHub Actions

Para mais informações ou dúvidas, sinta-se à vontade para abrir uma issue ou entrar em contato.

yaml
Copiar
Editar

---

### ✅ Dicas para Visualização no GitHub

- **Preview no VS Code**: Utilize a extensão "Markdown Preview Enhanced" ou pressione `Ctrl+Shift+V` para visualizar o README formatado.
- **Preview no GitHub**: Ao subir o arquivo para o repositório, o GitHub renderizará automaticamente o Markdown, mantendo a aparência organizada.

Se precisar de mais assistência ou ajustes específicos, estou à disposição para ajudar!
::contentReference[oaicite:0]{index=0}
 