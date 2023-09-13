import pandas as pd
import matplotlib.pyplot as plt

dict_={'a':[11,21,31],'b':[12,22,32]}

df=pd.DataFrame(dict_)
type(df)

#df = pd.DataFrame(dict_): This line creates a DataFrame named df using the pd.DataFrame() constructor. dict_ should be a dictionary where keys 
#are column names, and values are lists or arrays containing the data for each column. This code initializes a DataFrame with the data provided in the dictionary.
#type(df): This line checks the type of the df variable, which should be a Pandas DataFrame.

df.head() #When you call the method head the dataframe communicates with the API displaying the first few rows of the dataframe.
