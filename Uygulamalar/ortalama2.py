sayiListesi = []
num = 1

while True:

# sayıları girme ve listeye ekleme
    try:
        sayi = float(input(f"{num}. Sayıyı Giriniz: "))
        sayiListesi.append(sayi)
    except:
        print("Sayı Giriniz!")

# yeni sayı girme kontrolü
    while True:
        global devam
        devam = input("Devam edilsin mi? (e/h): ")

        if devam == "e" or devam == "E":
            num += 1
            break
        elif devam == "h" or devam == "H":
            break
        else:
            print("E veya H değeri giriniz!")

    if devam == "h" or devam == "H":
        break

print(f"Ortalaması alınacak sayı listeniz: {sayiListesi}. Toplam sayı miktarı: {len(sayiListesi)}")

# listemizdeki sayıları liste eleman sayısına böldük. ortalama hesaplamak için
ortListesi = []
for x in sayiListesi:
    
    x = x / len(sayiListesi)
    ortListesi.append(x)

print(f"Girdiğiniz sayıların ortalaması: {sum(ortListesi)}") #eleman sayısına bölünen sayılarımızı topladık ve ortalamayı bulduk

