import pandas as pd
import matplotlib.pyplot as plt

# 1. Citim datele din CSV
df = pd.read_csv("student.csv")

# 2. Afișăm tabelul pentru confirmare
print("\nDatele din CSV:")
print(df)

# 3. Creăm un grafic cu bare pentru nume și note
plt.figure(figsize=(8, 5))
plt.bar(df["Nume"], df["Nota"], color="skyblue", edgecolor="black")

# 4. Adăugăm titlu și etichete
plt.title("Notele studenților", fontsize=14, fontweight="bold")
plt.xlabel("Nume student")
plt.ylabel("Nota")

# 5. Salvăm graficul ca imagine
plt.tight_layout()
plt.savefig("note_stud.png")
print("\n✅ Grafic salvat ca 'note_stud.png' în folderul curent!")
