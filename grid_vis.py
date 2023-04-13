import tkinter as tk


class GridVisualizer:
    def __init__(self, root, grid_size):
        self.root = root
        self.grid_size = grid_size
        self.cell_width = 5
        self.cell_height = 5
        self.canvas_width = self.cell_width * self.grid_size
        self.canvas_height = self.cell_height * self.grid_size
        self.canvas = tk.Canvas(self.root, width=self.canvas_width, height=self.canvas_height)
        self.canvas.grid(row=0, column=0)

    def draw_grid(self, grid):
        self.canvas.delete(tk.ALL)
        for i in range(self.grid_size):
            for j in range(self.grid_size):
                color = "white" if grid[i][j] == 0 else "green" if grid[i][j] == 1 else "red"
                x1 = j * self.cell_width
                y1 = i * self.cell_height
                x2 = x1 + self.cell_width
                y2 = y1 + self.cell_height
                self.canvas.create_rectangle(x1, y1, x2, y2, fill=color)

