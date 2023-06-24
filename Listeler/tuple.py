
list = [1,2,30]

tuple = 1, "iki", 3     # tuple kodu ile köşeli parantez kullanmadan liste oluşturabiliriz

print(type(list))
print(type(tuple))

print(list[2])
print(tuple[2])

print(len(tuple))
print(len(list))

list = ["ayşe", "eren"]
tuple = ("behçet", "gizem", "behçet")   

list[0] = "ali"
# tuple[0] = "mehmet"   #tuple ile listeyi tamamen değiştirebiliriz ama listedeki seçlen indexteki elemanı değiştiremeyiz 

print(tuple.count("behçet")) #seçilen değerden kaç tane olduğunu söyler
print(tuple.index("gizem")) #seçilen değerin kaçınca indexte olduğunu söyler
 
names = ("emre", "murat") + tuple  # başka bir liste ile tuple birleştirilebilir
print(names)

#tuple ile listenin farkı ise tuple ile listeden eleman silemeyiz veya başka bir eleman ile elemanın yerini değiştiremeyiz