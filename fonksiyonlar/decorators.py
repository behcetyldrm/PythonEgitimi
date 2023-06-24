
def func(new_func):
    print("Fonksiyon başladı")
    new_func()
    print("fonksiyon bitti")

def hello_func():
    print("hello world")

func(hello_func)

"""fonkisyonumuz için istenen parametreyi fonskiyon içinde fonksiyon olarak çalıştırılmasını sağladık ve fonksiyonu çalıştırırken istenen değeri
fonskiyon olarak girdik"""

def yeni_fonk():
    print("yeni fonk")

    def yeni_fonk2():
        print("yeni fonk 2")
    
    return yeni_fonk2

"""burada yapılan return işlemi ile yeni fonk 2 nin yapacakları yeni fonk a eşitlendi. yani yeni fonk kendi işlemlerini değil yeni fonk 2 yi yapar"""


new_string = yeni_fonk() # değişkenimiz artık fonksiyon oldu+
new_string()

# DECORATOR:

def decorator_func(func):

    def wrapper_func():
        print("wrapper stared")
        func()
        print("wrapper ended")
    
    return wrapper_func


@decorator_func  #aşağıdaki fonksiyonun yukarıdaki fonksiyonun parametresi olarak alır    
def func_new():
    print("hello world")

func_new()