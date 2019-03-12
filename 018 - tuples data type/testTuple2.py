import timeit

data_list = timeit.timeit(stmt="[1,2,3,4,5,6,7,8,9,10]", number=1000000)
data_tuple = timeit.timeit(stmt="(1,2,3,4,5,6,7,8,9,10)", number=1000000)

print("Waktu untuk memproses list adalah :", data_list)
print("Waktu untuk memproses tuple adalah :", data_tuple)