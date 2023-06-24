#RANGE:

#range ile belirtilen  sayıdan istedğimiz sayıya kadar yazdırabiliriz

for item in range(1,10,2):  # 1den 10a kadar 2şer 2şer yazdırdık 
    print(item)

print(list(range(10,100,10))) #range ile liste oluşturabiliriz

print("-------------------")

#ENUMERATE:

# enumerate ile hangi elemanın hangi index numarasına karşılık geldiğiniz öğrenebiliriz

greeting = "hello"

for item in  enumerate(greeting):  
    print(item)

print("-------------------")


#ZİP:

# farklı listelerin aynı index numaralarına göre listeler

list1 = [1,2,3,4,5]
list2 = ["a","b","c","d","e"]

print(list(zip(list1, list2)))

for item in zip(list1, list2):
    print(item)

print("-------------------")

#RANDOM :

from random import randint
                                #rastgele sayı seçer
print(randint(0,1000))

my_list = list(range(0,10))
print(my_list)

from random import shuffle      #shuffle karştırma işlemi yapar

shuffle(my_list)
print(my_list)