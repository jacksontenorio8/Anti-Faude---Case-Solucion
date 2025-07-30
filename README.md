# Sistema Antifraude com Machine Learning no Google Colab

Este projeto é um sistema antifraude baseado em transações financeiras, utilizando regras simples e modelos supervisionados de aprendizado de máquina. O projeto foi desenvolvido para ser compatível com o Google Colab e conta com funcionalidades completas, desde a importação dos dados até a exportação de modelo e criação de endpoint.

## Funcionalidades

- Montagem do Google Drive para acesso ao `.csv`
- Carregamento de dados financeiros de transações
- Tratamento de dados e engenharia de features
- Aplicação de regras simples de fraude:
  - Muitas transações em pouco tempo
  - Transações com valores altos
  - Histórico de estorno (chargeback)
- Visualização de dados com gráficos
- Criação de modelos supervisionados:
  - RandomForest
  - XGBoost
  - LightGBM
- Avaliação dos modelos com métricas como:
  - Acurácia
  - Matriz de Confusão
  - Curva ROC e AUC
- Exportação do modelo `.pkl`
- Criação de um endpoint RESTful usando Flask (nota: parte do Flask deve ser executada localmente, pois o Colab não permite execução contínua de servidores)

## Como Usar

1. Faça upload do seu arquivo CSV no Google Drive.
2. Monte seu Google Drive no Colab com:
   ```python
   from google.colab import drive
   drive.mount('/content/drive')
   ```
3. Atualize o caminho do arquivo CSV no notebook:
   ```python
   df = pd.read_csv('/content/drive/MyDrive/seu_arquivo.csv')
   ```
4. Execute o notebook célula por célula.
5. O modelo será exportado como `modelo_fraude.pkl` no seu diretório `/content`.

## Requisitos

- Google Colab
- Python 3.x
- Bibliotecas:
  - pandas
  - numpy
  - matplotlib
  - seaborn
  - scikit-learn
  - xgboost
  - lightgbm
  - joblib
  - flask (para uso local)

## Observações

- A parte final do código, referente à criação do endpoint com Flask, deve ser executada fora do Google Colab, em ambiente local (como Jupyter Notebook ou terminal Python).
- A execução de servidores RESTful não é suportada diretamente pelo Colab.

## Licença

Este projeto está licenciado sob a Licença MIT.
Você é livre para usá-lo, modificá-lo e distribuí-lo com os devidos créditos.

