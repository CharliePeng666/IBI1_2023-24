import matplotlib.pyplot as plt

UK_cities=[0.56,0.62,0.04,9.7]
CN_cities=[0.58,8.4,29.9,22.2]

UK=["Edinburgh","Glsgow","Stirling","London"]

CN=["Haning","Hangzhou","Shanghai","Beijing"]
UK_cities.sort()
CN_cities.sort()

print(UK_cities)
print(CN_cities)

plt.figure()
plt.bar(UK,UK_cities)
plt.show()
plt.figure()
plt.bar(CN,CN_cities)
plt.show()
