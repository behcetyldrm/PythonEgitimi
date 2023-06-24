
numara = input("Öğrenci Numaranız: ")
ad = input("Adınız: ")
soyad = input("Soyadınız: ")
telefon = input("Telefon Numaranız: ")

ogrenciler = {
    numara : {
        "Ad: " : ad,
        "Soyad: " : soyad,
        "Telefon: " : telefon
    },
    numara : {
        "Ad: " : ad,
        "Soyad: " : soyad,
        "Telefon: " : telefon
    },
    numara : {
        "Ad: " : ad,
        "Soyad: " : soyad,
        "Telefon: " : telefon
    }
}

print(ogrenciler[numara])
