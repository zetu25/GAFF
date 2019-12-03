from realOrNot import checkWordInDic

def genInversionLetterKeypad(nlp, word):
    l = len(word) - 1
    neWord = list(word)
    tmp = [0] * 29
    panelOfWord = []

    if l > 1:
        for i in range(l):
            tmp[i] = neWord[i]
            neWord[i] = neWord[i+1]
            neWord[i+1] = tmp[i]
            neWordToSend = "".join(neWord)
            #print("Generating and writing", neWordToSend, "...")
            if checkWordInDic(nlp,word, neWordToSend) == False :
                panelOfWord.append(neWordToSend)
                neWord[i + 1] = neWord[i]
                neWord[i] = tmp[i]
            else:
                pass
    else:
        # panelOfWord.append(word)
        pass

    return panelOfWord