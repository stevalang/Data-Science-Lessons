outcomes = []
for r1 in range(1,6+1):
    for r2 in range(1,6+1):
        for r3 in range(1,6+1):
            outcomes.append([r1,r2,r3])
A = []
for outcome in outcomes:
    if sum(outcome) < 6:
        A.append(outcome)

print(len(A)/ len(outcomes))
