import re
from dryad.writer import render 
from python_hyphenator.hyphenator import Hyphenator

hyphenators = [
    Hyphenator(r'../3rd_party/python_hyphenator/hyph_ru_RU.dic')
]

def hyphenate(word):
    for hyphenator in hyphenators:
        word = hyphenator.inserted(word, '&shy;')
    return word

class Text:
    def write(self):
        escaped_text = render('{{body_text}}', body_text=self.body_text)
        
        return re.sub(
            '\w+', 
            lambda match_obj: hyphenate(match_obj.group(0)),
            escaped_text 
        )