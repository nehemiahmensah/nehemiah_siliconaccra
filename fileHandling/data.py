#load data file with pandas
import pandas as pd

file_path = "./resources/movies.csv"
#read csv

df = pd.read_csv(file_path)
print(df.head)
#print(df[:5 , 1:])