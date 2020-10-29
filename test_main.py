import unittest

"""
Authors: Edward and Billy
The user story:
A complete look at a user's genealogical history.

These tests are to check the function in the python_gedcom_reader file will accurately count the number of lines, content of the file,
"""
from main import gedcom_reader_func_matt
from main import gedcom_reader_func_guowei
from main import gedcom_reader_func_edward
from main import males_in_family
from main import females_in_family

class TestGedcomReader(unittest.TestCase):
    def test_gedcom_reader(self):
        self.assertEqual(gedcom_reader_func_edward("Guowei-Project02.ged"), "Unknown")

    def test_males_in_family(self):
        self.assertEqual(males_in_family("Guowei-Project02.ged"), 36)

    def test_females_in_family(self):
        ##Checks the first line of the gedcom file
        self.assertEqual(females_in_family("Holcomb-Project02.ged"), "Unknown")
    
    def test_total_married(self):
        self.assertEqual(total_married("Guowie.ged"), 10)


if __name__ == "__main__":
    unittest.main()
    print('Running unit tests')
