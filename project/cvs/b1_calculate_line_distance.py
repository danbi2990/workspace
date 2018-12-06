from itertools import combinations
from math import sin, cos, sqrt, atan2, radians

import numpy as np


def get_distance_from_coords(lat1, lon1, lat2, lon2):
    # approximate radius of earth in km
    R = 6373.0

    lat1 = radians(lat1)
    lon1 = radians(lon1)
    lat2 = radians(lat2)
    lon2 = radians(lon2)
    dlon = lon2 - lon1
    dlat = lat2 - lat1

    a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))
    distance = R * c * 1000
    return distance


a1 = ('id1', 'hi', '123', '45')
a2 = ('id2', 'bye', '234', '56')
a3 = ('id3', 'cool', '321', '54')
lst = [a1, a2, a3]

res = tuple(combinations(lst, 2))
print(res)
network = []
for pair in res:
    network.


# import pandas as pd
# from db.mongo import MyMongo

# directory = '/Users/jake/OneDrive - leverage innovative users/Documents/편의점/'
# file = 'cvs_all.tsv'

# cvs = pd.read_csv(directory+file, sep='\t', dtype=object)
# print(len(cvs))















