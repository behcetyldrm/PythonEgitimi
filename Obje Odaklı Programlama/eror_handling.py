while True:

	try: 
		my_int = int(input("Enter a number: "))

	except:
		print("Enter a number!!!")
		continue

	else:
		print("OK")
		break

	finally:
		print("finally")

#sayı gireceğimiz kısma sayı girmesek bile hata vermeden devam eder