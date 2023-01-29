import tkinter as tk
import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

data = [3, 5, 1, 7, 4, 6, 8, 2]

root = tk.Tk()

show_bar = tk.BooleanVar(value=True)
cb1 = tk.Checkbutton(root, text="Bar Chart", variable=show_bar)
cb1.pack()

show_pie = tk.BooleanVar(value=True)
cb2 = tk.Checkbutton(root, text="Pie Chart", variable=show_pie)
cb2.pack()

fig = Figure()
canvas = FigureCanvasTkAgg(fig, master=root)
canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

def generate():
    fig.clear()
    if show_bar.get():
        ax1 = fig.add_subplot(121)
        ax1.bar(range(len(data)), data)
    if show_pie.get():
        ax2 = fig.add_subplot(122, aspect="equal")
        ax2.pie(data)
    canvas.draw()

generate_button = tk.Button(root, text="Generate", command=generate)
generate_button.pack()

root.mainloop()
