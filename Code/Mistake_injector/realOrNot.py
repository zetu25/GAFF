# from textAnalyser import spacy

# nlp = spacy.load('fr_fasttext_lg')

def checkWordInDic(dico, word1, word2):

    try:
        dico[word1]
        # print("[i] Synonyms fonded for ", word1)
        return True

    except:
        # print('[X] ', word1, " has no synonyms")
        return False