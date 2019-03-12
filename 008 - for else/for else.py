#For else

number = 110

for i in range (10,100, 5):
    print(i)

    if i is number:
        print("Angka ", number, "ditemukan!")
        break
else:
    print("Sayang sekali, angka ", number, "tidak ditemukan!")