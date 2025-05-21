from Owner.TambahEditHapus import menu_kendaraan
#from Owner.RiwayatOwner import menu_riwayat
#from Owner.Status import lihat_status_kendaraan

def menu_owner():
    while True:
        print("=== MENU OWNER ===")
        print("1. List Kendaraan")
        print("2. Status Pemesanan/Penyewaan")
        print("3. Kembali ke Menu Utama")

        pilihan = input("Pilih menu (1-3): ")

        if pilihan == '1':
            menu_kendaraan()
        elif pilihan == '2':
            print ("menu_riwayat()")
        elif pilihan == '3':
            break
        else:
            print("Pilihan tidak valid.")
