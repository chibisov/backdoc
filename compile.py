# -*- coding: utf-8 -*-
src = open('./src/backdoc.py', 'r').read()
markdown2_src = open('./src/markdown2.py', 'r').read()
template_src = "template = u'''{0}'''".format(open('./src/template.html', 'r').read())

compiled_src = (
    src.replace('from markdown2 import Markdown', markdown2_src)
       .replace("template_html = open('./template.html', 'r').read()", template_src)
)

compile_to = open('./backdoc.py', 'w')
compile_to.write(compiled_src)