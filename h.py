param_dict = {"population_density": [0.9, 0.5], "no_rumor_time": [3], "skepticism": [{"S1": 0.25, "S2": 0.25, "S3": 0.25, "S4": 0.25}]}
number_of_iteration = 0
# initialize the simulation
for j in range(2):
    for k in range(1):
        for s in range(1):
            print("j = ", j, "k = ", k, "s = ", s)