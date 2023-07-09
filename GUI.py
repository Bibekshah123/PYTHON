import tkinter as tk

def add_value():
    global total
    try:
        value = float(entry.get())
        total += value
        display_total()
    except ValueError:
        pass

def subtract_value():
    global total
    try:
        value = float(entry.get())
        total -= value
        display_total()
    except ValueError:
        pass

def reset_total():
    global total
    total = 0
    display_total()

def display_total():
    total_label.config(text="Total: {:.2f}".format(total))

total = 0

window = tk.Tk()
window.title("Simple Calculator")

entry = tk.Entry(window, width=10)
add_button = tk.Button(window, text="+", width=5, command=add_value)
subtract_button = tk.Button(window, text="-", width=5, command=subtract_value)
reset_button = tk.Button(window, text="Reset", width=10, command=reset_total)
total_label = tk.Label(window, text="Total: 0.00")

entry.grid(row=0, column=0, padx=5, pady=5)
add_button.grid(row=0, column=1, padx=5, pady=5)
subtract_button.grid(row=0, column=2, padx=5, pady=5)
reset_button.grid(row=1, column=0, columnspan=3, padx=5, pady=5)
total_label.grid(row=2, column=0, columnspan=3, padx=5, pady=5)

window.mainloop()
