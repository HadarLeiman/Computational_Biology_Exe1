import tkinter as tk
import numpy as np

class GridVisualizer:
    def __init__(self, root, grid_size):
        self.root = root
        self.grid_size = grid_size
        self.cell_width = 5
        self.cell_height = 5
        self.canvas_width = self.cell_width * self.grid_size
        self.canvas_height = self.cell_height * self.grid_size
        self.canvas = tk.Canvas(self.root, width=self.canvas_width, height=self.canvas_height)
        self.canvas.grid(row=0, column=2, rowspan=6)

    def draw_grid(self, grid, count_gen):
        self.canvas.delete(tk.ALL)
        for i in range(self.grid_size):
            for j in range(self.grid_size):
                color = "white" if grid[i][j] == 0 else "green" if grid[i][j] == 1 else "red"
                x1 = j * self.cell_width
                y1 = i * self.cell_height
                x2 = x1 + self.cell_width
                y2 = y1 + self.cell_height
                self.canvas.create_rectangle(x1, y1, x2, y2, fill=color)
        # write the number of cells with 2 from the number of cells with 1+2 in the top left corner of the root
        # create a frame for the text
        text_frame = tk.Frame(self.root)
        text_frame.grid(row=6, column=2)

        # create the text widget in the frame
        text = tk.Text(text_frame, height=2, width=40)
        text.grid(row=6, column=2)
        text.insert(tk.END, "Exposed to rumor: " + str(round(100*np.sum(grid == 2)/(np.sum(grid == 1) + np.sum(grid == 2)),2)) + "%"+
                    "(" + str(np.sum(grid == 2)) + "/" + str(np.sum(grid == 1) + np.sum(grid == 2)) + ")" +
                    "\nGeneration: " + str(count_gen))