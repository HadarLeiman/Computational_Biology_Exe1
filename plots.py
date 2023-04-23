import matplotlib.pyplot as plt
import pandas as pd

for i in range(1, 36):
    # Load the data from the CSV file
    df = pd.read_csv('csv/data'+str(i)+'.csv', header=None, names=['simulation', 'generation', 'percentage', 'P', 'L', 's1', 's2', 's3', 's4'])

    # Group the data by simulation number
    groups = df.groupby('simulation')

    # Create a scatter plot for each simulation
    for name, group in groups:
        plt.plot(group.generation, group.percentage, marker='', linestyle='solid', label=name)

    # Set the plot labels and legend
    plt.xlabel('Generation')
    plt.ylabel('Exposed to rumor (%)')
    plt.legend(title='Simulation')
    # calculate and display the slope of the plot as rate of spread of the rumor
    slope = (df['percentage'][len(df)-1] - df['percentage'][0]) / (df['generation'][len(df)-1] - df['generation'][0])

    # plot the slope as rate in a column above the plot
    plt.text(0.5, 0.9, 'Rate of spread: ' + str(round(slope,2)), horizontalalignment='center', verticalalignment='center', transform=plt.gca().transAxes)

    # plot the p l AND s parameters on the plot
    plt.text(0.5, 0.8, 'p = ' + str(df['P'][0]) + ' l = ' + str(df['L'][0]) + ' s = ' + str(df['s1'][0]) + ' ' + str(df['s2'][0]) + ' ' + str(df['s3'][0]) + ' ' + str(df['s4'][0]), horizontalalignment='center', verticalalignment='center', transform=plt.gca().transAxes)
    # print the p l AND s parameters of the simulation by the order of the plots
    print("p = ", df['P'][0], "l = ", df['L'][0], "s = ", df['s1'][0], df['s2'][0], df['s3'][0], df['s4'][0])

    # Show the plot
    plt.savefig('plots/plot'+str(i)+'.png')
    plt.show()
