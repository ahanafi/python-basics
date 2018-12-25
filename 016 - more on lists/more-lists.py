Kota = [
    "Bandung", "Jakarta", "Bogor", "Bekasi", "Cirebon", "Surabaya"
]
print("List sebelum di modifikasi")
print(Kota)

print("\nList setelah di modifikasi")
# Fungsi untuk menambah item ke list
Kota.append("Palembang")
print(Kota)

# Menambah dengan iterable string (pisah-pisah per huruf)
Kota.extend("Medan")
print(Kota)

# Menambah item ke list dengan index tertentu
Kota.insert(2, "Semarang")
Kota.insert(5, "Cirebon")
print(Kota)

jumlahItem = Kota.count("Cirebon")
print("Jumlah kota Cirebpn di lists ada", jumlahItem)

# Menghapus item dari lists (Remove item yang pertama kali ditemukan!)
Kota.remove("Cirebon")
print(Kota)

# Membalikan urutan item di list
Kota.reverse()
print(Kota)
print(100*"===")
# Mencopy list ke variable baru
DaftarKota = Kota.copy()
DaftarKota.append("Malang")
print("List Kota =>", Kota)
print("List daftar kota => ",DaftarKota)