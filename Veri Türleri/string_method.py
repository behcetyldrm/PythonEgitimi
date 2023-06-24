message = "Hello There. My name is Behçet Emre"
message1 = "Hello There. My name is Behçet Emre"
message2 = "Hello There. My name is Behcet Emre"
message3 = "Hello There. My name is Behcet Emre"
message4 = "  Hello There. My name is Behcet Emre"
message5 = "Hello There. My name is Behcet Emre"


message = message.upper() # Bütün karakterleri büyük harf yapar
message1 = message1.lower() #.lower() karakterlerin tamamini kucuk yazar
message2 = message2.title() #.title() tum kelimelerin bas harflerini buyuk yazar
message3 = message3.capitalize() #.capitalize() cumlenin ilk harfini buyuk yapar
message4 = message4.strip() #.strip() cumlenin basinda biraktigimiz boslugu kapatir
message5 = message5.split() #.split() parantez içi boşken boşlukların bulunnduğu yerden kelimeleri birer karakter olarak alır
message6 = "--".join(message5) #.join() her kelimenin aras�n� belirtilen karakteri koyar
message7 = message1.find("name") #cumle icerisinde aradigimiz ifadenin bas harfinin kacinci eleman oldugunu soyler. Yoksa -1 yazar
message8 = message.startswith("H") #.startswith() cumlenin baslidığı harfi sorar eger dogru ise True yanlis ise False soyler
message9 = message.endswith("c") #.endswith() cumlenin bittigi harfi sorar dogru ise True yanlis ise False soyler 
message10 = message2.replace("Behcet","Burak") #.replace() cumlede sectigimiz karakteri baska karakterle degistirir


print(message)
print(message1)
print(message2)
print(message3)
print(message4)
print(message5)
print(message5[2]) # cümle parçalandığı için her kelime bir karakter olur
print(message6)
print(message7)
print(message8)
print(message9)
print(message10)

