#For di dalam for

buah = ["Mangga", "Jeruk", "Melon", "Pisang", "Durian", "Pepaya", "Anggur"]
sayur = ["Kangkung", "Kol", "Wortel", "Bawang", "Cabai", "Tomat"]

#Combine lists
combine = [buah, sayur]

for subCombine in combine:
    print("LIST =>", subCombine)
    for comp in subCombine:
        print(comp)