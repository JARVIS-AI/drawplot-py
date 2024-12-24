import math
import webbrowser
import re
from tkinter import *

def s(t):
    """
    Unit step function that returns 1 if t is 0, otherwise 0.

    Args:
        t (int): The input value.

    Returns:
        int: 1 if t is 0, otherwise 0.
    """
    return 1 if t == 0 else 0

def delta(t):
    """
    Delta function that returns 1 if t is 0, otherwise 0.

    Args:
        t (int): The input value.

    Returns:
        int: 1 if t is 0, otherwise 0.
    """
    return 1 if t == 0 else 0

def u(t):
    """
    Heaviside step function that returns 1 if t is greater than or equal to 0, otherwise 0.

    Args:
        t (int): The input value.

    Returns:
        int: 1 if t is greater than or equal to 0, otherwise 0.
    """
    return 1 if t >= 0 else 0

def exp_decay(t, alpha=1.0):
    """
    Exponential decay function.

    Args:
        t (int or float): The input value.
        alpha (float, optional): The decay rate. Defaults to 1.0.

    Returns:
        float: exp(-alpha * t) * u(t) to ensure it's defined for t >= 0.
    """
    return math.exp(-alpha * t) * u(t)

def e_1(t, alpha=1.0):
    """
    Alternate exponential decay function.

    Args:
        t (int or float): The input value.
        alpha (float, optional): The decay rate. Defaults to 1.0.

    Returns:
        float: exp(-alpha * t) * u(t) to ensure it's defined for t >= 0.
    """
    return math.exp(-alpha * t) * u(t)

def e(t, alpha=1.0):
    """
    Exponential growth function.

    Args:
        t (int or float): The input value.
        alpha (float, optional): The growth rate. Defaults to 1.0.

    Returns:
        float: exp(alpha * t) * u(t) to ensure it's defined for t >= 0.
    """
    return math.exp(alpha * t) * u(t)

def exp(t, alpha=1.0):
    """
    General exponential function.

    Args:
        t (int or float): The input value.
        alpha (float, optional): The exponent rate. Defaults to 1.0.

    Returns:
        float: exp(alpha * t) * u(t) to ensure it's defined for t >= 0.
    """
    return math.exp(alpha * t) * u(t)

def r(t):
    """
    Ramp function that returns t if t is greater than or equal to 0, otherwise 0.

    Args:
        t (int or float): The input value.

    Returns:
        int or float: t if t is greater than or equal to 0, otherwise 0.
    """
    return t if t >= 0 else 0

def sin(t, omega=1.0):
    """
    Sine function.

    Args:
        t (int or float): The input value.
        omega (float, optional): The frequency. Defaults to 1.0.

    Returns:
        float: sin(omega * t).
    """
    return math.sin(omega * t)

def cos(t, omega=1.0):
    """
    Cosine function.

    Args:
        t (int or float): The input value.
        omega (float, optional): The frequency. Defaults to 1.0.

    Returns:
        float: cos(omega * t).
    """
    return math.cos(omega * t)

def linspace(start, stop, num=400):
    """
    Generates num evenly spaced values from start to stop.

    Args:
        start (int or float): The starting value of the sequence.
        stop (int or float): The ending value of the sequence.
        num (int, optional): Number of values to generate. Defaults to 400.

    Yields:
        float: The next value in the sequence.
    """
    step = (stop - start) / (num - 1)
    yield from (start + i * step for i in range(num))


def restrict_to_english(event, entry):
    """
    Restrict the entry content to English letters, numbers, and spaces only.

    Args:
        event: The event object triggered by a key release.
        entry: The Tkinter Entry widget to be restricted.

    Returns:
        None
    """
    entry_content = entry.get()
    restricted_content = re.sub(r'[^(\-)* | a-zA-Z0-9\s]', '', entry_content)
    entry.delete(0, END)
    entry.insert(0, restricted_content)

def convert_expression(expression):
    """
    Convert the expression to include multiplication signs where necessary.

    Args:
        expression (str): The mathematical expression in string format.

    Returns:
        str: The converted expression with multiplication signs added.
    """
    converted_expression = re.sub(r'(\d+)([a-zA-Z]\()', r'\1 * \2', expression)
    return converted_expression

