# Models for the views
print('ok')
from spellchecker import SpellChecker
from autocorrect import Speller
import base64
import requests


corr= Speller('en')

checker = SpellChecker(distance=1)
word_incorrect = '''adam'''


def word_corr(words):
    sentence= str(words)
    new_sen = words.splitlines()
    corrected = []
    wrong = []

    for val,item in enumerate(new_sen):
        for word in checker.split_words(item.strip()):
            correct = checker.correction(word)
            if word != correct:
                sentence = sentence.replace(word,correct)
                corrected.append(correct)
                wrong.append(word)
    wordings = dict(zip(wrong,corrected))
    return sentence, wordings


checker.distance= 2




API = "AIzaSyDTq4cci16u92_lonCb5CA2oBhYvWagc3I"

def detect_text(image_file, access_token=None):
    print(type(image_file))
    with open(image_file, 'rb') as image:
        base64_image = base64.b64encode(image.read()).decode()

    url = 'https://vision.googleapis.com/v1/images:annotate?key={}'.format(
                                                                   access_token)
    header = {'Content-Type': 'application/json'}
    body = {
        'requests': [{
            'image': {
                'content': base64_image,
            },
            'features': [{
                'type': 'TEXT_DETECTION',
                'maxResults': 1,
            }]

        }]
    }
    response = requests.post(url, headers=header, json=body).json()
    text = response['responses'][0]['textAnnotations'][0]['description'] if len(response['responses'][0]) > 0 else ''
    return text


#if __name__ == '__main__':
#   app.run(debug = True)