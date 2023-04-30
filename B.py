import numpy as np
from parameters import parameters
from logic import init_simulation, one_generation


# this function updates csv file with the generation number and the number of people that have the rumor
def update_csv(percentage_of_people_who_heard_the_rumor, number_of_sim, file_name,p, l, s_values):
    global count_gen
    global num_people
    with open(file_name, 'a') as f:
        f.write(str(number_of_sim) + ',' + str(count_gen) + ',' +str(round(percentage_of_people_who_heard_the_rumor, 2))
             +','+str(p) + ',' + str(l) + ','+ str(s_values)[13:-2]+ "\n")


# create a dictionary of the parameters to run simulations:
param_dict = {"population_density": [0.7, 0.5], "no_rumor_time": 5, "skepticism": {"S1": 0.25, "S2": 0.25, "S3": 0.25, "S4": 0.25}}
number_of_iteration = 0
for j in range(2):
    number_of_iteration += 1
    param = parameters()
    param.update_param(param_dict["population_density"][j], param_dict["no_rumor_time"], param_dict["skepticism"])
    count_gen = 0
    filename = str("csv/data_no_location" + str(number_of_iteration) + ".csv")
    # delete the csv file content if it exists
    with open(filename, 'w') as f:
        f.write("")
    for i in range(10):
        grid, color_grid = init_simulation(param)
        num_people = np.sum(grid == 1) + 1
        count_gen = 0
        # write to csv file the number of the simulation
        while True:
            # run one generation of the simulation
            grid, color_grid = one_generation(grid, color_grid, param)
            percentage_people_who_heard_the_rumor = np.sum(color_grid==2) * 100 / num_people
            # every 10 generations, write the results to csv file
            # if count_gen%2==0:
            # update_csv(percentage_people_who_heard_the_rumor, i, filename, param_dict["population_density"][j], param_dict["no_rumor_time"], param_dict["skepticism"].values())
            # check if the rumor has reached 99.7% of the population
            if percentage_people_who_heard_the_rumor > 99.7:
                update_csv(percentage_people_who_heard_the_rumor, i, filename, param_dict["population_density"][j], param_dict["no_rumor_time"], param_dict["skepticism"].values())
                break
            # check if the simulation should stop
            elif np.sum(grid == -1) == 0 or np.sum(color_grid == 1) == 0 or count_gen>1000:
                update_csv(percentage_people_who_heard_the_rumor, i, filename, param_dict["population_density"][j], param_dict["no_rumor_time"], param_dict["skepticism"].values())
                break
            else:
                update_csv(percentage_people_who_heard_the_rumor, i, filename, param_dict["population_density"][j], param_dict["no_rumor_time"], param_dict["skepticism"].values())
            count_gen += 1