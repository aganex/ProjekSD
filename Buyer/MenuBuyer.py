# Buyer/MenuBuyer.py

from Data.PathData import KENDARAAN_JSON, ANTRIAN_JSON, RIWAYAT_JSON
import json

def muat_kendaraan():
    try:
        with open(KENDARAAN_JSON, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        return []

def muat_antrian():
    try:
        with open(ANTRIAN_JSON, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        return []

def simpan_antrian(data):
    with open(ANTRIAN_JSON, 'w') as file:
        json.dump(data, file, indent=4)

def muat_riwayat():
    try:
        with open(RIWAYAT_JSON, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        return []

def menu_buyer():
    while True:
        print("\nMenu Buyer (Penyewa Rental):")
        print("1. List Kendaraan")
        print("2. Status Penyewaan Anda")
        print("3. Kembali ke Menu Utama")

        pilihan = input("Pilih menu: ")

        if pilihan == '1':
            list_kendaraan()
        elif pilihan == '2':
            status_penyewaan()
        elif pilihan == '3':
            break
        else:
            print("Pilihan tidak valid, coba lagi.")

def list_kendaraan():
    kendaraan = muat_kendaraan()
    if not kendaraan:
        print("Data kendaraan kosong.")
        return

    print(f"{'No':<4} {'Nama':<15} {'Ukuran':<8} {'Stok':<6} {'Harga per hari':<15}")
    print("-" * 50)
    for idx, k in enumerate(kendaraan, 1):
        print(f"{idx:<4} {k['nama']:<15} {k['ukuran']:<8} {k['stok']:<6} Rp{k['harga_perhari']:<15,}")
 
 

    pilih = input("\nPilih nomor kendaraan untuk sewa (atau enter untuk batal): ")
    if pilih.strip() == '':
        return

    try:
        nomor = int(pilih)
        if nomor < 1 or nomor > len(kendaraan):
            print("Nomor tidak valid.")
            return
    except ValueError:
        print("Input harus angka.")
        return

    kendaraan_pilih = kendaraan[nomor-1]
    if kendaraan_pilih['stok'] <= 0:
        print("Maaf, stok kendaraan ini sedang kosong.")
        return

    proses_sewa(kendaraan_pilih)

def proses_sewa(kendaraan_pilih):
    print("\nInput Data Penyewa:")
    nik = input("NIK: ").strip()
    nama = input("Nama Lengkap: ").strip()
    no_hp = input("No HP: ").strip()
    try:
        hari = int(input("Berapa hari sewa: "))
        if hari < 1:
            print("Hari sewa harus minimal 1.")
            return
    except ValueError:
        print("Input hari harus angka.")
        return

    # Muat antrian
    antrian = muat_antrian()

    # Tambah data sewa ke antrian (queue)
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
    print("Sewa berhasil dimasukkan ke antrian. Silakan tunggu konfirmasi owner.")

def status_penyewaan():
    antrian = muat_antrian()
    if not antrian:
        print("Tidak ada data penyewaan.")
        return

    nik = input("Masukkan NIK Anda untuk cek status penyewaan: ").strip()
    found = False
    for item in antrian:
        if item['nik'] == nik:
            print(f"\nStatus Penyewaan untuk {item['nama']}:")
            print(f"Kendaraan: {item['kendaraan']} ({item['ukuran']} seat)")
            print(f"Lama sewa: {item['hari']} hari")
            print(f"Status: {item['status']}")
            found = True

    if not found:
        print("Data penyewaan tidak ditemukan dengan NIK tersebut.")
