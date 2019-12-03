import json

from realOrNot import checkWordInDic

def genErrorTyping(nlp, keybrd, wordConcerned):

    panelOfWord = []
    choiceOfDispo = "disposition_clavier/" + keybrd
    fileDispoKeybrd = open(choiceOfDispo, "r")
    dispositionKeyboard = json.load(fileDispoKeybrd)
    colonFlag = False
    for indice in range(len(wordConcerned)):
        tblWord = list(wordConcerned)
        if (wordConcerned[indice]) in dispositionKeyboard:
            for letter in dispositionKeyboard[wordConcerned[indice]].split(':'):

                if letter == '' and colonFlag is False:
                    letter = ':'
                    colonFlag = True
                else:
                    colonFlag = False
                    continue

                tblWord[indice] = letter
                writeWord = "".join(tblWord)
                if checkWordInDic(nlp, wordConcerned, writeWord) is False:
                    panelOfWord.append(writeWord)
        # except KeyError as e:
        #     # print("key: " + e.__str__() + " didn't exist into the dictionnary.")
        #     panelOfWord.append(wordConcerned)
        #     print('errorTyping result : \n')
        #     print(panelOfWord)

    return panelOfWord
