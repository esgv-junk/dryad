import pystache
from dryad.writer import str_nodes

math_admonition_template = """\
<div class="math_admonition {{admonition_type}}">

<span class="math_admonition_type {{admonition_type}}">\
{{type_text}}\
{{#has_number}} {{number}}{{/has_number}}.\
</span>

{{#has_title}}
<p><span class="math_admonition_title"> ({{{title_text}}})</span></p>
{{/has_title}}

{{{child_lines}}}

</div>"""

type_texts = {
    'theorem'    : 'Теорема',
    'definition' : 'Опр.',
    'paradox'    : 'Парадокс',
    'hypothesis' : 'Гипотеза',
    'example'    : 'Пример',
    'statement'  : 'Утверждение',
    'proof'      : 'Доказательство',
    'remark'     : 'Замечание',
    'consequence': 'Следствие',
    'lemma'      : 'Лемма'
}

has_number = frozenset((
    'theorem', 
    'definition', 
    'paradox', 
    'hypothesis', 
    'consequence',
    'lemma'
))

has_title = frozenset((
    'theorem', 
    'definition', 
    'paradox', 
    'hypothesis', 
    'consequence',
    'remark', 
    'example',
    'lemma'
))

class MathAdmonitionBlock:
    def write(self):
        context = {
            'admonition_type': self.admonition_type,
            'type_text'      : type_texts[self.admonition_type],
            'child_lines'    : str_nodes(*self.child_nodes, sep='\n\n'),
            
            'has_number'     : self.admonition_type in has_number,
            'number'         : self.number,
            'has_title'      : \
                self.title_nodes and self.admonition_type in has_title,
            'title_text'     : str_nodes(*self.title_nodes),
        }
        
        return pystache.render(math_admonition_template, context)