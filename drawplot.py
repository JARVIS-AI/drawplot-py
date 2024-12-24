import numpy as np
import matplotlib.pyplot as plt
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import io
import sys
import webbrowser

def s(t):
    return np.where(t == 0, 1, 0)

def delta(t):
    return np.where(t == 0, 1, 0)

def exp_decay(t, alpha=1.0):
    return np.exp(-alpha * t) * u(t)

def exp(t, alpha=1.0):
    return np.exp(alpha * t) * u(t)

def e(t, alpha=1.0):
    return np.exp(alpha * t) * u(t)

def e_1(t, alpha=1.0):
    return np.exp(-alpha * t) * u(t)

def sin(t, omega=1.0):
    return np.sin(omega * t)

def cos(t, omega=1.0):
    return np.cos(omega * t)

def u(t):
    return np.where(t >= 0, 1, 0)

def r(t):
    return np.where(t >= 0, t, 0)

def plot_and_save(t_start=-1, t_end=10, str_problem="u(t)", alpha=1.0, omega=1.0):
    t = np.linspace(t_start - 1, t_end, 300)
    problem = eval(str_problem)
    def x(t):
        return problem
    y = x(t)
    plt.plot(t, y, label="x(t)")
    plt.axhline(0, color='black', linewidth=0.5)
    plt.axvline(0, color='black', linewidth=0.5)
    plt.grid(color='gray', linestyle='--', linewidth=0.5)
    plt.title(str_problem)
    plt.xlabel('t')
    plt.ylabel('x(t)')
    plt.legend()
    
    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    img = Image.open(buf)
    plt.clf()
    return img

def show_plot():
    t_start = float(t_start_entry.get())
    t_end = float(t_end_entry.get())
    str_problem = problem_entry.get()
    alpha = float(alpha_entry.get()) if alpha_entry.get() else 1.0
    omega = float(omega_entry.get()) if omega_entry.get() else 1.0
    img = plot_and_save(t_start, t_end, str_problem, alpha, omega)
    img_tk = ImageTk.PhotoImage(img)
    panel.configure(image=img_tk)
    panel.image = img_tk

def on_closing():
    plt.close('all')
    root.destroy()
    sys.exit()

def open_url(event):
    webbrowser.open_new(r"https://t.me/Darker1063")

root = Tk()
root.iconbitmap(r'drawplot.ico')
root.title("رسم نمودار با توابع ویژه توسعه یافته توسط Mr.Hidden - https://t.me/Darker1063 - @Darker1063")
width = int(root.winfo_screenwidth())
height = int(root.winfo_screenheight())
RIGHT_RIGHT = str((int(width) - 800) // 2)
top_down = str((int(height) - 600) // 2)
root.resizable(width=False, height=False)
root.minsize(870, 700)
root.geometry(f"+{RIGHT_RIGHT}+{top_down}")
root.update()

t_start = StringVar(root, -1)
t_end = StringVar(root, 10)
sample_problem = StringVar(root, "u(t)")
alpha_val = StringVar(root, 1.0)
omega_val = StringVar(root, 1.0)

guide_label_1 = Label(root, text="u(t) - r(t) - sin(t، omega) - cos(t، omega) - delta(t) | s(t) - exp_decay(t، alpha) | e_1(t، alpha) - exp(t، alpha) | e(t، alpha) : لیست توابع", anchor='e', justify=RIGHT)
guide_label_2 = Label(root, text="u(t) - r(t-1) + 2*delta(t-2) : صورت مسئله را به این شکل وارد کنید مثال", anchor='e', justify=RIGHT)

guide_label_1.grid(row=0, column=0, columnspan=5, padx=10, pady=2, sticky=E)
guide_label_2.grid(row=1, column=0, columnspan=5, padx=10, pady=2, sticky=E)

t_start_label = Label(root, text=": شروع نمودار از")
t_start_label.grid(row=2, column=4)
t_start_entry = Entry(root, text=t_start, width=20, font=55)
t_start_entry.grid(row=2, column=3, pady=5, sticky=E)

t_end_label = Label(root, text=": پایان نمودار در")
t_end_label.grid(row=2, column=2)
t_end_entry = Entry(root, text=t_end, width=20, font=55)
t_end_entry.grid(row=2, column=1, pady=5, sticky=E)

problem_label = Label(root, text=": صورت مسئله")
problem_label.grid(row=3, column=4, pady=5)
problem_entry = Entry(root, text=sample_problem, width=57, font=55)
problem_entry.grid(row=3, column=1, columnspan=3, pady=5, sticky=E)

alpha_label = Label(root, text=": مقدار alpha")
alpha_label.grid(row=4, column=4, pady=5)
alpha_entry = Entry(root, text=alpha_val, width=20, font=55)
alpha_entry.grid(row=4, column=3, pady=5, sticky=E)

omega_label = Label(root, text=": مقدار omega")
omega_label.grid(row=4, column=2, pady=5)
omega_entry = Entry(root, text=omega_val, width=20, font=55)
omega_entry.grid(row=4, column=1, pady=5, sticky=E)

panel = Label(root)
panel.grid(row=6, column=0, columnspan=5, padx=20, pady=5)

btn = Button(root, text="رسم نمودار", command=show_plot, width=30)
btn.grid(row=5, column=0, columnspan=5, padx=20, pady=5)

owner = Label(root, text="Mr.Hidden - https://t.me/Darker1063 - @Darker1063", fg="blue", cursor="hand2")
owner.grid(row=7, column=0, columnspan=5, pady=5)
owner.bind("<Button-1>", open_url)

root.protocol("WM_DELETE_WINDOW", on_closing)

show_plot()

root.mainloop()
