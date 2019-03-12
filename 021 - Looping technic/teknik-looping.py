# Teknik Looping

bahasa = [
    "Python", "PHP", "Javascript", "Java", "C++", "HTML", "XML", "Ruby"
]

programmers = [
    "Andi", "Budi", "Coki", "Deni", "Eka", "Fuad", "Gofur", "Husen"
]
# Manual
index = 0
for i in bahasa:
    print("Index ke-",index, "adalah ", i)
    index+=1

print(100*"=")
print("Menggunana enumerate")

# enumerate
for i,lang in enumerate(bahasa):
    print("Index ke: ",i," adalah", lang)

print(100*"=")
print("Menampilkan isi 2 list dalam 1 looping")

# zip
for lang,dev in zip(bahasa, programmers):
    print(dev, "menguasai bahasa ",lang)
