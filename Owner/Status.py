import json
from Data.PathData import ANTRIAN_JSON, RIWAYAT_JSON, KENDARAAN_JSON
from Utils.Utils import muat_json, simpan_json
from datetime import datetime, timedelta

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

    # Load kendaraan
    kendaraan = muat_json(KENDARAAN_JSON)

    if keputusan == 'terima':
        for k in kendaraan:
            if k['nama'].lower() == data['kendaraan'].lower():
                if k['stok'] > 0:
                    k['stok'] -= 1
                    break
                else:
                    print("❌ Stok kendaraan habis. Tidak bisa menerima pesanan.")
                    return

    # Update status antrian
    for a in antrian:
        if a['nik'] == data['nik'] and a['status'] == 'pending':
            a['status'] = keputusan

    # Simpan ke riwayat
    riwayat = muat_json(RIWAYAT_JSON)
    data_riwayat = data.copy()
    data_riwayat['total_harga'] = data['harga_perhari'] * data['hari']
    
    tanggal_sewa = datetime.today()
    tanggal_kembali = tanggal_sewa + timedelta(days=data['hari'] - 1)

    data_riwayat['tanggal_sewa'] = tanggal_sewa.strftime('%Y-%m-%d')
    data_riwayat['tanggal_kembali'] = tanggal_kembali.strftime('%Y-%m-%d')
    data_riwayat['status'] = keputusan

    riwayat.append(data_riwayat)

    simpan_json(ANTRIAN_JSON, antrian)
    simpan_json(RIWAYAT_JSON, riwayat)
    if keputusan == 'terima':
        simpan_json(KENDARAAN_JSON, kendaraan)

    print(f"✅ Pemesanan telah di-{keputusan}.")
