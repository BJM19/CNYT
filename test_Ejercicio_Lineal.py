import unittest,calculadora
class TestCases(unittest.TestCase):
    def test_proba(self):
        a=2
        b=[(4,8),(7,2),(1,4)]
        self.assertEqual(calculadora.probability(a,b),20.26)
    def test_transicion(self):
        a=[(4,8),(7,2),(1,4)]
        b=[(4,8),(7,2),(1,4)]
        self.assertEqual(calculadora.transition(a,b),(98.0, -17.0))
    
if __name__=="__main__":
    unittest.main()
