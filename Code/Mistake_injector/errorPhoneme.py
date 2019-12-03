import json
import re

from realOrNot import checkWordInDic


def genErrorPhoneme(nlp, wordConcerned):
    panelOfWord = []
    dirRestriLow = 'phoneme/restriction_low'
    dirRestriHard = 'phoneme/restriction_hard'
    dirRestriConsonant = 'phoneme/restriction_consonant'
    dirRestriNo = 'phoneme/restriction_no'

    fileRestriLow = open(dirRestriLow, 'r')
    fileRestriHard = open(dirRestriHard, 'r')
    fileRestriConsonant = open(dirRestriConsonant, 'r')
    fileRestriNo = open(dirRestriNo, 'r')

    bdLow = json.load(fileRestriLow)
    bdHard = json.load(fileRestriHard)
    bdConsonant = json.load(fileRestriConsonant)
    bdNo = json.load(fileRestriNo)

    for key in bdNo.keys():

        if re.findall(key, wordConcerned):

            for value in bdNo[key].split(':'):
                wordToWrite = wordConcerned.replace(key, value)
                if checkWordInDic(nlp, wordConcerned, wordToWrite) is False:
                    panelOfWord.append(wordToWrite)

    for keyCons in bdConsonant.keys():

        regexCons = '\\b\\w*[^aeiouy]', keyCons, '[^aeiouy]\\w*\\b'
        regexCleanCons = re.compile(''.join(regexCons), re.IGNORECASE)

        if re.search(regexCleanCons, wordConcerned):

            for value in bdConsonant[keyCons].split(':'):
                wordToWrite = wordConcerned.replace(keyCons, value)
                if checkWordInDic(nlp, wordConcerned, wordToWrite) is False:
                    panelOfWord.append(wordToWrite)

    for keyLow in bdConsonant.keys():

        regexLow = keyLow, '\\b'
        regexCleanLow = re.compile(''.join(regexLow), re.IGNORECASE)

        if re.search(regexCleanLow, wordConcerned):

            for value in bdLow[keyLow].split(':'):
                wordToWrite = wordConcerned.replace(keyLow, value)
                if checkWordInDic(nlp, wordConcerned, wordToWrite) is False:
                    panelOfWord.append(wordToWrite)

    for keyHard in bdHard.keys():

        regexHard = '\\b', keyHard, '\\b'
        regexCleanHard = re.compile(''.join(regexHard), re.IGNORECASE)

        if re.search(regexCleanHard, wordConcerned):

            for value in bdLow[keyHard].split(':'):
                wordToWrite = wordConcerned.replace(keyHard, value)
                if checkWordInDic(nlp, wordConcerned, wordToWrite) is False:
                    panelOfWord.append(wordToWrite)


    return panelOfWord
