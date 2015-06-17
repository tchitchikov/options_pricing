__author__ = 'John'
from MarkIt import DataPull
import unittest


class TestMarkItCall(unittest.TestCase):
    # def setUp(self):
    #     pass

    def test_markit_pull(self):
        markit = DataPull()
        result = markit.stock_quote_api()
        self.assertIn("SUCCESS", str(result))

