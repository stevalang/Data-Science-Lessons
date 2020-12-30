def dec_to_bin(dec, n_bits):
    
    
    bin_lst = []
    x = dec

    while x >= 0:
        bin_lst.append(x % 2)
        x //= 2

    return bin_lst[::-1]


def get_binary(n_bits):
    bins_d = dict()

    for dec in range(2**n_bits):
        bins_d[dec] = dec_to_bin(dec, n_bits)

    return bins_d


def binomial_distr(n_trials):
    
    binomial_dict = dict()

    bin_dict = get_binary(n_bits=n_trials)

    for _, val in bin_dict.items():
        
        sum_bits = sum(val)

        if sum_bits not in binomial_dict:
            binomial_dict[sum_bits] = 0
        binomial_dict[sum_bits] += 1

    return binomial_dict

d = binomial_distr(12)

for k, v in d.items():
    print(f'{k}: {v}')


