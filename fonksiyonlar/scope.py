my_string = "Atil"  #Global

def my_func():
    my_string = "James"  #Enclosing

    def my_func2():

        my_string = "Lars" #Local
        print(my_string)

    my_func2()


my_func()
print(my_string)

y = 10

def func_new(y):
    print(y)
    y = 5
    print(y)
    return y

func_new(10)

y = func_new(y)
print(y)

#2. yöntem 

def func_new2():
    global y
    y = 7
    print(y)

func_new2()
print(y)