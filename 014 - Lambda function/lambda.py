# Basic function dengan argument
def jumlahkan(a, b):
    c = a + b
    return  c

hasil = jumlahkan(10, 5)
print(hasil)

print("==="*50)

# Membuat anonymous function dengan lambda
print("Lambda function")

kali = lambda x, y: x * y

hasil2 = kali(10, 3)
print(hasil2)