import matplotlib.pyplot as plt #import matplotlib to draw graphs

dic1={"Sleeping":8,"Classes":6,"Studying":3.5,"TV":2,"Music":1} #make a dictionary to record the data correspondence
dic1["other"]=24-dic1["Sleeping"]-dic1["Classes"]-dic1["Studying"]-dic1["TV"]-dic1["Music"]

Activity=["Sleeping","Classes","Studying","TV","Music","other"]
average=[dic1["Sleeping"],dic1["Classes"],dic1["Studying"],dic1["TV"],dic1["Music"],dic1["other"]]
plt.figure()
plt.pie(average,labels=Activity,startangle=90) #use pie graph that is included in the matplotlib
plt.show() #show the graph in a new window
plt.clf() #close the graph

print('What is the average hours spending on each type of activities? Sleeping, Classes, Studying, TV, Music, Other')
user_input = input('Please input one type of activities: ')
if user_input in dic1:
    print('The average hours spending on',user_input,'is',dic1[user_input])
else:
    print('Value error')