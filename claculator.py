import tkinter as tk
import math
def click(x):
    entry.insert(tk.END, x)
def clac():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, result)
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")
def clear():
    entry.delete(0, tk.END)
def backspace():
    entry.delete(len(entry.get()) - 1, tk.END)
def sin_fun():
    value = float(entry.get())
    result = math.sin(math.radians(value))
    entry.delete(0, tk.END) 
    entry.insert(tk.END, result)
def cos_fun():
    value = float(entry.get())
    result = math.cos(math.radians(value))
    entry.delete(0, tk.END) 
    entry.insert(tk.END, result)
def tan_fun():
    value = float(entry.get())
    result = math.tan(math.radians(value))
    entry.delete(0, tk.END) 
    entry.insert(tk.END, result)
root = tk.Tk()
root.title("Calculator")
root.configure(bg="black")
#root.geometry("500x600")
root.resizable(False, False)
#root.resizable(True, True)
entry = tk.Entry(
    root,
    font=("Arial", 24),
    bg="black",
    fg="white",
    bd=2,
    justify="right"
)
entry.grid(row=0, column=0, columnspan=7, padx=2, pady=2, ipady=10,ipadx=10)
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+'
]
r = 1
c = 0
for b in buttons:
    cmd = clac if b == '=' else lambda x=b: click(x)
    tk.Button(
        root,
        text=b,
        command=cmd,
        font=("Arial", 18),
        bg ="yellow" if b in "+-*/=" else "gray90",
        bd=0,
        width=4,
        height=2
    ).grid(row=r, column=c, padx=2, pady=2)

    c += 1
    if c == 4:
        c = 0
        r += 1
tk.Button(
    root,
    text='C',
    command=clear,
    font=("Arial", 18),
    bg="red",
    fg="white",
    bd=0,
    width=5,
    height=2,
    justify="right"
).grid(row=r, column=0, columnspan=1, padx=2, pady=2)

tk.Button(
    root,
    text='BS',
    command=backspace,
    font=("Arial", 18),
    bg="orange",
    fg="black",
    bd=0,
    width=5,
    height=2,
    justify="right"
).grid(row=r, column=2, columnspan=1, padx=2, pady=2)
tk.Button(root, text="sin", command=sin_fun,bg="lightblue",
          font=("Arial", 16), width=4).grid(row=1, column=5, columnspan=4, padx=2, pady=2, ipady=10)

tk.Button(root, text="cos", command=cos_fun,bg="lightblue",
          font=("Arial", 16), width=4).grid(row=2, column=5, columnspan=4, padx=2, pady=2, ipady=10)

tk.Button(root, text="tan", command=tan_fun,bg="lightblue",
          font=("Arial", 16), width=4).grid(row=3, column=5, columnspan=4, padx=2, pady=2, ipady=10)
root.mainloop()
