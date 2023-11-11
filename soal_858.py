import sys
print("Selamat datang di layanan *858# Telkomsel")
print("Pilih menu yang Anda inginkan:")

def send():
    tombol = input("Tekan 'send' untuk lanjut atau 'cancel' untuk keluar: ")
    if tombol.lower() == 'cancel' and tombol != "":
        print("Terima kasih, keluar dari layanan *858#.")
        sys.exit()
    elif tombol.lower() == 'send' and tombol != "":
        pass
    else:
        send()

def menuOK():
    yakin = input("send / cancel: ")
    if yakin.lower() == 'cancel' and yakin != "":
        menu()
    elif yakin.lower() == 'send' and yakin != "":
        pass
    else:
        menuOK()

def YaBack():
    print("1. Ya")
    print("2. Back")
    answer = int(input())
    if answer == 1:
        print("")
    else:
        print(" ")
        menu()
    

def menu():
    print("Mau Samsung Fold 4 dr Aldi Taher?")
    print("Hub di *500*352#")
    print("1. Transfer Pulsa")
    print("2. Minta Pulsa")
    print("3. Auto Top-Up")
    print("4. Hapus Auto Top-Up")
    print("5. Daftar Auto Top-Up")
    print("6. Cek Kupon Undian Top-Up")

    choice = int(input("Masukkan angka menu: "))

    if choice == 1:
        menuOK()
        # Implementasi logika untuk Transfer Pulsa
        nomor_tujuan = int(input("Silahkan masukkan nomor tujuan Transfer Pulsa : (contoh: 08xxxx atau 628xxxx)\n "))
        send()
        jumlah_pulsa = int(input("Silahkan masukkan jumlah pulsa yang akan ditransfer :(min 5000, max 1 jt & tanpa.(titik) atau , (koma))\n "))
        send()
        print("Hati2 penipuan. Anda akan Transfer pulsa ", jumlah_pulsa , "ke nomor", nomor_tujuan, "?","(Biaya 1850 & 1Poin undian TP iphone14")
        YaBack()
        print("Transfer pulsa anda berhasil")
    elif choice == 2:
        menuOK()
        # Implementasi logika untuk Minta Pulsa
        nomor_pinjam = int(input("Silahkan masukkan nomor tujuan Minta Pulsa: (contoh: 08xxxx atau 628xxxx)\n"))
        send()
        pulsa_pinjam = int(input("Silahkan masukkan jumlah pulsa yang akan diminta : (min 5000, max 1 jt & tanpa.(titik) atau , (koma))\n "))
        send()
        print("Anda akan meminta pulsa: ", pulsa_pinjam, "ke nomor", nomor_pinjam, "? (biaya Rp. 100)" )
        YaBack()
        print("Terima kasih permintaan Anda sedang diproses")
        

    elif choice == 3:
        menuOK()
        print("Anda memilih Auto Top-Up")
            # Implementasi logika untuk Auto Top-Up
        noAuto = int(input("Silahkan masukkan nomor tujuan yg Anda Auto Transfer Pulsa: \n"))
        send()

        jumAuto = int(input("Silahkan masukkan jumlah pulsa yang akan ditransfer :(min 5000, max 1 jt & tanpa.(titik) atau , (koma))\n" ))
        send()
        tglAuto= int(input("Silahkan masukkan tanggal transfer,\n(cth: 15)\n"))
        send()
        print("Hati2 penipuan. Anda akan Transder pulsa", jumAuto, " ke nomor", noAuto , " setiap tanggal", tglAuto, "? (biaya 1850 & 1Poin undian TP iPhone14)")
        YaBack()
        print("Terima kasih permintaan Anda sedang diproses")


    elif choice == 4:
        menuOK()
        print("Anda memilih Hapus Auto Top-Up")
            # Implementasi logika untuk Hapus Auto Top-Up
        DelnoAuto = int(input("Silahkan masukkan nomor tujuan yang akan dihapus dari list Auto\nTransfer Pulsa:\n"))
        send()
        print("Anda akan menghapus nomor", DelnoAuto, "dari daftar Auto Transfer Anda?")
        print("1.Setuju")
        print("06.Back")
        print("07.Home")
        deljawab = int(input())
        send()
        if deljawab == 1:
            print("Terima kasih permintaan Anda sedang diproses")
        else:
            print("Terima kasih, keluar dari layanan *858#.")
            sys.exit()
        
    elif choice == 5:
        menuOK()
            # Implementasi logika untuk Daftar Auto Top-Up
        print("Informasi akan dikirimkan lewat pesan")
            
    elif choice == 6:
        menuOK()
        print("Jumlah kupon Anda: ")
            # Implementasi logika untuk Cek Kupon Undian Telkomsel
        pass
    else:
        print("Pilihan tidak valid. Silakan pilih angka menu (1-6) atau t ekan Cancel.")

menu()
