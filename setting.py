class Tag:
    def __init__(self, before='', after='', clas='', delete=False):
        self.before = before
        self.after = after
        self.clas = clas
        self.delete = delete



option = {
    'article title': 'h1',
    'main': Tag('div','', 'text jsArticleBody js-mediator-article'),
    'a_link': Tag(' [', '] '),
    'h1': Tag('\n\n', '\n\n'),
    'h2': Tag('\n\n', '\n\n'),
    'h3': Tag('\n\n', '\n\n'),
    'p': Tag('\n\n'),
    'script': Tag('', '','', True),
    #'i': Tag('', '','', True),
    'br/': Tag('\n\n'),
    'a': Tag(''),
    'blockquote': Tag('\n\n'),
    #'div': Tag('','','menu-about', True),



}