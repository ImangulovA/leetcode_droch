# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        """
        Удаляет дубликаты из отсортированного связного списка.
        
        Args:
            head: Голова связного списка
            
        Returns:
            Голова списка без дубликатов
        """
        # Если список пустой или содержит только один элемент
        if not head or not head.next:
            return head
        
        current = head
        
        # Проходим по списку и удаляем дубликаты
        while current.next:
            # Если текущий элемент равен следующему, пропускаем следующий
            if current.val == current.next.val:
                current.next = current.next.next
            else:
                current = current.next
        
        return head

# Функция для создания связного списка из массива (для тестирования)
def create_linked_list(arr):
    if not arr:
        return None
    
    head = ListNode(arr[0])
    current = head
    
    for val in arr[1:]:
        current.next = ListNode(val)
        current = current.next
    
    return head

# Функция для преобразования связного списка в массив (для тестирования)
def linked_list_to_array(head):
    result = []
    current = head
    
    while current:
        result.append(current.val)
        current = current.next
    
    return result

# Тестирование
if __name__ == "__main__":
    # Тест 1: [1,1,2] -> [1,2]
    test1 = create_linked_list([1, 1, 2])
    solution = Solution()
    result1 = solution.deleteDuplicates(test1)
    print("Тест 1:", linked_list_to_array(result1))
    
    # Тест 2: [1,1,2,3,3] -> [1,2,3]
    test2 = create_linked_list([1, 1, 2, 3, 3])
    result2 = solution.deleteDuplicates(test2)
    print("Тест 2:", linked_list_to_array(result2))
    
    # Тест 3: [1,1,1] -> [1]
    test3 = create_linked_list([1, 1, 1])
    result3 = solution.deleteDuplicates(test3)
    print("Тест 3:", linked_list_to_array(result3))
    
    # Тест 4: [] -> []
    test4 = create_linked_list([])
    result4 = solution.deleteDuplicates(test4)
    print("Тест 4:", linked_list_to_array(result4) if result4 else [])
