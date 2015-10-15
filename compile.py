# -*- coding: utf-8 -*-
import sys

if sys.version_info[0] < 3:
    from io import open

src = open('./src/backdoc.py', 'r', encoding='utf-8').read()
markdown2_src = open('./src/markdown2.py', 'r', encoding='utf-8').read()
template_src = "template_html = u'''{0}'''".format(open('./src/template.html', 'r', encoding='utf-8').read())

compiled_src = (
    src.replace('from markdown2 import Markdown', markdown2_src)
       .replace("template_html = open('./template.html', 'r').read()", template_src)
)

compile_to = open('./backdoc.py', 'w', encoding='utf-8')
compile_to.write(compiled_src)