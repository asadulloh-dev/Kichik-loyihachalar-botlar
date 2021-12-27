from random import randint


def son_top(x):
    taxmin_men = 0
    javob = 1
    komp_son = randint(1, x)
    print(f"1 dan {x} gacha bo'lgan son o'yladim. Topa olasizmi ?")
    while javob:
        taxmin_men += 1
        men_son = int(input(">> "))

        if komp_son > men_son:
            print("Uzr, bundan kattaroq. Yana xarakat qiling: ")

        elif komp_son < men_son:
            print("Uzr, bundan kichikroq. Yana xarakat qiling: ")

        else:
            break
    print(f"Tabriklayman, siz {taxmin_men} ta taxmin bilan topdingiz!")
    return taxmin_men


def son_top_pc(x):
    input(f"1 dan {x} gacha son o'ylang va istalgan tugmani bosing. Men topaman.")
    quyi = 1
    yuqori = x
    taxminlar_komp = 0

    while True:
        taxminlar_komp += 1
        if quyi != yuqori:
            taxmin = randint(quyi, yuqori)
        else:
            taxmin = quyi

        javob = input(f"Siz {taxmin} ni o'yladingiz: to'g'ri(t), kattaroq(+), kichikroq(-): ")
        if javob == "-":
            yuqori = taxmin - 1
        elif javob == "+":
            quyi = taxmin + 1
        else:
            break
    print(f"Men {taxminlar_komp} ta taxmin bilan topdim!")
    return taxminlar_komp


def play(x):
    yana = 1
    while yana:
        taxminlar_user = son_top(x)
        taxminlar_pc = son_top_pc(x)
        if taxminlar_user > taxminlar_pc:
            print("Men yutdim !")
        elif taxminlar_user < taxminlar_pc:
            print("Siz yutdingiz !")
        else:
            print("Durrang.")

        yana = int(input("Yana o'ynaymizmi ?"))

play(10)
play(100)
play(500)