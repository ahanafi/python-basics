from collections import deque

antrian = deque([1,2,3,4,5])

print("Data sekarang ",antrian)

# Menambahkan data
antrian.append(6)
print("Data masuk: ", 6)
print("Data sekarang ",antrian)

antrian.append(7)
print("Data masuk: ", 7)
print("Data sekarang ",antrian)

# Mengurangi antrian dari sebelah kiri
out = antrian.popleft()
print("Data keluar", out)
print("Data sekarang ",antrian)

out = antrian.popleft()
print("Data keluar", out)
print("Data sekarang ",antrian)

antrian.append(8)
print("Data masuk: ", 8)
print("Data sekarang ",antrian)