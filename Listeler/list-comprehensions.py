years = [1990,1974,1943,2000]
ages = [2020 - year for year in years]
#for döngüsünü liste içinde kullanabiiriz ve bu şekilde kolayca listemizi oluştururuz

print(ages)

numbers = [x**2 for x in range(10) if x**2 % 3 == 0]
print(numbers)
# range ile 0 dan 10 a kadar olan sayıları x içine aldık ve x in karesinin aldık daha sonra 3 e bölünen sayıları bulduk

result = [x if x%2==0 else "TEK" for x in range(1,10)]
print(result)
#if yapısını x e değer vermeden kullandığımız için x in 2 ye bölünmediği durumlarda tek yazmasını sağladık

results = [(x,y) for x in range(3) for y in range(3)]
print(results)
#x ve y den 1er tane sayı alarak liste şeklnde yazar

#BİR ÜSTTEKİ KODUN DİĞER YÖNTEMİ:

result1 = []

for x in range(3):
    for y in range(3):
        result1.append((x,y))


print(result1)