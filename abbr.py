def abbr(inp):
    inps = inp.split()
    abbriv = ''
    for s in inps:
        el = s[0]
        if el.isalpha():
            abbriv += el.upper()
    return abbriv

# Примеры использования
ex = [
    "Today I learned",
    "Высшее учебное заведение",
    "Кот обладает талантом",
    "Ар 2 Ди #2",
    "Анна-Мария Волхонская"
]

for i in ex:
    print(i, "-", abbr(i))
