import tkinter as tk
import random

class Snowflake:
    def __init__(self, canvas, x, y, size):
        self.canvas = canvas
        self.size = size
        self.x = x
        self.y = y
        self.id = self.canvas.create_oval(x, y, x + size, y + size, fill='white')

    def fall(self):
        self.canvas.move(self.id, 0, self.size)
        self.y += self.size

        if self.y > self.canvas.winfo_height():
            self.canvas.move(self.id, 0, -self.canvas.winfo_height())
            self.y = 0

class SnowAnimation:
    def __init__(self, root, canvas_width, canvas_height, num_snowflakes):
        self.root = root
        self.canvas = tk.Canvas(root, width=canvas_width, height=canvas_height, bg='black')
        self.canvas.pack()
        self.snowflakes = []

        for _ in range(num_snowflakes):
            x = random.randint(0, canvas_width)
            y = random.randint(0, canvas_height)
            size = random.randint(2, 6)
            snowflake = Snowflake(self.canvas, x, y, size)
            self.snowflakes.append(snowflake)

        self.animate()

    def animate(self):
        for snowflake in self.snowflakes:
            snowflake.fall()
        self.root.after(50, self.animate)

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Snow Animation")
    app = SnowAnimation(root, 800, 600, 100)
    root.mainloop()
