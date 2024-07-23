import tkinter as tk
from tkinter import messagebox
import random

class Game:
    def __init__(self, word_list):
        self.words = word_list
        self.secret_word = random.choice(self.words)
        self.guesses = []

    def check_guess(self, guess):
        self.guesses.append(guess)
        feedback = ""
        for i in range(len(self.secret_word)):
            if guess[i] == self.secret_word[i]:
                feedback += "✔"
            elif guess[i] in self.secret_word:
                feedback += "○"
            else:
                feedback += "❌"
        return feedback

class GuessWordApp:
    def __init__(self, master, game):
        self.master = master
        self.master.title("Adivina la palabra de 5 letras")
        self.master.configure(bg="#222222")  # Fondo oscuro
        self.game = game

        self.create_widgets()

    def create_widgets(self):
        self.label = tk.Label(self.master, text="Introduce una palabra de 5 letras:", font=("Arial", 12), bg="#222222", fg="white")
        self.label.grid(row=0, column=0, columnspan=5, pady=10)

        self.entries = []
        for i in range(5):
            entry = tk.Entry(self.master, width=3, font=("Arial", 14), justify="center")
            entry.grid(row=1, column=i, padx=5, pady=5)
            entry.config(bg="#333333", fg="#fafafa", insertbackground="white")
            self.entries.append(entry)

        self.button = tk.Button(self.master, text="Adivinar", command=self.check_guess, font=("Arial", 12), bg="#007bff", fg="white")
        self.button.grid(row=2, column=0, columnspan=5, pady=10)

        for i in range(3):  # 3 filas
            self.master.grid_rowconfigure(i, weight=1)
        for i in range(5):  # 5 columnas
            self.master.grid_columnconfigure(i, weight=1)

    def check_guess(self):
        guess = ''.join(entry.get().lower() for entry in self.entries)

        if len(guess) != 5:
            messagebox.showwarning("Error", "Por favor introduce una palabra de 5 letras.")
            return

        feedback = self.game.check_guess(guess)

        self.update_entry_colors(feedback)

        #messagebox.showinfo("Feedback", feedback)

    def update_entry_colors(self, feedback):
        for i, char in enumerate(feedback):
            if char == "✔":
                self.entries[i].config(bg="#28a745")  # Verde
            elif char == "○":
                self.entries[i].config(bg="#ffc107")  # Amarillo
            elif char == "❌":
                self.entries[i].config(bg="#dc3545")  # Rojo







words = ['papel', 'pazos', 'manos', 'grano', 'plata', 'fuego', 'dedos', 'rosas', 'coraz', 'tiros']
game = Game(words)

root = tk.Tk()
root.geometry("400x150")
app = GuessWordApp(root, game)
root.mainloop()
