import unittest
from src.calculator import calculator


class TestCalculator(unittest.TestCase):
    """Тесты для функции calculator"""
    
    def test_addition(self):
        """Тестирование сложения"""
        self.assertEqual(calculator(2, 3, 'add'), 5)
        self.assertEqual(calculator(-1, 1, 'add'), 0)
        self.assertEqual(calculator(0, 0, 'add'), 0)
        self.assertEqual(calculator(2.5, 3.5, 'add'), 6.0)
        self.assertEqual(calculator(-5, -3, 'add'), -8)
    
    def test_subtraction(self):
        """Тестирование вычитания"""
        self.assertEqual(calculator(10, 4, 'subtract'), 6)
        self.assertEqual(calculator(5, 5, 'subtract'), 0)
        self.assertEqual(calculator(0, 5, 'subtract'), -5)
        self.assertEqual(calculator(-3, 2, 'subtract'), -5)
        self.assertEqual(calculator(3.5, 1.5, 'subtract'), 2.0)
    
    def test_multiplication(self):
        """Тестирование умножения"""
        self.assertEqual(calculator(3, 4, 'multiply'), 12)
        self.assertEqual(calculator(0, 5, 'multiply'), 0)
        self.assertEqual(calculator(-3, 4, 'multiply'), -12)
        self.assertEqual(calculator(-2, -3, 'multiply'), 6)
        self.assertEqual(calculator(2.5, 4, 'multiply'), 10.0)
    
    def test_division(self):
        """Тестирование деления"""
        self.assertEqual(calculator(10, 2, 'divide'), 5.0)
        self.assertEqual(calculator(9, 3, 'divide'), 3.0)
        self.assertEqual(calculator(5, 2, 'divide'), 2.5)
        self.assertEqual(calculator(-10, 2, 'divide'), -5.0)
        self.assertEqual(calculator(0, 5, 'divide'), 0.0)
    
    def test_division_by_zero(self):
        """Тестирование деления на ноль"""
        with self.assertRaises(ZeroDivisionError):
            calculator(10, 0, 'divide')
    
    def test_invalid_operation(self):
        """Тестирование недопустимой операции"""
        with self.assertRaises(ValueError):
            calculator(10, 2, 'invalid_operation')


if __name__ == '__main__':
    unittest.main()