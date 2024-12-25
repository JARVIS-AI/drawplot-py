import math
import webbrowser
import re
from tkinter import *
import base64

def s(t):
    return 1 if t == 0 else 0

def delta(t):
    return 1 if t == 0 else 0

def u(t):
    return 1 if t >= 0 else 0

def exp_decay(t, alpha=1.0):
    return math.exp(-alpha * t) * u(t)

def e_1(t, alpha=1.0):
    return math.exp(-alpha * t) * u(t)

def e(t, alpha=1.0):
    return math.exp(alpha * t) * u(t)

def exp(t, alpha=1.0):
    return math.exp(alpha * t) * u(t)

def r(t):
    return t if t >= 0 else 0

def sin(t, omega=1.0):
    return math.sin(omega * t)

def cos(t, omega=1.0):
    return math.cos(omega * t)

def linspace(start, stop, num=400):
    step = (stop - start) / (num - 1)
    yield from (start + i * step for i in range(num))


def convert_expression(expression):
    converted_expression = re.sub(r'(\d+)([a-zA-Z]\()', r'\1 * \2', expression)
    return converted_expression

def draw_function(canvas, x_origin, y_origin, step_size_x, step_size_y, x_values, str_problem, alpha=1.0, omega=1.0):
    prev_x, prev_y = None, None
    for t in x_values:
        y = eval(str_problem)
        img_x = x_origin + t * step_size_x
        img_y = y_origin - y * step_size_y
        if prev_x is not None and prev_y is not None:
            canvas.create_line(prev_x, prev_y, img_x, img_y, fill='red', width=2)
        prev_x, prev_y = img_x, img_y



def draw_graph(canvas, t_start, t_end, str_problem, alpha=1.0, omega=1.0, width=665, height=500, y_min=-10, y_max=10):
    canvas.delete("all")
    t_start_adjusted = t_start
    x_origin = int((0 - t_start_adjusted) * (width / (t_end - t_start_adjusted + 1)))
    y_origin = int(height * (1 - (0 - y_min) / (y_max - y_min)))  # Correctly calculate y_origin
    step_size_x = width / (t_end - t_start_adjusted + 1)
    step_size_y = height / (y_max - y_min)

    # Draw vertical grid lines
    for i in range(t_start_adjusted, t_end + 1):
        img_x = (i - t_start_adjusted) * step_size_x
        if 0 <= img_x <= width:
            canvas.create_line(img_x, 0, img_x, height, fill='lightgray')

    # Draw horizontal grid lines
    for i in range(y_min, y_max + 1):
        img_y = height - ((i - y_min) * step_size_y)  # Correctly calculate img_y
        if 0 <= img_y <= height:
            canvas.create_line(0, img_y, width, img_y, fill='lightgray')

    # Draw x and y axes
    canvas.create_line(0, y_origin, width, y_origin, fill='black', width=2)
    canvas.create_line(x_origin, 0, x_origin, height, fill='black', width=2)

    # Draw the function
    x_values = list(linspace(t_start, t_end + 1))
    draw_function(canvas, x_origin, y_origin, step_size_x, step_size_y, x_values, str_problem, alpha, omega)


def show_plot():
    t_start = int(t_start_entry.get())
    t_end = int(t_end_entry.get())
    str_problem = problem_entry.get()
    str_problem = convert_expression(str_problem)
    alpha = float(alpha_entry.get()) if alpha_entry.get() else 1.0
    omega = float(omega_entry.get()) if omega_entry.get() else 1.0
    draw_graph(canvas, t_start, t_end, str_problem, alpha, omega)


def open_url(event):
    webbrowser.open_new(r"https://t.me/Darker1063")

def open_url_jm(event):
    webbrowser.open_new(r"https://me.amsl.ir")

# Initialize the main Tkinter window
root = Tk()
with open("icon.py", "r") as wri:
    encoded_string = wri.read()

icon = base64.b64decode(encoded_string)

with open("temp.ico", "wb") as temp_icon:
    temp_icon.write(icon)
root.iconbitmap(r'temp.ico') # Set the icon for the window
root.title("Drawplot Farsi")  # Set the window title

