import os

print(os.listdir()) #bulunulan klasördeki dosyaları gösterir

"""
#DOSYA OLUŞTURMA
ogrenciler = os.open("ogreciler.txt", os.O_RDWR|os.O_CREAT)
#adı girilen dosya eğer varsa rdwr onu okur ve yazma yetkisi verir ama yoksa creat onu oluşturur


#DOSYAYA YAZI YAZMA
os.write(ogrenciler, "Behçet Emre -> 100\n".encode())
os.write(ogrenciler, "Gizem -> 100\n".encode())
os.write(ogrenciler, "Ali -> 12".encode())

os.close(ogrenciler)
#write ile bulunan dosyamıza yazı yazdırdık. close ile de dosyadan çıkış yaptık
"""

#DOSYA OKUMA
ogrenciler = os.open("ogreciler.txt", os.O_RDONLY)
dosya_uzunluk = os.stat(ogrenciler).st_size
icerik = os.read(ogrenciler, dosya_uzunluk)

print(icerik.decode())
os.close(ogrenciler)

#rdonly ile dosyaya okuma yetkisi verdik. 
#stat ile dosyayı aldık ve st_size ilede uzunluğunu bulduk. uzunluğu bulunmadan dosya okunamaz
#read ilede dosyamızı okuduk

"""
os.unlink("ogreciler.txt") dosya silinir
"""





