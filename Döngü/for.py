numbers = [1,2,3,4,5]

for num in numbers:
    print(num)  
#for döngüsüne listemizi atmak için for içinde değişken oluşturduk ve listemizi onun içine attık.
#listemizdeki elemanları tek tek yazdrımamızı sağlar

for num in numbers:
    print("hello")
#for döngüsünün içine aldığımız listemizin 5 elemanı vardı ve bizde listemizdeki eleman kadar hello yazdırdık

names = ["behçet", "emre"]

for name in names:
    print(f"Benim adım {name}")
#for döngülerini bu şekilde de kullanabilriz

ad = "Behçet"

for a in ad:
    print(a)
#listede her bir eleman 1 karakteri belirtir. Buarada liste kullanmadık ama string ifadenin her karakteri alt alta yazar

d = {"k1":1, "k2":2, "k3":3}

for key,value in d.items():
    print(key, value)
#elemanlara atadğımız değerleri ve elemanları bu şekilde görebiliriz