main_width = 880  # Width of the main window
main_height = 700  # Height of the main window

# Get screen dimensions
screen_width = int(root.winfo_screenwidth())
screen_height = int(root.winfo_screenheight())

# Calculate position to center the window on the screen
RIGHT_RIGHT = str((int(screen_width) - main_width) // 2)
top_down = str((int(screen_height) - main_height) // 2)

# Set window properties
root.resizable(width=False, height=False)  # Prevent window resizing
root.maxsize(main_width, main_height)  # Set the maximum size of the window
root.geometry(f"{main_width}x{main_height}+{RIGHT_RIGHT}+{top_down}")  # Position the window
root.update()

# Initialize Tkinter StringVar variables for user input
t_start = StringVar(root, -2)
t_end = StringVar(root, 5)
sample_problem = StringVar(root, "u(t)")
alpha_val = StringVar(root, 1.0)
omega_val = StringVar(root, 1.0)

# Create guide labels
guide_label_1 = Label(root, text="u(t) - r(t) - sin(t, omega) - cos(t, omega) - delta(t)  |  s(t) - exp_decay(t, alpha)  |  e_1(t, alpha) - exp(t, alpha)  |  e(t, alpha) : لیست توابع", anchor='e', justify=RIGHT)
guide_label_2 = Label(root, text="u(t) - r(t-1) + 2*delta(t-2) : صورت مسئله را به این شکل وارد کنید مثال", anchor='e', justify=RIGHT)

# Position guide labels
guide_label_1.grid(row=0, column=0, columnspan=5, padx=10, pady=2, sticky=E)
guide_label_2.grid(row=1, column=0, columnspan=5, padx=10, pady=2, sticky=E)

# Create and position labels and entry fields for user inputs
t_start_label = Label(root, text="شروع نمودار از :")
t_start_label.grid(row=2, column=4)
t_start_entry = Entry(root, text=t_start, width=20, font=55)
t_start_entry.grid(row=2, column=3, pady=5, sticky=E)

t_end_label = Label(root, text="پایان نمودار در :")
t_end_label.grid(row=2, column=2)
t_end_entry = Entry(root, text=t_end, width=20, font=55)
t_end_entry.grid(row=2, column=1, pady=5, sticky=E)

problem_label = Label(root, text="صورت مسئله :")
problem_label.grid(row=3, column=4, pady=5)
problem_entry = Entry(root, text=sample_problem, width=57, font=55)
problem_entry.grid(row=3, column=1, columnspan=3, pady=5, sticky=E)

alpha_label = Label(root, text="مقدار alpha :")
alpha_label.grid(row=4, column=4, pady=5)
alpha_entry = Entry(root, text=alpha_val, width=20, font=55)
alpha_entry.grid(row=4, column=3, pady=5, sticky=E)

omega_label = Label(root, text="مقدار omega :")
omega_label.grid(row=4, column=2, pady=5)
omega_entry = Entry(root, text=omega_val, width=20, font=55)
omega_entry.grid(row=4, column=1, pady=5, sticky=E)

# Create and position the "Draw Plot" button
btn = Button(root, text="رسم نمودار", command=show_plot, width=30)
btn.grid(row=5, column=0, columnspan=5, padx=20, pady=5)

# Create and position the label with hyperlink
owner = Label(root, text="Mr.Hidden - Tel: @Darker1063", fg="blue", cursor="hand2")
owner.grid(row=7, column=0, columnspan=5, pady=5)
owner.bind("<Button-1>", open_url)  # Bind the label click event to open the URL

owner2 = Label(root, text="J4RVIS - me.amsl.ir - Tel: @J4RVIS", fg="blue", cursor="hand2")
owner2.grid(row=8, column=0, columnspan=5, pady=5)
owner2.bind("<Button-1>", open_url_jm)

# Create and position the canvas for drawing the plot
canvas = Canvas(root, width=565, height=400)
canvas.grid(row=6, column=0, columnspan=5, padx=20, pady=5)

# Initialize the plot with the default values
show_plot()

# Start the Tkinter main loop
root.mainloop()
