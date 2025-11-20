from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import pandas as pd

# Încarcă Iris Dataset
iris = load_iris()
X = pd.DataFrame(iris.data, columns=iris.feature_names)
y = iris.target

# Split train/test
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Lista de parametri pentru test
n_estimators_list = [10, 50, 100, 200]
max_features_list = ['sqrt', 'log2', None]

# Experimentează toate combinațiile
for n in n_estimators_list:
    for mf in max_features_list:
        model = RandomForestClassifier(n_estimators=n, max_features=mf, random_state=42)
        model.fit(X_train, y_train)
        y_pred = model.predict(X_test)
        acc = accuracy_score(y_test, y_pred)
        print(f"n_estimators={n}, max_features={mf}, Accuracy={acc:.3f}")
