import tkinter as tk
import random
import math

def bezier_curve(p0, p1, p2, p3, t):
    """Calculate a point on a cubic Bezier curve."""
    x = (1 - t) ** 3 * p0[0] + 3 * (1 - t) ** 2 * t * p1[0] + 3 * (1 - t) * t ** 2 * p2[0] + t ** 3 * p3[0]
    y = (1 - t) ** 3 * p0[1] + 3 * (1 - t) ** 2 * t * p1[1] + 3 * (1 - t) * t ** 2 * p2[1] + t ** 3 * p3[1]
    return x, y

def generate_random_points(width, height):
    """Generate four random control points within the given dimensions."""
    return [
        (random.randint(0, width), random.randint(0, height)) for _ in range(4)
    ]

def draw_bezier(canvas, width, height):
    """Draw a random Bezier curve on the canvas."""
    canvas.delete("all")
    points = generate_random_points(width, height)
    
    prev_point = points[0]
    for i in range(1, 101):  # Draw 100 segments
        t = i / 100
        new_point = bezier_curve(*points, t)
        canvas.create_line(prev_point[0], prev_point[1], new_point[0], new_point[1], fill=random.choice(["red", "blue", "green", "yellow", "cyan", "magenta"]))
        prev_point = new_point
    
    canvas.after(1000, lambda: draw_bezier(canvas, width, height))  # Redraw every second

def main():
    root = tk.Tk()
    root.title("Bezier Curve Screensaver")
    root.attributes("-fullscreen", True)
    root.configure(bg="black")
    
    width = root.winfo_screenwidth()
    height = root.winfo_screenheight()
    
    canvas = tk.Canvas(root, width=width, height=height, bg="black")
    canvas.pack()
    
    root.bind("<Escape>", lambda e: root.destroy())  # Exit on Escape key
    
    draw_bezier(canvas, width, height)
    
    root.mainloop()

if __name__ == "__main__":
    main()

