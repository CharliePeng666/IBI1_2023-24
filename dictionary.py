time_management={'sleeping':8,'classes':6,'studying':3.5,'TV':2,'music':1,'other':3.5}

import matplotlib.pyplot as plt
activities=['sleeping','classes','studying','TV','music','other']
time_duration=[8,6,3.5,2,1,3.5]
plt.figure()
plt.pie(time_duration,labels=activities,startangle=90)
plt.show()