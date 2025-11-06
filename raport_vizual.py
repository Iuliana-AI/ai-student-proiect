import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
from datetime import datetime

# === 1️⃣ Citirea fișierului CSV ===
df = pd.read_csv("student.csv")

# === 2️⃣ Crearea fișierului PDF pentru raport ===
# Creăm numele fișierului cu dată și oră
nume_pdf = datetime.now().strftime("raport_grafic_%Y%m%d_%H%M%S.pdf")
with PdfPages(nume_pdf) as pdf:

    # === Pagina 1: Introducere ===
    plt.figure(figsize=(8.5, 6))
    plt.axis("off")
    plt.text(
        0.5,
        0.8,
        "📘 RAPORT VIZUAL STUDENȚI",
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
        "• Distribuția notelor\n• Media notelor pe vârstă\n• Notele fiecărui student",
        ha="center",
        va="center",
        fontsize=12,
    )
    pdf.savefig()
    plt.close()

    # === Pagina 2: Distribuția notelor ===
    plt.figure()
    df["Nota"].plot(kind="hist", bins=5, color="skyblue", edgecolor="black")
    plt.title("Distribuția Notelor Studenților")
    plt.xlabel("Nota")
    plt.ylabel("Număr Studenți")
    pdf.savefig()
    plt.close()

    # === Pagina 3: Media notelor pe vârstă ===
    plt.figure()
    df.groupby("Varsta")["Nota"].mean().plot(kind="bar", color="lightgreen")
    plt.title("Media Notelor în Funcție de Vârstă")
    plt.xlabel("Vârstă")
    plt.ylabel("Notă Medie")
    pdf.savefig()
    plt.close()

    # === Pagina 4: Notele fiecărui student ===
    plt.figure()
    plt.scatter(df["Varsta"], df["Nota"], color="orange")
    plt.title("Notele Studenților în Funcție de Vârstă")
    plt.xlabel("Vârstă")
    plt.ylabel("Nota")
    pdf.savefig()
    plt.close()

print("✅ Raportul complet a fost generat: raport_grafic.pdf")

import os

os.system(f"open {nume_pdf}")
