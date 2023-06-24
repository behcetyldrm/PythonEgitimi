
myList = [1,2,3]
print(myList)

myList2 = ["hello",2,True,5.8] # liste içinde bütün veri türleri aynı anda olabilir
print(myList2)

list1 = ["one","two","three"]
list2 = ["four","five","six"]

numbers = list1 + list2 # listeleri birleştirebiliriz
print(numbers)

print(len(numbers)) #liste içinde kaç eleman bulunduğunu görebiliriz
print(numbers[2]) # listelerin elemanlarına tek tek ulaşabiliriz (1. elemanın indexi 0'dır)

usersA = ["Behçet", 14]
usersB = ["Emre", 15]

users = [usersA, usersB] # liste içinde liste yapmazı sağlar. Bu şekilde 1 liste içinde 1 den çok liste saklayabiliriz 

print(usersA)
print(usersB)
print(users) 

print(users[1]) #liste içinde liste özelliğinden yararlanarak 1 kullanıcıya ait verileri almış olduk

print(users[1][0]) #listenin içinden listemizi aldık ve bu listeninde ilk elemanını almış olduk 