from alav_cevre_class import geometri

print("*****ALAN VE ÇEVRE HESAPLAMA*****")  

while True:

    sekil = input("Bir geometrik cisim giriniz: ")

    if sekil == "kare" or sekil == "Kare":
        geometri.kare()

    elif sekil == "dikdörtgen" or sekil == "dikdortgen":
        geometri.dikdortgen()

    elif sekil == "üçgen" or sekil == "Üçgen":
        geometri.ucgen()

    elif sekil == "daire" or sekil == "Daire":
        geometri.daire()

    elif sekil == "koni" or sekil == "Koni":
        geometri.koni()
    
    elif sekil == "küre" or sekil == "Küre":
        geometri.kure()

    elif sekil == "dikdörtgen prizması" or "Dikdörtgen prizması":
        geometri.dikdortgen_prizma()
        
    else:
        print("Şeklin ismini düzgün girdiğinizden emin olun. Örnek -> kare, Kare")
    

