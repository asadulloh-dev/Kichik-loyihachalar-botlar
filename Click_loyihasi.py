# parol0 = 2001
# balance1 = 0
# balance2 = 0
# savol = "Parolni kiriting: "
# parol = int(input(savol))
# while True:
#     if parol == parol0:
#         amal = int(input("\nAmalning raqamini kiriting\n"
#                      "(1-balansni tekshirish\n"
#                      "2-balansni to'ldirish\n"
#                      "3-balansdan pul yechish\n"
#                      "4-kartaga pul o'tkazish\n"
#                      "0-to'xtatish): "))
#         if amal == 1:
#             balance = int(input("\nQaysi kartadagi balansni tekshirmoqchisiz: "))
#             if balance == 1:
#                 print("\n1-kartadagi balans:", balance1, "so'm")
#             if balance == 2:
#                 print("\n2-kartadagi balans:", balance2, "so'm")
#
#         elif amal == 2:
#             karta = int(input("\nQaysi karta hisobini to'ldirmoqchisiz: "))
#             if karta == 1:
#                 kirish = int(input("\n1-kartaga qancha pul tushirmoqchisiz: "))
#                 balance1 += kirish
#             elif karta == 2:
#                 kirish = int(input("\n2-kartaga qancha pul tushirmoqchisiz: "))
#                 balance2 += kirish
#
#
#         elif amal == 3:
#             karta = int(input("\nQaysi kartadan pul yechmoqchisiz: "))
#             if karta == 1:
#                 chiqish = int(input("\n1-kartadan qancha pul yechmoqchisiz: "))
#                 if chiqish > balance1:
#                     print("\nUzr, 1-kartangizda buncha mablag' yo'q!")
#                 else:
#                     balance1 -= chiqish
#             elif karta == 2:
#                 chiqish = int(input("\n2-kartadan qancha pul yechmoqchisiz: "))
#                 if chiqish > balance2:
#                     print("\nUzr, 2-kartangizda buncha mablag' yo'q!")
#                 else:
#                     balance2 -= chiqish
#
#         elif amal == 4:
#             karta = int(input("\nQaysi kartaga pul o'tkazmoqchisiz: "))
#             if karta == 1:
#                 summa = int(input("\n1-kartaga qancha o'tkazmoqchisiz: "))
#                 if balance2 < summa:
#                     print("\nUzr, sizning 2-kartangizda buncha mablag' yo'q!")
#                 else:
#                     balance1 += summa
#                     balance2 -= summa
#             if karta == 2:
#                 summa = int(input("\n2-kartaga qancha o'tkazmoqchisiz: "))
#                 if balance1 < summa:
#                     print("\nUzr, sizning 1-kartangizda buncha mablag' yo'q!")
#                 else:
#                     balance1 -= summa
#                     balance2 += summa
#         elif amal == 0:
#             break
#     else:
#         print("Parolni noto'g'ri kiritdingiz!")
#         break

