import tkinter as tk
from tkinter import colorchooser

class SimplePaint:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Paint")
        self.root.geometry("800x600")

        self.color = 'black'
        self.brush_size = 5

        self.canvas = tk.Canvas(self.root, bg='white')
        self.canvas.pack(fill=tk.BOTH, expand=True)

        self.canvas.bind("<B1-Motion>", self.paint)
        
        self.setup_menu()

    def setup_menu(self):
        self.menu_bar = tk.Menu(self.root)

        self.file_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.file_menu.add_command(label="Clear", command=self.clear_canvas)
        self.file_menu.add_command(label="Exit", command=self.root.quit)
        self.menu_bar.add_cascade(label="File", menu=self.file_menu)

        self.options_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.options_menu.add_command(label="Brush Size", command=self.choose_brush_size)
        self.options_menu.add_command(label="Color", command=self.choose_color)
        self.menu_bar.add_cascade(label="Options", menu=self.options_menu)

        self.root.config(menu=self.menu_bar)

    def paint(self, event):
        x1, y1 = (event.x - self.brush_size), (event.y - self.brush_size)
        x2, y2 = (event.x + self.brush_size), (event.y + self.brush_size)
        self.canvas.create_oval(x1, y1, x2, y2, fill=self.color, outline=self.color)

    def clear_canvas(self):
        self.canvas.delete("all")

    def choose_brush_size(self):
        size = tk.simpledialog.askinteger("Brush Size", "Enter brush size (1-50):", minvalue=1, maxvalue=50)
        if size:
            self.brush_size = size

    def choose_color(self):
        color = colorchooser.askcolor(color=self.color)[1]
        if color:
            self.color = color

if __name__ == "__main__":
    root = tk.Tk()
    app = SimplePaint(root)
    root.mainloop()
