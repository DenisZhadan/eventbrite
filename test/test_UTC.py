import datetime
from unittest import TestCase

from UTC import UTC


class TestUTC(TestCase):
    def test__last_sunday(self):
        utc = UTC()

        # Test for February 2024 (leap year)
        assert utc.get_last_sunday_of_month(2024, 2) == 25

        # Test for March 2024
        assert utc.get_last_sunday_of_month(2024, 3) == 31

        # Test for April 2024
        assert utc.get_last_sunday_of_month(2024, 4) == 28

        # Test for December 2024
        assert utc.get_last_sunday_of_month(2024, 12) == 29

    def test__is_dst(self):
        utc = UTC()

        self.assertFalse(utc.is_dst(datetime.datetime(2024, 12, 31, 0, 0, 0)))
        self.assertFalse(utc.is_dst(datetime.datetime(2024, 1, 1, 0, 0, 0)))

        self.assertFalse(utc.is_dst(datetime.datetime(2024, 3, 30, 3, 0, 0)))
        self.assertTrue(utc.is_dst(datetime.datetime(2024, 3, 31, 3, 0, 0)))
        self.assertTrue(utc.is_dst(datetime.datetime(2024, 3, 31, 4, 0, 0)))

        self.assertTrue(utc.is_dst(datetime.datetime(2024, 10, 26, 3, 0, 0)))
        self.assertTrue(utc.is_dst(datetime.datetime(2024, 10, 27, 3, 0, 0)))
        self.assertFalse(utc.is_dst(datetime.datetime(2024, 10, 27, 4, 0, 0)))
        self.assertFalse(utc.is_dst(datetime.datetime(2024, 10, 27, 5, 0, 0)))

    def test__tallinn_to_utc(self):
        utc = UTC()

        self.assertEqual(utc.tallinn_to_utc('2024-03-30 19:00:00'), '2024-03-30T17:00:00Z')
        self.assertEqual(utc.tallinn_to_utc('2024-03-31 19:00:00'), '2024-03-31T16:00:00Z')

        self.assertEqual(utc.tallinn_to_utc('2024-10-26 19:00:00'), '2024-10-26T16:00:00Z')
        self.assertEqual(utc.tallinn_to_utc('2024-10-27 19:00:00'), '2024-10-27T17:00:00Z')

