import unittest
from joshDataPDFRedactor.pdf_redactor import addTrailingSpaceIfAbsent


class MyTestCase(unittest.TestCase):
    def testWithoutTrailingSpace(self):
        self.assertEqual(addTrailingSpaceIfAbsent('hello'), 'hello ')

    def testWithTrailingSpace(self):
        self.assertEqual(addTrailingSpaceIfAbsent('hello '), 'hello ')

    def testWithTrailingTab(self):
        self.assertEqual(addTrailingSpaceIfAbsent('hello\t'), 'hello\t')


if __name__ == '__main__':
    unittest.main()
