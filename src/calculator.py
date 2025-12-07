def calculator(a, b, operation):
    """
    Выполняет базовые арифметические операции.
    
    Args:
        a: первое число
        b: второе число
        operation: строка с названием операции ('add', 'subtract', 'multiply', 'divide')
    
    Returns:
        Результат операции
    
    Raises:
        ValueError: если операция не поддерживается
    """
    if operation == 'add':
        return a + b
    elif operation == 'subtract':
        return a - b
    elif operation == 'multiply':
        return a * b
    elif operation == 'divide':
        if b == 0:
            raise ZeroDivisionError("Деление на ноль невозможно")
        return a / b
    else:
        raise ValueError(f"Неподдерживаемая операция: {operation}")


def is_even(num):
    """
    Проверяет, является ли число четным.
    
    Args:
        num: число для проверки
    
    Returns:
        True если число четное, иначе False
    """
    return num % 2 == 0


def safe_divide(a, b):
    """
    Выполняет безопасное деление с обработкой исключения.
    
    Args:
        a: делимое
        b: делитель
    
    Returns:
        Результат деления a на b
    
    Raises:
        ZeroDivisionError: при попытке деления на ноль
    """
    if b == 0:
        raise ZeroDivisionError("Деление на ноль невозможно")
    return a / b