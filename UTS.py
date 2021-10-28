print("***Aplikasi Pencatatan Uang Digital***")
print("**************************************")
print("[1] Informasi Saldo")
print("[2] Tambah Saldo")
print("[3] Ambil Saldo")
print("[4] Keluar")
print("**************************************")
option=int(input("PIlih Menu:"))
uang=0
if option==1:
    print("Saldo umum Anda saat ini adalah: Rp.0,-")
    print("Saldo tabungan Anda saat ini adalah: Rp.0,-")
    print("**************************************")
elif option==2:
    print("[1] Umum")
    print("[2] Tabungan")
    option2=int(input("Pilih Penyimpanan:"))
    print("**************************************")
    if option2==1:
    option3=int(input("Nominal uang yang akan ditambahkan :"))
    hasil1=uang+option3
    print("Saldo umum Anda saat ini adalah:",hasil1)
    elif option2==2:
    option4=int(input("Nominal uang yang akan ditambahkan :"))
    hasil2=uang+option4
    print("Saldo umum Anda saat ini adalah:",hasil2)
