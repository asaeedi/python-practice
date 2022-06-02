#%%

# First solution: in-place shuffling
import numpy as np
months = np.arange(1, 13)
print('Original months are: ', months)

np.random.shuffle(months)
print('Shuffled months are: ', months)

#%%
# Second solution: not in-place shuffling
import random as rnd
months = list(range(1, 13))
print('Original months are: ', months)

shuffled_months = rnd.sample(months, len(months))
print('Shuffled months are: ', shuffled_months)

