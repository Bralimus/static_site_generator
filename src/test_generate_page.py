import unittest
from generate_page import *

class TestGeneratePage(unittest.TestCase):
    def test_base(self):
        text = "# Headline"
        self.assertEqual(extract_title(text), '"Headline"')

    def test_multiline(self):
        text = """
# Headline
## Headline 2
### Headline 3
        """
        self.assertEqual(extract_title(text), '"Headline"')

    def test_notfirst(self):
        text = """
### Headline
## Headline 2
# Headline 3
        """
        self.assertEqual(extract_title(text), '"Headline 3"')


if __name__ == "__main__":
    unittest.main()