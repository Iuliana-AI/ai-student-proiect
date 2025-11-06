import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Citim datele
df = pd.read_csv("student_data.csv")

# Alegem doar variabilele relevante
X = df[["Timp_studiu"]]
y = df["Nota"]

# Creăm și antrenăm modelul
model = LinearRegression()
model.fit(X, y)

# Facem predicții
y_pred = model.predict(X)

# === VIZUALIZARE ===
plt.figure(figsize=(8, 5))
plt.scatter(X, y, color="blue", label="Date reale (observații)")
plt.plot(X, y_pred, color="red", linewidth=2, label="Linia modelului (predicție)")

plt.title("📊 Relația dintre timpul de studiu și notă")
plt.xlabel("Timp de studiu (ore/zi)")
plt.ylabel("Nota obținută")
plt.legend()
plt.grid(True)
plt.show()
