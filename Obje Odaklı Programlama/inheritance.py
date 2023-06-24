class Class1():

    def __init__(self):
        print("Class 1 created")

    def method_1(self):
        print("method 1")
    
    def method_2(self):
        print("method 2")

my_instance = Class1()
print(my_instance.method_1())
print(my_instance.method_2())

class Class2(Class1):  # class 1 sınıfını farklı bir sınıfa atarak o sınıf içinde özelliklerini kullandık

    def __init__(self):

        Class1.__init__(self)  #class 1'in __init__ fonksiyonunu kullandık
        print("Class2 created")

my_instance_2 = Class2()

my_instance_2.method_1() 
#değişkenimiz class2 sınıfına kayıtlı olmasını rağman class1 methodu kullandık çünkü class1'i sınıfımıza eklemiştik

