'''
Using random(), we can change our p value
'''

from random import random

def get_success(p=0.5):
    if random() < p:
        return 1
    return 0

# print(get_succes(0.25))

def generate_n_successes(n=8, p=0.5):
    
    lst = []
    
    for _ in range(n):
        lst.append(get_success(p))
    
    return lst

# print(generate_n_successes(8, 0.5))

#verify, as 12 * 0.25 = 3
test_trials = 100_000
trial_results = []

for _ in range(test_trials):
    trial_results.append(generate_n_successes(12, p=0.75).count(1))

print(sum(trial_results)/test_trials)

def binary_sampling_vary_p(num_bits=8, p=0.5, num_samples=1000):
    d = dict()

    for _ in range(num_samples):
        binary = generate_n_successes(num_bits, p)
        k = sum(binary)

        if k not in d:
            d[k] = 0
        d[k] += 1
    
    return d


''' One trial of 1000 samples'''

# d = binary_sampling_vary_p(8, 0.3, 1000)

# for k, v in sorted(d.items()):
#     print(f'{k}: {v}')


''' 500 trials of 1000 samples '''

def binary_sampling_clt_vary_p(n_bits=8, p=0.5, num_samples=1000, num_trials=500):
    d_out = dict()

    for _ in range(num_trials):
        
        d = binary_sampling_vary_p(n_bits, p, num_samples)

        for k, v in d.items():
            if k not in d_out:
                d_out[k] = []
            d_out[k].append(v)

    for k, v in d_out.items():
        d_out[k] = sum(v) / len(v)
    
    return d_out

d = binary_sampling_clt_vary_p(8, 0.25, 1000)

for k, v in sorted(d.items()):
    print(f'{k}: {v}')