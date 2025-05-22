import json
from Data.PathData import ANTRIAN_JSON, RIWAYAT_JSON
from Utils.Utils import muat_json, simpan_json
from datetime import datetime

def proses_pemesanan():
    antrian = muat_json(ANTRIAN_JSON)
    if not antrian:
        print("Tidak ada antrian pemesanan.")
        return

    pending = [a for a in antrian if a['status'] == 'pending']
    if not pending:
        print("Tidak ada pemesanan yang pending.")
        return

    for idx, p in enumerate(pending, 1):
        print(f"{idx}. {p['nama']} - {p['kendaraan']} ({p['hari']} hari) - Rp{p['harga_perhari']}/hari")

    try:
        pilihan = int(input("Pilih nomor untuk diproses (0 untuk batal): "))
        if pilihan == 0:
            return
        data = pending[pilihan - 1]
    except (ValueError, IndexError):
        print("Pilihan tidak valid.")
        return

    keputusan = input("Terima atau Tolak pemesanan ini? (terima/tolak): ").lower()
    if keputusan not in ['terima', 'tolak']:
        print("Pilihan tidak valid.")
        return

    # Update data antrian
    for a in antrian:
        if a['nik'] == data['nik'] and a['status'] == 'pending':
            a['status'] = keputusan

    # Simpan ke riwayat jika diterima atau ditolak
    riwayat = muat_json(RIWAYAT_JSON)
    data_riwayat = data.copy()
    data_riwayat['total_harga'] = data['harga_perhari'] * data['hari']
    data_riwayat['tanggal_sewa'] = datetime.today().strftime('%Y-%m-%d')
    data_riwayat['status'] = keputusan
    riwayat.append(data_riwayat)

    simpan_json(ANTRIAN_JSON, antrian)
    simpan_json(RIWAYAT_JSON, riwayat)
    print(f"✅ Pemesanan telah di-{keputusan}.")
