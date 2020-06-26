import pandas as pd

import wtiproj05_redis_client as redis_client
from wtiproj04_ETL_and_data_processing import calculate_mean_rating_for_genres, calculate_mean_rating_for_user, \
    calculate_user_profile_ratings

df: pd.DataFrame = pd.DataFrame()
user_ratedmovies_data = pd.read_table("resources/user_ratedmovies.dat")
movie_genres_data = pd.read_table('resources/movie_genres.dat')

keys = ['genre-Action', 'genre-Adventure', 'genre-Animation', 'genre-Children',
        'genre-Comedy', 'genre-Crime', 'genre-Documentary', 'genre-Drama',
        'genre-Fantasy', 'genre-Film-Noir', 'genre-Horror', 'genre-IMAX',
        'genre-Musical', 'genre-Mystery', 'genre-Romance', 'genre-Sci-Fi',
        'genre-Short', 'genre-Thriller', 'genre-War', 'genre-Western']


def insert_rating(data: dict):
    series = pd.Series(data)

    global df
    df = df.append(series, ignore_index=True)
    redis_client.set_movie(data)


def get_ratings():
    # return df
    return redis_client.get_movies()


def delete_ratings():
    # global df
    # df = df[0:0]
    redis_client.clear()


def get_genre_avg_rating_all_users():
    global df, keys
    # global_means = calculate_mean_rating_for_genres(df, keys)
    data = get_ratings()
    return calculate_mean_rating_for_genres(data, keys)


def get_genre_avg_rating_for_user(user_id: float):
    global df, user_ratedmovies_data, movie_genres_data, keys

    # global_means = calculate_mean_rating_for_genres(df, keys)
    # user_means = calculate_mean_rating_for_user(float(user_id), df, keys)

    data = get_ratings()
    global_means = get_genre_avg_rating_all_users()
    user_means = calculate_mean_rating_for_user(float(user_id), data, keys)
    user_profile = calculate_user_profile_ratings(user_means, global_means)
    redis_client.set_user_profile(user_profile)

    return user_profile
