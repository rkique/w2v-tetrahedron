import numpy as np
from wordfreq import zipf_frequency
from gensim.models import KeyedVectors

#change this from 1 to 430 to search different coordinate ranges for tetrahedron-like structures.
START_INDEX = 1

#Keep these large
MAX_DIST_DIFFERENCE = 50
MAX_CD_DIFFERENCE = 50

#Keep this small
OKAY_DIST_DIFFERENCE = 1

# find 4 equidistant points from the embedding
coords = np.loadtxt("3D_px49_w2v_2.1_tsne.txt")
print(np.shape(coords))
#wv = KeyedVectors.load("w2v_2.1.kv")
#vocab = wv.index_to_key

def txt_to_list(path):
    txt_file = open(path, 'r', encoding="utf-8")
    txt = txt_file.readlines()
    txt = [x.strip() for x in txt]
    return txt

vocab = txt_to_list("vocab.txt")

def distance(a, b):
    return np.sqrt(((a - b)**2).sum(-1))

def validate_distances(a,b,c,d, MAX_DIST_DIFFERENCE):
    if a > 10 or b > 10 or c > 10 or d > 10:
        return MAX_DIST_DIFFERENCE
    distance_diffs = np.abs([a-b, b-c, c-d, d-a, b-d, a-c])
    diff = max(distance_diffs)
    if diff < MAX_DIST_DIFFERENCE:
        print(f'distance of {a}')
        return diff
    return MAX_DIST_DIFFERENCE

def validate_crossdistances(a,b,c,d, MAX_CD_DIFFERENCE):
    crossdistances = np.abs(np.array([distance(a,b), distance(b,c), distance(c,d), distance(d,a), distance(b,d), distance(a,c)])).astype('float16')
    cb = np.array(list((combinations(crossdistances, 2))))
    #print(cb)
    diff = max(np.abs(cb[:,1]-cb[:,0]))
    if diff < MAX_CD_DIFFERENCE:
        #print(np.where(coords == a))
        aword = vocab[np.where(coords == a)[0][0]]
        bword = vocab[np.where(coords == b)[0][0]]
        cword = vocab[np.where(coords == c)[0][0]]
        dword = vocab[np.where(coords == d)[0][0]]
        print(f'best cd_diff found of {diff} at {aword} {bword} {cword} {dword}')
        return diff
    return MAX_CD_DIFFERENCE
        
print(distance(coords[0], coords[1]))

from itertools import combinations
# now find four points as close as possible, that are the same distance from one another

#coords = np.sort(coords)
#distances = np.sort(distances)
coord = np.array([0,0,0])
distances = np.array([distance(coord,c) for c in coords])


def find_tetrahedron(k, MAX_CD_DIFFERENCE):
    idxs = tuple(combinations(range(k,k+100), 4))
    for idx in idxs:
        r = coords[idx[0]]
        s = coords[idx[1]]
        t = coords[idx[2]]
        u = coords[idx[3]]
        #MAX_DIST_DIFFERENCE = validate_distances(a,b,c,d, MAX_DIST_DIFFERENCE)
        #if MAX_DIST_DIFFERENCE < 1:
            #print(f"dist_validated: {a:.3f} {b:.3f} {c:.3f} {d:.3f}")
            #print(f'{r} {s} {t} {u}')
        MAX_CD_DIFFERENCE = validate_crossdistances(r,s,t,u, MAX_CD_DIFFERENCE)

#An optimized version that first validates the distance from the centroid before calculating all six cross distances.

def find_tetrahedron_fast(k, MAX_DIST_DIFFERENCE,MAX_CD_DIFFERENCE):
    idxs = tuple(combinations(range(k,k+100), 4))
    for idx in idxs:
        a,b,c,d = [distances[axis] for axis in idx]
        r,s,t,u = [coords[axis] for axis in idx]
        MAX_DIST_DIFFERENCE = validate_distances(a,b,c,d, MAX_DIST_DIFFERENCE)
        if MAX_DIST_DIFFERENCE < OKAY_DIST_DIFFERENCE:
            #print(f"dist_validated: {a:.3f} {b:.3f} {c:.3f} {d:.3f}")
            MAX_CD_DIFFERENCE = validate_crossdistances(r,s,t,u, MAX_CD_DIFFERENCE)

for i in range(START_INDEX, 430):
    find_tetrahedron_fast(i*100, MAX_DIST_DIFFERENCE, MAX_CD_DIFFERENCE)


