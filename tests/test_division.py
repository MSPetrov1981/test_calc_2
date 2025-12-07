import unittest
from src.calculator import safe_divide


class TestSafeDivide(unittest.TestCase):
    """Тесты для функции safe_divide с обработкой исключений"""
    
    def test_normal_division(self):
        """Тестирование нормального деления"""
        test_cases = [
            (10, 2, 5.0),
            (9, 3, 3.0),
            (5, 2, 2.5),
            (0, 5, 0.0),
            (-10, 2, -5.0),
            (10, -2, -5.0),
            (-10, -2, 5.0),
            (1, 3, 1/3),  # дробный результат
        ]
        
        for a, b, expected in test_cases:
            with self.subTest(a=a, b=b, expected=expected):
                self.assertEqual(safe_divide(a, b), expected)
    
    def test_division_by_zero(self):
        """Тестирование деления на ноль с использованием assertRaises"""
        # Тестирование что исключение возникает
        with self.assertRaises(ZeroDivisionError):
            safe_divide(10, 0)
        
        # Тестирование с проверкой сообщения об ошибке
        with self.assertRaises(ZeroDivisionError) as context:
            safe_divide(5, 0)
        
        self.assertEqual(str(context.exception), "Деление на ноль невозможно")
        
        # Несколько тестов на деление на ноль
        test_cases = [
            (10, 0),
            (-5, 0),
            (0, 0),  # 0/0 тоже вызывает ZeroDivisionError
            (3.14, 0),
        ]
        
        for a, b in test_cases:
            with self.subTest(a=a, b=b):
                with self.assertRaises(ZeroDivisionError):
                    safe_divide(a, b)
    
    def test_division_with_float(self):
        """Тестирование деления с дробными числами"""
        self.assertEqual(safe_divide(5.5, 2), 2.75)
        self.assertEqual(safe_divide(10, 4.0), 2.5)
        self.assertEqual(safe_divide(3.14, 2), 1.57)
    
    def test_division_large_numbers(self):
        """Тестирование деления больших чисел"""
        self.assertEqual(safe_divide(1000000, 2), 500000)
        self.assertEqual(safe_divide(1, 1000000), 0.000001)
    
    def test_division_result_type(self):
        """Тестирование типа результата деления"""
        # Деление целых чисел может давать float
        result = safe_divide(5, 2)
        self.assertIsInstance(result, float)
        
        # Деление целых чисел может давать int (если делится нацело)
        result = safe_divide(10, 2)
        self.assertIsInstance(result, float)  # В Python 3 всегда float при делении


if __name__ == '__main__':
    unittest.main()