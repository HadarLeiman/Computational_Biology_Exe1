import matplotlib.pyplot as plt
import pandas as pd

# read the csv file to a dataframe
df1 = pd.read_csv('csv/data1.csv', header=None, names=['simulation', 'generation', 'percentage', 'P', 'L', 's1', 's2', 's3', 's4'])
df4 = pd.read_csv('csv/data4.csv', header=None, names=['simulation', 'generation', 'percentage', 'P', 'L', 's1', 's2', 's3', 's4'])
df7 = pd.read_csv('csv/data7.csv', header=None, names=['simulation', 'generation', 'percentage', 'P', 'L', 's1', 's2', 's3', 's4'])
df10 = pd.read_csv('csv/data10.csv', header=None, names=['simulation', 'generation', 'percentage', 'P', 'L', 's1', 's2', 's3', 's4'])

# add a count column to the dataframe that resets to 0 every time the generation number change to zero again
df1['count'] = df1.groupby('simulation')['generation'].transform(lambda x: (x != x.shift()).cumsum())
df4['count'] = df4.groupby('simulation')['generation'].transform(lambda x: (x != x.shift()).cumsum())
df7['count'] = df7.groupby('simulation')['generation'].transform(lambda x: (x != x.shift()).cumsum())
df10['count'] = df10.groupby('simulation')['generation'].transform(lambda x: (x != x.shift()).cumsum())

# add a column called generationMaxcount that contains the max value of the count column for each simulation
df1['generationMaxcount'] = df1.groupby('simulation')['count'].transform('max')
df4['generationMaxcount'] = df4.groupby('simulation')['count'].transform('max')
df7['generationMaxcount'] = df7.groupby('simulation')['count'].transform('max')
df10['generationMaxcount'] = df10.groupby('simulation')['count'].transform('max')


# get the min value from all the simulationMaxcount column
min_count = df1['generationMaxcount'].min()
print("df")
print(min_count)
min_count = df4['generationMaxcount'].min()
print("df")
print(min_count)
min_count = df7['generationMaxcount'].min()
print("df")
print(min_count)
min_count = df10['generationMaxcount'].min()
print("df")
print(min_count)


# add a binary column called newDataFrame that indicate 1 if the count column twice 2 is smaller or equal then the min_count and 0 otherwise
df1['newDataFrame'] = df1['count']  <= min_count
df4['newDataFrame'] = df4['count']  <= min_count
df7['newDataFrame'] = df7['count']  <= min_count
df10['newDataFrame'] = df10['count']  <= min_count


#create a new data frame that is called df2 and contains only the rows that have 1 in the newDataFrame column
df1_new = df1[df1['newDataFrame'] == 1]
df4_new = df4[df4['newDataFrame'] == 1]
df7_new = df7[df7['newDataFrame'] == 1]
df10_new = df10[df10['newDataFrame'] == 1]

# save the new data frame into csv file
df1_new.to_csv('csv/data_location21_new.csv', index=False)
df4_new.to_csv('csv/data_location21_new.csv', index=False)
df7_new.to_csv('csv/data_location21_new.csv', index=False)
df10_new.to_csv('csv/data_location21_new.csv', index=False)


# calculate the average percentage for each generation in df_new and df2_new
df1_avg = df1_new.groupby('generation').mean()
df4_avg = df4_new.groupby('generation').mean()
df7_avg = df7_new.groupby('generation').mean()
df10_avg = df10_new.groupby('generation').mean()


print(df1_avg)
print(df4_avg)
print(df7_avg)
print(df10_avg)


#plot df_new and df2_new average on the same plot
plt.plot(df1_avg['percentage'], marker='', linestyle='solid', label='L=0')
plt.plot(df4_avg['percentage'], marker='', linestyle='solid', label='L=1')
plt.plot(df7_avg['percentage'], marker='', linestyle='solid', label='L=5')
plt.plot(df10_avg['percentage'], marker='', linestyle='solid', label='L=20')
plt.title('Average percentage of people exposed to rumor')
plt.xlabel('Generation')
plt.ylabel('Exposed to rumor (%)')
plt.legend()
plt.show()

