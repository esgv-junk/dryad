import pystache
from dryad.writer import str_nodes

math_admonition_template = """\
<div class="math_admonition {{admonition_type}}">

<span class="math_admonition_title {{admonition_type}}">{{title_text}}</span>

{{{child_lines}}}

</div>"""

title_texts = {
    'theorem'    : 'Теорема {number}.',
    'definition' : 'Определение {number}.',
    'paradox'    : 'Парадокс {number}.',
    'hypothesis' : 'Гипотеза {number}.',
    'example'    : 'Пример.',
    'statement'  : 'Утверждение.',
    'proof'      : 'Доказательство.',
    'remark'     : 'Замечание.',
    'consequence': 'Следствие {number}.'
}

class MathAdmonitionBlock:
    def write(self):
        context = {
            'admonition_type': self.admonition_type,
            'title_text'     : \
                title_texts[self.admonition_type].format(number=self.number), 
            'child_lines'    : str_nodes(*self.child_nodes, sep='\n\n')
        }
        
        return pystache.render(math_admonition_template, context)