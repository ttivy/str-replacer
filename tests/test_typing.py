import unittest


class TestTyping(unittest.TestCase):
    @staticmethod
    def replacements(replacements):
        import replacer
        return replacer.Replacer(replacements)

    @staticmethod
    def content(content):
        import replacer
        return replacer.Replacer({}).replace(content)

    def test_replacements_raise(self):
        from collections import OrderedDict
        # Not raises
        self.replacements(dict())
        self.replacements(OrderedDict())
        # Raises
        self.assertRaises(ValueError, self.replacements, None)
        self.assertRaises(ValueError, self.replacements, int())
        self.assertRaises(ValueError, self.replacements, str())
        self.assertRaises(ValueError, self.replacements, bytes())
        self.assertRaises(ValueError, self.replacements, list())
        self.assertRaises(ValueError, self.replacements, set())

    def test_content_raise(self):
        # Not raises
        self.content(str())
        # Raises
        self.assertRaises(ValueError, self.content, None)
        self.assertRaises(ValueError, self.content, int())
        self.assertRaises(ValueError, self.content, bytes())
        self.assertRaises(ValueError, self.content, list())
        self.assertRaises(ValueError, self.content, set())
        self.assertRaises(ValueError, self.content, dict())
