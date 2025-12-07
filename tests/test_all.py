import unittest

# Импортируем все тестовые классы
from tests.test_calculator import TestCalculator
from tests.test_even_number import TestIsEven
from tests.test_division import TestSafeDivide

def run_all_tests():
    """Запускает все тесты"""
    # Создаем test suite
    test_suite = unittest.TestSuite()
    
    # Добавляем тесты
    loader = unittest.TestLoader()
    
    test_suite.addTests(loader.loadTestsFromTestCase(TestCalculator))
    test_suite.addTests(loader.loadTestsFromTestCase(TestIsEven))
    test_suite.addTests(loader.loadTestsFromTestCase(TestSafeDivide))
    
    # Запускаем тесты
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(test_suite)
    
    return result

if __name__ == '__main__':
    run_all_tests()