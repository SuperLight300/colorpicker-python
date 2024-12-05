from tkinter import *
from tkinter import ttk
import random
import time

start_time = time.time()
best_time = None

COLORS = ["piros", "zöld", "kék", "sárga", "narancs", "lila", "rózsaszín", "barna", "fekete", "fehér"]

COLORS_dict = {
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

root = Tk()
root.title("Színválasztó")

def next_round():
    global last_time, best_time, start_time, rnd_clr_hu, rnd_text, rnd_clr, clr_amnt
    start_time = time.time()
    rnd_clr_hu = COLORS[random.randint(0, int(clr_amnt.get())-1)]
    rnd_text = COLORS[random.randint(0, int(clr_amnt.get())-1)]
    rnd_clr = COLORS_dict[rnd_clr_hu]
    clr_lbl.config(text=rnd_text, fg=rnd_clr)
    result_inpt.delete(0, END)

def main(event):
    global last_time, best_time, start_time
    last_time = time.time() - start_time
    user_inpt = result_inpt.get().strip().lower()
    correct = rnd_clr_hu
    if user_inpt == correct:
        prev_lbl.config(text=f"Előző idő: {last_time:.2f}")
        if best_time is None or last_time < best_time:
            best_time = last_time
            best_lbl.config(text=f"Legjobb idő: {last_time:.2f}")
        fbck_lbl.config(text="Helyes!", fg="green")
        next_round()
    else:
        fbck_lbl.config(text="Helytelen!", fg="red")


rnd_clr_hu = COLORS[random.randint(0, 3)]
rnd_text = COLORS[random.randint(0, 3)]
rnd_clr = COLORS_dict[rnd_clr_hu]

clr_lbl = Label(root, font=("Helvetica", 26))
clr_lbl.config(text=rnd_text, fg=rnd_clr)
result_inpt = Entry(root, width=20, font=("Arial", 24))
prev_lbl = Label(root, text="Előző idő: --", font=("Arial", 18), pady=10)
best_lbl = Label(root, text="Legjobb idő: --", font=("Arial", 18))
fbck_lbl = Label(root, font=("Arial", 14), pady=10)
clr_amnt = StringVar()
dropdown = ttk.Combobox(root, textvariable=clr_amnt, values=list(range(1, 11)), state="readonly")
dropdown.set(4)

clr_lbl.grid(column=0, row=0)
result_inpt.grid(column=0, row=1)
prev_lbl.grid(column=0, row=2)
best_lbl.grid(column=0, row=3)
fbck_lbl.grid(column=0, row=4)
dropdown.grid(column=0, row=5)
result_inpt.bind("<Return>", main)

root.mainloop()