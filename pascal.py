def pascal(rowIndex):
    old = [1]
    for i in range(1, rowIndex + 1):
        # Создаем новый ряд на основе предыдущего:
        new = [1]
        for j in range(1, len(old)):
            new.append(old[j - 1] + old[j])
        new.append(1)
        old = new
    return old

print(pascal(3))
print(pascal(0))
print(pascal(1))
