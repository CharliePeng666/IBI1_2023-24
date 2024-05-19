import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

os.chdir("c:/Users/彭成远/Desktop/IBI/IBI1_2023-24/Practical_7")
dalys_data = pd.read_csv("dalys-rate-from-all-causes.csv")
print(dalys_data.head(5))
dalys_data.info()
dalys_data.iloc[2,0:5]
dalys_data.iloc[0:2,:]
dalys_data.iloc[0:10:2,0:5]

for i in range(len(dalys_data)):
    if dalys_data.iloc[:,0]=="Afghanistan":
        print(dalys_data.loc[:,"DALYs"])
        