
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from joblib import dump

dados = pd.read_csv("dados/jogos.csv")

X = dados[["media_gols_casa", "media_gols_fora", "forma_casa", "forma_fora"]]
y = dados["resultado"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
modelo = RandomForestClassifier()
modelo.fit(X_train, y_train)

dump(modelo, "modelos/preditivo.pkl")
