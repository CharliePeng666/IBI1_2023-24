import numpy as np
import matplotlib.pyplot as plt

N = 10000
S, I, R = N - 1, 1, 0
beta, gamma = 0.3, 0.05

S_arr, I_arr, R_arr = [], [], []

for _ in range(1000):

    S_arr.append(S)
    I_arr.append(I)
    R_arr.append(R)

plt.plot(S_arr, label='Susceptible')
plt.plot(I_arr, label='Infected')
plt.plot(R_arr, label='Recovered')
plt.xlabel('Time')
plt.ylabel('Number of People')
plt.title('SIR Model')
plt.legend()
plt.show()