data_kunjungan = []
id_counter = 1

def tambah_kunjungan():
    global id_counter

    print("\n=== Tambah Data Pengunjung ===")
    while True:
        nama_pengunjung = input("Nama pengunjung     : ").strip()
        if nama_pengunjung.isalpha():
            break
        print("Nama pengunjung harus huruf! Silakan coba lagi.")

    while True:
        nama_santri = input("Nama santri dijenguk: ").strip()
        if nama_santri.isalpha():
            break
        print("Nama santri harus huruf! Silakan coba lagi.")

    daerah = input("Daerah asal (Sumatra/Kalimantan/Jawa): ").strip().capitalize()
    if daerah not in ["Sumatra", "Kalimantan", "Jawa"]:
        print("Daerah tidak valid! Harus Sumatra, Kalimantan, atau Jawa.")
        return

    data_kunjungan.append([id_counter, nama_pengunjung, nama_santri, daerah])
    print(f"Data berhasil ditambahkan dengan ID Antrian: {id_counter}")
    id_counter += 1


def tampilkan_kunjungan():
    print("\n=== Daftar Kunjungan (Urut Berdasarkan Daerah) ===")
    urutan_daerah = ["Sumatra", "Kalimantan", "Jawa"]
    hasil_urut = []

    for d in urutan_daerah:
        for data in data_kunjungan:
            if data[3] == d:
                hasil_urut.append(data)

    if not hasil_urut:
        print("Belum ada data kunjungan.")
    else:
        for d in hasil_urut:
            print(f"ID: {d[0]}, Pengunjung: {d[1]}, Santri: {d[2]}, Daerah: {d[3]}")


def hapus_kunjungan():
    print("\n=== Hapus Data Pengunjung ===")
    try:
        id_hapus = int(input("Masukkan ID antrian yang akan dihapus: "))
    except ValueError:
        print("ID harus berupa angka!")
        return

    for data in data_kunjungan:
        if data[0] == id_hapus:
            data_kunjungan.remove(data)
            print("Data berhasil dihapus.")
            return

    print("ID tidak ditemukan!")


# ========== PROGRAM UTAMA ==========
while True:
    print("\n=== SISTEM KUNJUNGAN SANTRI ===")
    print("1. Tambah Pengunjung")
    print("2. Tampilkan Daftar Pengunjung")
    print("3. Hapus Data Pengunjung")
    print("4. Keluar")

    pilihan = input("Pilih menu (1/2/3/4): ")

    if pilihan == "3":
        if len(data_kunjungan) == 0:
            print("Input data dulu broo")
            continue
        else:
            hapus_kunjungan()
            continue

    if pilihan == "1":
        tambah_kunjungan()

    elif pilihan == "2":
        tampilkan_kunjungan()

    elif pilihan == "4":
        print("Program selesai.")
        break

    else:
        print("Pilihan tidak valid! Silakan coba lagi.")