def count(num):
    ls = [0] * 10
    for i in str(num):
        ls[int(i)] += 1

    for j in range(10):
        if ls[j] != 0:
            print(j, "-", ls[j])

# Пример использования
num = int(input("Введите число: "))
count(num)
