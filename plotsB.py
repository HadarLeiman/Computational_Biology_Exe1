import matplotlib.pyplot as plt
import pandas as pd

# read the csv file to a dataframe
df = pd.read_csv('csv/data_location21.csv', header=None, names=['simulation', 'generation', 'percentage', 'P', 'L', 's1', 's2', 's3', 's4'])
df2 = pd.read_csv('csv/data_no_location1.csv', header=None, names=['simulation', 'generation', 'percentage', 'P', 'L', 's1', 's2', 's3', 's4'])

# add a count column to the dataframe that resets to 0 every time the generation number change to zero again
df['count'] = df.groupby('simulation')['generation'].transform(lambda x: (x != x.shift()).cumsum())
df2['count'] = df2.groupby('simulation')['generation'].transform(lambda x: (x != x.shift()).cumsum())

# add a column called generationMaxcount that contains the max value of the count column for each simulation
df['generationMaxcount'] = df.groupby('simulation')['count'].transform('max')
df2['generationMaxcount'] = df2.groupby('simulation')['count'].transform('max')


# get the min value from all the simulationMaxcount column
min_count = df['generationMaxcount'].min()
print("df")
print(min_count)
min_count = df2['generationMaxcount'].min()
print("df2")
print(min_count)

# add a binary column called newDataFrame that indicate 1 if the count column twice 2 is smaller or equal then the min_count and 0 otherwise
df['newDataFrame'] = df['count']  <= min_count
df2['newDataFrame'] = df2['count']  <= min_count

#create a new data frame that is called df2 and contains only the rows that have 1 in the newDataFrame column
df_new = df[df['newDataFrame'] == 1]
df2_new = df2[df2['newDataFrame'] == 1]
# save the new data frame into csv file
df_new.to_csv('csv/data_location21_new.csv', index=False)
df2_new.to_csv('csv/data_no_location1_new.csv', index=False)

# calculate the average percentage for each generation in df_new and df2_new
df_avg = df_new.groupby('generation').mean()
df2_avg = df2_new.groupby('generation').mean()

print(df_avg)
print(df2_avg)

#plot df_new and df2_new average on the same plot
plt.plot(df_avg['percentage'], marker='', linestyle='solid', label='Pattern')
plt.plot(df2_avg['percentage'], marker='', linestyle='solid', label='No Pattern')
plt.title('Average percentage of people exposed to rumor')
plt.xlabel('Generation')
plt.ylabel('Exposed to rumor (%)')
plt.legend()
plt.show()



# # plot the average percentage of people exposed to rumor
# plt.plot(df2['generation'], df2['percentage'], marker='', linestyle='solid', label='Average')
# plt.title('Average percentage of people exposed to rumor')
# plt.xlabel('Generation')
# plt.ylabel('Exposed to rumor (%)')
# # calculate the slope
# # if len(df2) > 1:
# #     slope = (df2['percentage'][len(df2)-1] - df2['percentage'][0]) / (df2['generation'][len(df2)-1] - df2['generation'][0])
# #     # plot the slope as rate in a column above the plot
# #     plt.text(0.5, 0.9, 'Rate of spread: ' + str(round(slope,2)), horizontalalignment='center', verticalalignment='center', transform=plt.gca().transAxes)
# # plot the p l AND s parameters on the plot
# plt.text(0.5, 0.8, 'p = ' + str(df['P'][0]) + ' l = ' + str(df['L'][0]) + ' s = ' + str(df['s1'][0]) + ' ' + str(df['s2'][0]) + ' ' + str(df['s3'][0]) + ' ' + str(df['s4'][0]), horizontalalignment='center', verticalalignment='center', transform=plt.gca().transAxes)
# # show plot
# plt.show()