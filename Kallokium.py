from typing import List, Optional


# 1. Генерация первых n чисел Фибоначчи
def fibonacci(n: int) -> List[int]:
    if n <= 0:
        return []
    elif n == 1:
        return [0]

    fib_sequence = [0, 1]
    while len(fib_sequence) < n:
        next_num = fib_sequence[-1] + fib_sequence[-2]
        fib_sequence.append(next_num)

    return fib_sequence[:n]


# 2. Проверка является ли число палиндромом
def is_palindrome(number: int) -> bool:
    if number < 0:
        return False
    return str(number) == str(number)[::-1]


# 3. Разворот связного списка итеративным методом
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverse_linked_list(head: Optional[ListNode]) -> Optional[ListNode]:
    prev = None
    current = head

    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node

    return prev


# Примеры использования
if __name__ == "__main__":
    # Тестирование чисел Фибоначчи
    print("Первые 10 чисел Фибоначчи:", fibonacci(10))

    # Тестирование палиндромов
    test_numbers = [121, 123, 12321, 123421]
    for num in test_numbers:
        print(f"Число {num} {'является' if is_palindrome(num) else 'не является'} палиндромом")

    # Тестирование разворота связного списка
    # Создаем список: 1 -> 2 -> 3 -> 4 -> 5
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    print("\nИсходный список:")
    current = head
    while current:
        print(current.val, end=" -> " if current.next else "")
        current = current.next

    # Разворачиваем список
    reversed_head = reverse_linked_list(head)

    print("\nРазвернутый список:")
    current = reversed_head
    while current:
        print(current.val, end=" -> " if current.next else "")
        current = current.next