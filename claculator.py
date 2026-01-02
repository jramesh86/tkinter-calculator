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
    entry.delete(0, tk.END)
    entry.insert(0, math.sin(math.radians(value)))

def cos_fun():
    value = float(entry.get())
    entry.delete(0, tk.END)
    entry.insert(0, math.cos(math.radians(value)))

def tan_fun():
    value = float(entry.get())
    entry.delete(0, tk.END)
    entry.insert(0, math.tan(math.radians(value)))

def sqrt_fun():
    value = float(entry.get())
    entry.delete(0, tk.END)
    entry.insert(0, math.sqrt(value))

def cube_root():
    value = float(entry.get())
    entry.delete(0, tk.END)
    entry.insert(0, value ** (1/3))

def square():
    value = float(entry.get())
    entry.delete(0, tk.END)
    entry.insert(0, value ** 2)

def cube():
    value = float(entry.get())
    entry.delete(0, tk.END)
    entry.insert(0, value ** 3)

def log_fun():
    value = float(entry.get())
    entry.delete(0, tk.END)
    entry.insert(0, math.log10(value))

def ln_fun():
    value = float(entry.get())
    entry.delete(0, tk.END)
    entry.insert(0, math.log(value))

def pi_fun():
    entry.insert(tk.END, math.pi)

root = tk.Tk()
root.title("Advanced Calculator")
root.configure(bg="#1e1e1e")
root.resizable(False, False)

entry = tk.Entry(
    root,
    font=("Consolas", 24),
    bg="#000000",
    fg="#00ffcc",
    bd=3,
    justify="right"
)
entry.grid(row=0, column=0, columnspan=8, padx=5, pady=5, ipady=10)

buttons = [
    '7','8','9','/',
    '4','5','6','*',
    '1','2','3','-',
    '0','.','=','+'
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
        bg="#ffcc00" if b in "+-*/=" else "#444444",
        fg="black" if b in "+-*/=" else "white",
        width=4,
        height=2,
        bd=0
    ).grid(row=r, column=c, padx=2, pady=2)

    c += 1
    if c == 4:
        c = 0
        r += 1

tk.Button(root, text="C", command=clear,
          bg="#ff4444", fg="white",
          font=("Arial", 16), width=4).grid(row=5, column=0, padx=2, pady=2)

tk.Button(root, text="BS", command=backspace,
          bg="#ff8800", fg="black",
          font=("Arial", 16), width=4).grid(row=5, column=1, padx=2, pady=2)

tk.Button(root, text="sin", command=sin_fun,
          bg="#00bfff", font=("Arial", 14), width=4).grid(row=1, column=5)

tk.Button(root, text="cos", command=cos_fun,
          bg="#00bfff", font=("Arial", 14), width=4).grid(row=2, column=5)

tk.Button(root, text="tan", command=tan_fun,
          bg="#00bfff", font=("Arial", 14), width=4).grid(row=3, column=5)

tk.Button(root, text="√", command=sqrt_fun,
          bg="#66ff66", font=("Arial", 14), width=4).grid(row=1, column=6)

tk.Button(root, text="∛", command=cube_root,
          bg="#66ff66", font=("Arial", 14), width=4).grid(row=2, column=6)

tk.Button(root, text="x²", command=square,
          bg="#66ff66", font=("Arial", 14), width=4).grid(row=3, column=6)

tk.Button(root, text="x³", command=cube,
          bg="#66ff66", font=("Arial", 14), width=4).grid(row=4, column=6)

tk.Button(root, text="log", command=log_fun,
          bg="#cc99ff", font=("Arial", 14), width=4).grid(row=1, column=7)

tk.Button(root, text="ln", command=ln_fun,
          bg="#cc99ff", font=("Arial", 14), width=4).grid(row=2, column=7)

tk.Button(root, text="π", command=pi_fun,
          bg="#cc99ff", font=("Arial", 14), width=4).grid(row=3, column=7)

root.mainloop()
