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
param_dict = {"population_density": [0.9, 0.7, 0.5], "no_rumor_time": [0, 5, 20], "skepticism": [{"S1": 0.25, "S2": 0.25, "S3": 0.25, "S4": 0.25},
                                                                                                {"S1": 0.5, "S2": 0.25, "S3": 0.25, "S4": 0},
                                                                                                {"S1": 0, "S2": 0.25, "S3": 0.25, "S4": 0.5}]}
number_of_iteration = 0
# initialize the simulation
# loop through the parameters of param_dict
for j in range(param_dict["population_density"]):
    for k in range(param_dict["no_rumor_time"]):
        for s in range(param_dict["skepticism"]):
            number_of_iteration += 1
            print(number_of_iteration)
            print("j = ", j, "k = ", k, "s = ", s)
            param = parameters()
            param.update_param(param_dict["population_density"][j], param_dict["no_rumor_time"][k], param_dict["skepticism"][s])
            count_gen = 0
            filename = str("csv/data" + str(number_of_iteration) + ".csv")
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
                    if count_gen%10==0:
                        update_csv(percentage_people_who_heard_the_rumor, i, filename, param_dict["population_density"][j], param_dict["no_rumor_time"][k], param_dict["skepticism"][s].values())
                    # check if the rumor has reached 99.7% of the population
                    elif percentage_people_who_heard_the_rumor > 99.7:
                        update_csv(percentage_people_who_heard_the_rumor, i, filename, param_dict["population_density"][j], param_dict["no_rumor_time"][k], param_dict["skepticism"][s].values())
                        break
                    # check if the simulation should stop
                    elif np.sum(grid == -1) == 0 or np.sum(color_grid == 1) == 0 or count_gen>1000:
                        update_csv(percentage_people_who_heard_the_rumor, i, filename, param_dict["population_density"][j], param_dict["no_rumor_time"][k],  param_dict["skepticism"][s].values())
                        break
                    count_gen += 1
