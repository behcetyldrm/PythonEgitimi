name = "Behçet"
surname = "Yıldırım"
age = 14

greeting = "My name is " + name + " " + surname + " and \nI am " + str(age) + " years old" #\n alt satıra geçirir

length = len(greeting)

print(length)
print(greeting) 
print(greeting[0]) # Cümlelerdeki her harf, boşluk vb. karakterdir ve karakter sayımı 0'dan başlar
print(greeting[6])
print(len(greeting)) # len kodu ile cümlenin toplam kaç karakterli olduğunu görürüz
# 1. Yöntem
print(greeting[length - 1]) 
# len kodu toplam karakteri gösterir 1'den başlar bu yüzden 1 karakter fazla gibi olur son karakteri görmek içinse 1 çıkarılır
# 2. Yöntem
print(greeting[-1])

print(greeting[3:10]) # 3. karakterden 10. karaktere kadar olan ki karakterleri yazar 10 hariç
print(greeting[3:]) # 3. karakterden son karaktere kadar yazar
print(greeting[:12]) # ilk karakterden başlayıp 12. karaktere kadar yazar
print(greeting[3:40:2]) # 3. karakterden 40. karaktere kadar gider ama her iki karakterden 1 tanesini alır
