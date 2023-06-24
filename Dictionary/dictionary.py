
plakalar = { "kocaeli" : 41, "istanbul" : 34 }  # dictionary ile anahtar kelimelere değer atayabiliriz

print(plakalar["kocaeli"])
print(plakalar["istanbul"])

plakalar["ankara"] = 6 # plakalar içine anahtar kelime olarak ankara ve değer olarak 6 ekledik

plakalar["istanbul"] = 16 # daha önceden eklenen anahtar kelimenin değerini değiştirebilriz

print(plakalar)

users = {
    "behcet" : {
        "age" : 14,
        "email" : "behcet@gmail.com",
        "addres" : "Bursa",                       #dictionary de alt alta işlem yapılabilir
        "phone" : "05396584743"
    },
    "emre" :  {
        "age" : 25,                               #atanan anahtar keliimenin altına farklı anahtar kelimeleri atanabilir
        "email" : "emre@gmail.com",
        "addres" : "istanbul",
        "phone" : "0539664533"        
    }
}

print(users["behcet"])  
print(users["emre"])
print(users["behcet"]["email"])