all_toys_possible  = []

for toy1 in five_toys:
    for toy2 in five_toys:
        for toy3 in five_toys:
            for toy4 in five_toys:
                for toy5 in five_toys:
                    all_toys_possible.append([toy1, toy2, toy3, toy4, toy5])

A = []
for toys in all_toys_possible:
    if 'pog' in toys and 'fidget spinner' in toys and 'tamagotchi' in toys:
        A.append(toys)

# for toys in all_toys_possible:
    # print(toys)

# print(len(all_toys_possible))

# print(len(A))

for toys in A:
    print(toys)

print(len(A)/ len(all_toys_possible))
