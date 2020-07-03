import unittest
from src.statement import statement


class TestAppleSauce(unittest.TestCase):
    def test_sanity(self):
        self.assertEqual("FOO", statement())


if __name__ == '__main__':
    unittest.main()
