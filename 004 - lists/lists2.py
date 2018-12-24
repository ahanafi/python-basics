#list didalam list
data1 = [1, 4, 3, 21, 55, 101]
data2 = [100, 200, 300, 400, 500, 600, 700, 800]

data = [data1, data2]

#mengakses list dengan multidimensional lists
list1 = data[0]
list_hundred = data[1][0]

#Menambah item ke list
data1.append(200)

#menghitung panjang list
length = len(data1)
print(length)