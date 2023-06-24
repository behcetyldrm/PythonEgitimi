
sayi = int(input("Sayı Giriniz: "))

bolenler = []

for num in range(1,sayi + 1):

    if sayi % num == 0:

        bolenler.append(num)

print(f"Girdiğiniz sayı: {sayi} Tam bölenleri: {bolenler}")

