from realOrNot import checkWordInDic

def genOversightLetter(nlp, word):
    l = len(word)
    neWord = list(word)
    tmp = []
    panelOfWord = []

    try:
        for i in range(l):
            tmp.append(neWord[i])
            neWord[i] = ""
            neWordToSend = "".join(neWord)
            if checkWordInDic(nlp, word, neWordToSend) is False:
                panelOfWord.append(neWordToSend)
                neWord[i] = tmp[i]
            else:
                continue

    except KeyError as e:
        # print("key: " + e.__str__() + " didn't exist into the dictionnary.")
        panelOfWord.append("")
        print('oversight result : \n', panelOfWord)

    return panelOfWord
