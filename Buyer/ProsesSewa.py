# Buyer/ProsesSewa.py

from Data.PathData import ANTRIAN_JSON, KENDARAAN_JSON
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

def proses_sewa(kendaraan_pilih):
    print("\nInput Data Penyewa:")
    nik = input("NIK: ").strip()
    nama = input("Nama Lengkap: ").strip()
    no_hp = input("No HP: ").strip()
    try:
        hari = int(input("Berapa hari sewa: "))
        if hari < 1:
            print("Hari sewa minimal 1.")
            return
    except ValueError:
        print("Input hari harus angka.")
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
    print("Sewa berhasil ditambahkan ke antrian. Tunggu konfirmasi owner.")
