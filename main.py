import numpy as np
import pandas as pd

moviemeta = pd.read_csv('movies_metadata.csv', low_memory=False)


# calculating mean vote
meanvote = moviemeta['vote_average'].mean()


# calculating cutoff value
minimumvote = moviemeta['vote_count'].quantile(0.90)
# print(minimumvote)


q_movies = moviemeta.copy().loc[moviemeta['vote_count'] >= minimumvote]
q_movies.shape


def weighted_rating(x, minimumvote = minimumvote, meanvote = meanvote ):
  voters = x['vote_count']
  avg_vote = x['vote_average']
  # calculations based on IMDB formula
  return (voters/(voters+minimumvote) * avg_vote) + (minimumvote/(voters+minimumvote) * meanvote)

# caluclating the scores using above formula
q_movies['score'] = q_movies.apply(weighted_rating, axis=1)

# sorting the dataframe in descending order 

q_movies = q_movies.sort_values('score', ascending= False)

pd.set_option('precision', 2)
print(q_movies[['title', 'vote_count', 'vote_average', 'score']].head(20))