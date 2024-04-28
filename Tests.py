import unittest
from unique_names_counter import unique_names_counter

class TestUniqueNamesCounter(unittest.TestCase):
    
    def test_same_names(self):
        self.assertEqual(unique_names_counter.countUniqueNames("Deborah","Egli","Deborah","Egli","Deborah Egli"), 1)
        
    def test_same_reordered_names(self):
        self.assertEqual(unique_names_counter.countUniqueNames("Deborah","Egli","Deborah","Egli","Egli Deborah"), 1)
                         
    def test_middle_names(self):
        self.assertEqual(unique_names_counter.countUniqueNames("Deborah", "Egli", "Deborah", "Egli", "Deborah S Egli"), 1)
        self.assertEqual(unique_names_counter.countUniqueNames("Deborah", "Egli", "Deborah S", "Egli", "Deborah Egli"), 1)
        self.assertEqual(unique_names_counter.countUniqueNames("Deborah S", "Egli", "Deborah", "Egli", "Deborah Egli"), 1)
        
    def test_different_firstnames(self):
        self.assertEqual(unique_names_counter.countUniqueNames("Michele", "Egli", "Deborah", "Egli", "Michele Egli"), 2)
        self.assertEqual(unique_names_counter.countUniqueNames("Deborah", "Egli", "Michele", "Egli", "Michele Egli"), 2)
        self.assertEqual(unique_names_counter.countUniqueNames("Michele", "Egli", "Michele", "Egli", "Deborah Egli"), 2)
        
    def test_different_lastnames(self):
        self.assertEqual(unique_names_counter.countUniqueNames("Deborah", "Cohen", "Deborah", "Egli", "Deborah Cohen"), 2)
        self.assertEqual(unique_names_counter.countUniqueNames("Deborah", "Egli", "Deborah", "Cohen", "Deborah Cohen"), 2)
        self.assertEqual(unique_names_counter.countUniqueNames("Deborah", "Cohen", "Deborah", "Cohen", "Deborah Egli"), 2)
        
    def test_typos_firstnames(self):
        self.assertEqual(unique_names_counter.countUniqueNames("Deburah", "Egli", "Deborah", "Egli", "Deborah Egli"), 1)
        self.assertEqual(unique_names_counter.countUniqueNames("Deborah", "Egli", "Deburah", "Egli", "Deborah Egli"), 1)
        self.assertEqual(unique_names_counter.countUniqueNames("Deborah", "Egli", "Deborah", "Egli", "Deburah Egli"), 1)
        
    def test_typos_lastnames(self):
        self.assertEqual(unique_names_counter.countUniqueNames("Deborah", "Egni", "Deborah", "Egli", "Deborah Egli"), 1)
        self.assertEqual(unique_names_counter.countUniqueNames("Deborah", "Egli", "Deborah", "Egni", "Deborah Egli"), 1)
        self.assertEqual(unique_names_counter.countUniqueNames("Deborah", "Egli", "Deborah", "Egli", "Deborah Egni"), 1)
    
    def test_nicknames(self):
        self.assertEqual(unique_names_counter.countUniqueNames("Deborah", "Egli", "Debbie", "Egli", "Debbie Egli"), 1)
        self.assertEqual(unique_names_counter.countUniqueNames("Debbie", "Egli", "Deborah", "Egli", "Debbie Egli"), 1)
    
    # assumptions: at least one original firstname(no nickname) in firstname1 or firstname2
    #              no composing cases
        
        

if __name__ == '__main__':
    unittest.main()
