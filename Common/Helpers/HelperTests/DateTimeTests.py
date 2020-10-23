import unittest

from Helpers.DateTimeHelpers import DateTimeHelpers


class DateTimeTests(unittest.TestCase):

    def test_LargeDateRange(self):
        difference = DateTimeHelpers._getDateDiff('2020-10-01T06:48:52.662-0400', '2020-10-31T06:48:52.662-0400')
        print(difference)
        self.assertEqual(22, difference)

    def test_SmallDateRange(self):
        difference = DateTimeHelpers._getDateDiff('2020-10-21T06:48:52.662-0400', '2020-10-22T06:48:52.662-0400')
        print(difference)
        self.assertEqual(2, difference)

    def test_SmallestDateRange(self):
        difference = DateTimeHelpers._getDateDiff('2020-10-21T06:48:52.662-0400', '2020-10-21T12:48:52.662-0400')
        print(difference)
        self.assertEqual(1, difference)


if __name__ == '__main__':
    unittest.main()
