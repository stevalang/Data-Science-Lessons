'''
How to count in binary?
00 0000
01 0001
02 0010
03 0011
04 0100
05 0101
06 0110
07 0111
08 1000
09 1001
10 1010
11 1011
12 1100
13 1101
14 1110
15 1111


1    1    0    1
8's  4's  2's  1's places

1*8 + 1*4 + 0*2 + 1*1 = 13

Can think of a binary number (word) as being a series of successes
and failures
1100
SSFF

The count of 1's in 4-bit binary will follow a binomial distribution

0: *
1: ****
2: ******
3: ****
4: *

0: 1/16
1: 4/16
2: 6/16
3: 4/16
4: 1/16
'''

'''
count in 4-bit binary
'''

def gen_4_bit_binary():
    
    bin_dct = dict()
    
    decimal = 0

    for i in range(2):
        for j in range(2):
            for k in range(2):
                for l in range(2):
                    bin_dct[decimal] = [i,j,k,l]
                    decimal += 1
    return bin_dct

# for dec , bin_ in gen_4_bit_binary().items():
    # print(f'{dec}:{bin_}')



'''
    Code the dec_to_bin function. 
    Should take as input 2 things:
        a decimal value (dec)
        a number of bits (n_bits=8)
    algorithm
    Given a decimal number
        -take the modulus by 2
            - set aside the result
        - floor divide the number by 2
            -until that number is 0
        - reverse the sequence of outcomes

    dec_to_bin(43)
'''


def dec_to_bin(dec, n_bits=8):
    
    
    bin_lst = []
    x = dec

    for i in range(n_bits):
        bin_lst.append(x % 2)
        x //= 2

    return bin_lst[::-1]


# print(dec_to_bin(43))


def get_binary(n_bits=16):
    bins_d = dict()

    for dec in range(2**n_bits):
        bins_d[dec] = dec_to_bin(dec, n_bits)

    return bins_d

# for dec, bin_ in get_binary().items():
#     print(f'{dec}: {bin_}')




'''
Construct the binomial distr for n trials with prob=0.5 for each trial
'''

def binomial_distr(n_trials=8):
    
    binomial_dict = dict()

    bin_dict = get_binary(n_bits=n_trials)

    for _, val in bin_dict.items():
        
        sum_bits = sum(val)

        if sum_bits not in binomial_dict:
            binomial_dict[sum_bits] = 0
        binomial_dict[sum_bits] += 1

    return binomial_dict

d = binomial_distr(n_trials=12)

for k, v in d.items():
    print(f'{k}: {round(v / sum(d.values()),5)}')


'''
You flip a coin 12 times. 
What is the probability that you get 9 heads in 12 flips?

What is the probability of getting 4 or less heads in 12 flips?
P(X=0) + P(X=1) + P(X=2) + P(X=3) + P(X=4) = 0.19384
'''

