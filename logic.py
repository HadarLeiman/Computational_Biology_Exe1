import numpy as np

count_gen = 0
# simulate one generation of the automaton
# todo - organize the parameters the function gets
def one_generation(old_grid, color_grid, param):
    # Create a new grid to store the new state of the automaton
    new_grid = np.zeros_like(old_grid)
    # Loop through the cells of the grid
    for i in range(param.grid_size):
        for j in range(param.grid_size):
            # If the cell is empty, skip it
            if old_grid[i, j] == 0:
                continue
            # if the cell does not have the rumor, check if it should get it
            elif old_grid[i, j] == 1:
                # Get the neighbors of the cell
                neighbors = old_grid[max(0, i - 1):min(param.grid_size, i + 2),
                            max(0, j - 1):min(param.grid_size, j + 2)]
                # Get the number of neighbors that have the rumor
                num_neighbors_with_rumor = np.sum(neighbors == -1)
                # If the cell has no neighbors with the rumor, skip it
                if num_neighbors_with_rumor == 0:
                    new_grid[i, j] = 1
                    continue
                # if the cell has one neighbor with the rumor, update its color in the color grid to 2
                color_grid[i, j] = 2
                # Get the skepticism level of the cell
                if num_neighbors_with_rumor == 1:
                    skepticism_level = param.skepticism[i, j]
                else:
                    skepticism_level = param.skepticism_reduction[param.skepticism[i, j]]
                # Get the probability of transmission
                transmission_probability = param.transmission_probabilities[skepticism_level]
                # Check if the cell should get the rumor
                if np.random.random() < transmission_probability:
                    new_grid[i, j] = -1
                else:
                    new_grid[i, j] = 1

            # If the cell has the rumor, update its value to gossip_rest_period+1
            elif old_grid[i, j] == -1:
                new_grid[i, j] = param.gossip_rest_period + 1

            # If the cell has a value greater than 1, reduce it by 1
            elif old_grid[i, j] > 1:
                new_grid[i, j] = old_grid[i, j] - 1

    return new_grid, color_grid


def init_simulation(param):
    # Create a grid with the specified population density
    grid = np.random.choice([0, 1], size=(param.grid_size, param.grid_size),
                            p=[1 - param.population_density, param.population_density])

    # Create a grid to store the color of each cell (0 for empty, 1 for no rumor, 2 for rumor)
    color_grid = np.copy(grid)

    # init random cell with the rumor in grid and color grid
    # get the indices of the cells with one
    indices = np.argwhere(grid == 1)
    # choose one of the indices randomly
    index = indices[np.random.choice(len(indices))]
    # set the value of the cell to -1 (rumor)
    grid[index[0], index[1]] = -1
    # set the color of the cell to 2 (rumor)
    color_grid[index[0], index[1]] = 2

    return grid, color_grid


def update(root, old_grid, old_color_grid, param, gridVis):
    global count_gen
    count_gen += 1
    # run one generation of the simulation
    new_grid, new_color_grid = one_generation(old_grid, old_color_grid, param)
    # update the grid
    gridVis.draw_grid(new_color_grid, count_gen)
    # check if the simulation should stop
    if np.sum(new_grid == -1) == 0:
        # empty the grid and write "No rumor spreaders left" in the center
        gridVis.canvas.create_text(param.grid_size / 2 * gridVis.cell_width, param.grid_size / 2 * gridVis.cell_height,
                                        text="No rumor spreaders left", font=("Purisa", 30))
        # wait 5 seconds and then close the window
        root.after(5000, root.destroy)
        return
    elif np.sum(new_color_grid == 1) == 0:
        # empty the grid and write "Rumor spread to all cells" in the center
        gridVis.canvas.create_text(param.grid_size / 2 * gridVis.cell_width, param.grid_size / 2 * gridVis.cell_height,
                                      text="Rumor spread to all cells", font=("Purisa", 30))
        # wait 5 seconds and then close the window
        root.after(5000, root.destroy)
        return
    # run the function again after 100 milliseconds
    root.after(100, update, root, new_grid, new_color_grid, param, gridVis)
