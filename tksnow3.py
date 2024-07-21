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

        # Draw the fractal horizon (ground)
        self.draw_fractal_horizon(canvas_width, canvas_height)

        self.snowflakes = []

        for _ in range(num_snowflakes):
            x = random.randint(0, canvas_width)
            y = random.randint(0, canvas_height)
            size = random.randint(2, 6)
            snowflake = Snowflake(self.canvas, x, y, size)
            self.snowflakes.append(snowflake)

        self.animate()

    def draw_fractal_horizon(self, canvas_width, canvas_height):
        # Recursive function to draw fractal triangles
        def draw_triangle(x1, y1, x2, y2, x3, y3, depth):
            if depth == 0:
                self.canvas.create_polygon(x1, y1, x2, y2, x3, y3, fill='gray', outline='gray')
            else:
                # Midpoints of the sides
                mx1 = (x1 + x2) / 2
                my1 = (y1 + y2) / 2
                mx2 = (x2 + x3) / 2
                my2 = (y2 + y3) / 2
                mx3 = (x1 + x3) / 2
                my3 = (y1 + y3) / 2

                # Recursive calls to draw smaller triangles
                draw_triangle(x1, y1, mx1, my1, mx3, my3, depth - 1)
                draw_triangle(mx1, my1, x2, y2, mx2, my2, depth - 1)
                draw_triangle(mx3, my3, mx2, my2, x3, y3, depth - 1)

        # Initial triangle coordinates and recursion depth
        x1, y1 = 0, canvas_height - 100
        x2, y2 = canvas_width, canvas_height - 100
        x3, y3 = canvas_width // 2, canvas_height - 300
        recursion_depth = 4  # Adjust depth as needed for more/less detail

        draw_triangle(x1, y1, x2, y2, x3, y3, recursion_depth)

    def animate(self):
        for snowflake in self.snowflakes:
            snowflake.fall()
        self.root.after(50, self.animate)

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Snow Animation with Fractal Horizon")
    app = SnowAnimation(root, 800, 600, 100)
    root.mainloop()
