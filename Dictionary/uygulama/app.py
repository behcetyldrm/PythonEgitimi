# 1. 4 tane öğrencinin ad, soyad, yaş, email, sınıf ve numara bilgilerini giriniz.

from turtle import st


students = {

    "Behçet" : {

        "tam_ad" : "Behçet Yıldırım",
        "Yaş" : 14,
        "Email" : "behcet@gmail.com",
        "Sınıf" : "9/A",
        "Numara" : 880
    },

    "Gizem" : {

        "tam_ad" : "Gizem Yıldırım",
        "Yaş" : 17,
        "Email" : "gizem@gmail.com",
        "Sınıf" : "12/D",
        "Numara" : 475
    },

        "Berk" : {

        "tam_ad" : "Berk Çelik",
        "Yaş" : 17,
        "Email" : "berk@gmail.com",
        "Sınıf" : "12/C",
        "Numara" : 567
    },

        "Eyüp" : {

        "tam_ad" : "Eyüp Yılmaz",
        "Yaş" : 15,
        "Email" : "eyup@gmail.com",
        "Sınıf" : "9/B",
        "Numara" : 251
    } 
}

#2. Öğrencileri 9. sınıf ve 12. sınıf olarak ayır ????


#3. Eyüp'ün email bilgisini al

print(students["Eyüp"]["Email"])

