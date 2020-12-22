from math import factorial


def combs(n, k):

    perm = 1

    for num in range(n, n-k, -1):
        perm *= num
    
    return perm/factorial(k)

print(combs(11, 5))

num_comba = combs(11, 5)



def futsol_team_combs():
    
    eleven_nums = range(1, 11 + 1)

    base_11 = []
    for p1 in eleven_nums:
        for p2 in eleven_nums:
            for p3 in eleven_nums:
                for p4 in eleven_nums:
                    for p5 in eleven_nums:
                        base_11.append([p1, p2, p3, p4, p5])
    
    permutations = []

    for five in base_11:
        if len(list(set(five))) == 5:
            permutations.append(five)
    
    # for perm in permutations:
        # print(perm)

#     combinations = []

#     for five in permutations:
#         sorted_five = sorted(five)

#         if sorted_five not in combinations:
#             combinations.append(sorted_five)
#     return combinations

# for five in futsol_team_combs():
#     print(five)










'''
an expensive sampling approach
We can sample 5 players from out list of 11, 
can build combinations until we reach combs(11, 5)
'''

from random import choice


def futsol_combs_samp(team_size=11, num_players=5):
     
    player_combs = []

    player_range = range(1, team_size + 1)
     
    while len(player_combs) < combs(team_size, num_players):
        player_comb = []

        while len(player_comb) < num_players:
            player_num = choice(player_range)

            if player_num not in player_comb:
                player_comb.append(player_num)

        player_comb = sorted(player_comb)

        if player_comb not in combs:
            print(player_comb)
            player_combs.append(player_comb)

    return player_combs


team_size = 11
num_player = 5

print(combs(team_size, num_player))

print(len(futsol_combs_samp()))

