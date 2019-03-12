#OPERATOR LOGIKA UNTUK LISTS DAN STRING

bahasa = ["PHP", "Python", "Javascript", "C++", "Java", "Ruby", "HTML", "CSS", "NodeJS", "ReactJS"]

py = "Pythonx"

print(bahasa)

if py in bahasa:
    print("bahasa ", py, " ketemu! di list bahasa")
# else:
#    print("bahasa ", py, " ngga ketemu di list!")
if not py in bahasa:
    print("Kata ", py, " ngga ketemu!")

char = "x"

if char in py:
    print(char, "ketemu di ", py)
else:
    print(char, " tidak ketemu")