from random import randint

tutulanSayi = randint(1,101)
n = 0

print(tutulanSayi)

print("******SAYI TAHMİN ETMECE****** \n")
while True:
    
    try:
        tahmin = int(input("Sayı Tahmininiz: "))
        n += 1

        if tahmin == tutulanSayi:
            print("Tebrikler sayıyı buldun!")
            print(f"Tutulan sayı: {tutulanSayi}")
            print(f"Tahmin sayınız: {n}")
            break
        else:
            print("Tekrar deneyin!")

    except:
        print("Lütfen sayı giriniz!")

    

