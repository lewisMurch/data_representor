import tkinter as tk
import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

data = [3, 5, 1, 7, 4, 6, 8, 2]

def draw_plot():
    fig = Figure()
    if var.get() == "Bar Chart":
        ax = fig.add_subplot(111)
        ax.bar(range(len(data)), data)
    elif var.get() == "Pie Chart":
        ax = fig.add_subplot(111, aspect="equal")
        ax.pie(data)
    canvas = FigureCanvasTkAgg(fig, master=root)
    canvas.draw()
    canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

root = tk.Tk()
var = tk.StringVar(value="Bar Chart")
rb1 = tk.Radiobutton(root, text="Bar Chart", variable=var, value="Bar Chart", command=draw_plot)
rb2 = tk.Radiobutton(root, text="Pie Chart", variable=var, value="Pie Chart", command=draw_plot)
btn = tk.Button(root, text="Draw", command=draw_plot)

rb1.pack()
rb2.pack()
btn.pack()

root.mainloop()
