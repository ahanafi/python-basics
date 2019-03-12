class Mahasiswa():

    # atribut yang bersifat private
    __nilai = 0
    # atribut yang bersifat public
    prodi = "Teknik Informatika"

    def __init__(self, nama_mhs, nim_mhs):
        self.nama = nama_mhs    # atribut yang bersifat public
        self.nim = nim_mhs      # atribut yang bersifat public

    def uts(self, nilai):
        self.__nilai += nilai

    def uas(self, nilai):
            self.__nilai += nilai

    def cek_nilai(self):
        if self.__nilai <= 50:
            print(self.nama, "tidak lulus")
        else:
            print(self.nama, "lulus")

ahmad = Mahasiswa("Ahmad Hanafi", 2017102020)
ahmad.uts(90)
ahmad.uas(85)
ahmad.cek_nilai()