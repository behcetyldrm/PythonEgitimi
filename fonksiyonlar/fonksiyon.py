def sayHello(name = "User"):  #fonksiyonu kullanmamız için bir name değeri istedik ve eğer değer girilmezse user yazar
    print("Hello " + name)

sayHello("Behçet")
sayHello("Emre")
sayHello()

def sayHellos(names = "User"):
    return ("Hello " + names)

#burada ise bir parametre aldık ve bunu return ile fonksiyonumuza attık ve names değeri Behçet oldu

mesaj = sayHellos("Behçet")
print(mesaj)

def yasHesapla(dogumYili):
    return 2021 - dogumYili

def EmekliligeKacYilKaldi(dogumYili, isim):

    """ EMEKLİLİĞE NE KADAR KALDI HESAPLAMA """

    yas = yasHesapla(dogumYili)
    emeklilik = 65 - yas

    if emeklilik > 0:
        print(f"{isim} Bey emekliliğinize {emeklilik} yıl kaldı.")
    else:
        print(f"{isim} Bey emekli olmuşsunuz.")
    
EmekliligeKacYilKaldi(1990, "Behçet")
EmekliligeKacYilKaldi(1940, "Emre")