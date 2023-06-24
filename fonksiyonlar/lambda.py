
def square(num):
    return num ** 2

numbers = [1, 3, 5, 7]

result = list(map(square, numbers)) 
# map belirtilen listenin girilen fonskiyon içine atılmasını ve işlem yapılmasını sağlar

print(result)

numbers = [1, 3, 5, 7]

sonuc = list(map(lambda num: num ** 2, numbers))
# lambda isimsiz ve daha önce oluşturmadığımız bir fonksiyon görevi görür
print(sonuc)

multiply = lambda number : number * 3
print(multiply)

def sayi(num): 
    return num % 2 == 0

numbers = [1, 3, 5, 10, 2, 4]

result = list(filter(sayi, numbers))
#filter ile sadece True değerini çıkartan sonuçlar ekrana yazıldı
print(result)