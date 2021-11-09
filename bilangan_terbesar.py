print("Program Mencari Nilai Terbesar Dari 3 Buah Bilangan ")

bil1 = int(input("Masukan Bilangan 1: "))
bil2 = int(input("Masukan Bilangan 2: "))
bil3 = int(input("Masukan Bilangan 3: "))

if bil1 > bil2 > bil3:
    print("Bilangan Terbesar Adalah = ", bil1)
elif bil2 > bil3:
    print("Bilangan Terbesar Adalah = ", bil2)
else:
    print("Bilangan Terbesar Adalah = ", bil3)
