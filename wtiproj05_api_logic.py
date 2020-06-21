
import pandas as pd

from wtiproj04_ETL_and_data_processing import calculate_mean_rating_for_genres, calculate_mean_rating_for_user


df: pd.DataFrame = pd.DataFrame()
user_ratedmovies_data = pd.read_table("resources/user_ratedmovies.dat")
movie_genres_data = pd.read_table('resources/movie_genres.dat')


def insert_rating(data: dict):
    series = pd.Series(data)

    global df
    df = df.append(series, ignore_index=True)
    print(df.loc[df['userID'] == 75])


def get_ratings():
    return df.to_json()


def delete_ratings():
    global df
    df = df[0:0]


def get_genre_avg_rating_all_users():
    global df
    keys = [x for x in df.keys().tolist() if x not in ['userID', 'movieID', 'rating']]
    genre_averages_dict = calculate_mean_rating_for_genres(df, keys)
    return genre_averages_dict


def get_genre_avg_rating_for_user(user_id: float):
    global df, user_ratedmovies_data, movie_genres_data

    keys = [x for x in df.keys().tolist() if x not in ['userID', 'movieID', 'rating']]
    genre_averages_dict = calculate_mean_rating_for_user(float(user_id), df, keys)

    # TODO: dobrze zwraca czy powinien wykonać jeszcze jeden krok i zwrócić profil ?
    return genre_averages_dict
