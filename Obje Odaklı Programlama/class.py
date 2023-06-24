
class Musician():

    job = "musician"  # sınıftaki herkse için aynı olan özelliği fonksiyon dışına yazarız

    def __init__(self, name, age, instrument):  

        #ATTRİBUTE
        self.name = name
        self.age = age
        self.instrument = instrument
    
    #METHOD

    def sing(self):
        print(f"We are the champions {self.instrument}") 


#İNSTANCE
my_musician = Musician("Edd Sheraan", 38, "Guitar")

print(my_musician.name)
print(my_musician.instrument)
print(my_musician.age)
print(my_musician.job)
print(my_musician.sing())

print("---------------------")

class DogYears():

    year_factor = 7

    def __init__(self, age = 5):  #age'e tanımlanan değer olduğu için parametre girmesek bile çalışır

        self.age = age
        self.age_multiplied = age * 7   #1. yöntem

        #2. yöntem
    def calculation(self):

        return self.age * DogYears.year_factor # self.year_factor

#1. yöntem
my_dog = DogYears() #5
print(my_dog.age_multiplied)        

#2. yöntem
my_dog = DogYears(10) 
print(my_dog.calculation())

