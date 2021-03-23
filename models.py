# Models for the views
print('ok')
from spellchecker import SpellChecker
from autocorrect import Speller

corr= Speller('en')

checker = SpellChecker(distance=1)
word_incorrect = '''adam'''


def word_corr(words):
    sentence= str(words)
    new_sen = words.splitlines()
    wrong = []

    for val,item in enumerate(new_sen):
        for word in checker.split_words(item.strip()):
            correct = checker.correction(word)
            if word != correct:
                sentence = sentence.replace(word,correct)
                print(word)
                wrong.append(word)
    return sentence,word


checker.distance= 2