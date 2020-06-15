import json

import pandas as pd
import requests

server_address = 'http://localhost:5000'


pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)


def sort_by_column_name(table, column_name):
    table = table.sort_values(column_name)
    print(table)


def find_user_by_id(table, user_id):
    return table.loc[table['userID'] == user_id]


def find_movie_by_id(table, movie_id):
    return table.loc[table['movieID'] == movie_id]


def test_data(table, userID, movieID):
    table = find_movie_by_id(table, movieID)
    return find_user_by_id(table, userID)


def create_table(user_id, movie_id):
    column_names = ["userID", "movieID", "rating", "genre-Action", "genre-Adventure", "genre-Animation",
                    "genre-Children", "genre-Comedy", "genre-Crime", "genre-Documentary", "genre-Drama",
                    "genre-Fantasy", "genre-Film-Noir", "genre-Horror", "genre-IMAX", "genre-Musical",
                    "genre-Mystery", "genre-Romance", "genre-Sci-Fi", "genre-Short", "genre-Thriller", "genre-War",
                    "genre-Western"]



def exercise_01():
    user_ratedmovies_data = pd.read_table('resources/user_ratedmovies.dat')
    movie_genres_data = pd.read_table('resources/movie_genres.dat')

    user_ratedmovies_data = user_ratedmovies_data[['userID', 'movieID', 'rating']]

    movie_genres_data["dummy"] = 1
    movie_genres_pivoted = pd.pivot_table(movie_genres_data, index='movieID', columns='genre', values='dummy')
    movie_genres_pivoted = movie_genres_pivoted.fillna('{:d}'.format(0))

    result = pd.DataFrame.merge(user_ratedmovies_data, movie_genres_pivoted,
                                on='movieID',
                                how='inner')

    result.rename(columns={'Action': 'genre-Action', 'Adventure': "genre-Adventure", 'Animation': "genre-Animation",
                           'Children': "genre-Children", 'Comedy': "genre-Comedy", 'Crime': "genre-Crime",
                           'Documentary': "genre-Documentary", 'Drama': "genre-Drama", 'Fantasy': "genre-Fantasy",
                           'Film-Noir': "genre-Film-Noir",
                           'Horror': "genre-Horror", 'IMAX': "genre-IMAX", 'Musical': "genre-Musical",
                           'Mystery': "genre-Mystery", "Romance": "genre-Romance", "Sci-Fi": "genre-Sci-Fi",
                           "Short": "genre-Short", "Thriller": "genre-Thriller", "War": "genre-War",
                           "Western": "genre-Western"}, inplace=True)

    return result


def exercise_02(data):
    #data = test_data(data, 78, 903)
    for index, row in data.iterrows():
        print(row.to_json())

def print_request_info(request: requests):
    print("------------------------------------")
    print("request.url " + request.url)
    print("request.status_code " + str(request.status_code))
    print("request.headers " + str(request.headers))
    print("request.text " + request.text)
    print("request.request.body " + str(request.request.body))
    print("request.request.headers " + str(request.request.headers))
    print("------------------")

j = {"userID": 75.0, "movieID": 3.0, "rating": 1.0, "genre-Action": 0.0, "genre-Adventure": 1.0, "genre-Animation": 0.0,
                "genre-Children": 0.0, "genre-Comedy": 0.0, "genre-Crime": 1.0, "genre-Documentary": 0.0, "genre-Drama": 0.0, "genre-Fantasy": 0.0,
                "genre-Film-Noir": 0.0, "genre-Horror": 0.0, "genre-IMAX": 0.0, "genre-Musical": 0.0, "genre-Mystery": 0.0, "genre-Romance": 0.0,
                "genre-Sci-Fi": 0.0, "genre-Short": 0.0, "genre-Thriller": 0.0, "genre-War": 0.0, "genre-Western": 0.0}

def main():
    #exercise 1
    #result = exercise_01()

    #print(result)

    #exercise 2
    #exercise_02(result)

    get_request = requests.get(url=server_address + '/ratings')
    print(get_request.text)

    request_result = requests.post(url=server_address + '/rating', json=j)
    print(request_result.text)

    '''get_request = requests.get(url=server_address + '/ratings')
    print(get_request.text)

    j = '{"userID": 75}'
    delete_request = requests.delete(url=server_address + '/ratings', json=json.loads(j))
    print(delete_request.text)'''

    get_request = requests.get(url=server_address + '/ratings')
    print(get_request.text)


if __name__ == '__main__':
    main()
