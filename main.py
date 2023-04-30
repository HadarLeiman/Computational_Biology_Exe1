import tkinter as tk
import parameters
from tkinter import messagebox
from logic import update, init_simulation
from grid_vis import GridVisualizer


# Define the function that runs the simulation
def run_simulation():

    # Get the values entered by the user
    population_density = float(density_entry.get())
    gossip_rest_period = int(gossip_rest_period_entry.get())
    skepticism_distribution = {
        "S1": float(s1_probability_entry.get()),
        "S2": float(s2_probability_entry.get()),
        "S3": float(s3_probability_entry.get()),
        "S4": float(s4_probability_entry.get())
    }

    # if the sum of the skepticism probabilitys is not equal to one, show an error message
    if sum(skepticism_distribution.values()) != 1:
        tk.messagebox.showerror("Error", "The sum of the skepticism probabilitys must be equal to 1")
        return

    # if the population density is not between 0 and 1, show an error message
    if population_density <= 0 or population_density > 1:
        tk.messagebox.showerror("Error", "The population density must be between 0 and 1")
        return

    # if the Gossip rest period is not a positive integer, show an error message
    if gossip_rest_period <= 0 or gossip_rest_period != int(gossip_rest_period):
        tk.messagebox.showerror("Error", "The Gossip rest period must be a positive integer")
        return

    # remove the run button
    run_button.grid_forget()
    # Add a button to quit the program
    quit_button = tk.Button(root, text="Quit", command=root.destroy)
    quit_button.grid(row=6, column=0, columnspan=2, padx=5, pady=5)

    # update the parameters file with the values entered by the user
    param = parameters.parameters()
    param.update_param(population_density, gossip_rest_period, skepticism_distribution)

    # initialize the simulation
    grid, color_grid = init_simulation(param)

    # create the grid visualizer
    grid_vis = GridVisualizer(root, param.grid_size)

    # run the simulation
    update(root, grid, color_grid, param, grid_vis)


# Create the main window
root = tk.Tk()
root.title("Simulation")

# Create input fields for the variables
density_label = tk.Label(root, text="Population Density (P)")
density_entry = tk.Entry(root)
# Set the default value for the population density
density_entry.insert(0, "1")
density_label.grid(row=0, column=0, padx=5, pady=0, sticky="w")
density_entry.grid(row=0, column=1, padx=5, pady=0)

gossip_rest_period_label = tk.Label(root, text="Gossip Rest Period (L)")
gossip_rest_period_entry = tk.Entry(root)
# Set the default value for the Gossip rest period
gossip_rest_period_entry.insert(0, "5")
gossip_rest_period_label.grid(row=1, column=0, padx=5, pady=0, sticky="w")
gossip_rest_period_entry.grid(row=1, column=1, padx=5, pady=0)

s1_probability_label = tk.Label(root, text="S1 probability")
s1_probability_entry = tk.Entry(root)
# Set the default value for the S1 probability
s1_probability_entry.insert(0, "0.25")
s1_probability_label.grid(row=2, column=0, padx=5, pady=0, sticky="w")
s1_probability_entry.grid(row=2, column=1, padx=5, pady=0)

s2_probability_label = tk.Label(root, text="S2 probability")
s2_probability_entry = tk.Entry(root)
# Set the default value for the S2 probability
s2_probability_entry.insert(0, "0.25")
s2_probability_label.grid(row=3, column=0, padx=5, pady=0, sticky="w")
s2_probability_entry.grid(row=3, column=1, padx=5, pady=0)

s3_probability_label = tk.Label(root, text="S3 probability")
s3_probability_entry = tk.Entry(root)
# Set the default value for the S3 probability
s3_probability_entry.insert(0, "0.25")
s3_probability_label.grid(row=4, column=0, padx=5, pady=0, sticky="w")
s3_probability_entry.grid(row=4, column=1, padx=5, pady=0)

s4_probability_label = tk.Label(root, text="S4 probability")
s4_probability_entry = tk.Entry(root)
# Set the default value for the S4 probability
s4_probability_entry.insert(0, "0.25")
s4_probability_label.grid(row=5, column=0, padx=5, pady=0, sticky="w")
s4_probability_entry.grid(row=5, column=1, padx=5, pady=0)

# Add a button to run the simulation
run_button = tk.Button(root, text="Run Simulation", command=run_simulation)
run_button.grid(row=6, column=0, columnspan=2, padx=5, pady=5)

# Start the main loop
root.mainloop()

