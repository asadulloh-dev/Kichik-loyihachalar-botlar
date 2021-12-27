# 27/12/2021
# Loyiha muallifi: Rahimov Asadbek
# Ustoz: Anvar Narzullayev
# O'yin: Tosh, Qaychi, Qog'oz

import random


def ToshQaychiQogoz():
    javob = 1
    (input("Keling, Tosh, Qaychi, Qog'oz o'yinini o'ynaymiz \n"
           "Boshlash uchun ENTER tugmangizni bosing !"))
    men = 0
    siz = 0
    while javob:
        tqq = ['tosh', 'qaychi', "qog'oz"]
        komp = random.choice(tqq)
        foydal = input('Siz kiriting: ')
        print(komp)
        if (komp.lower() == 'tosh' and foydal.lower() == "qog'oz") \
                or (komp == "qog'oz" and foydal.lower() == 'qaychi') \
                or (komp == 'qaychi' and foydal.lower() == 'tosh'):
            print("Siz yutdingiz")
            siz += 1

        elif (komp == foydal.lower()):
            print("Durrang !")

        elif (komp == 'tosh' and foydal.lower() == 'qaychi') \
                or (komp == 'qaychi' and foydal.lower() == "qog'oz") \
                or (komp == "qog'oz" and foydal.lower() == 'tosh'):
            print("Men yutdim")
            men += 1

        else:
            print("Notog'ri yozdingiz !!!")

        print(f"Menda {men} ochko, sizda {siz} ochko")

        javob = int(input("Yana o'ynaymizmi ? (1-ha,0-yo'q)"))

    if men > siz:
        print("Umumiy hisobda men yutdim !")
    elif men < siz:
        print("Tabriklayman umumiy hisobda siz yutdingiz !")
    else:
        print("Umumiy hisobda durrang !")
    print("Hayr !")

ToshQaychiQogoz()