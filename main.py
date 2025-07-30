# %% [markdown]
# <a href="https://colab.research.google.com/github/jacksontenorio8/Anti-Faude---Case-Solucion/blob/main/antifraude.ipynb" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>

# %% [markdown]
# 1. Importação de bibliotecas

# %%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import lightgbm as lgb
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix, roc_auc_score, roc_curve
import pickle
from flask import Flask, request, jsonify

# %% [markdown]
# 2. Montar Google Drive

# %%
# from google.colab import drive
# drive.mount('/content/drive')

# %% [markdown]
# 3. Leitura e tratamento de dados

# %%
csv_path = 'C:\\Workspace\\Anti-Faude---Case-Solucion\\transactional-sample.csv'
df = pd.read_csv(csv_path)

# Conversão de timestamp
if 'timestamp' in df.columns:
    df['timestamp'] = pd.to_datetime(df['timestamp'])

# Tratamento de nulos
df.fillna(0, inplace=True)

# Conversão de tipos
if 'has_cbk' in df.columns:
    df['has_cbk'] = df['has_cbk'].astype(bool)


# %% [markdown]
# 
# 4. Regras simples antifraude

# %%
def regras_simples(df):
    if 'timestamp' in df.columns:
        df['flag_muitas_transacoes'] = df.groupby('user_id')['timestamp'].transform(lambda x: x.diff().dt.total_seconds().fillna(9999) < 10)
    else:
        df['flag_muitas_transacoes'] = False
    df['flag_valor_alto'] = df['transaction_amount'] > 10000
    df['flag_estorno'] = df['has_cbk']
    df['fraude_regra'] = df[['flag_muitas_transacoes', 'flag_valor_alto', 'flag_estorno']].any(axis=1)
    return df

df = regras_simples(df)

# %% [markdown]
# 5. Modelo Supervisionado

# %%
features = ['transaction_amount', 'flag_muitas_transacoes', 'flag_valor_alto', 'flag_estorno']
X = df[features].astype(float)
y = df['fraude_regra'].astype(int)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

model = lgb.LGBMClassifier()
model.fit(X_train, y_train)


# %% [markdown]
# 6. Avaliação do Modelo

# %%
y_pred = model.predict(X_test)
y_proba = model.predict_proba(X_test)[:,1]

print(classification_report(y_test, y_pred))
print("ROC AUC Score:", roc_auc_score(y_test, y_proba))

# Matriz de confusão
sns.heatmap(confusion_matrix(y_test, y_pred), annot=True, fmt='d')
plt.title('Confusion Matrix')
plt.xlabel('Predito')
plt.ylabel('Real')
plt.show()

# ROC Curve
fpr, tpr, _ = roc_curve(y_test, y_proba)
plt.plot(fpr, tpr, label='ROC Curve (area = %0.2f)' % roc_auc_score(y_test, y_proba))
plt.plot([0, 1], [0, 1], 'k--')
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('Receiver Operating Characteristic')
plt.legend(loc="lower right")
plt.show()

# Feature importance
lgb.plot_importance(model)
plt.title("Feature Importance")
plt.show()

# %% [markdown]
# 7. Exportação do modelo

# %%
# salvar o modelo treinado
import pickle

with open('modelo_antifraude.pkl', 'wb') as f:
    pickle.dump(model, f)



# %% [markdown]
# 8. Endpoint RESTful (exemplo)

# %%
#Este código deve ser executado localmente, não no Colab.
from flask import Flask, request, jsonify
import pandas as pd
import pickle

app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json(force=True)
    X_input = pd.DataFrame([data])
    with open('modelo_antifraude.pkl', 'rb') as f:
        model = pickle.load(f)
    prediction = model.predict(X_input)[0]
    return jsonify({'fraude': bool(prediction)})

if __name__ == '__main__':
    app.run(port=5000, debug=True)



