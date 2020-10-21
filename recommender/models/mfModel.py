import pickle

from mf import MF
from recommender.utils.dataprocess import ratings, meanRatings

userCount = ratings['userId'].max()
movieCount = ratings['movieIndex'].max() + 1

mf = MF(movieCount, userCount, meanRatings, alpha=0.01, reg=0.01, iterations=20, K=20)
mf.train(ratings)

pickle.dump(mf, open('pkl/mfModel.pkl', 'wb'))
