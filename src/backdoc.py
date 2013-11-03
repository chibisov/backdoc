# -*- coding: utf-8 -*-
#!/usr/bin/env python
"""
Backdoc is a tool for backbone-like documentation generation. 
Backdoc main goal is to help to generate one page documentation from one markdown source file.

https://github.com/chibisov/backdoc
"""
import sys
import argparse

from markdown2 import Markdown


template_html = open('./template.html', 'r').read()


def force_text(text):
    if isinstance(text, unicode):
        return text
    else:
        return text.decode('utf-8')


class BackDoc(object):
    def __init__(self, markdown_converter, template_html, stdin, stdout):
        self.markdown_converter = markdown_converter
        self.template_html = force_text(template_html)
        self.stdin = stdin
        self.stdout = stdout
        self.parser = self.get_parser()

    def run(self, argv):
        kwargs = self.get_kwargs(argv)
        self.stdout.write(self.get_result_html(**kwargs).encode('utf-8'))

    def get_kwargs(self, argv):
        parsed = dict(self.parser.parse_args(argv)._get_kwargs())
        return self.prepare_kwargs_from_parsed_data(parsed)

    def prepare_kwargs_from_parsed_data(self, parsed):
        kwargs = {}
        kwargs['title'] = force_text(parsed.get('title') or 'Documentation')
        if parsed.get('source'):
            kwargs['markdown_src'] = open(parsed['source'], 'r').read()
        else:
            kwargs['markdown_src'] = self.stdin.read()
        kwargs['markdown_src'] = force_text(kwargs['markdown_src'] or '')
        return kwargs

    def get_result_html(self, title, markdown_src):
        response = self.get_converted_to_html_response(markdown_src)
        return (
            self.template_html.replace('<!-- title -->', title)
                              .replace('<!-- toc -->', response.toc_html and force_text(response.toc_html) or '')
                              .replace('<!-- main_content -->', force_text(response))
        )

    def get_converted_to_html_response(self, markdown_src):
        return self.markdown_converter.convert(markdown_src)

    def get_parser(self):
        parser = argparse.ArgumentParser()
        parser.add_argument(
            '-t',
            '--title',
            help='Documentation title header',
            required=False,
        )
        parser.add_argument(
            '-s',
            '--source',
            help='Markdown source file path',
            required=False,
        )
        return parser


if __name__ == '__main__':
    BackDoc(
        markdown_converter=Markdown(extras=['toc']), 
        template_html=template_html,
        stdin=sys.stdin,
        stdout=sys.stdout
    ).run(argv=sys.argv[1:])
