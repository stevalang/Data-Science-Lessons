from random import random

def bernoulli(p=.5):
    if random() < p:
        return 1
    return 0

def perform_geom(p=.5):

    num_trials = 0

    for _ in range(2_000_000):
        flip = bernoulli(p)
        num_trials += 1
        print(f'trial: {flip}')
        if flip == 1:
            break

    print(f'Success on the {num_trials} trial')

def geometric(p=0.5):
    # num of failures prior to success
    lst = []

    for _ in range(100000):
        flip = bernoulli(p)
        lst.append(flip)

        if flip == 1:
            break
    
    return len(lst) - 1
# print(geometric(p=0.005))
# perform_geom()


def geometric_samples_dict(p=0.05, num_samples=10_000):

    d = {}

    for _ in range(num_samples):
        num_failures = geometric(p)

        if num_failures not in d:
            d[num_failures] = 0
        d[num_failures] += 1

    return d


dic = geometric_samples_dict()

# for k, v in sorted(dic.items()):
#     print(f'{k}: {v}')



''' could do mult trials of our sampling approach '''

def geom_samp_prob_dict(p=0.05, num_samples=10_000):
    
    d = geometric_samples_dict(p, num_samples)
    d_out = dict()

    for k, v in d.items():
        d_out[k] = v/ num_samples

    return d_out

d = geom_samp_prob_dict()
# for k, v in d.items():
#     print(f'{k}: {v}')

