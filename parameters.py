import numpy as np


class parameters:
    # Define the grid size
    grid_size = 100

    # Define the levels of skepticism
    skepticism_levels = ["S1", "S2", "S3", "S4"]

    # Define the parameters for rumor transmission
    transmission_probabilities = {
        "S4": 0,
        "S3": 1 / 3,
        "S2": 2 / 3,
        "S1": 1
    }

    # Define the parameters for skepticism reduction when faced with multiple rumors
    skepticism_reduction = {
        "S4": "S3",
        "S3": "S2",
        "S2": "S1",
        "S1": "S1"
    }

    def update_param(self, population_density_up, no_rumor_time_up, skepticism_distribution_up):
        # update the population density
        self.population_density = population_density_up
        # Define the number of generations to wait until spreading a rumor again
        self.no_rumor_time = no_rumor_time_up
        # Define the percentage of the population that has each level of skepticism
        self.skepticism_distribution = skepticism_distribution_up
        # Assign skepticism levels to the population
        self.skepticism = np.random.choice(self.skepticism_levels, size=(self.grid_size, self.grid_size),
                                      p=[self.skepticism_distribution[s] for s in self.skepticism_levels])

