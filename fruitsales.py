import pandas as pd
"""
This imports the pandas library (module)

Creates a dataframe that has two series, one for 2017 sales and 2018 sales.
"""

data = pd.DataFrame({"Apples":[35,41],"Bananas":[21,34]},index=['2017 Sales','2018 Sales'])

data.to_csv("fruit.csv")
