
def hesap():

   islem = input("Yapacağınız işlemi seçiniz: (+,-,*,/) ")

   if islem == "+":
       print(f"{sayi1} + {sayi2} = {sayi1 + sayi2}")

   elif islem == "-":
       print(f"{sayi1} - {sayi2} = {sayi1 - sayi2}")
   
   elif islem == "*":
       print(f"{sayi1} * {sayi2} = {sayi1 * sayi2}")

   elif islem == "/":
       print(f"{sayi1} / {sayi2} = {sayi1 / sayi2}")

   else: 
       print("Lütfen doğru işlem seçiniz")
     


while True:

   sayi1 = int(input("1. sayıyı giriniz: "))
   sayi2 = int(input("2. sayıyı giriniz: "))
   
   hesap()







