# dalys.py
import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

data_file_path ='c:\Users\彭成远\Desktop\IBI\IBI1_2023-24\Practical_7\dalys-rate-from-all-causes(1).csv'
os.chdir(os.path.dirname(data_file_path))
dalys_data = pd.read_csv("dalys-rate-from-all-causes(1).csv")

print(dalys_data.iloc[0:100:10, 3])

afghanistan_dalys = dalys_data[dalys_data['Entity'] == 'Afghanistan']['DALYs']
print(afghanistan_dalys)

china_data = dalys_data[dalys_data['Entity'] == 'China']
mean_dalys_china = china_data['DALYs'].mean()
china_2019_dalys = china_data[china_data['Year'] == 2019]['DALYs'].values[0]
print(f"Mean DALYs in China: {mean_dalys_china}")
print(f"DALYs in China in 2019: {china_2019_dalys}")
print(f"Was 2019 above or below the mean DALYs in China? {'Above' if china_2019_dalys > mean_dalys_china else 'Below'}")

plt.plot(china_data['Year'], china_data['DALYs'], 'b+')
plt.xlabel('Year')
plt.ylabel('DALYs')
plt.title('DALYs in China Over Time')
plt.xticks(rotation=-90) 
plt.show()


        