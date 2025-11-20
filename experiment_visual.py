from sklearn.datasets import load_wine
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Încarcă datele Wine
wine = load_wine()
X = pd.DataFrame(wine.data, columns=wine.feature_names)
y = wine.target

# Split train/test
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Lista de parametri pentru comparatie
n_estimators_list = [10, 50, 100]
max_features_list = ['sqrt', None]

# Setare culoare pentru grafic
colors = ['skyblue', 'salmon', 'lightgreen']

# Experimentează toate combinațiile și vizualizează importanța feature-urilor
for mf in max_features_list:
    plt.figure(figsize=(12,6))
    for i, n in enumerate(n_estimators_list):
        model = RandomForestClassifier(n_estimators=n, max_features=mf, random_state=42)
        model.fit(X_train, y_train)
        y_pred = model.predict(X_test)
        acc = accuracy_score(y_test, y_pred)
        importances = model.feature_importances_
        sorted_idx = importances.argsort()[::-1]

        plt.bar(
            np.arange(len(importances)) + i*0.25, 
            importances[sorted_idx], 
            width=0.25, 
            color=colors[i], 
            label=f"n_estimators={n}, Accuracy={acc:.3f}"
        )

    plt.xticks(np.arange(len(importances)) + 0.25, X.columns[sorted_idx], rotation=90)
    plt.title(f"Importanța feature-urilor (max_features={mf})")
    plt.legend()
    plt.show()
