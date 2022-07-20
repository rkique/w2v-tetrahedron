from wordfreq import zipf_frequency
from gensim.models import KeyedVectors
import random
from sklearn.manifold import TSNE
from sklearn.decomposition import PCA
import numpy as np

def fmt(coord):
    return f"({coord[0]},{coord[1]},{coord[2]})"


if __name__ == "__main__":
    wv = KeyedVectors.load("w2v_2.1.kv")
    vocab = wv.index_to_key
    f = open("vocab.txt", "w+", encoding='utf-8')
    for word in vocab:
        f.write(word)
        f.write("\n")
    f.close()

    #print(vocab[2], vocab[10], vocab[18], vocab[22])
    #print(vocab[10], vocab[83], vocab[93], vocab[98])
    coords = np.loadtxt("3D_px49_w2v_2.1_tsne.txt")
    print(fmt(coords[wv.key_to_index["bank"]]))
    print(fmt(coords[wv.key_to_index["bailout"]]))
    print(fmt(coords[wv.key_to_index["financial"]]))
    print(fmt(coords[wv.key_to_index["money"]]))
    print(fmt(coords[wv.key_to_index["river"]]))
    print(fmt(coords[wv.key_to_index["land"]]))
    print(fmt(coords[wv.key_to_index["water"]]))
    print(fmt(coords[wv.key_to_index["embankment"]]))

