import unittest
from homework4 import Gedcom

#tests for searching how many people were born in a given time frame.
class BuggyGedcom(unittest.TestCase):
    def test_searchByYear(self):
        "test if obeject stored properly in __init__()"
        f = Gedcom("test GEDCOM file",1960,1970)
        self.assertEqual(f.searchByYears(),2)
        f = Gedcom("test GEDCOM file",1950,1960)
        self.assertEqual(f.searchByYears(),3)
        f = Gedcom("test GEDCOM file",1950,2000)
        self.assertEqual(f.searchByYears(),10)
        f = Gedcom("test GEDCOM file",1980,2000)
        self.assertEqual(f.searchByYears(),7)
        f = Gedcom("test GEDCOM file",1900,2020)
        self.assertEqual(f.searchByYears(),11)

if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit = False)