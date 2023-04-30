import matplotlib.pyplot as plt
import pandas as pd

# location = [None,1,2,3,4]
#
# for l in location:
for i in range(1,37):
    print('csv/data_'+ str(i)+'.csv')
    # read the csv file to a dataframe
    df = pd.read_csv('csv/data'+ str(i)+'.csv', header=None, names=['simulation', 'generation', 'percentage', 'P', 'L', 's1', 's2', 's3', 's4'])

    # add a count column to the dataframe that resets to 0 every time the generation number change to zero again
    df['count'] = df.groupby('simulation')['generation'].transform(lambda x: (x != x.shift()).cumsum())

    # add a column called generationMaxcount that contains twice the size minus 3 of the max value of the count column for each simulation
    df['generationMaxcount'] = df.groupby('simulation')['count'].transform(lambda x: 2 * x.max() - 3)

    # get the min value from all the simulationMaxcount column
    min_count = df['generationMaxcount'].min()
    print(min_count)

    # add a binary column called newDataFrame that indicate 1 if the count column twice 2 is smaller or equal then the min_count and 0 otherwise
    df['newDataFrame'] = df['count'] * 2 <= min_count

    #create a new data frame that is called df2 and contains only the rows that have 1 in the newDataFrame column
    df2 = df[df['newDataFrame'] == 1]
    # save the new data frame into csv file
    df2.to_csv('csv/data'+ str(i)+'_new.csv', index=False)

    # calculate the average percentage for each generation in df2
    df2 = df2.groupby('generation')['percentage'].mean().reset_index()
    print(df2)


    # plot the average percentage of people exposed to rumor
    plt.plot(df2['generation'], df2['percentage'], marker='', linestyle='solid', label='Average')
    plt.title('Average percentage of people exposed to rumor')
    plt.xlabel('Generation')
    plt.ylabel('Exposed to rumor (%)')
    # calculate the slope
    if len(df2) > 1:
        slope = (df2['percentage'][len(df2)-1] - df2['percentage'][0]) / (df2['generation'][len(df2)-1] - df2['generation'][0])
        # plot the slope as rate in a column above the plot
        plt.text(0.5, 0.9, 'Rate of spread: ' + str(round(slope,2)), horizontalalignment='center', verticalalignment='center', transform=plt.gca().transAxes)
    # plot the p l AND s parameters on the plot
    plt.text(0.5, 0.8, 'p = ' + str(df['P'][0]) + ' l = ' + str(df['L'][0]) + ' s = ' + str(df['s1'][0]) + ' ' + str(df['s2'][0]) + ' ' + str(df['s3'][0]) + ' ' + str(df['s4'][0]), horizontalalignment='center', verticalalignment='center', transform=plt.gca().transAxes)
    # show plot
    plt.show()


        # plt.plot(df['generation'], df['percentage'], marker='', linestyle='solid', label='Average')
        # plt.title('Average percentage of people exposed to rumor')
        # plt.xlabel('Generation')
        # plt.ylabel('Exposed to rumor (%)')
        # plt.text(0.5, 0.7, 'csv/data_'+str(l) + str(i), horizontalalignment='center', verticalalignment='center', transform=plt.gca().transAxes)
        # # plot the p l AND s parameters on the plot
        # plt.text(0.5, 0.8, 'p = ' + str(df['P'][0]) + ' l = ' + str(df['L'][0]) + ' s = ' + str(df['s1'][0]) + ' ' + str(df['s2'][0]) + ' ' + str(df['s3'][0]) + ' ' + str(df['s4'][0]), horizontalalignment='center', verticalalignment='center', transform=plt.gca().transAxes)
        # # print the p l AND s parameters of the simulation by the order of the plots
        # print("p = ", df['P'][0], "l = ", df['L'][0], "s = ", df['s1'][0], df['s2'][0], df['s3'][0], df['s4'][0])
        # plt.show()
        #
        # # Create a scatter plot for each simulation
        # for name, group in groups:
        #     plt.plot(group.generation, group.percentage, marker='', linestyle='solid', label=name)
        #
        # # Set the plot labels and legend
        # plt.xlabel('Generation')
        # plt.ylabel('Exposed to rumor (%)')
        # plt.legend(title='Simulation')
        # # calculate and display the slope of the plot as rate of spread of the rumor
        # slope = (df['percentage'][len(df)-1] - df['percentage'][0]) / (df['generation'][len(df)-1] - df['generation'][0])
        #
        # # plot the slope as rate in a column above the plot
        # plt.text(0.5, 0.9, 'Rate of spread: ' + str(round(slope,2)), horizontalalignment='center', verticalalignment='center', transform=plt.gca().transAxes)
        # plt.text(0.5, 0.7, 'csv/data_'+str(l) + str(i), horizontalalignment='center', verticalalignment='center', transform=plt.gca().transAxes)
        #
        # # plot the p l AND s parameters on the plot
        # plt.text(0.5, 0.8, 'p = ' + str(df['P'][0]) + ' l = ' + str(df['L'][0]) + ' s = ' + str(df['s1'][0]) + ' ' + str(df['s2'][0]) + ' ' + str(df['s3'][0]) + ' ' + str(df['s4'][0]), horizontalalignment='center', verticalalignment='center', transform=plt.gca().transAxes)
        # # print the p l AND s parameters of the simulation by the order of the plots
        # print("p = ", df['P'][0], "l = ", df['L'][0], "s = ", df['s1'][0], df['s2'][0], df['s3'][0], df['s4'][0])
        #
        # # Show the plot
        # plt.savefig('plots/plot'+str(i)+'.png')
        # plt.show()




        # print('csv/data_'+str(l) + str(i)+'.csv')
        #
        # # add a count column to the dataframe that resets to 0 every time the generation number change to zero again
        # df['count'] = df.groupby('simulation')['generation'].transform(lambda x: (x != x.shift()).cumsum())
        #
        # # add a column called generationMaxcount that contains the max value of the count column for each simulation
        # df['simulationMaxcount'] = df.groupby('simulation')['count'].transform('max')
        #
        #
        # # get the min value for each simulation from the simulationMaxcount column
        # min_count = df.groupby('simulation')['simulationMaxcount'].min().min()
        # print(min_count)
        #
        # # add a column that indicate 1 if the count column is smaller or equal then the min_count and 0 otherwise
        # df['min_count'] = df['count'] <= min_count
        #
        # print(df)
        #
        #
        # # calculate the average percentage for each generation that her min_count is True
        # average_percentage = df.groupby('generation')['percentage'].mean().where(df['min_count'] == True).dropna().tolist()
        #
        # # save the average percentage of each generation number to a new dataframe
        # average_df = pd.DataFrame(average_percentage)
        # print(average_df)
        #




    #df = pd.read_csv('csv/data_l'+ str(i)+'.csv', header=None, names=['simulation', 'generation', 'percentage', 'P', 'L', 's1', 's2', 's3', 's4'])
    # Group the data by simulation number
    # groups = df.groupby('simulation')
    #
    # # Create a scatter plot for each simulation
    # for name, group in groups:
    #     plt.plot(group.generation, group.percentage, marker='', linestyle='solid', label=name)
    #
    # # Set the plot labels and legend
    # plt.xlabel('Generation')
    # plt.ylabel('Exposed to rumor (%)')
    # plt.legend(title='Simulation')
    # # calculate and display the slope of the plot as rate of spread of the rumor
    # slope = (df['percentage'][len(df) - 1] - df['percentage'][0]) / (
    #             df['generation'][len(df) - 1] - df['generation'][0])
    # # plot the slope as rate in a column above the plot
    # plt.text(0.5, 0.9, 'Rate of spread: ' + str(round(slope, 2)), horizontalalignment='center',
    #          verticalalignment='center', transform=plt.gca().transAxes)
    # plt.text(0.5, 0.7, 'csv/data_' + str(l) + str(i), horizontalalignment='center', verticalalignment='center',
    #          transform=plt.gca().transAxes)
    #
    # # plot the p l AND s parameters on the plot
    # plt.text(0.5, 0.8,
    #          'p = ' + str(df['P'][0]) + ' l = ' + str(df['L'][0]) + ' s = ' + str(df['s1'][0]) + ' ' + str(
    #              df['s2'][0]) + ' ' + str(df['s3'][0]) + ' ' + str(df['s4'][0]), horizontalalignment='center',
    #          verticalalignment='center', transform=plt.gca().transAxes)
    # # print the p l AND s parameters of the simulation by the order of the plots
    # print("p = ", df['P'][0], "l = ", df['L'][0], "s = ", df['s1'][0], df['s2'][0], df['s3'][0], df['s4'][0])
    #
    # # Show the plot
    # plt.savefig('plots/plot' + str(i) + '.png')
    # plt.show()