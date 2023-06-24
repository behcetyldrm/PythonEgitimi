sayiListesi = []
num = 1

while True:

    try:
        sayi = int(input(f"{num}. sayıyı giriniz: "))
    except:
        if sayi != int or sayi != float:
            print("Sayı giriniz!")
            continue

    sayiListesi.append(sayi)
    
    devam = input("Devam Edilsin mi? (e/h): ")

    
    if devam == "e":
        num += 1
        continue
    elif devam == "h":
        break
    else:
        print("e veya h değeri giriniz!")
        num += 1

print(f"Sayı Listeniz: {sayiListesi}")

def ortalama(sayiList):

    for ort in sayiList:

        n = 0
        toplam = ort[n] + ort[n+1]
        n += 1

        return toplam / len[ort]
       
print(f"Girdiniz sayıların ortalaması: {ortalama(sayiListesi)}")

        

