BehcetHesap = {
    "ad" : "Behcet Emre",
    "hesapNo" : "1564234",
    "bakiye" : 3000,
    "ekBakiye" : 2000
}

GizemHesap = {
    "ad" : "Gizem",
    "hesapNo" : "1518233",
    "bakiye" : 4000,
    "ekBakiye" : 3000
}

def ParaCek(hesap, miktar) :

    print(f"Merhaba {hesap['ad']}")

    if hesap["bakiye"] >= miktar:
        print(f"Para çekme işlemi başarılı. Kalan bakiyeniz: {miktar - hesap['bakiye']}")
    else:
        toplam = hesap["bakiye"] + hesap["ekBakiye"]

        if toplam >= miktar:
            EkbakiyeKullanimi = input("Bakiyeniz yetersiz. Ek Bakiye kullanılsın mı ? (evet/hayır): ")

            if EkbakiyeKullanimi == "evet":

                print(f"Paranızı çekebilirsiniz. Kalan ek bakiyeniz: {miktar - (hesap['bakiye'] + hesap['ekBakiye'])}")
            else:
                print("Para çekme işlemi başarısız")
        else:
            print("Bakiyeniz ve ek bakiyenizde yetersiz.")

            

ParaCek(BehcetHesap, 7000)

print("----------------------------")

ParaCek(GizemHesap, 3700)
        


