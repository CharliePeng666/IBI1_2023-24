import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

os.chdir('c:\Users\彭成远\Desktop\IBI\IBI1_2023-24\Practical_7\dalys-rate-from-all-causes(1).csv')

dalys_data = pd.read_csv("dalys-rate-from-all-causes(1).csv")
dalys_data.head(4)
dalys_data.info()
dalys_data.describe()

print(dalys_data.iloc[0:101:10,3])
my_columns=[False,False,False,True]
print(dalys_data.loc[0:29,my_columns])
china_data=dalys_data.iloc[1140:1170,[0,2,3]]
np.mean(china_data.DALYs)

#DALYs in China in 2019 was larger than the mean

plt.plot(china_data.Year, china_data.DALYs, 'b+')
plt.xticks(china_data.Year,rotation=-90)
plt.show()
plt.close()

print(dalys_data[dalys_data.Year==2019].DALYs)
dalys_data_2019=dalys_data[dalys_data.Year==2019]
low_dalys_data=dalys_data_2019[dalys_data_2019.DALYs<18000]
print(low_dalys_data['Entity'])