import json
import os
from Data.PathData import KENDARAAN_JSON

def muat_kendaraan():
    if not os.path.exists(KENDARAAN_JSON):
        return []
    with open(KENDARAAN_JSON, 'r') as file:
        try:
            return json.load(file)
        except json.JSONDecodeError:
            return []

def simpan_kendaraan(data):
    with open(KENDARAAN_JSON, 'w') as file:
        json.dump(data, file, indent=4)

def tampil_kendaraan():
    kendaraan = muat_kendaraan()
    if not kendaraan:
        print("Data kendaraan kosong.")
        return

    print(f"{'No':<4} {'Nama':<15} {'Ukuran':<10} {'Stok':<6} {'Harga per Hari':<20}")
    print("-" * 60)
    for idx, k in enumerate(kendaraan, 1):
        print(f"{idx:<4} {k['nama']:<15} {k['ukuran']:<10} {k['stok']:<6} Rp{k['harga_perhari']:<20,}")

def tambah_kendaraan():
    print("\n--- Tambah Kendaraan ---")
    nama = input("Nama Mobil         : ").lower()
    ukuran = input("Ukuran (2/4/6 seat): ")
    try:
        stok = int(input("Stok Tersedia      : "))
        harga = int(input("Harga per Hari     : "))
    except ValueError:
        print("Input harus berupa angka untuk stok dan harga.")
        return

    kendaraan = muat_kendaraan()
    kendaraan.append({
        "nama": nama,
        "ukuran": ukuran,
        "stok": stok,
        "harga_perhari": harga
    })
    simpan_kendaraan(kendaraan)
    print("✅ Kendaraan berhasil ditambahkan.\n")

def edit_hapus_kendaraan():
    kendaraan = muat_kendaraan()
    if not kendaraan:
        print("Belum ada data kendaraan.")
        return

    print("--- Daftar Kendaraan ---")
    print(f"{'No':<4} {'Nama':<15} {'Ukuran':<10} {'Stok':<6} {'Harga per Hari':<20}")
    print("-" * 60)
    for idx, k in enumerate(kendaraan, 1):
        print(f"{idx:<4} {k['nama']:<15} {k['ukuran']:<10} {k['stok']:<6} Rp{k['harga_perhari']:<20,}")

    try:
        idx = int(input("Pilih nomor kendaraan (0 untuk batal): ")) - 1
    except ValueError:
        print("Input tidak valid.")
        return

    if idx == -1:
        return

    if 0 <= idx < len(kendaraan):
        print("1. Edit")
        print("2. Hapus")
        aksi = input("Pilih aksi: ")

        if aksi == '1':
            data_lama = kendaraan[idx]

            nama_baru = input(f"Nama Baru        ({data_lama['nama']}): ").strip()
            ukuran_baru = input(f"Ukuran Baru      ({data_lama['ukuran']}): ").strip()
            stok_baru = input(f"Stok Baru        ({data_lama['stok']}): ").strip()
            harga_baru = input(f"Harga Baru       ({data_lama['harga_perhari']}): ").strip()

            if nama_baru:
                kendaraan[idx]['nama'] = nama_baru.lower()
            if ukuran_baru:
                kendaraan[idx]['ukuran'] = ukuran_baru
            if stok_baru:
                try:
                    kendaraan[idx]['stok'] = int(stok_baru)
                except ValueError:
                    print("Stok harus berupa angka. Perubahan dibatalkan.")
                    return
            if harga_baru:
                try:
                    kendaraan[idx]['harga_perhari'] = int(harga_baru)
                except ValueError:
                    print("Harga harus berupa angka. Perubahan dibatalkan.")
                    return

            simpan_kendaraan(kendaraan)
            print("Data kendaraan diperbarui.")

        elif aksi == '2':
            konfirmasi = input("Yakin ingin menghapus kendaraan ini? (y/n): ")
            if konfirmasi.lower() == 'y':
                kendaraan.pop(idx)
                simpan_kendaraan(kendaraan)
                print("Kendaraan dihapus.")
        else:
            print("Aksi tidak valid.")
    else:
        print("Nomor tidak valid.")


def menu_kendaraan():
    while True:
        print("\n=== MENU KENDARAAN ===")
        tampil_kendaraan()
        print("-" * 60)
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
