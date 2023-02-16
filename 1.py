def Func(x1, x2):
    return x1 ** 2 - x1 * x2 + 3 * x2 ** 2 - x1


e = 0.1  # точность
h = 0.2  # шаг
d = 2  # коэффициент уменьшения шага
m = 0.5
table = [[0, [0, 0], 0]]
min = table[0][2]
min1 = min
for qwerty in range(0, 10):
    print('номер итерации №', qwerty + 1)
    x1_plus = table[qwerty][1][0] + h
    func_rez = Func(x1_plus, table[qwerty][1][1])
    if min > func_rez:
        table.append([qwerty + 1, [x1_plus, 0], func_rez])
        min = func_rez

    x2_plus = table[qwerty][1][1] + h
    func_rez = Func(table[qwerty][1][0], x2_plus)
    if min > func_rez:
        table.append([qwerty + 1, [x1_plus, 0], func_rez])
    else:
        min = min1

    x2_minus = table[qwerty][1][1] - h
    func_rez = Func(table[qwerty][1][0], x2_minus)
    if min1 > func_rez:
        table.append([qwerty + 1, [x1_plus, 0], func_rez])
    else:
        table.append([qwerty + 2, [table[qwerty + 1][1][0] + m * (table[qwerty + 1][1][0] - table[qwerty][1][0]), table[qwerty + 1][1][1] + m * (table[qwerty + 1][1][1] - table[qwerty][1][1])], 0])
        table[qwerty + 2][2] = Func(table[qwerty + 2][1][0], table[qwerty + 2][1][1])
    if table[qwerty + 2][2] > min:
        table.pop()
    for i in table:
        print(i)
