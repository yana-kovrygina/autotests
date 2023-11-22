import unittest
import requests
from unittests_words import join_words
from unittest.mock import Mock, MagicMock, patch
import datetime


def mocked_get(*args, **kwargs):
    return "badger-racoon"


class TestWords(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("A test suite begins")

    @classmethod
    def tearDownClass(cls):
        print("\nA test suite ends")

    def setUp(self):
        print("\nA test begins")

    def tearDown(self):
        print("A test ends")

    def test_smoke(self):
        result = join_words("sponge", "bob")

        self.assertEqual(result, "sponge-bob")

    def test_empty(self):
        result = join_words("", "")

        self.assertEqual(result, "-")

    @unittest.skip("Skipped")
    def test_skip(self):
        print("This test is skipped")
        pass

    @unittest.expectedFailure
    def test_xfail(self):
        result = join_words("", "")
        self.assertEqual(result, "")

    @patch("requests.get", side_effect=mocked_get)
    def test_badger(self, mock):
        response = requests.get("https://www.google.com/search?q=badger")

        self.assertEqual(response, "badger-racoon")

    @unittest.skipIf(datetime.datetime.now().weekday() in [0, 2, 4], "Skip on Monday, Wednesday, Friday")
    def test_skipping_on_days(self):
        result = join_words("square", "pants")
        self.assertNotEqual(result, "squarepants")

    @patch('requests.get')
    def test_google_request(self, mock_get):
        mock_get.return_value.status_code = 404
        response = requests.get('https://www.google.com')

        self.assertEqual(response.status_code, 404)
