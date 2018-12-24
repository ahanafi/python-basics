#IF ELSE IF

nilai = 50
predikat = ''

if 80 <= nilai <= 100:
    predikat = "A"
elif 70  <= nilai < 80:
    predikat = "B"
elif 60 <= nilai < 70:
    predikat = "C"
elif 50 <= nilai < 60:
    predikat = "D"
else:
    predikat = "E"

print("Nilai Anda adalah ", nilai, " mendapatkan predikat ", predikat)
