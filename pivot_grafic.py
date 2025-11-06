import pandas as pd
import matplotlib.pyplot as plt

# 1️⃣ Citim datele
df = pd.read_csv("student.csv")

# 2️⃣ Pivot table: media și numărul de studenți pe vârstă
pivot = df.pivot_table(index="Varsta", values="Nota", aggfunc=["mean", "count"])

print("\n=== Pivot table ===")
print(pivot)

# 3️⃣ Grafic: Media notelor pe vârstă
plt.figure(figsize=(6, 4))
pivot["mean"].plot(kind="bar", color="skyblue", edgecolor="black")
plt.title("Media notelor pe vârstă")
plt.xlabel("Vârstă")
plt.ylabel("Notă medie")
plt.xticks(rotation=0)
plt.tight_layout()

# 4️⃣ Salvăm graficul ca imagine
plt.savefig("pivot_grafic.png")
plt.show()  # afișăm graficul pe ecran
