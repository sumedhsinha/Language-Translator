"""
This will be used for translations
"""
import unittest
from translator import english_to_french, french_to_english

class TestEnglishtofrench(unittest.TestCase):
    """
    This class will be used for testing English to French
    """
    def test1(self):
        """
        This is a test for English to French
        """
        self.assertEqual(english_to_french("Hello"), "Bonjour") #test e2f-1-ae
        self.assertEqual(english_to_french("Goodbye"), "Au revoir") #test e2f-2-ae
        self.assertEqual(english_to_french("Good day"), "Bonne journée") #test e2f-3-ae
        self.assertNotEqual(english_to_french("hello"), "hello") #test e2f-4-ane

class TestFrenchtoenglish(unittest.TestCase):
    """
    This class will be used for testing French to English
    """
    def test1(self):
        """
        This is a test for French to English
        """
        self.assertEqual(french_to_english("Bonjour"), "Hello") #test f2e-1-ae.
        self.assertEqual(french_to_english("Au revoir"), "Goodbye") #test f2e-2-ae
        self.assertEqual(french_to_english("Bonne journée"), "Good day") #test f2e-3-ae.
        self.assertNotEqual(french_to_english("bonjour"), "bonjour") #test f2e-4-ane

unittest.main()
