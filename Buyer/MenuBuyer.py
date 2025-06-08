# Buyer/MenuBuyer.py
from Data.PathData import KENDARAAN_JSON, ANTRIAN_JSON, RIWAYAT_JSON
from Buyer.StatusPenyewaan import status_penyewaan
import json

def muat_kendaraan():
    try:
        with open(KENDARAAN_JSON, 'r') as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def muat_antrian():
    try:
        with open(ANTRIAN_JSON, 'r') as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def simpan_antrian(data):
    with open(ANTRIAN_JSON, 'w') as file:
        json.dump(data, file, indent=4)

def muat_riwayat():
    try:
        with open(RIWAYAT_JSON, 'r') as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def menu_buyer():
    while True:
        print("\nMenu Buyer (Penyewa Rental):")
        print("1. List Kendaraan")
        print("2. Status Penyewaan Anda")
        print("3. Kembali ke Menu Utama")

        pilihan = input("Pilih menu: ").strip()

        if pilihan == '1':
            list_kendaraan()
        elif pilihan == '2':
            status_penyewaan()  # Now properly imported from separate file
        elif pilihan == '3':
            break
        else:
            print("\nPilihan tidak valid, coba lagi.")

def list_kendaraan():
    kendaraan = muat_kendaraan()
    if not kendaraan:
        print("\nData kendaraan kosong.")
        return

    print(f"\n{'No':<4} {'Nama':<15} {'Ukuran':<8} {'Stok':<6} {'Harga per hari':<15}")
    print("-" * 50)
    for idx, k in enumerate(kendaraan, 1):
        print(f"{idx:<4} {k['nama']:<15} {k['ukuran']:<8} {k['stok']:<6} Rp{k['harga_perhari']:<14,.0f}")

    pilih = input("\nPilih nomor kendaraan untuk sewa (atau enter untuk batal): ").strip()
    if not pilih:
        return

    try:
        nomor = int(pilih)
        if nomor < 1 or nomor > len(kendaraan):
            print("\nNomor tidak valid.")
            return
    except ValueError:
        print("\nInput harus angka.")
        return

    kendaraan_pilih = kendaraan[nomor-1]
    if kendaraan_pilih['stok'] <= 0:
        print("\nMaaf, stok kendaraan ini sedang kosong.")
        return

    proses_sewa(kendaraan_pilih)

def proses_sewa(kendaraan_pilih):
    print("\nInput Data Penyewa:")
    nik = input("NIK: ").strip()
    nama = input("Nama Lengkap: ").strip()
    no_hp = input("No HP: ").strip()
    
    try:
        hari = int(input("Berapa hari sewa: ").strip())
        if hari < 1:
            print("\nHari sewa harus minimal 1.")
            return
    except ValueError:
        print("\nInput hari harus angka.")
        return

    antrian = muat_antrian()
    data_sewa = {
        "nik": nik,
        "nama": nama,
        "no_hp": no_hp,
        "kendaraan": kendaraan_pilih['nama'],
        "ukuran": kendaraan_pilih['ukuran'],
        "harga_perhari": kendaraan_pilih['harga_perhari'],
        "hari": hari,
        "status": "pending"
    }
    antrian.append(data_sewa)
    simpan_antrian(antrian)
    print("\nSewa berhasil dimasukkan ke antrian. Silakan tunggu konfirmasi owner.")