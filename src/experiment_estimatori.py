from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import matplotlib.pyplot as plt

# Încarcă datele
data = load_iris()
X = data.data
y = data.target

# Împărțire train/test
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)

# Lista de estimatori testați
n_list = [1, 5, 10, 20, 50, 100, 200, 300]
accuracies = []

# Rulează experimentul
for n in n_list:
    model = RandomForestClassifier(n_estimators=n, random_state=42)
    model.fit(X_train, y_train)
    acc = model.score(X_test, y_test)
    accuracies.append(acc)
    print(f"n_estimators={n}, Accuracy={acc:.3f}")

# Graficul evoluției acurateții
plt.figure(figsize=(8, 5))
plt.plot(n_list, accuracies, marker="o")
plt.xlabel("Numărul de estimatori (copaci)")
plt.ylabel("Acuratețe")
plt.title("Evoluția acurateții în funcție de numărul de copaci")
plt.grid(True)
plt.savefig("accurate_vs_trees.png")
print("Grafic salvat: accurate_vs_trees.png")
