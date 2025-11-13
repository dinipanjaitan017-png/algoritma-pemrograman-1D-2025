def gabung_dan_urutkan(t1, t2):
    gabungan = t1 + t2

    unik = ()
    for angka in gabungan:
        sudah_ada = False
        for u in unik:
            if angka == u:
                sudah_ada = True
                break
        if not sudah_ada:
            unik = unik + (angka,)

    unik = list(unik)
    n = len(unik)
    for i in range(n - 1):
        for j in range(i + 1, n):
            if unik[i] < unik[j]:
                temp = unik[i]
                unik[i] = unik[j]
                unik[j] = temp

    hasil = ()
    for angka in unik:
        hasil = hasil + (angka,)

    return hasil


t1 = ()
n1 = int(input("Masukkan jumlah elemen tuple pertama: "))
for i in range(n1):
    elemen = int(input(f"Masukkan elemen ke-{i+1} tuple pertama: "))
    t1 = t1 + (elemen,)

t2 = ()
n2 = int(input("Masukkan jumlah elemen tuple kedua: "))
for i in range(n2):
    elemen = int(input(f"Masukkan elemen ke-{i+1} tuple kedua: "))
    t2 = t2 + (elemen,)

hasil = gabung_dan_urutkan(t1, t2)
print("\n=== HASIL ===")
print("Tuple pertama :", t1)
print("Tuple kedua   :", t2)
print("Tuple gabung tanpa duplikat (descending):", hasil)