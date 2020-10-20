import pickle
from recommender.utils.dataprocess import getPopularMovies, getFullMovies, getRecommendedMovies, searchForMovies

from flask import Blueprint

recommender_api = Blueprint('recommender_api', __name__)

mfModel = pickle.load(open('recommender/pkl/mfModel.pkl', "rb"))
knnModel = pickle.load(open('recommender/pkl/knnModel.pkl', "rb"))


@recommender_api.route('/api/fullMovies')
def getFullMovieList():
    return getFullMovies()


@recommender_api.route('/api/popularMovies')
def getPopularMoviesList():
    return getPopularMovies()


@recommender_api.route('/api/recommendedMovies/<movieIndex>')
def getRecommendedMoviesList(movieIndex):
    movieFeatures = mfModel.Q
    selectedMovieFeature = movieFeatures[int(movieIndex), :]
    dist, indices = knnModel.kneighbors([selectedMovieFeature], 20)
    movies = getRecommendedMovies(dist, indices)
    return movies


@recommender_api.route('/api/search/<param>')
def getMoviesByTitle(param):
    selectedMovies = searchForMovies(param)
    return selectedMovies

