from wordfreq import zipf_frequency
from gensim.models import KeyedVectors
import random
from sklearn.manifold import TSNE
from sklearn.decomposition import PCA
import numpy as np

if __name__ == "__main__":
    wv = KeyedVectors.load("w2v_2.1.kv")
    vectors = wv[wv.key_to_index]
    # a list containing the keys or words for each word in the dictionary
    print(len(wv.key_to_index), random.choice(wv.index_to_key))
    pca = PCA(n_components=50)
    pcaVectors = pca.fit_transform(vectors)
    tsne = TSNE(n_components=3, 
    perplexity=49,
    early_exaggeration=12,
    learning_rate=200,
    n_iter=1000,
    n_iter_without_progress=300,
    min_grad_norm=1e-7,
    metric='euclidean',
    init='pca',
    random_state=18,
    method='barnes_hut',
    angle=0.5)

    tsneVectors = tsne.fit_transform(pcaVectors)
    np.savetxt('3D_px49_w2v_2.1_tsne.txt', tsneVectors, fmt='%f')
    