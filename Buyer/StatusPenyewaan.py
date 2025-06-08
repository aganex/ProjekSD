from Data.PathData import ANTRIAN_JSON, KENDARAAN_JSON, RIWAYAT_JSON
import json
from datetime import datetime, timedelta

# Helper untuk load dan simpan JSON
def muat_data(filepath):
    try:
        with open(filepath, 'r') as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def simpan_data(filepath, data):
    with open(filepath, 'w') as file:
        json.dump(data, file, indent=4)

def status_penyewaan():
    antrian = muat_data(ANTRIAN_JSON)
    kendaraan = muat_data(KENDARAAN_JSON)
    riwayat = muat_data(RIWAYAT_JSON)

    nik = input("\nMasukkan NIK Anda untuk cek status penyewaan: ").strip()
    data_user = [item for item in antrian if item['nik'] == nik]

    if not data_user:
        print("\n❌ Tidak ada data penyewaan dengan NIK tersebut.")
        return

    while True:
        print(f"\n📋 Status Penyewaan untuk {data_user[0]['nama']}:")
        print("-" * 60)

        for i, item in enumerate(data_user, 1):
            status_map = {
                'pending': '🟡 Menunggu Konfirmasi',
                'terima': '🟢 Disetujui',
                'tolak': '🔴 Ditolak',
                'selesai': '✅ Selesai/Dikembalikan'
            }
            status = status_map.get(item['status'].lower(), item['status'])
            total_harga = item['harga_perhari'] * item['hari']
            tanggal_sewa = item.get('tanggal_sewa', '-')
            tanggal_kembali = item.get('tanggal_kembali')
            if not tanggal_kembali and tanggal_sewa != '-':
                try:
                    tanggal_awal = datetime.strptime(tanggal_sewa, "%Y-%m-%d")
                    tanggal_kembali = (tanggal_awal + timedelta(days=item['hari'])).strftime("%Y-%m-%d")
                    item['tanggal_kembali'] = tanggal_kembali
                except:
                    tanggal_kembali = '-'

            print(f"\n🔹 {i}. {item['kendaraan']} ({item['ukuran']} seat)")
            print(f"   📆 Tgl Sewa: {tanggal_sewa} ➜ Tgl Kembali: {tanggal_kembali}")
            print(f"   ⏳ Lama sewa: {item['hari']} hari")
            print(f"   💰 Harga: Rp{item['harga_perhari']:,}/hari")
            print(f"   🧾 Total: Rp{total_harga:,}")
            print(f"   📌 Status: {status}")

        print("\n📝 Menu:")
        print("1. Kembalikan kendaraan (untuk status Disetujui)")
        print("2. Lihat riwayat penyewaan")
        print("3. Kembali ke Menu Buyer")

        pilihan = input("\nPilih menu (1-3): ").strip()

        if pilihan == '1':
            kembalikan_kendaraan(antrian, kendaraan, riwayat, data_user, nik)
        elif pilihan == '2':
            lihat_riwayat(nik)
        elif pilihan == '3':
            simpan_data(ANTRIAN_JSON, antrian)
            break
        else:
            print("\n❌ Pilihan tidak valid!")

def kembalikan_kendaraan(antrian, kendaraan, riwayat, data_user, nik):
    kendaraan_diterima = [item for item in data_user 
                         if item['status'].lower() == 'terima']

    if not kendaraan_diterima:
        print("\n❌ Tidak ada kendaraan yang bisa dikembalikan.")
        return

    print("\n🚗 Daftar Kendaraan yang Dapat Dikembalikan:")
    for i, item in enumerate(kendaraan_diterima, 1):
        print(f"{i}. {item['kendaraan']} (Sewa {item['hari']} hari) - Rp{item['harga_perhari'] * item['hari']:,}")

    try:
        pilih = int(input("\nPilih nomor kendaraan (0 untuk batal): "))
        if pilih == 0:
            return
        if not (1 <= pilih <= len(kendaraan_diterima)):
            print("\n❌ Nomor tidak valid!")
            return

        selected = kendaraan_diterima[pilih-1]

        for item in antrian:
            if item['nik'] == selected['nik'] and item['kendaraan'] == selected['kendaraan'] and item['status'].lower() == 'terima':
                item['status'] = 'selesai'
                item['tanggal_pengembalian'] = datetime.now().strftime("%Y-%m-%d")
                riwayat.append(item)
                break

        for k in kendaraan:
            if k['nama'].lower() == selected['kendaraan'].lower():
                k['stok'] += 1
                break

        simpan_data(ANTRIAN_JSON, antrian)
        simpan_data(KENDARAAN_JSON, kendaraan)
        simpan_data(RIWAYAT_JSON, riwayat)

        print(f"\n✅ {selected['kendaraan']} berhasil dikembalikan!")

    except ValueError:
        print("\n❌ Input harus berupa angka!")

def lihat_riwayat(nik):
    riwayat = muat_data(RIWAYAT_JSON)
    riwayat_user = [item for item in riwayat if item['nik'] == nik]

    if not riwayat_user:
        print("\n📭 Tidak ada riwayat penyewaan.")
        return

    print(f"\n📜 Riwayat Penyewaan:")
    print("-" * 60)

    for i, item in enumerate(riwayat_user, 1):
        total = item['harga_perhari'] * item['hari']
        print(f"\n🔹 {i}. {item['kendaraan']} ({item['ukuran']} seat)")
        print(f"   👤 Penyewa: {item['nama']}")
        print(f"   📅 Lama sewa: {item['hari']} hari")
        print(f"   💰 Total biaya: Rp{total:,}")
        print(f"   📆 Tanggal kembali (rencana): {item.get('tanggal_kembali', '-')}")
        print(f"   ⏱️ Tanggal pengembalian (nyata): {item.get('tanggal_pengembalian', '-')}")

    input("\nTekan Enter untuk kembali...")
