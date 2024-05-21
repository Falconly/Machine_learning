import math

s = [1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0]

lst_gini_weight = []
N = len(s)

for i in range(len(s)):
    N_left = len(s[:i + 1])
    N_right = len(s[i + 1:])

    if N_right == 0 or N_left == 0:
        break

    gini_left = 1 - math.pow(s[:i + 1].count(1) / N_left, 2) - math.pow(s[:i + 1].count(0) / N_left, 2)
    gini_right = 1 - math.pow(s[i + 1:].count(1) / N_right, 2) - math.pow(s[i + 1:].count(0) / N_right, 2)

    gini_weight = N_left / N * gini_left + N_right / N * gini_right
    lst_gini_weight.append(gini_weight)

min_ = 10
index = 0
for i, val in enumerate(lst_gini_weight):
    print(f'Узел {i}: {round(val, 2)}')

    if val < min_:
        min_ = val
        index = i

print(f'Узел с порядковым номером - {index} имеет наименьший весовой показатель {min_}, следовательно, в этом узле '
      f'лучше всего начинать разделение для дерева')