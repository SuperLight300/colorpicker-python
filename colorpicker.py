import tkinter as tk
from tkinter import ttk
import random
import time

COLORS = {
    'piros': 'red',
    'zöld': 'green',
    'kék': 'blue',
    'sárga': 'yellow',
    'narancs': 'orange',
    'lila': 'purple',
    'rózsaszín': 'pink',
    'barna': 'brown',
    'fekete': 'black',
    'fehér': 'white'
}
COLOR_NAMES = list(COLORS.keys())

class ColorGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Színválasztó játék")
        
        self.start_time = 0
        self.best_time = None
        self.current_color = ""
        self.current_word = ""
        self.colors_to_use = COLOR_NAMES[:4]
        self.num_colors = tk.IntVar(value=4)
        
        self.setup_ui()
        self.next_round()
    
    def setup_ui(self):
        self.color_label = tk.Label(self.root, text="", font=("Arial", 24))
        self.color_label.grid(row=0, column=0, columnspan=2, pady=10)
        
        self.entry = tk.Entry(self.root, font=("Arial", 16))
        self.entry.grid(row=1, column=0, columnspan=2, pady=10)
        self.entry.bind("<Return>", self.check_answer)
        
        self.time_label = tk.Label(self.root, text="Eltelt idő: 0.00 s", font=("Arial", 14))
        self.time_label.grid(row=2, column=0, pady=10)
        
        self.best_label = tk.Label(self.root, text="Legjobb idő: --", font=("Arial", 14))
        self.best_label.grid(row=2, column=1, pady=10)
        
        self.feedback_label = tk.Label(self.root, text="", font=("Arial", 14), fg="red")
        self.feedback_label.grid(row=3, column=0, columnspan=2, pady=10)
        
        tk.Label(self.root, text="Színek száma:", font=("Arial", 14)).grid(row=4, column=0, pady=10)
        self.color_dropdown = ttk.Combobox(self.root, textvariable=self.num_colors, 
                                           values=list(range(2, len(COLOR_NAMES) + 1)))
        self.color_dropdown.grid(row=4, column=1, pady=10)
        self.color_dropdown.bind("<<ComboboxSelected>>", self.update_colors)
    
    def update_colors(self, event):
        num = self.num_colors.get()
        self.colors_to_use = COLOR_NAMES[:num]
        self.next_round()
    
    def next_round(self):
        self.entry.delete(0, tk.END)
        self.feedback_label.config(text="")
        
        self.current_word = random.choice(self.colors_to_use)
        self.current_color = random.choice(self.colors_to_use)
        
        self.color_label.config(
            text=self.current_word, 
            fg=COLORS[self.current_color]
        )
        
        self.start_time = time.time()
    
    def check_answer(self, event):
        user_input = self.entry.get().strip().lower()
        correct_answer = self.current_color
        
        elapsed_time = time.time() - self.start_time
        
        if user_input == correct_answer:
            self.feedback_label.config(text="Helyes!", fg="green")
            
            self.time_label.config(text=f"Eltelt idő: {elapsed_time:.2f} s")
            
            if self.best_time is None or elapsed_time < self.best_time:
                self.best_time = elapsed_time
                self.best_label.config(text=f"Legjobb idő: {elapsed_time:.2f} s")
            
            self.root.after(1000, self.next_round)
        else:
            self.feedback_label.config(text=f"Helytelen! Helyes válasz: {correct_answer}", fg="red")

if __name__ == "__main__":
    root = tk.Tk()
    game = ColorGame(root)
    root.mainloop()
