#  Copyright (c) 2021. by Danil Smirnov
#  zabanen.nu@ya.ru
#  The input to the program is a sequence of words,
#  each word on a separate line. The end of the sequence is the word "КОНЕЦ"
#  program displays the members of the given sequence

word = input()
while word != 'КОНЕЦ':
    print(word)
    word = input()
