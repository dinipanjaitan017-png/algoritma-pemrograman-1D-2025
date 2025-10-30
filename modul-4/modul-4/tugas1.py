# Program Mengecek Kondisi Lampu di Taman Kota

# Meminta jumlah baris lampu
jumlah_baris = int(input("Masukkan jumlah baris lampu: "))

# Perulangan untuk setiap baris lampu
for y in range(1, jumlah_baris + 1):
    jumlah_lampu = int(input(f"Masukkan jumlah lampu pada baris ke-{y}: "))

    # Perulangan untuk setiap lampu di baris tersebut
    for x in range(1, jumlah_lampu + 1):
        if x % 3 == 0:
            print(f"Lampu ke-{x} pada baris {y} rusak.")
        else:
            print(f"Lampu ke-{x} pada baris {y} menyala.")
    
    # Jika ini adalah baris terakhir, tampilkan pesan tambahan
    if y == jumlah_baris:
        print("Periksa sambungan daya utama.")