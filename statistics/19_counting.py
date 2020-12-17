four_sided = [1, 2, 3, 4]
fair_coint = ['H', 'T']

samp_space = []

for roll in four_sided:
    for flip1 in fair_coint:
        for flip2 in fair_coint:
            samp_space.append([roll, flip1, flip2])

for outcome in samp_space:
    print(outcome)
