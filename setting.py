class Tag:
    def __init__(self, after, before='', delete=False):
        self.before = before
        self.after = after
        self.delete = delete


option = {
    'h1': Tag('\n\n', '\n\n'),
    'h2': Tag('\n\n', '\n\n'),
    'h3': Tag('\n\n', '\n\n'),
    'p': Tag('\n\n'),
    'a_link': Tag('] ', ' ['),
    'a': Tag(''),
    'blockquote': Tag('\n\n')
}