#BREAK:

# break döngü içinde çaıştığı anda döngü sonlanır

x = "Behçet"

for name in x:
    if name == "ç":
        break
    print(name)
# ç harfine geldiği anda break çalıştı ve döngü bitti

y = 0

while y < 5:
    y += 1          #y 3 e eşit olduğu anda break çalıştı ve döngü bitti
    if y == 3:
        break
    print(y)

#CONTİNUE:

#continue döngü içinde çalıştığı zaman sadece çalıştı anda işle yapılmaz diğer işlemler yapılmaya devam eder

a = "Behçet"

for names in a:
    if names == "ç":   
        continue
    print(names)

b = 0

while b < 5:
    b += 1         
    if b == 3:      #continue b 3 e eşit olduğu zaman çalıştı ve 3 yazılmadı ama sonraki işlemler yapıldı
        continue
    print(b)

#PASS :

name = "behçet"

for a in name:
    pass            # pass döngüyü boş bırakmak için kullanılır
