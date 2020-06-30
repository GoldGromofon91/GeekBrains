fruit_1 = ['дыня','арбуз','виноград','фейхоа','груша']
fruit_2 = ['груша','слива','яблоки','арбуз','гранат']
res_fruit = []
# Классическое решение
for fru in fruit_1:
    if fru in fruit_2:
        res_fruit.append(fru)
print(res_fruit)
# Через генератор списка
res_fruit = [fruit for fruit in fruit_1 if fruit in fruit_2]
print(res_fruit)