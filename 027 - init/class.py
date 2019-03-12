class Mahasiswa():

    # Init adalah method otomatis yang pertama kali dijalankan
    # ketika class di instance -kan
    def __init__(self, nama_mhs, nim_mhs):
        self.nama = nama_mhs
        self.nim = nim_mhs
        print("Nama saya adalah", self.nama, "dengan NIM =>", self.nim)

    def belajar(self, kondisi):
        print(self.nama, "sedang belajar", kondisi)

    def tidur(self):
        print(self.nama, "sedang tidur di kelas")

ahmad = Mahasiswa("Ahmad Hanafi", 2017102020)