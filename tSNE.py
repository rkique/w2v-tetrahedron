from gensim.models import KeyedVectors
import numpy as np

from sklearn.decomposition import PCA
from sklearn.manifold import TSNE


wv = KeyedVectors.load('glove_2.1.kv')
print(wv.most_similar("kindling",topn=20))
print([q[0] for q in wv.most_similar("kindling", topn=20)])

print(wv.n_similarity(["kindling"]*20, [q[0] for q in wv.most_similar("kindling", topn=20)]))

#print(wv.similarity("kindling", ""))


# #gets v with len 200
# print(len(wv.key_to_index))
# print(wv.index_to_key[0])
# vectors = wv[wv.key_to_index]
# print(vectors[0])

# pca = PCA(n_components=50)
# pcaVectors = pca.fit_transform(vectors)

# tsne = TSNE(n_components=2, 
# perplexity=49,
# early_exaggeration=12,
# learning_rate=200,
# n_iter=1000,
# n_iter_without_progress=300,
# min_grad_norm=1e-7,
# metric='euclidean',
# init='pca',
# random_state=18,
# method='barnes_hut',
# angle=0.5)

# tsneVectors = tsne.fit_transform(pcaVectors)
# np.savetxt('px49_glove_2.1_tsne.txt', tsneVectors, fmt='%f')


