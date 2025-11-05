

def hitung_gaji(nama, jabatan, gaji_pokok):
    pajak = 0.05 * gaji_pokok 
    
    if jabatan.lower() == "manager":
        tunjangan = 0.10 * gaji_pokok
    elif jabatan.lower() == "staff":
        tunjangan = 0.05 * gaji_pokok
    else:
        tunjangan = 0 
    gaji_bersih = gaji_pokok - pajak + tunjangan

    print("Nama Karyawan :", nama)
    print("Jabatan       :", jabatan)
    print("Gaji Pokok    : Rp", gaji_pokok)
    print("Pajak (5%)    : Rp", pajak)
    print("Tunjangan     : Rp", tunjangan)
    print("Gaji Bersih   : Rp", gaji_bersih)

nama_karyawan = input("Masukkan nama karyawan: ")
jabatan_karyawan = input("Masukkan jabatan (Manager/Staff): ")
gaji_pokok = float(input("Masukkan gaji pokok: "))

hitung_gaji(nama_karyawan, jabatan_karyawan, gaji_pokok)