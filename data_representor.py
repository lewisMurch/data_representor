import tkinter as tk
import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from mpl_toolkits.mplot3d import Axes3D

data = [3, 5, 1, 7, 4, 6, 8, 2]

root = tk.Tk()

show_bar = tk.BooleanVar(value=True)
cb1 = tk.Checkbutton(root, text="Bar Chart", variable=show_bar)
cb1.pack()

show_pie = tk.BooleanVar(value=True)
cb2 = tk.Checkbutton(root, text="Pie Chart", variable=show_pie)
cb2.pack()

show_3d = tk.BooleanVar(value=True)
cb3 = tk.Checkbutton(root, text="3D Plot", variable=show_3d)
cb3.pack()

fig = Figure()
canvas = FigureCanvasTkAgg(fig, master=root)
canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

def generate():
    fig.clear()
    if show_bar.get() and show_pie.get() and show_3d.get():
        ax1 = fig.add_subplot(131)
        ax1.bar(range(len(data)), data)
        ax2 = fig.add_subplot(132, aspect="equal")
        ax2.pie(data)
        ax3 = fig.add_subplot(133, projection="3d")
        ax3.scatter(range(len(data)), data, data)
    elif show_bar.get() and show_pie.get():
        ax1 = fig.add_subplot(121)
        ax1.bar(range(len(data)), data)
        ax2 = fig.add_subplot(122, aspect="equal")
        ax2.pie(data)
    elif show_bar.get() and show_3d.get():
        ax1 = fig.add_subplot(121)
        ax1.bar(range(len(data)), data)
        ax3 = fig.add_subplot(122, projection="3d")
        ax3.scatter(range(len(data)), data, data)
    elif show_pie.get() and show_3d.get():
        ax2 = fig.add_subplot(121, aspect="equal")
        ax2.pie(data)
        ax3 = fig.add_subplot(122, projection="3d")
        ax3.scatter(range(len(data)), data, data)
    elif show_bar.get():
        ax1 = fig.add_subplot(111)
        ax1.bar(range(len(data)), data)
    elif show_pie.get():
        ax2 = fig.add_subplot(111, aspect="equal")
        ax2.pie(data)
    elif show_3d.get():
        ax3 = fig.add_subplot(111, projection="3d")
        ax3.scatter(range(len(data)), data, data)
    canvas.draw()

generate_button = tk.Button(root, text="Generate", command=generate)
generate_button.pack()

root.mainloop()
