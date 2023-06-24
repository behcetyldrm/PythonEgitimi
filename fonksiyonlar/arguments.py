def changeName(n):
    n = "ada"

name = "behçet"

changeName(name)
print(name)

def sehir(a):

    a[0] = "İstanbul"

sehirler = ["İzmir", "Bursa"]
sehir(sehirler)

print(sehirler)

"""
foksiyonumuz içerisindeki a değişkenine biz bir parametre atadık daha sonra foksiyon dışında sehirler listemizi oluşturduk ve listemizi foksiyonumuza
attık. Foksiyona attığımızda oluşturduğumuz değişken fonksiyon içindeki a değişkenin adres yoluna bağlandı ve a değişkenine atanan parametreye göre 
güncellendi.
"""

def add(*params): # * işareti ile belirttimiz zaman istedğimiz kadar değer kullanabiliriz ve tuple listesi oluşturur
    print(params)
    return sum((params))    #sum foksiyonu toplama işlemi yapar

print(add(10,20,30,60))
print(add(34,79))

def disPlayUser(**args): # ** ile belirttimiz zaman dictionary oluşturur
    
    for key, value in args.items():

        print(f"{key} is {value}")
    
disPlayUser(name = "Behçet", age = 14, city = "Bursa")
print("-----------")
disPlayUser(name = "Emre", age = 10, city = "İstanbul", telefon = "05678921457")
print("--------")
def myFunc(a, b, *args, **kwargs):

    print(a)
    print(b)
    print(args)
    print(kwargs)

myFunc(10, 20, 30, 40, 50, key1 = "behçet", key2 = "emre")

"""
fonksiyon içine atılan değerler sırasıyla belirtilen parametrelere yerleşti ve fazladan kalan sayılar tuple listesi içine geldi, anahtar sözcük ve
değer belirtenlerde dictionary listesine içine girdi
"""
