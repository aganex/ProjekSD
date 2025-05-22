from Owner.TambahEditHapus import menu_kendaraan
from Owner.RiwayatOwner import menu_riwayat
from Owner.Status import proses_pemesanan


def menu_owner():
    while True:
        print("=== MENU OWNER ===")
        print("1. List Kendaraan")
        print("2. Status Pemesanan/Penyewaan")
        print("3. Riwayat Penyewaan")
        print("4. Kembali ke Menu Utama")

        pilihan = input("Pilih menu (1-4): ")

        if pilihan == '1':
            menu_kendaraan()
        elif pilihan == '2':
            proses_pemesanan()
        elif pilihan == '3':
            menu_riwayat()
        elif pilihan == '4':
            break
        else:
            print("Pilihan tidak valid.")
