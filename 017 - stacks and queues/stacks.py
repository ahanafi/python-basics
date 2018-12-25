tumpukan = [1,2,3,4,5,6]
print("List asli ",tumpukan)

# masukkan item baru ke list
tumpukan.append(7)
print("Data masuk:", 7)
print("List baru", tumpukan)

tumpukan.append(8)
print("Data masuk:", 8)
print("List baru", tumpukan)

# Menghilangkan data paling belakang
out = tumpukan.pop()
print("Data keluar:", out)
print("List saat ini", tumpukan)
