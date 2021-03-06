
from random import randint
from time import clock
import numpy as np
import cos_sim_sk

"""
For using sklearn's method directly, use the following code (with the same
np arrays as below):

from sklearn.metrics.pairwise import cosine_similarity
(...)
similarity = cosine_similarity(V)[0][-1]
"""

size = 50000
print('Generating 2 vectors of size {}. Similarity should be: -1.0'.format(size))
A = np.array([-10 for x in range(size)])
B = np.array([10 for x in range(size)])
O = np.array([0 for x in range(size)])

repeat = 50
print('Calculating Cosine Similarity. Repeating {}x.'.format(repeat))
avg_runtime = 0
similarity = None
for i in range(repeat):
    start = clock()
    similarity = cos_sim_sk.get_cosine_similarity(A,B,O)
    end = clock()
    avg_runtime += (end-start)
avg_runtime = round(avg_runtime / repeat, 4)
print('Done. Average runtime: {} s. Similarity: {}.'.format(avg_runtime,similarity))
