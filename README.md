# Sistema Antifraude com Machine Learning

Este projeto desenvolve um sistema antifraude baseado em dados de transações financeiras. Inicialmente prototipado no **Google Colab**, foi posteriormente adaptado para execução **local**, com um servidor Flask expondo o modelo via API.

---

## Etapas do Projeto

- Exploração e pré-processamento de dados no Google Colab
- Treinamento e validação do modelo com Scikit-learn
- Salvamento do modelo (`modelo_antifraude.pkl`)
- Deploy local com Flask usando `main.py` e ambiente virtual Python
- Criação do arquivo `.gitignore` com [Toptal Gitignore Generator](https://www.toptal.com/developers/gitignore)

---

## Tecnologias Utilizadas

- Python 3.x
- Pandas
- Scikit-learn
- Flask
- Pickle
- Google Colab
- Ambiente virtual Python (venv)

---

## Estrutura do Projeto

```
Anti-Fraude---Case-Solucion/
├── transactional-sample.csv         # Base de dados de transações
├── main.py                          # Código principal com Flask
├── modelo_antifraude.pkl            # Modelo salvo (gerado após treinamento)  
├── .gitignore                       # Gerado com https://www.toptal.com/developers/gitignore
└── README.md                        # Este arquivo
```

---

## Como Executar Localmente

### 1. Crie um ambiente virtual

```bash
python -m venv .venv
```

### 2. Ative o ambiente

**Windows:**
```powershell
.venv\Scripts\Activate.ps1
```

**Linux/Mac:**
```bash
source .venv/bin/activate
```

### 3. Instale as dependências

```bash
pip install -r requirements.txt
```

### 4. Execute o servidor Flask

```bash
python main.py
```

A aplicação estará disponível em `http://127.0.0.1:5000`.

---

## Testando a API

### Endpoint de predição:

```
POST http://127.0.0.1:5000/predict
```

### Exemplo de JSON de entrada:

```json
{
  "transaction_amount": 100.0,
  "user_id": 1234,
  "transaction_type": "credit"
}
```

### Resposta esperada:

```json
{
  "is_fraud": false
}
```

---

## Desempenho do Modelo

Durante os testes, o modelo atingiu:

```
ROC AUC Score: 1.0
```

Esse valor indica um alto poder discriminativo nos dados usados. Para uso real, recomenda-se testes com bases externas para validação mais robusta.

---

## Observações

- O modelo (`modelo_antifraude.pkl`) é gerado automaticamente se não existir.
- O uso inicial foi no **Google Colab**, o que facilitou o protótipo antes de migrar para produção local.
- O arquivo `.py` (`main.py`) foi criado para permitir execução com Flask fora do Colab.
- O `.gitignore` foi gerado usando o [Toptal Gitignore Generator](https://www.toptal.com/developers/gitignore) para evitar versionamento de arquivos como `.venv`, `.pkl`, entre outros.

---

## Autor

Desenvolvido por **Jackson Tenorio** – Projeto de detecção de fraudes com machine learning.
