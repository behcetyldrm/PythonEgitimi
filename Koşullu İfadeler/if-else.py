kullaniciadi = "behcetemre"
password = "1234"

#1. YÖNTEM

if kullaniciadi == "behcetemre" and password == "1234":
    print("Giriş Başarılı")
else:
    print("Kullanıcı adı veya şifre yanlış")

#2. YÖNTEM

if kullaniciadi == "behcetemre":
    if password == "12345":
        print("Giriş Başarılı")
    else:
        print("Şifre yanlış")
else:
    print("Kullanıcı adı yanlış")


x = int(input("Sayı : "))

if x > 0:
    print("sayı pozitif")
elif x < 0:
    print("sayı negatif")
else:
    print("sayı sıfır")

# elif birden fazla koşul oluşturulacağı zaman kullanılır

my_string = "Hello World"

if "Hello" in my_string:
    print("true")
else:
    print("false")  

# Hello kelimesinin my_string içinde olup olmama durumunu kontrol eder

my_list = [1, 2, 3, 4, 5]

if 3 in my_list:
    print("true")
else:
    print("false")
# aynı işlemi liste içinde yapabiriz

my_dictionary = {"k1": 100, "k2": 120}

if "k1" in my_dictionary.keys():
    print("true")

if 100 in my_dictionary.values():
    print("true")
#aynı işlem sözlük içinde yapılabilir