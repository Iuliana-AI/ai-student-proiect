import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
from datetime import datetime
import os

# === 1️⃣ Citim datele ===
df = pd.read_csv("student.csv")

# === 2️⃣ Creăm pivot table: media și numărul de studenți pe vârstă ===
pivot = df.pivot_table(index="Varsta", values="Nota", aggfunc=["mean", "count"])

# === 3️⃣ Creăm fișier PDF cu dată în nume ===
nume_pdf = datetime.now().strftime("raport_pivot_%Y%m%d_%H%M%S.pdf")

with PdfPages(nume_pdf) as pdf:
    # --- Pagina 1: Introducere ---
    plt.figure(figsize=(8.5, 6))
    plt.axis("off")
    plt.text(
        0.5,
        0.8,
        "📘 RAPORT PIVOT STUDENȚI",
        ha="center",
        va="center",
        fontsize=20,
        fontweight="bold",
    )
    plt.text(
        0.5,
        0.6,
        f"Data generării: {datetime.now().strftime('%d %B %Y, %H:%M')}",
        ha="center",
        va="center",
        fontsize=12,
    )
    plt.text(
        0.5,
        0.5,
        f"Număr total de studenți: {len(df)}",
        ha="center",
        va="center",
        fontsize=14,
    )
    plt.text(0.5, 0.35, "Acest raport conține:", ha="center", va="center", fontsize=12)
    plt.text(
        0.5,
        0.25,
        "• Pivot table: media și număr studenți pe vârstă\n• Grafice generate automat",
        ha="center",
        va="center",
        fontsize=12,
    )
    pdf.savefig()
    plt.close()

    # --- Pagina 2: Grafic media notelor pe vârstă ---
    plt.figure(figsize=(6, 4))
    pivot["mean"].plot(kind="bar", color="skyblue", edgecolor="black")
    plt.title("Media notelor pe vârstă")
    plt.xlabel("Vârstă")
    plt.ylabel("Notă medie")
    plt.xticks(rotation=0)
    plt.tight_layout()
    pdf.savefig()
    plt.close()

    # --- Pagina 3: Grafic număr studenți pe vârstă ---
    plt.figure(figsize=(6, 4))
    pivot["count"].plot(kind="bar", color="lightgreen", edgecolor="black")
    plt.title("Numărul de studenți pe vârstă")
    plt.xlabel("Vârstă")
    plt.ylabel("Număr studenți")
    plt.xticks(rotation=0)
    plt.tight_layout()
    pdf.savefig()
    plt.close()

print(f"✅ Raportul pivot complet a fost generat: {nume_pdf}")

# --- Deschidem automat PDF-ul ---
os.system(f"open {nume_pdf}")
