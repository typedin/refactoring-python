import json
import unittest
from src.statement import statement

with open("data/plays.json") as f:
    plays = json.load(f)
with open("data/invoices.json") as f:
    invoices = json.load(f)


EXPECTATION = '''Statement for BigCo
 Hamlet: $650.00 (55 seats)
 As You Like It: $580.00 (35 seats)
 Othello: $500.00 (40 seats)
Amount owed is $1,730.00
You earned 47 credits
'''


class TestStatement(unittest.TestCase):
    def test_sanity(self):
        self.assertMultiLineEqual(EXPECTATION, statement(invoices[0], plays))


if __name__ == '__main__':
    unittest.main()
