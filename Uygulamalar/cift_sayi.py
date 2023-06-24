
numbers = []
cift_sayi = []
tek_sayi = []

while True:

    try:
        sayi = int(input("Sayı Giriniz: "))
    except:
        print("Lütfen sayı girin!")
        continue
    
    numbers.append(sayi)

    devam = input("Devam edilsin mi ? (e/h): ")

    if devam == "e":
        continue

    elif devam == "E":
        continue

    elif devam == "h":
        break

    elif devam == "H":
        break

    else:
        print("e veya h giriniz!!")
        

print(f"\nOluşturduğunuz sayı listesi: {numbers}")

for sayilar in numbers:

    if sayilar % 2 == 0:       
        cift_sayi.append(sayilar)

    else:
        tek_sayi.append(sayilar)

print(f"Listenizdeki çift sayılar: {cift_sayi}. Listenizdeki en büyük çift sayı: {max(cift_sayi)}")
print(f"Listenizdeki tek sayılar: {tek_sayi}. Listenizdeki en büyük tek sayı: {max(tek_sayi)}")
print(f"Listenizdeki en büyük sayı: {max(numbers)}")
 