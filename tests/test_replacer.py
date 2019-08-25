import unittest


class TestReplace(unittest.TestCase):
    @staticmethod
    def replace(replacements, content):
        import replacer
        return replacer.Replacer(replacements).replace(content)

    def test_replace_empty(self):
        replacements = {}
        self.assertEqual(self.replace(replacements, 'abcdef'), 'abcdef')

    def test_replace_start(self):
        replacements = {
            'a'  : '<A>',
            'ab' : '<AB>',
            'abc': '<ABC>',
        }
        self.assertEqual(self.replace(replacements, 'abcdef'), '<ABC>def')

    def test_replace_end(self):
        replacements = {
            'abc': '<ABC>',
            'bc' : '<BC>',
            'c'  : '<C>',
        }
        self.assertEqual(self.replace(replacements, 'abcdef'), '<ABC>def')

    def test_replace_overlap(self):
        replacements = {
            'ab': '<AB>',
            'bc': '<BC>',
            'cd': '<CD>',
        }
        self.assertEqual(self.replace(replacements, 'abcdef'), '<AB><CD>ef')
