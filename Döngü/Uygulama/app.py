# 1.   Bir liste içindeki sayılardan beşin katı olan sayıları listeleyin.

sayilar = [8,25,12,85,65,36,10,120,32,34,268,10,5,4,32]

for kat in sayilar :

    if kat % 5 == 0:
        print(f"5 in Katı sayılar : {kat}")

print("-------------------------")

# Üçün katı dışındaki sayıların ekrana yazdırılması

for a in range(1,20):

    if a % 3 != 0:
        print(a)
    else:
        continue

print("-------------------------")

#3. 1 – 100 arasındaki sayıların toplamını bulan programı yazınız.

a = 0
sn = 0

while a <= 100 :

    sn = a + sn
    a = a + 1 

print(sn)
    
