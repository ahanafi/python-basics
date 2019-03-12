import sys

data_list = [1,2,3,4,5,6,7,8, "Kelas", "Terbuka", "Sekolah", "Koding", 3.14]
data_tuple = (1,2,3,4,5,6,7,8, "Kelas", "Terbuka", "Sekolah", "Koding", 3.14)

besar_datalist = sys.getsizeof(data_list)
besar_datatuple = sys.getsizeof(data_tuple)

print("Besar data list adalah :", besar_datalist)
print("Besar data tuple adalah :", besar_datatuple)