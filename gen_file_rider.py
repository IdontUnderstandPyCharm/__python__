def read_lines(name):
    with open(name) as f:
        return f.read().split('\n')[0:-1:]


for line in read_lines("example.txt"):
    print(line.strip())
