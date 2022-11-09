# 27/12/2021
# Loyiha muallifi: Rahimov Asadbek
# So'z topish o'yini

from uzwords import words
from random import choice


def get_word():
    word = choice(words)
    while "-" in word or " " in word:
        word = choice(words)
    return word.upper()


def display(user_letters, word):
    display_letter = ''
    for letter in word:
        if letter in user_letters:
            display_letter += letter
        else:
            display_letter += '-'
    return display_letter


def play():
    word = get_word()
    word_letters = set(word)
    user_letters = ''
    print(f"Men {len(word)} xonali so'z o'yladim. Topa olasizmi?")

    while word_letters:
        print(display(user_letters, word))
        if user_letters:
            print(f"Shu vaqtgacha kiritgan xarflaringiz: {user_letters}")

        letter = input("Xarf kiriting: ").upper()
        if letter in user_letters:
            print("Bu xarfni avval kiritgansiz. Boshqa xarf kiriting.")
            continue
        elif letter in word:
            word_letters.remove(letter)
            print(f"{letter} xarfi to'g'ri.")
        else:
            print("Bunday xarf yo'q.")
        user_letters += letter
    print(f"Tabriklayman! {word} so'zini {len(user_letters)} ta urinishda topdingiz.")

play()
