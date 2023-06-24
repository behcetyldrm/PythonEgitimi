
numbers = [1,2,3,4,5,17,13]
letters = ["a","b","f","h","y","s","a"]

val1 = min(numbers) #listedeki en küçük sayıyı alır
val2 = max(numbers) # listedeki en büyük sayıyı alır

print(val2)
print(val1)

val3 = min(letters)  # listedeki en küçük harfi alır
val4 = max(letters)  # listedeki en büyük harfi alır

print(val3)
print(val4)

val5 = numbers[2:5] # 2. indexten 5. indexe kadar yazar (5. hariç)
val6 = numbers[:4] # 0. indexten 4. indexe kadar yazar. Tam terside yapılabilir [4:]

print(val5)
print(val6)

numbers[4] = 40 # listedeki 4 index numaralı elemanı 40 ile değiştirdik

numbers.append(50) #listenin sonuna 50 elemanını ekler
numbers.append([10,14,25]) #liste içine liste ekleyebiliri

numbers.extend([10,14,25]) # liste içine elemanları ayrı liste olarak değil eleman olarak ekler

numbers.insert(3,76) #listenin 3. index'ine 76 elemanını ekler diğerlerini sağa doğru kaydırır
numbers.insert(-1, 58) # -1 sonuncu indexi belirtir bu şekilde sondan 1 önceki indexe 58'i eklemiş olduk

numbers.pop() #sonuncu elemanı siler
numbers.pop(0) #pop ile istedğimiz inex numaralı elemanı silebiliriz

numbers.remove(40) #liste içinde arama yapar ve girilen değer bulunursa listeden siler

numbers.sort() #listedeki elemanları küçükten büyüğe dizer
letters.sort() #listedeki harfleri alfabetik sıraya göre dizer

numbers.reverse() #listedeki elemanları büyükten küçüğe dizer
letters.reverse() #listedeki harfleri alfabetik sıranın tersine göre dizer

print(numbers)
print(letters)

print(numbers.count(3)) #listede girilen değerden kaç tane olduğunu söyler
print(letters.count("a"))

numbers.clear() #listedeki bütün elemanları siler
print(numbers)