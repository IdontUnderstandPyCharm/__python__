def farray(mass):
    ans, mass_exp = [], mass
    while mass != []:
        mas, k = [], []
        for i in range(len(mass)):
            #print(mass[i], i, mass)
            if mass[i] not in mas:
                mas.append(mass[i])
                k.append(int(i))
        for j in range(len(k)):
            mass.pop(j)
        ans.append(mas)
    return ans

print(farray([1,3,4,1,2,3,1]))
