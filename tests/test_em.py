# -*- coding: utf-8 -*-

from unittest import TestCase

try:
    from unittest.mock import call, patch  # Python 3
    print_function = 'builtins.print'
except ImportError:
    from mock import call, patch  # Python 2
    print_function = '__builtin__.print'

from em import cli


class TestCli(TestCase):

    @patch('em.docopt')
    @patch('em.sys.exit')
    @patch('em.xerox.copy')
    @patch(print_function)
    def test_star(self, mock_print, mock_xerox, mock_exit, mock_docopt):
        mock_docopt.return_value = {
            '<name>': ['star'],
            '--no-copy': None,
            '-s': None
        }

        cli()
        mock_xerox.assert_called_once_with(u'⭐')
        mock_print.assert_called_once_with(u'Copied! ⭐')

    @patch('em.docopt')
    @patch('em.sys.exit')
    @patch('em.xerox.copy')
    @patch(print_function)
    def test_no_copy(self, mock_print, mock_xerox, mock_exit, mock_docopt):
        mock_docopt.return_value = {
            '<name>': ['star'],
            '--no-copy': True,
            '-s': None
        }

        cli()
        mock_xerox.assert_not_called()
        mock_print.assert_called_once_with(u'⭐')

    @patch('em.docopt')
    @patch('em.sys.exit')
    @patch('em.xerox.copy')
    @patch(print_function)
    def test_search_star(self, mock_print, mock_xerox, mock_exit, mock_docopt):
        mock_docopt.return_value = {
            '<name>': ['star'],
            '--no-copy': None,
            '-s': True
        }
        expected = (
            u'💫  dizzy',
            u'⭐  star',
            u'✳️  eight_spoked_asterisk',
        )

        cli()
        mock_xerox.assert_not_called()
        for arg in expected:
            self.assertIn(call(arg), mock_print.call_args_list)
