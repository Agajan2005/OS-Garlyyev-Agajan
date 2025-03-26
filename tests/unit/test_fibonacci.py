import unittest
from app.services.fibonacci import FibonacciService

class TestFibonacciService(unittest.TestCase):
    def test_generation(self):
        self.assertEqual(FibonacciService.generate(5), [0, 1, 1, 2, 3])
        self.assertEqual(FibonacciService.generate(1), [0])
        self.assertEqual(FibonacciService.generate(0), [])
    
    def test_validation(self):
        with self.assertRaises(ValueError):
            FibonacciService.generate(-1)
        with self.assertRaises(ValueError):
            FibonacciService.generate("invalid")
