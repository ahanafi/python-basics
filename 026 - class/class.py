# definisi class
class Mahasiswa():
    # ini adalah attribut
    nama = "nama"

    # ini adalah method / fungsi
    def belajar(self, kondisi):
        print(self.nama, "sedang belajar", kondisi)

    def tidur(self):
        print(self.nama, "sedang tidur di kelas")

# Instance class Mahasiswa
otong = Mahasiswa()
ucup = Mahasiswa()

# Set nilai atribut nam
otong.nama = "Otong Suroto"
ucup.nama = "Michael Ucup"

otong.belajar("dengan giat")
ucup.tidur()