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

        # Draw the fractal hill
        self.draw_fractal_hill(canvas_width, canvas_height)

        self.snowflakes = []

        for _ in range(num_snowflakes):
            x = random.randint(0, canvas_width)
            y = random.randint(0, canvas_height)
            size = random.randint(2, 6)
            snowflake = Snowflake(self.canvas, x, y, size)
            self.snowflakes.append(snowflake)

        self.animate()

    def draw_fractal_hill(self, canvas_width, canvas_height):
        # Recursive function to draw fractal hill
        def draw_fractal_line(x1, y1, x2, y2, depth):
            if depth == 0:
                self.canvas.create_line(x1, y1, x2, y2, fill='gray')
            else:
                # Midpoint and random displacement
                mx = (x1 + x2) / 2
                my = (y1 + y2) / 2 + random.uniform(-canvas_height / 10, canvas_height / 10)

                # Recursive calls to draw two segments
                draw_fractal_line(x1, y1, mx, my, depth - 1)
                draw_fractal_line(mx, my, x2, y2, depth - 1)

        # Initial coordinates and recursion depth
        x1, y1 = 0, canvas_height - 100
        x2, y2 = canvas_width, canvas_height - 100
        initial_peak_y = canvas_height // 2  # Initial peak height
        recursion_depth = 8  # Adjust depth as needed for more/less detail

        # Start with a simple triangle
        draw_fractal_line(x1, y1, canvas_width / 2, initial_peak_y, recursion_depth)
        draw_fractal_line(canvas_width / 2, initial_peak_y, x2, y2, recursion_depth)

    def animate(self):
        for snowflake in self.snowflakes:
            snowflake.fall()
        self.root.after(50, self.animate)

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Snow Animation with Fractal Hill")
    app = SnowAnimation(root, 800, 600, 100)
    root.mainloop()
