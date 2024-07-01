import tkinter as tk
from tkinter import colorchooser, filedialog, messagebox
from PIL import Image, ImageDraw, ImageTk

class SimplePaint:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Paint")
        self.root.geometry("800x600")

        self.color = 'black'
        self.brush_size = 5
        self.image = Image.new("RGB", (800, 600), "white")
        self.draw = ImageDraw.Draw(self.image)

        self.canvas = tk.Canvas(self.root, bg='white')
        self.canvas.pack(fill=tk.BOTH, expand=True)

        self.tool = "brush"
        self.line_start = None

        self.setup_menu()
        self.setup_tools()

        self.unsaved_changes = False
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)

    def setup_menu(self):
        self.menu_bar = tk.Menu(self.root)

        self.file_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.file_menu.add_command(label="New", command=self.new_file)
        self.file_menu.add_command(label="Open", command=self.open_file)
        self.file_menu.add_command(label="Save", command=self.save_file)
        self.file_menu.add_command(label="Clear", command=self.clear_canvas)
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Exit", command=self.on_closing)
        self.menu_bar.add_cascade(label="File", menu=self.file_menu)

        self.options_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.options_menu.add_command(label="Brush Size", command=self.choose_brush_size)
        self.options_menu.add_command(label="Color", command=self.choose_color)
        self.menu_bar.add_cascade(label="Options", menu=self.options_menu)

        self.root.config(menu=self.menu_bar)

    def setup_tools(self):
        self.tool_frame = tk.Frame(self.root, bd=1, relief=tk.RAISED)
        self.tool_frame.pack(side=tk.TOP, fill=tk.X)

        self.brush_button = tk.Button(self.tool_frame, text="Brush", command=self.use_brush)
        self.brush_button.pack(side=tk.LEFT, padx=2, pady=2)
        self.line_button = tk.Button(self.tool_frame, text="Line", command=self.use_line)
        self.line_button.pack(side=tk.LEFT, padx=2, pady=2)
        self.fill_button = tk.Button(self.tool_frame, text="Fill", command=self.use_fill)
        self.fill_button.pack(side=tk.LEFT, padx=2, pady=2)

        self.use_brush()

    def use_brush(self):
        self.tool = "brush"
        self.canvas.unbind("<Button-1>")
        self.canvas.unbind("<B1-Motion>")
        self.canvas.unbind("<ButtonRelease-1>")
        self.canvas.bind("<B1-Motion>", self.paint)

    def use_line(self):
        self.tool = "line"
        self.canvas.unbind("<Button-1>")
        self.canvas.unbind("<B1-Motion>")
        self.canvas.unbind("<ButtonRelease-1>")
        self.canvas.bind("<Button-1>", self.start_line)
        self.canvas.bind("<ButtonRelease-1>", self.draw_line)

    def use_fill(self):
        self.tool = "fill"
        self.canvas.unbind("<Button-1>")
        self.canvas.unbind("<B1-Motion>")
        self.canvas.unbind("<ButtonRelease-1>")
        self.canvas.bind("<Button-1>", self.fill_area)

    def start_line(self, event):
        self.line_start = (event.x, event.y)

    def draw_line(self, event):
        if self.line_start:
            x1, y1 = self.line_start
            x2, y2 = event.x, event.y
            self.canvas.create_line(x1, y1, x2, y2, fill=self.color, width=self.brush_size)
            self.draw.line([x1, y1, x2, y2], fill=self.color, width=self.brush_size)
            self.line_start = None
            self.unsaved_changes = True

    def paint(self, event):
        x1, y1 = (event.x - self.brush_size), (event.y - self.brush_size)
        x2, y2 = (event.x + self.brush_size), (event.y + self.brush_size)
        self.canvas.create_oval(x1, y1, x2, y2, fill=self.color, outline=self.color)
        self.draw.ellipse([x1, y1, x2, y2], fill=self.color, outline=self.color)
        self.unsaved_changes = True

    def fill_area(self, event):
        x, y = event.x, event.y
        pixel_color = self.image.getpixel((x, y))
        self.flood_fill(x, y, pixel_color, self.color)
        self.photo_image = ImageTk.PhotoImage(self.image)
        self.canvas.create_image(0, 0, image=self.photo_image, anchor=tk.NW)
        self.unsaved_changes = True

    def flood_fill(self, x, y, target_color, replacement_color):
        target_color = tuple(target_color)
        replacement_color = tuple(int(replacement_color[i:i+2], 16) for i in (1, 3, 5))
        if target_color == replacement_color:
            return
        edge = [(x, y)]
        while edge:
            new_edge = []
            for (x, y) in edge:
                if self.image.getpixel((x, y)) == target_color:
                    self.image.putpixel((x, y), replacement_color)
                    if x > 0:
                        new_edge.append((x - 1, y))
                    if x < self.image.width - 1:
                        new_edge.append((x + 1, y))
                    if y > 0:
                        new_edge.append((x, y - 1))
                    if y < self.image.height - 1:
                        new_edge.append((x, y + 1))
            edge = new_edge

    def clear_canvas(self):
        self.canvas.delete("all")
        self.image = Image.new("RGB", (800, 600), "white")
        self.draw = ImageDraw.Draw(self.image)
        self.unsaved_changes = True

    def new_file(self):
        if self.check_for_unsaved_changes():
            self.clear_canvas()
            self.unsaved_changes = False

    def open_file(self):
        if self.check_for_unsaved_changes():
            file_path = filedialog.askopenfilename(defaultextension=".png",
                                                   filetypes=[("PNG files", "*.png"), ("All files", "*.*")])
            if file_path:
                self.image = Image.open(file_path)
                self.image = self.image.resize((800, 600), Image.ANTIALIAS)
                self.draw = ImageDraw.Draw(self.image)
                self.photo_image = ImageTk.PhotoImage(self.image)
                self.canvas.create_image(0, 0, image=self.photo_image, anchor=tk.NW)
                self.unsaved_changes = False

    def save_file(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".png",
                                                 filetypes=[("PNG files", "*.png"), ("All files", "*.*")])
        if file_path:
            self.image.save(file_path)
            self.unsaved_changes = False

    def choose_brush_size(self):
        size = tk.simpledialog.askinteger("Brush Size", "Enter brush size (1-50):", minvalue=1, maxvalue=50)
        if size:
            self.brush_size = size

    def choose_color(self):
        color = colorchooser.askcolor(color=self.color)[1]
        if color:
            self.color = color

    def check_for_unsaved_changes(self):
        if self.unsaved_changes:
            response = messagebox.askyesnocancel("Unsaved Changes",
                                                 "You have unsaved changes. Do you want to save them?")
            if response:  # Yes
                self.save_file()
                return True
            elif response is None:  # Cancel
                return False
        return True

    def on_closing(self):
        if self.check_for_unsaved_changes():
            self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = SimplePaint(root)
    root.mainloop()

