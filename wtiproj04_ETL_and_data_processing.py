import pandas as pd

import wtiproj05_API_client


def exercise_1(user_ratedmovies_data: pd.DataFrame, movie_genres_data: pd.DataFrame):
    # initialize data of lists.
    user_ratedmovies_data = pd.read_table("resources/user_ratedmovies.dat")
    movie_genres_data = pd.read_table('resources/movie_genres.dat')

    user_ratedmovies_data = user_ratedmovies_data[['userID', 'movieID', 'rating']]
    user_ratedmovies_data.fillna(0).astype(int)

    movie_genres_data["dummy"] = 1
    movie_genres_pivoted = pd.pivot_table(movie_genres_data, index='movieID', columns='genre', values='dummy')
    movie_genres_pivoted = movie_genres_pivoted.fillna('{:d}'.format(0))

    result = pd.DataFrame.merge(user_ratedmovies_data, movie_genres_pivoted,
                                on='movieID',
                                how='inner')

    result.rename(columns={'Action': 'genre-Action', 'Adventure': "genre-Adventure", 'Animation': "genre-Animation",
                           'Children': "genre-Children", 'Comedy': "genre-Comedy", 'Crime': "genre-Crime",
                           'Documentary': "genre-Documentary", 'Drama': "genre-Drama", 'Fantasy': "genre-Fantasy",
                           'Film-Noir': "genre-Film-Noir", 'Horror': "genre-Horror", 'IMAX': "genre-IMAX",
                           'Musical': "genre-Musical", 'Mystery': "genre-Mystery", "Romance": "genre-Romance",
                           "Sci-Fi": "genre-Sci-Fi", "Short": "genre-Short", "Thriller": "genre-Thriller",
                           "War": "genre-War", "Western": "genre-Western"}, inplace=True)

    genres_list = result.columns[3:-1].values

    return result, genres_list


def dataframe_to_dictionary(data):
    return data.to_dict(orient='records')


def dictionary_to_dataframe(data):
    return pd.DataFrame.from_dict(data)


def check_if_conversion_is_correct(primary_df, secondary_df):
    df = pd.concat([primary_df, secondary_df])
    df_diff = df.drop_duplicates(keep=False)
    # print(df_diff)


def calculate_mean_rating_for_genres(user_genre, g):
    mean_genres = {}
    for genres in g:
        mean_genres[genres] = user_genre['rating'][user_genre[genres] == 1].mean()

    return mean_genres


def calculate_mean_rating_for_user(user_id, df, genres):
    mean_rating_for_user = {}
    for genre in genres:
        mean_rating_for_user[genre] = df[(df['userID'] == user_id) & (df[genre] == 1)]['rating'].mean()

    return mean_rating_for_user


def calculate_user_profile_ratings(user_ratings, mean_genres):
    user_profile_mean = {}
    for genres, mean in user_ratings.items():
        if mean > 0.0:
            user_profile_mean[genres] = mean_genres[genres] - mean
        else:
            user_profile_mean[genres] = 0.0

    return user_profile_mean


if __name__ == '__main__':
    user_ratedmovies_data = pd.read_table("resources/user_ratedmovies.dat")
    movie_genres_data = pd.read_table('resources/movie_genres.dat')

    # exercise 1
    result = exercise_1(user_ratedmovies_data, movie_genres_data)
    # exercise 2
    # result2 = dataframe_to_dictionary(result[0])
    # exercise 3
    # result3 = dictionary_to_dataframe(result2)
    # exercise 4
    # check_if_conversion_is_correct(result[0], result3)
    # exercise 5
    result4 = (calculate_mean_rating_for_genres(result[0], result[1]))
    # exercise 6
    result6 = calculate_mean_rating_for_user(75, result[0], result[1])
    print(result6)
    # exercise 7
    result7 = calculate_user_profile_ratings(result6, result4)
