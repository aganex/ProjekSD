# Buyer/StatusPenyewaan.py

from Data.PathData import ANTRIAN_JSON
import json

def muat_antrian():
    try:
        with open(ANTRIAN_JSON, 'r') as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def cek_status_penyewaan():
    antrian = muat_antrian()
    if not antrian:
        print("Tidak ada data penyewaan.")
        return

    nik = input("Masukkan NIK Anda untuk cek status penyewaan: ").strip()
    ditemukan = False
    for item in antrian:
        if item['nik'] == nik:
            print(f"\nStatus Penyewaan untuk {item['nama']}:")
            print(f"Kendaraan: {item['kendaraan']} ({item['ukuran']} seat)")
            print(f"Lama sewa: {item['hari']} hari")
            print(f"Status: {item['status']}")
            ditemukan = True

    if not ditemukan:
        print("Data penyewaan dengan NIK tersebut tidak ditemukan.")
