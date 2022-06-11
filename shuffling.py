import random

def shuffleWord(Str):



    text1 = list(Str[1:-1])
    random.shuffle(text1)

    text2 = Str[0] + ''.join(text1) + Str[-1]

    return text2


def shuffleWords(Str):
    Str = Str.split()


    for i in Str:

        j = [h for h in i]
        print(shuffleWord(j), end = " ")

# Driver code
Str= "kelimeler çokça nazikler"
shuffleWords(Str)
