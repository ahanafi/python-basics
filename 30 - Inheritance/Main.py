class Ojek():

    def __init__(self, nama, transmisi, daerah):
        self.nama = nama
        self.transmisi = transmisi
        self.daerah = daerah

    def cek_id(self):
        print("Nama driver :", self.nama)
        print('Motor :', self.transmisi)
        print('Daerah :', self.daerah)
        print(50*"=")


# Turunan dari kelas Ojek
class Gojek(Ojek):
    pass

# Turunan dari kelas Ojek
class Grab(Ojek):
    pass

ojek1 = Gojek("Mario", "Manual", "Jakarta Selatan")
ojek2 = Grab("Jacky", "Automatic", "Surabayar")

ojek1.cek_id()
ojek2.cek_id()