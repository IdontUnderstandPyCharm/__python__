class Slice:
    def __init__(self, data, start=0, stop=None, step=1):
        self.data = data
        self.start = start
        self.stop = stop
        self.step = step
        self.curr = self.start

        # отрицательное, положительное
        if self.start < 0:
            self.start += len(data)
            self.curr = self.start

        if self.stop < 0:
            self.stop += len(data)

        # почему нет
        self.start = max(0, min(self.start, len(data)))
        self.stop = max(0, min(self.stop, len(data)))

    def __iter__(self):
        return self

    def __next__(self):
        if (self.step > 0 and self.curr >= self.stop) or (self.step < 0 and self.curr <= self.stop):
            raise StopIteration

        if 0 <= self.curr < len(self.data): # почему нет
            value = self.data[self.curr]
            self.curr += self.step
            return value
        else:
            raise StopIteration

data = [10, 20, 30, 40, 50, 60, 70, 80]
slice = Slice(data, start=1, stop=6, step=2)
for i in slice:
    print(i)
