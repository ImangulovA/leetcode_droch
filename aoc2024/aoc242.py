s1 = 0
s2 = 0

def reportcheck(arr):
    if len(arr) == 2:
        return True
    if arr[0] > arr[1]:
        for i in range(1,len(arr)):
            delta = arr[i-1] - arr[i]
            if (delta < 1) or (delta > 3):
                return False
    elif arr[0] < arr[1]:
        for i in range(1,len(arr)):
            delta = arr[i] - arr[i-1]
            if (delta < 1) or (delta > 3):
                return False
    elif arr[0] == arr[1]:
        return False
    return True

with open('C:/Users/Amal Imangulov/Downloads/input_2.txt', 'r') as f:
    for line in f:
        arr = list(map(int, line.split(' ')))
        is_ok = reportcheck(arr)
        if is_ok:
            s1+=1
            s2+=1
        else:
            extra = False
            for i in range(len(arr)):
                if reportcheck(arr[:i] + arr[i+1:]):
                    extra = True
                    break
            if extra:
                s2+=1

print(s1)
print(s2)
