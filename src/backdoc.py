# -*- coding: utf-8 -*-
#!/usr/bin/env python
"""
Backdoc is a tool for backbone-like documentation generation. 
Backdoc main goal is to help to generate one page documentation from one markdown source file.

https://github.com/chibisov/backdoc
"""
import argparse


class BackDock(object):
    def __init__(self, markdown_converter, template_html, stdin, stdout):
        self.markdown_converter = markdown_converter
        self.template_html = template_html
        self.stdin = stdin
        self.stdout = stdout
        self.parser = self.get_parser()

    def run(self, args_string):
        kwargs = self.get_kwargs(args_string)
        self.stdout.write(self.get_result_html(**kwargs))

    def get_kwargs(self, args_string):
        parsed = self.parser.parse_args(args_string)._get_kwargs()
        return self.prepare_kwargs_from_parsed_data(parsed)

    def prepare_kwargs_from_parsed_data(self, parsed):
        kwargs = {}
        kwargs['title'] = parsed.get('title', 'Documentation')
        if 'source' in parsed:
            kwargs['markdown_src'] = open(parsed['source'], 'r').read()
        else:
            kwargs['markdown_src'] = self.stdin.read()
        return kwargs

    def get_result_html(self, title, markdown_src):
        response = self.get_converted_to_html_response(markdown_src)
        return (
            self.template_html.replace('<!-- title -->', title)
                              .replace('<!-- toc -->', response.toc_html)
                              .replace('<!-- main content -->', response)
                              .encode('utf-8')
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
    import sys
    from markdown2 import Markdown
    template_html = open('./template.html', 'r').read()

    args_string = u' '.join([i.decode('utf-8') for i in sys.argv[1:]])
    BackDock(
        markdown_converter=Markdown(extras=['toc']), 
        template_html=template_html,
        stdin=sys.stdin,
        stdout=sys.stdout
    ).run(args_string=args_string)
