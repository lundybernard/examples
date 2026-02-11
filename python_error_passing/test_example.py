from unittest import TestCase
from unittest.mock import patch


from python_error_passing.example import err_returning_func

class ExampleTests(TestCase):

    @patch('python_error_passing.example.side_effects', autospec=True)
    def test_err_returning_func(t, side_effects: Mock) -> None:
        with t.subTest('success'):
            side_effects.return_value = None

            ok, err = err_returning_func()

            side_effects.assert_called_once()
            t.assertIs(True, ok)
            t.assertIs(None, err)

        side_effects.reset_mock()

        with t.subTest('Exception'):
            captured_exception = NotImplementedError('test exception')
            side_effects.side_effect = captured_exception

            ok, err = err_returning_func()

            side_effects.assert_called_once()
            t.assertIs(False, ok)
            t.assertIs(captured_exception, err)
