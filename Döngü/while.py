
x = 0

while x <= 100:
    print(x)
    x += 1
print("bitti")
#0 dan 100 e kadar sayıları yazar ve koşul false değer olduğunda durur. x'e 1 ekleyerek ilerler


# 0 DAN 100 E KADAR ÇİFT VE TEK SAYILAR YAZILIR
y = 0

while y <= 100:
    if y % 2 == 0:
        print(f"sayı çift: {y}")
    else:
        print(f"sayı tek: {y}")
    y += 1
print("bitti")
# y'in 2 bölündüğünde kalanın sıfır olduğu durumlarda y yazılır. ama if koşulu sağlanmasa bile y 1 arttırılır

name = "" #false değer

while not name.split(): #true  #split baştaki ve sondaki karakterleri siler. burada ismimizi boş bırakmamız engellenir
    name = input("İsminizi Giriniz: ")
    
print(f"Merhaba, {name}")