class geometri():
    
    def kare():

        kenar = int(input("Kenar uzunluğu giriniz: "))

        sonuc = kenar * kenar
        print(f"Karenin alanı: {sonuc}")

        sonuc = kenar * 4
        print(f"Karenin çevresi: {sonuc}")


    def dikdortgen():
    
        kisa_kenar = int(input("Kısa kenar uzunluğunu giriniz: "))               
        uzun_kenar = int(input("Uzun kenar uzunluğunu giriniz: "))                   

        sonuc = uzun_kenar * kisa_kenar
        print(f"Dikdörtgenin alanı: {sonuc}")

        sonuc = (uzun_kenar + kisa_kenar)*2
        print(f"Dikdörtgenin çevresi: {sonuc}")


    def ucgen():

        yukseklik = int(input("Yükseklik giriniz: "))
        taban = int(input("Taban uzunluğu: "))
        kenar1 = int(input("Kenar uzunluğu giriniz: "))
        kenar2 = int(input("Kenar uzunluğu giriniz: "))

        sonuc = (taban * yukseklik) / 2
        print(f"Üçgenin alanı: {sonuc}")

        sonuc = kenar1 + kenar2 + taban
        print(f"Üçgenin çevresi: {sonuc}")

    def daire():

        yari_cap = int(input("Yarı çap giriniz: "))
        pi = 3

        sonuc = pi * (yari_cap ** 2)
        print(f"Dairenin alanı: {sonuc}")

        sonuc = 2 * pi * yari_cap
        print(f"Dairenin çevresi: {sonuc}")

    def koni():

        yukseklik = int(input("Yükseklik giriniz: "))
        yari_cap = int(input("Yarı çap giriniz: "))
        pi = 3

        sonuc = pi * yari_cap**2 * yukseklik
        print(f"Koninin alanı: {sonuc}")

        sonuc = 2 * pi * yari_cap
        print(f"Koninin çevresi: {sonuc}")

    def kure():

        yari_cap = int(input("Yarı çap giriniz: "))
        pi = 3

        sonuc = 4/3 * pi * yari_cap**3
        print( f"Kürenin hacmi: {sonuc}")

        sonuc = 4 * pi * yari_cap**2
        print(f"Kürenin alanı: {sonuc}")

    def dikdortgen_prizma():

        kenar1 = int(input("Kenar uzunluğu giriniz: ")) 
        kenar2 = int(input("Kenar uzunluğu giriniz: ")) 
        kenar3 = int(input("Kenar uzunluğu giriniz: ")) 

        sonuc = (kenar2 + kenar1 + kenar3) * 4
        print(f"Dikdörgen prizmasının hacmi: {sonuc}")

        sonuc = 2 * (kenar1*kenar2 + kenar2*kenar3 + kenar1*kenar3) ** 2
        print(f"Dikdörtgen prizması alanı: {sonuc}")

        sonuc = (kenar3 + kenar1 + kenar2) *  4
        print(f"Dikdörtgen prizması çevresi: {sonuc}")