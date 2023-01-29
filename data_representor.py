import tkinter as tk
import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

data = [3, 5, 1, 7, 4, 6, 8, 2]

def draw_plot():
    fig = Figure()
    canvas = FigureCanvasTkAgg(fig, master=root)
    canvas.get_tk_widget().pack_forget()
    if show_bar.get():
        ax = fig.add_subplot(111)
        ax.bar(range(len(data)), data)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)
    if show_pie.get():
        ax = fig.add_subplot(111, aspect="equal")
        ax.pie(data)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

def generate():
    fig = Figure()
    canvas = FigureCanvasTkAgg(fig, master=root)
    canvas.get_tk_widget().pack_forget()
    if show_bar.get():
        ax = fig.add_subplot(111)
        ax.bar(range(len(data)), data)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)
    if show_pie.get():
        ax = fig.add_subplot(111, aspect="equal")
        ax.pie(data)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

root = tk.Tk()

show_bar = tk.BooleanVar(value=True)
cb1 = tk.Checkbutton(root, text="Bar Chart", variable=show_bar)

show_pie = tk.BooleanVar(value=True)
cb2 = tk.Checkbutton(root, text="Pie Chart", variable=show_pie)

cb1.pack()
cb2.pack()

generate_button = tk.Button(root, text="Generate", command=generate)
generate_button.pack()

root.mainloop()