def draw_function(canvas, x_origin, y_origin, step_size_x, step_size_y, x_values, str_problem, alpha=1.0, omega=1.0):
    """
    Draw the function on the canvas using the given parameters.

    Args:
        canvas: The Tkinter Canvas widget to draw on.
        x_origin (int): The x-coordinate of the origin.
        y_origin (int): The y-coordinate of the origin.
        step_size_x (float): The step size for the x-axis.
        step_size_y (float): The step size for the y-axis.
        x_values (list): The list of x values to plot.
        str_problem (str): The mathematical expression to evaluate.
        alpha (float, optional): The alpha parameter for exponential functions. Defaults to 1.0.
        omega (float, optional): The omega parameter for trigonometric functions. Defaults to 1.0.

    Returns:
        None
    """
    prev_x, prev_y = None, None
    for t in x_values:
        y = eval(str_problem)
        img_x = x_origin + t * step_size_x
        img_y = y_origin - y * step_size_y
        if prev_x is not None and prev_y is not None:
            canvas.create_line(prev_x, prev_y, img_x, img_y, fill='red', width=2)
        prev_x, prev_y = img_x, img_y



def draw_graph(canvas, t_start, t_end, str_problem, alpha=1.0, omega=1.0, width=665, height=500, y_min=-10, y_max=10):
    """
    Draw the graph on the canvas using the given parameters.

    Args:
        canvas: The Tkinter Canvas widget to draw on.
        t_start (int): The starting value of the t-axis.
        t_end (int): The ending value of the t-axis.
        str_problem (str): The mathematical expression to evaluate.
        alpha (float, optional): The alpha parameter for exponential functions. Defaults to 1.0.
        omega (float, optional): The omega parameter for trigonometric functions. Defaults to 1.0.
        width (int, optional): The width of the canvas. Defaults to 665.
        height (int, optional): The height of the canvas. Defaults to 500.
        y_min (int, optional): The minimum value of the y-axis. Defaults to -10.
        y_max (int, optional): The maximum value of the y-axis. Defaults to 10.

    Returns:
        None
    """
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
    """
    Retrieve input values from the GUI entries, process them, and draw the graph on the canvas.

    Args:
        None

    Returns:
        None
    """
    t_start = int(t_start_entry.get())
    t_end = int(t_end_entry.get())
    str_problem = problem_entry.get()
    str_problem = convert_expression(str_problem)
    alpha = float(alpha_entry.get()) if alpha_entry.get() else 1.0
    omega = float(omega_entry.get()) if omega_entry.get() else 1.0
    draw_graph(canvas, t_start, t_end, str_problem, alpha, omega)


def open_url(event):
    """
    Open a specific URL in a new web browser tab.

    Args:
        event: The event object triggered by a user action, such as a mouse click.

    Returns:
        None
    """
    webbrowser.open_new(r"https://t.me/Darker1063")


# Initialize the main Tkinter window
root = Tk()
root.iconbitmap(r'drawplot.ico')  # Set the icon for the window
root.title("Drawplot")  # Set the window title

main_width = 700  # Width of the main window
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
guide_label_1 = Label(root, text="u(t) - r(t) - sin(t, omega) - cos(t, omega) - delta(t) | s(t) - exp_decay(t, alpha) | e_1(t, alpha) - exp(t, alpha) | e(t, alpha): لیست توابع", anchor='e', justify=RIGHT)
guide_label_2 = Label(root, text="u(t) - r(t-1) + 2*delta(t-2): صورت مسئله را به این شکل وارد کنید مثال", anchor='e', justify=RIGHT)

# Position guide labels
guide_label_1.grid(row=0, column=0, columnspan=5, padx=10, pady=2, sticky=E)
guide_label_2.grid(row=1, column=0, columnspan=5, padx=10, pady=2, sticky=E)

# Create and position labels and entry fields for user inputs
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

# Create and position the "Draw Plot" button
btn = Button(root, text="رسم نمودار", command=show_plot, width=30)
btn.grid(row=5, column=0, columnspan=5, padx=20, pady=5)

# Create and position the label with hyperlink
owner = Label(root, text="Mr.Hidden - https://t.me/Darker1063 - @Darker1063", fg="blue", cursor="hand2")
owner.grid(row=7, column=0, columnspan=5, pady=5)
owner.bind("<Button-1>", open_url)  # Bind the label click event to open the URL

# Create and position the canvas for drawing the plot
canvas = Canvas(root, width=665, height=500)
canvas.grid(row=6, column=0, columnspan=5, padx=20, pady=5)

# Bind key release events to the restrict_to_english function
t_start_entry.bind('<KeyRelease>', lambda event: restrict_to_english(event, t_start_entry))
t_end_entry.bind('<KeyRelease>', lambda event: restrict_to_english(event, t_end_entry))
problem_entry.bind('<KeyRelease>', lambda event: restrict_to_english(event, problem_entry))
alpha_entry.bind('<KeyRelease>', lambda event: restrict_to_english(event, alpha_entry))
omega_entry.bind('<KeyRelease>', lambda event: restrict_to_english(event, omega_entry))

# Initialize the plot with the default values
show_plot()

# Start the Tkinter main loop
root.mainloop()
