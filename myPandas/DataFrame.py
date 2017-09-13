from pandas.io.parsers import read_csv

df = read_csv('sample.csv')
print('Dataframe',df)
print('Shape',df.shape)
print('Length',len(df))
print('Series of Flightno',df['Flightno'])