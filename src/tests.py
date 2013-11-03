# -*- coding: utf-8 -*-
from StringIO import StringIO
import json
import unittest

from markdown2 import Markdown

from backdoc import BackDoc


class BackDocTest(unittest.TestCase):
    def setUp(self):
        self.template_html = json.dumps({
            'title': '<!-- title -->',
            'toc': '<!-- toc -->',
            'main_content': '<!-- main_content -->',
        })
        self.stdin = StringIO()
        self.stdin.read = self.stdin.getvalue
        self.stdout = StringIO()
        self.backdoc = BackDoc(
            markdown_converter=Markdown(extras=['toc']), 
            template_html=self.template_html,
            stdin=self.stdin,
            stdout=self.stdout
        )

    def _get_stdout_as_json(self):
        response = (
            self.stdout.getvalue()
                .replace('\n', '')
                .replace('="', "='")
                .replace('">', "'>")
        )
        try:
            return json.loads(response)
        except ValueError as e:
            self.fail('\nError occured while json loading from:\n{0}\n\nError:\n{1}'.format(
                response,
                e.args[0]
            ))

    def test_no_argv_and_no_stdin(self):
        self.backdoc.run([])
        self.assertEqual(
            self._get_stdout_as_json()['title'], 
            'Documentation', 
            'if no title specified, then "Documentation" title should be used'
        )
        self.assertEqual(
            self._get_stdout_as_json()['toc'], 
            '', 
            'if no source specified, then no TOC should be used'
        )
        self.assertEqual(
            self._get_stdout_as_json()['main_content'], 
            '<p></p>', 
            'if no source specified and no stdin, then empty paragrapth should used as main content'
        )

    def test_no_argv_but_with_stdin(self):
        self.stdin.write('Hello\n')
        self.backdoc.run([])
        self.assertEqual(
            self._get_stdout_as_json()['main_content'], 
            '<p>Hello</p>', 
            'if no source specified, but stdin is filled, then html should be generated from stdin'
        )
        self.assertEqual(
            self._get_stdout_as_json()['toc'], 
            '', 
            'if source specified without headers, then TOC should not been generated'
        )

    def test_if_source_in_argv_and_in_stdin_then_argv_source_should_be_used(self):
        self.stdin.write('Hello\n')
        self.backdoc.run(['--source', './test.md'])
        self.assertEqual(
            self._get_stdout_as_json()['main_content'], 
            '<p>World</p>', 
            'if source specified in argv and in stdin, then argv source should be used'
        )

    def test_title_from_argv(self):
        self.backdoc.run(['--title', 'My documentation'])
        self.assertEqual(
            self._get_stdout_as_json()['title'], 
            'My documentation', 
            'if title specified in argv, then it should be used'
        )

    def test_short_argv_names(self):
        self.backdoc.run(['-t', 'My documentation', '-s', './test.md'])
        self.assertEqual(self._get_stdout_as_json()['title'], 'My documentation')
        self.assertEqual(self._get_stdout_as_json()['main_content'], '<p>World</p>')

    def test_not_ascii_chars(self):
        self.stdin.write('Заголовок')
        self.backdoc.run(['--title', 'Документация'])
        self.assertEqual(
            self._get_stdout_as_json()['title'], 
            u'Документация', 
            'if not ascii chars in title, then they should be processed properly'
        )
        self.assertEqual(
            self._get_stdout_as_json()['main_content'], 
            u'<p>Заголовок</p>', 
            'if not ascii chars in source, then they should be processed properly'
        )

    def test_stdout_should_be_written_with_utf8_encoded_str(self):
        self.stdin.write('Заголовок')
        self.backdoc.run(['--title', 'Документация'])
        response = self.stdout.getvalue()
        
        expected = '{"toc": "", "main_content": "<p>Заголовок</p>\n", "title": "Документация"}'
        self.assertEqual(response, expected)
        self.assertEqual(type(response), str)


if __name__ == '__main__':
    unittest.main()