import pandas as pd

data = pd.DataFrame({"Apples":[35,41],"Bananas":[21,34]})

data.to_csv("fruit.csv")
