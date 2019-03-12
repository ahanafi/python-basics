for i in range(1,10):

    if i is 6:
        print("Enam => ", i)
        continue
        print("Cek cek") #Ini tidak akan muncul, karena di atas ada continue

    print("Nilai saat ini adalah ", i)
else:
    print("Akhir dari for")
