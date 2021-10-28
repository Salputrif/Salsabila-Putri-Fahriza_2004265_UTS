class Uang:
    def __init__(self,saldo_umum, saldo_tabungan,tambah_umum,tambah_tabungan, ambil_umum,ambil_tabungan):
        self.saldo=saldo_umum
        self.saldo1=saldo_tabungan
        self.tambah=tambah_umum
        self.tambah1=tambah_tabungan
        self.ambil=ambil_umum
        self.ambil1=ambil_tabungan

    def saldo_umum(self):
        print("Saldo umum Anda saat ini adalah: Rp.0,-", self.saldo)

    def saldo_tabungan(self):
        print("Saldo tabungan Anda saat ini adalah: Rp.0,-", self.saldo1)

    def tambah_umum(self):
        print("Nominal uang yang akan ditambahkan :", self.tambah)

    def tambah_tabungan(self):
        print("Nominal uang yang akan ditambahkan :", self.tambah1)

    def ambil_umum(self):
        print("Nominal Uang yang akan diambil :", self.ambil)
    
    def ambil_tabungan(self):
        print("Nominal Uang yang akan diambil :", self.ambil1)


#Kelas Turunan

class InformasiUm(Uang):
    def Infoumum(self):
        Uang.saldo_umum(self)

    def keterangan(self):
        print("Saldo umum Anda saat ini adalah: Rp.0,-")

class InformasiTab(Uang):
    def InfoTabungan(self):
        Uang.saldo_tabungan(self)

    def keterangan(self):
        print("Saldo Tabungan Anda saat Ini adalah: Rp.0,-")

class TambahUm(Uang):
    def TambahUmum(self):
        Uang.tambah_umum(self)

    def keterangan(self):
        print("Nominal uang yang akan ditambahkan :")

class TambahTab(Uang):
    def TambahTabungan(self):
        Uang.tambah_tabungan(self)

    def keterangan(self):
        print("Nominal Uang yang akan Ditambahkan :")

class AmbilUm(Uang):
    def AmbilUmum(self):
        Uang.ambil_umum(self)

    def keterangan(self):
        print("Nominal Uang yang akan diambil :")

class AmbilTab(Uang):
    def AmbilTabungan(self):
        Uang.ambil_tabungan(self)      

    def keterangan(self):
        print("Nominal Uang yang akan diambil :")  

print("***Aplikasi Pencatatan Uang Digital***")
print("**************************************")
print("[1] Informasi Saldo")
print("[2] Tambah Saldo")
print("[3] Ambil Saldo")
print("[4] Keluar")
print("**************************************")
option=int(input("PIlih Menu:"))
if option==1:
    i=InformasiUm
    i.Infoumum
    i.keterangan

    i=InformasiTab
    i.InfoTabungan
    i.keterangan

elif option==2:
    print("[1] Umum")
    print("[2] Tabungan")
    option=int(input("Pilih Penyimpanan:"))
    print("**************")
if option==1:
    i=TambahUm
    i.TambahUmum()
    i.keterangan()
elif option==2:
    i=TambahTab
    i.TambahTabungan
    i.keterangan

elif option==3:
    print("[1] Umum")
    print("[2] Tabungan")
    option=int(input("Pilih Penyimpanan:"))
    print("**************")
if option==1:
    i=AmbilUm
    i.AmbilUmum
    i.keterangan
elif option==2:
    i=AmbilTab
    i.AmbilTabungan
    i.keterangan
