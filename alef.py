import numpy as np
from parameters import parameters
from logic import init_simulation, one_generation

# update csv file with the generation number and the number of people that have the rumor
def update_csv(percentage_of_people_who_heard_the_rumor):
    global count_gen
    global num_people
    with open('data.csv', 'a') as f:
        f.write(str(count_gen) + ',' + str(percentage_of_people_who_heard_the_rumor)+"\n")

param = parameters()
param.update_param(0.8, 5, {"S1": 0.25, "S2": 0.25, "S3": 0.25, "S4": 0.25})
count_gen = 0

# delete the csv file content if it exists
with open('data.csv', 'w') as f:
    f.write("")
# initialize the simulation

for i in range(10):
    grid, color_grid = init_simulation(param)
    num_people = np.sum(grid == 1) + 1
    count_gen = 0
    # write the to csv file the number of the simulation
    with open('data.csv', 'a') as f:
        f.write(str(i)+"\n")
    while True:
        # run one generation of the simulation
        grid, color_grid = one_generation(grid, color_grid, param)
        percentage_people_who_heard_the_rumor = np.sum(color_grid==2) * 100 / num_people
        # every 10 generations, write the results to csv file
        if count_gen%10==0:
            update_csv(percentage_people_who_heard_the_rumor)
        # check if the rumor has reached 99.7% of the population
        elif percentage_people_who_heard_the_rumor > 99.7:
            update_csv(percentage_people_who_heard_the_rumor)
            break
        # check if the simulation should stop
        elif np.sum(grid == -1) == 0:
            update_csv(percentage_people_who_heard_the_rumor)
            break
        elif np.sum(color_grid == 1) == 0:
            update_csv(percentage_people_who_heard_the_rumor)
            break
        count_gen += 1


