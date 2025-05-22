# Owner/RiwayatOwner.py
import json
import os
from Data.PathData import RIWAYAT_JSON

def menu_riwayat():
    if not os.path.exists(RIWAYAT_JSON):
        print("Belum ada riwayat.")
        return

    with open(RIWAYAT_JSON, 'r') as file:
        try:
            riwayat = json.load(file)
        except json.JSONDecodeError:
            riwayat = []

    if not riwayat:
        print("Data riwayat kosong.")
        return

    print("\n=== RIWAYAT PENYEWAAN ===")
    print(f"{'No':<4} {'Nama':<20} {'Kendaraan':<15} {'Total Harga':<15} {'Tanggal':<12} {'Status':<10}")
    print("-" * 80)
    for i, data in enumerate(riwayat, 1):
        print(f"{i:<4} {data['nama']:<20} {data['kendaraan']:<15} Rp{data['total_harga']:<15,} {data['tanggal_sewa']:<12} {data['status']:<10}")
