
print("Memasukkan bilangan bulat")
bilangan = int(input("Masukkan bilangan: "))

faktorial = 1
i = 1
while i <= bilangan:
    faktorial = faktorial * i
    i = i + 1
print("Hasil faktorial =", faktorial)