from math import pow

class Solution:
    def maximumSwap(self, num: int) -> int:
        nlist = list(map(int,list(str(num))))
        mdelta = 0
        mik = [0,0]
        for i in range(0, len(nlist)-1):
            for k in range(1, len(nlist)):
                if nlist[i] < nlist[k]:
                    delta = (nlist[k]-nlist[i]) * pow(10, k) + (nlist[i] - nlist[k]) * pow(10, i)
                    if delta > mdelta:
                        mdelta = delta
                        mik = [i,k]
                        print(delta,i,k)
        return num + delta

# Исправленная версия
class SolutionFixed:
    def maximumSwap(self, num: int) -> int:
        nlist = list(map(int, list(str(num))))
        max_num = num
        
        for i in range(len(nlist)):
            for j in range(i + 1, len(nlist)):
                # Меняем местами цифры
                nlist[i], nlist[j] = nlist[j], nlist[i]
                # Преобразуем обратно в число
                new_num = int(''.join(map(str, nlist)))
                # Обновляем максимум
                max_num = max(max_num, new_num)
                # Возвращаем цифры на место для следующей итерации
                nlist[i], nlist[j] = nlist[j], nlist[i]
        
        return max_num

def test_maximum_swap():
    # Тестовые случаи
    test_cases = [
        (2736, 7236),  # Ожидаемый результат: 7236
        (9973, 9973),  # Ожидаемый результат: 9973 (уже максимальное)
        (98368, 98863), # Ожидаемый результат: 98863
        (1993, 9913),  # Ожидаемый результат: 9913
        (1234, 4231),  # Ожидаемый результат: 4231
        (4321, 4321),  # Ожидаемый результат: 4321 (уже максимальное)
        (0, 0),        # Ожидаемый результат: 0
        (10, 10),      # Ожидаемый результат: 10
        (12, 21),      # Ожидаемый результат: 21
    ]
    
    print("Тестирование оригинальной версии:")
    print("=" * 50)
    
    for i, (input_num, expected) in enumerate(test_cases):
        try:
            result = Solution().maximumSwap(input_num)
            status = "✓" if result == expected else "✗"
            print(f"Тест {i+1}: {input_num} -> {result} (ожидалось: {expected}) {status}")
            if result != expected:
                print(f"  ОШИБКА: Получено {result}, ожидалось {expected}")
        except Exception as e:
            print(f"Тест {i+1}: {input_num} -> ОШИБКА: {e}")
    
    print("\nТестирование исправленной версии:")
    print("=" * 50)
    
    for i, (input_num, expected) in enumerate(test_cases):
        try:
            result = SolutionFixed().maximumSwap(input_num)
            status = "✓" if result == expected else "✗"
            print(f"Тест {i+1}: {input_num} -> {result} (ожидалось: {expected}) {status}")
            if result != expected:
                print(f"  ОШИБКА: Получено {result}, ожидалось {expected}")
        except Exception as e:
            print(f"Тест {i+1}: {input_num} -> ОШИБКА: {e}")

if __name__ == "__main__":
    test_maximum_swap() 