# 🧪 Allure Reports com Histórico por Ambiente (QC, UAT, PRD)

Este projeto automatiza a execução de testes com **pytest** e **Allure**, mantendo o histórico de execuções e publicando relatórios em um bucket **AWS S3** com hospedagem estática. Ele suporta múltiplos ambientes (QC, UAT, PRD) e fornece um painel centralizado para acesso aos relatórios.

---

## 📁 Estrutura do Projeto

```bash
.
├── tests/                  # Casos de teste
├── conftest.py            # Configuração do pytest
├── requirements.txt       # Dependências
├── .github/
│   └── workflows/
│       └── allure-report.yml  # Pipeline CI/CD
├── index.html             # Painel central
└── README.md

---

## 🌐 Estrutura no AWS S3

Configure seu bucket S3 com a seguinte estrutura:


s3://estatico-jj/
├── index.html            # Painel principal
├── QC/
│   ├── index.html        # Relatório QC
│   └── history/          # Histórico QC (últimas 20 execuções)
├── UAT/
│   ├── index.html        # Relatório UAT
│   └── history/          # Histórico UAT
└── PRD/
    ├── index.html        # Relatório PRD
    └── history/          # Histórico PRD

---

⚙️ Configuração
1. Instalação de Dependências
bash
pip install -r requirements.txt
2. Allure CLI
Siga o guia oficial de instalação.

🧪 Execução Local
bash
# Executar testes para ambiente QC
pytest tests/ --alluredir=allure-results --env QC

# Preservar histórico
cp -r allure-report/history allure-results/history

# Gerar relatório
allure generate allure-results --clean -o allure-report

# Visualizar relatório
allure open allure-report
🤖 GitHub Actions (.github/workflows/allure-report.yml)
yaml
name: Allure Report

on: [push]

jobs:
  test:
    runs-on: ubuntu-latest
    strategy:
      matrix:
        env: [QC, UAT, PRD]
    
    steps:
    - name: Checkout
      uses: actions/checkout@v3
    
    - name: Setup Python
      uses: actions/setup-python@v4
      with:
        python-version: '3.10'
    
    - name: Install Dependencies
      run: |
        pip install -r requirements.txt
    
    - name: Run Tests
      run: |
        pytest tests/ --alluredir=allure-results --env ${{ matrix.env }}
    
    - name: Upload to S3
      env:
        AWS_ACCESS_KEY_ID: ${{ secrets.AWS_ACCESS_KEY_ID }}
        AWS_SECRET_ACCESS_KEY: ${{ secrets.AWS_SECRET_ACCESS_KEY }}
      run: |
        aws s3 sync allure-report s3://estatico-jj/${{ matrix.env }} --delete
🔒 Variáveis de Ambiente
Configure no GitHub Secrets:

AWS_ACCESS_KEY_ID

AWS_SECRET_ACCESS_KEY

AWS_DEFAULT_REGION

📊 Painel Central (index.html)
html
<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <title>Relatórios Allure</title>
</head>
<body>
    <h1>Ambientes</h1>
    <ul>
        <li><a href="/QC/index.html">QC</a></li>
        <li><a href="/UAT/index.html">UAT</a></li>
        <li><a href="/PRD/index.html">PRD</a></li>
    </ul>
</body>
</html>
📚 Recursos Úteis
Documentação Allure

Configurar Hospedagem S3

GitHub Actions para AWS
