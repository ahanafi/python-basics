class Mahasiswa():

    jumlah_mhs = 0

    def __init__(self, nama, nim):
        self.nama = nama
        self.nim = nim
        Mahasiswa.jumlah_mhs+= 1

ahmad = Mahasiswa("Ahmad", 2017102020)
hanafi = Mahasiswa("Hanafi", 2017102030)
octa = Mahasiswa("Octa", 20178089)

print(Mahasiswa.jumlah_mhs)