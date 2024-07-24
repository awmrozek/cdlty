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

class Player:
    def __init__(self, canvas, x, y, color):
        self.canvas = canvas
        self.x = x
        self.y = y
        self.id = self.canvas.create_rectangle(x, y, x + 20, y + 20, fill=color)
        self.speed = 10

    def move_left(self):
        self.canvas.move(self.id, -self.speed, 0)

    def move_right(self):
        self.canvas.move(self.id, self.speed, 0)

    def move_up(self):
        self.canvas.move(self.id, 0, -self.speed)

    def move_down(self):
        self.canvas.move(self.id, 0, self.speed)

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

        # Add players
        self.player1 = Player(self.canvas, canvas_width // 4, canvas_height - 60, 'red')
        self.player2 = Player(self.canvas, 3 * canvas_width // 4, canvas_height - 60, 'blue')

        # Bind keyboard events to player movement
        self.root.bind('<Left>', lambda event: self.player1.move_left())
        self.root.bind('<Right>', lambda event: self.player1.move_right())
        self.root.bind('<Up>', lambda event: self.player1.move_up())
        self.root.bind('<Down>', lambda event: self.player1.move_down())
        self.root.bind('a', lambda event: self.player2.move_left())
        self.root.bind('d', lambda event: self.player2.move_right())
        self.root.bind('w', lambda event: self.player2.move_up())
        self.root.bind('s', lambda event: self.player2.move_down())

        self.animate()

    def draw_fractal_hill(self, canvas_width, canvas_height):
        # List to hold the points of the hill
        points = []

        # Recursive function to generate fractal hill points
        def generate_fractal_points(x1, y1, x2, y2, depth):
            if depth == 0:
                points.append((x1, y1))
                points.append((x2, y2))
            else:
                # Midpoint and random displacement
                mx = (x1 + x2) / 2
                my = (y1 + y2) / 2 + random.uniform(-canvas_height / 10, canvas_height / 10)

                # Recursive calls to generate points for two segments
                generate_fractal_points(x1, y1, mx, my, depth - 1)
                generate_fractal_points(mx, my, x2, y2, depth - 1)

        # Initial coordinates and recursion depth
        x1, y1 = 0, canvas_height - 100
        x2, y2 = canvas_width, canvas_height - 100
        initial_peak_y = canvas_height // 2  # Initial peak height
        recursion_depth = 8  # Adjust depth as needed for more/less detail

        # Generate fractal points for the hill
        generate_fractal_points(x1, y1, canvas_width / 2, initial_peak_y, recursion_depth)
        generate_fractal_points(canvas_width / 2, initial_peak_y, x2, y2, recursion_depth)

        # Remove duplicate points
        unique_points = list(dict.fromkeys(points))

        # Add bottom points to close the polygon
        unique_points.append((canvas_width, canvas_height))
        unique_points.append((0, canvas_height))

        # Draw the filled polygon representing the hill
        self.canvas.create_polygon(unique_points, fill='gray', outline='gray')

    def animate(self):
        for snowflake in self.snowflakes:
            snowflake.fall()
        self.root.after(50, self.animate)

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Snow Animation with Fractal Hill and Players")
    app = SnowAnimation(root, 800, 600, 100)
    root.mainloop()

