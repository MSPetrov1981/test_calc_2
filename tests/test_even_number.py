import unittest
from src.calculator import is_even


class TestIsEven(unittest.TestCase):
    """Параметрические тесты для функции is_even"""
    
    def test_even_numbers(self):
        """Тестирование четных чисел с использованием subTest"""
        test_cases = [
            (0, True),      # ноль
            (2, True),      # положительное четное
            (-4, True),     # отрицательное четное
            (100, True),    # большое четное
            (-100, True),   # большое отрицательное четное
            (2.0, True),    # дробное, но целое четное
        ]
        
        for num, expected in test_cases:
            with self.subTest(num=num, expected=expected):
                self.assertEqual(is_even(num), expected)
    
    def test_odd_numbers(self):
        """Тестирование нечетных чисел с использованием subTest"""
        test_cases = [
            (1, False),     # положительное нечетное
            (-3, False),    # отрицательное нечетное
            (99, False),    # большое нечетное
            (-99, False),   # большое отрицательное нечетное
            (1.0, False),   # дробное, но целое нечетное
        ]
        
        for num, expected in test_cases:
            with self.subTest(num=num, expected=expected):
                self.assertEqual(is_even(num), expected)
    
    def test_edge_cases(self):
        """Тестирование граничных случаев"""
        edge_cases = [
            (0, True),          # ноль
            (1, False),         # минимальное положительное нечетное
            (-1, False),        # максимальное отрицательное нечетное
            (2, True),          # минимальное положительное четное
            (-2, True),         # максимальное отрицательное четное
            (1000000, True),    # очень большое четное
            (1000001, False),   # очень большое нечетное
        ]
        
        for num, expected in edge_cases:
            with self.subTest(num=num, expected=expected):
                self.assertEqual(is_even(num), expected)
    
    def test_float_numbers(self):
        """Тестирование дробных чисел (ожидается ошибка)"""
        with self.subTest("Дробное четное"):
            # 2.2 % 2 = 0.2, что не равно 0, поэтому False
            self.assertEqual(is_even(2.2), False)
        
        with self.subTest("Дробное нечетное"):
            self.assertEqual(is_even(3.7), False)


if __name__ == '__main__':
    unittest.main()