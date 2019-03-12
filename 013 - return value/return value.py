# Function dengan return value

def kuadratkan(angka):
    total = angka**2
    return total

kuadrat = kuadratkan(5)
print("Hasil 5^2 adalah ", kuadrat)

print(10*"===")

# Fungsi Multiple argument

def tambahin(angka1, angka2):
    total = angka1 + angka2
    return total

a = kuadratkan(5)
hasil = tambahin(25, a)
print(hasil)