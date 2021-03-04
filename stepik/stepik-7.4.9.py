#  Copyright (c) 2021. by Danil Smirnov
#  zabanen.nu@ya.ru
#  The input to the program is a sequence of words, each word on a separate line.
#  The end of the sequence is one of three words: "стоп", "хватит", "достаточно".
#  program prints out the members of the given sequence.

word = input()
total_words = 0
while word != 'стоп' and word != 'хватит' and word != 'достаточно':
    total_words += 1
    word = input()

print(total_words)
