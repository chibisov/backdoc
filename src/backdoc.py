# -*- coding: utf-8 -*-
#!/usr/bin/env python
from markdown2 import Markdown

template = open('./template.html', 'r').read()


def get_markdown_src():
    import sys
    if len(sys.argv) > 1:
        return open(sys.argv[1], 'r').read()
    else:
        return sys.stdin.read()


if __name__ == '__main__':
    response = Markdown(extras=['toc']).convert(get_markdown_src())
    print (template.replace('<!-- toc -->', response.toc_html)
                   .replace('<!-- main content -->', response)).encode('utf-8')