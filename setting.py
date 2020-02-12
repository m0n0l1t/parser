class Tag:
    def __init__(self, before='', after='', delete=False):
        self.before = before
        self.after = after
        self.delete = delete



option = {
    'article title': 'h1',
    'main': 'br',
    'a_link': Tag(' [', '] '),
    'h1': Tag('\n\n', '\n\n'),
    'h2': Tag('\n\n', '\n\n'),
    'h3': Tag('\n\n', '\n\n'),
    'p': Tag('\n\n'),
    'br/': Tag('\n\n'),
    'a': Tag(''),
    'blockquote': Tag('\n\n')

}