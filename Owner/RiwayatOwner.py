# Owner/RiwayatOwner.py
import json
import os
from Data.PathData import RIWAYAT_JSON

def menu_riwayat():
    if not os.path.exists(RIWAYAT_JSON):
        print("❌ Belum ada riwayat penyewaan.")
        return

    with open(RIWAYAT_JSON, 'r') as file:
        try:
            riwayat = json.load(file)
        except json.JSONDecodeError:
            riwayat = []

    if not riwayat:
        print("📭 Data riwayat masih kosong.")
        return

    print("\n=== 📜 RIWAYAT PENYEWAAN ===")
    print(f"{'No':<4}{'Nama':<20}{'Kendaraan':<15}{'Lama':<6}{'Total':<15}{'Tgl Sewa':<12}{'Tgl Kembali':<12}{'Status':<10}")
    print("-" * 120)

    for i, data in enumerate(riwayat, 1):
        lama_sewa = f"{data.get('hari', '-')}"
        total_harga = f"Rp{data.get('total_harga', 0):,}"
        tanggal_sewa = data.get('tanggal_sewa', '-')
        tanggal_kembali = data.get('tanggal_kembali', '-')
        status = data.get('status', '-')

        print(f"{i:<4}{data['nama']:<20}{data['kendaraan']:<15}{lama_sewa:<6}{total_harga:<15}{tanggal_sewa:<12}{tanggal_kembali:<12}{status:<10}")
