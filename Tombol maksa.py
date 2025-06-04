import tkinter as tk
import random

def ya_clicked():
    label.config(text="Yay! Aku juga suka kamu!")

def tidak_clicked(event):
    # Fungsi untuk membuat tombol "Tidak" menghindar
    x = random.randint(50, 350)
    y = random.randint(50, 250)
    tombol_tidak.place(x=x, y=y)

# Membuat jendela utama
jendela = tk.Tk()
jendela.title("Pertanyaan Penting")
jendela.geometry("400x300")

# Label pertanyaan
label = tk.Label(jendela, text="Apakah kamu menyukaiku?", font=("Arial", 14))
label.pack(pady=20)

# Tombol "Ya"
tombol_ya = tk.Button(jendela, text="Ya", command=ya_clicked, padx=20, pady=10)
tombol_ya.place(x=100, y=100)

# Tombol "Tidak"
tombol_tidak = tk.Button(jendela, text="Tidak", padx=20, pady=10)
tombol_tidak.place(x=200, y=100)
tombol_tidak.bind("<Enter>", tidak_clicked)  # Memanggil fungsi saat kursor masuk

jendela.mainloop()
