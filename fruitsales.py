import pandas as pd
"""
This imports the pandas library (module)

Creates a dataframe that is then thrown into a csv at the place the script is ran.

"""

data = pd.DataFrame({"Apples":[35,41],"Bananas":[21,34]},index=['2017 Sales','2018 Sales'])

data.to_csv("fruit.csv")

print(data)

