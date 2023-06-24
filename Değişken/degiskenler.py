maasAli = 5000
maasAhmet = 4000
vergi = 0.27

print(maasAli - (maasAli * vergi))
print(maasAhmet- (maasAhmet * vergi))

# DEĞİŞKEN TANIMLAMA KURALLARI:

# 1. Rakam ile başlayamaz ama ortasında veya sonunda rakam kullanılabilir

number1 = 50 # doğru

# 1number = 50 yanlış

# Büyük küçük harf duyarlılığı vardır 

age = 15
AGE = 20

print(age)
print(AGE)

# Türkçe karakter kullanılmamalı

yas = 40 #doğru
# yaş = 40 yanlış

x = 1                   # integer
y = 2.8                 # float
name = "Behçet"         # string
isStudent = True        # bool

x, y, name, isStudent = (1, 2.8, "Behçet", True) # tek bir satırda da değişkenlere eleman atayabiliriz

a = "15"
b = "20"

print(a + b) # string ifadeleri toplarken matematik işlemi yapılmaz iki elemanı birleştirir Sonuç: 1520 olur

name1 = "Behçet"
lastname = " Yıldırım"

print(name1 + lastname) # lastname'in başında boşluk bıraktığımız için sonuç Behçet Yıldırım olur


# Boşluk Olamaz

Soy_isim = "Yıldırım" #doğru
# Soy isim = "Yıldırım" yanlış

