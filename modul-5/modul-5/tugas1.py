

def hitung_faktorial(n):

    if n <= 1:
        return 1
    else:
        return n * hitung_faktorial(n - 1)

angka = int(input("Masukkan bilangan bulat non-negatif: "))

if angka < 0:
    print("Maaf, bilangan tidak boleh negatif!")
else:
    hasil = hitung_faktorial(angka)
    print(f"Hasil dari {angka}! = {hasil}")