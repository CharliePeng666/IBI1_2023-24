import numpy as np
import matplotlib.pyplot as plt

N = 10000
beta, gamma = 0.3, 0.05

def sir_vaccination(N, beta, gamma, vaccination_rate):
    S, I, R = N * (1 - vaccination_rate), 1, N * vaccination_rate
    
    S_arr, I_arr, R_arr = [S], [I], [R]

    for _ in range(1000):
        new_I = np.random.binomial(I, beta * S / N)
        new_R = np.random.binomial(I, gamma)

        S -= new_I
        I -= new_R + new_I
        R += new_R

        S_arr.append(S)
        I_arr.append(I)
        R_arr.append(R)

    return S_arr, I_arr, R_arr

vaccination_rates = np.linspace(0, 1, 11)  
for vac_rate in vaccination_rates:
    S_arr, I_arr, R_arr = sir_vaccination(N, beta, gamma, vac_rate)
    plt.plot(I_arr, label=f'{int(vac_rate * 100)}% Vaccination')

plt.xlabel('Time')
plt.ylabel('Number of Infected')
plt.title('SIR Model with Vaccination')
plt.legend()
plt.show()