website = "http://www.sadikturan.com"
course = "Python Kursu: Baştan Sona Python Programlama Rehberiniz (40 Saat)"

# 1. "course" karakter dizininde kaç karakter var

x = len(course)
print(x)

# 2. "website" içinde www karakterini alın

print(website[7:10])

# 3. "website" içinde com karakterini alın

print(website[-3:])

# 4. "course" içindeki ilk 15 ve son 15 karakteri al

print(course[:15])

print(course[-15:])

# 5.  'course' ifadesindeki karakterleri tersten yazdırın

print(course[::-1])

name, surname, age, job = "Bora","Yılmaz",32,"mühendis"

# 6.  Yukarıdakiler ile "Benim adım Bora Yılmaz, yaşım 32 ve mesleğim mühendis."

print(f"Benim adım {name} {surname}, yaşım {age} ve mesleğim {job}")

# 7. "Hello world" ifadesindeki w harfini W ile değiştirin

a = "Hello world"

print(a[:6] + "W" + a[7:])

# 8. "abc" 3 defa yan yana yazdır

print("abc" * 3)