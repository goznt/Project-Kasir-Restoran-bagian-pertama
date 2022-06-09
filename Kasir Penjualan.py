
menu = "y" or "Y"
while menu == "y" or "Y":
    print(" -------------------------------------------")
    print(" |Selamat Datang Di Restoran Padang Sambian | ")
    print(" |Menu Restoran Padang Sambian              |")
    print(" -------------------------------------------")
    print(" ===========================================")
    print("|   KETUT GEDE RAI WISTIKA PUTRA_210030178  |")
    print("|===========================================|")
    print("| 1. Ayam Gulai : Rp 16.000                 |")
    print("| 2. Kambing Bakar : Rp 35.000              |")
    print("| 3. Sate Babi : Rp 28.000                  |")
    print("| 4. Paket Hemat : Rp 25.000                |")  
    print("| 5. Paket Spesial : Rp. 40.000             |")
    print("| ==========================================|")
    listMenu=str(input(" Masukkan Menu yang Anda Pilih = "))
    jumlahPesanan=int(input(" Jumlah dibeli = "))
    if listMenu == "1":
        namaMenu= " Ayam Gulai"
        harga=(16000*jumlahPesanan)
        pajak= int(harga * 0.1)
        if jumlahPesanan >= 5:
            totalHarga=int(harga+pajak)
        else:
            totalHarga=int(harga+pajak)
    elif listMenu == "2":
        namaMenu= "Kambing Bakar"
        harga = (35000*jumlahPesanan)
        pajak = int(harga * 0.1)
        if jumlahPesanan >= 5:
            totalHarga =int(harga+pajak)
        else:
            totalHarga =int(harga+pajak)
    elif listMenu == "3":
        namaMenu= " Sate Ayam"
        harga=int(28000*jumlahPesanan)
        pajak = int(harga * 0.1)
        totalHarga=int(harga+pajak)
    elif listMenu == "4":
        namaMenu= " Paket Hemat"
        harga=int(25000*jumlahPesanan)
        pajak = int(harga * 0.1)
        totalHarga = int(harga+pajak)
    elif listMenu == "5":
        namaMenu= " Paket Spesial"
        harga=int(40000*jumlahPesanan)
        pajak = int(harga * 0.1)
        totalHarga = int(harga+pajak)
    else:
        menu=input("Mohon Maaf,Menu Yang Anda Pilih Tidak Tersedia Di Restoran :)")
 
    print(" ------------------------------")
    print(" Menu Yang Akan Dipesan :",namaMenu)
    print(" Jumlah Pesanan :", jumlahPesanan)
    print(" Harga Makanan :", harga)
    print(" Pajak :", pajak)
    print(" ------------------------------")
    print(" Total Pembayaran :", totalHarga)
    print(" ------------------------------")
    menu=input(" Apakah Anda Mau Pesan Makanan lagi? pilih Y (yes) jika Ya, pilih N (NO) jika Tidak (Y/N) = ")