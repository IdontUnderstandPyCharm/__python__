class FlattenIterator:
    def __init__(self, nested_list):
        self.ls = [iter(nested_list)]

    def __iter__(self):
        return self

    def __next__(self):
        while self.ls:
            try:
                current = next(self.ls[-1])
                if isinstance(current, list):
                    self.ls.append(iter(current))
                else:
                    return current
            except StopIteration:
                self.ls.pop()
        raise StopIteration

# Пример использования:
nested_list = [1, [2, [3, 4], 5], 6]
flat = FlattenIterator(nested_list)
for num in flat:
    print(num)
