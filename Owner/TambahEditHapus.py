import json
import os
from Data.PathData import KENDARAAN_JSON

def muat_kendaraan():
    if not os.path.exists(KENDARAAN_JSON):
        return []
    with open(KENDARAAN_JSON, 'r') as file:
        return json.load(file)

def simpan_kendaraan(data):
    with open(KENDARAAN_JSON, 'w') as file:
        json.dump(data, file, indent=4)

def tambah_kendaraan():
    print("--- Tambah Kendaraan ---")
    nama = input("Nama Mobil       : ").lower()
    ukuran = input("Ukuran (2/4/6 seat): ")
    stok = int(input("Stok Tersedia    : "))
    harga = int(input("Harga per Hari   : "))

    kendaraan = muat_kendaraan()
    kendaraan.append({
        "nama": nama,
        "ukuran": ukuran,
        "stok": stok,
        "harga": harga
    })
    simpan_kendaraan(kendaraan)
    print("Kendaraan berhasil ditambahkan.")

def edit_hapus_kendaraan():
    kendaraan = muat_kendaraan()
    if not kendaraan:
        print("Belum ada data kendaraan.")
        return

    print("--- Daftar Kendaraan ---")
    for i, k in enumerate(kendaraan):
        print(f"{i+1}. {k['nama']} | {k['ukuran']} seat | Stok: {k['stok']} | Rp{k['harga']}")

    idx = int(input("Pilih nomor kendaraan (0 untuk batal): ")) - 1
    if idx == -1:
        return

    if 0 <= idx < len(kendaraan):
        print("1. Edit")
        print("2. Hapus")
        aksi = input("Pilih aksi: ")

        if aksi == '1':
            kendaraan[idx]['nama'] = input("Nama Baru        : ").lower()
            kendaraan[idx]['ukuran'] = input("Ukuran Baru      : ")
            kendaraan[idx]['stok'] = int(input("Stok Baru        : "))
            kendaraan[idx]['harga'] = int(input("Harga Baru       : "))
            simpan_kendaraan(kendaraan)
            print("Data kendaraan diperbarui.")
        elif aksi == '2':
            kendaraan.pop(idx)
            simpan_kendaraan(kendaraan)
            print("Kendaraan dihapus.")
        else:
            print("Aksi tidak valid.")
    else:
        print("Nomor tidak valid.")

def menu_kendaraan():
    while True:
        print("=== MENU KENDARAAN ===")
        print("1. Tambah Kendaraan")
        print("2. Edit/Hapus Kendaraan")
        print("3. Kembali")

        pilihan = input("Pilih menu (1-3): ")
        if pilihan == '1':
            tambah_kendaraan()
        elif pilihan == '2':
            edit_hapus_kendaraan()
        elif pilihan == '3':
            break
        else:
            print("Pilihan tidak valid.")
