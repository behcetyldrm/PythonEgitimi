x = input("1. Sayi1: ")
y = input("2. Sayi: ")

print(type(x))
# type kodu ile de�i�kenlerin hangi veri tipine sahip oldu�unu g�r�r�z
print(type(y))

toplam = int(x) + int(y) # x ve y de�i�kenleriyle matematik i�lemi yapmak i�in integer tipine getirdik

print(toplam)

# Veri Tipi Dönüşümleri

# 1. İnt to Float

sayi1 = 15 #int
a = float(sayi1)
print(a)
print(type(a))

# 2. Float to İnt

sayi2 = 14.8 #float
b = int(sayi2)
print(b)
print(type(b))

# bool to int

isOnline = False
print(type(isOnline))

isOnline = int(isOnline) # bool tipini int yaparsak e�er false ise 0 True ise 1 yazar
print(isOnline)
print(type(isOnline))



