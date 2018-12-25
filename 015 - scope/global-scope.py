# Scope variable: global

nama = "Ahmad Hanafi"

def rubahNama(namaBaru):
    global nama
    nama = namaBaru
    print("Nama saya dirubah menjadi", nama)

rubahNama("Alhanif")
print("Nama saya saat ini adalah", nama)

print("***"*100)

