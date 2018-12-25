# FUnction dengan argumen sederhana
def siswa(nama):
    print("Siswa ini bernama", nama)

siswa("Ahmad")

print(50*"=")

# Function dengan keywords argumen
def guru(nama, pelajaran):
    print("Guru ini bernama", nama)
    print("Mengajar ", pelajaran)

guru("Hilman", "Web Development")
guru(pelajaran="HTML", nama="Sandika Galih")
guru("Faqihza", "Python")

# Fungsi dengan default arguments
def penjagaSekolah(nama, shift = "Pagi", galak = "Tidak"):
    print("Nama penjaga sekolah :", nama)
    print("Shiftnya adalah :", shift)
    print("Galak ? :", galak)

penjagaSekolah("Maman")
penjagaSekolah("Udin", "Malam", "Ya")