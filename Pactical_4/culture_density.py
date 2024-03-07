cell_density=0.05
number_of_days=0
while cell_density<=0.9: #when cell density <= 90%, continue the while loop
    cell_density=cell_density*2 #As every while loop is working, cell density doubles
    number_of_days=number_of_days+1 #As every while loop is working, number of days increases by 1
str(number_of_days) #make the variable "number of days" (number) into a string
print("the number of days required to exceed 90% is ", number_of_days) #print the results

#results: the number of days required to exceed 90% is  5
# 4 is the maximum number of days I	can	have a holiday from the	lab