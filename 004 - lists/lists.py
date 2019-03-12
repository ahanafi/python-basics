
#declare integer of array
data = [1, 4, 3, 21, 55, 101]

#getting by index or array
first = data[0]
last = data[-1] #get from last index array

#Cuting list
many = data[2:4]
many2 = data[:4]

second_data = [100, 200, 300, 400, 500, 600, 700, 800]

#Adding to list
master = data + second_data

#Change data in lists
data[4] = 234

#Copied list to new variable
a = data[:]

#Change item lists with slicing method
data[3:4] = [33, 45]
print(data)