import re
from dryad.writer import render 
from python_hyphenator.hyphenator import Hyphenator

hyphenator = Hyphenator(r'../3rd_party/python_hyphenator/hyph_ru_RU.dic')

class Text:
    def write(self):
        escaped_text = render('{{body_text}}', body_text=self.body_text)
        
        return re.sub(
            '\w+', 
            lambda match_obj: hyphenator.inserted(match_obj.group(0), '&shy;'),
            escaped_text 
        )