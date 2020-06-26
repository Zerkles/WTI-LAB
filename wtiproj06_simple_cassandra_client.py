import re

import pandas as pd
from cassandra.cluster import Cluster
from cassandra.query import dict_factory

session = None
keyspace = "user_ratings"
table_movies = "movie_genres"
table_profiles = "user_profile"


def create_keyspace(session, keyspace):
    session.execute("""
    CREATE KEYSPACE IF NOT EXISTS """ + keyspace + """
    WITH replication = { 'class': 'SimpleStrategy', 'replication_factor': '1' }
    """)


def create_table(session, keyspace, table_name, for_movies: bool):
    session.execute(f"CREATE TABLE IF NOT EXISTS {keyspace}.{table_name} ({get_col_type_list(for_movies)})")


def push_data_table(session, keyspace, table, userId, avgMovieRating):
    session.execute("""INSERT INTO """ + keyspace + """.""" + table + """ (user_id, avg_movie_rating)
        VALUES (%(user_id)s, %(avg_movie_rating)s)""",
                    {
                        'user_id': userId,
                        'avg_movie_rating': avgMovieRating
                    }
                    )


def push_data_dict_table(session, keyspace, table_name, data: dict):
    query = re.sub("[][']", '',
                   f"INSERT INTO {keyspace}.{table_name} ({list(data.keys())}) VALUES ({list(data.values())})".replace(
                       '-', '_'))
    session.execute(query)


def get_data_table(session, keyspace, table):
    rows = session.execute("SELECT * FROM " + keyspace + "." + table + ";")
    df = pd.DataFrame(columns=rows.column_names)

    for row in rows:
        df = df.append(row, ignore_index=True)
    return df


def clear_table(session, keyspace, table):
    session.execute("TRUNCATE " + keyspace + "." + table + ";")


def delete_table(session, keyspace, table):
    session.execute("DROP TABLE " + keyspace + "." + table + ";")


def get_col_type_list(for_movies: bool):
    if for_movies:
        return "genre-Action float, genre-Adventure float, genre-Animation float, genre-Children float, " \
               "genre-Comedy float, genre-Crime float, genre-Documentary float, genre-Drama float, " \
               "genre-Fantasy float, genre-Film-Noir float, genre-Horror float, genre-IMAX float, " \
               "genre-Musical float, genre-Mystery float, genre-Romance float, genre-Sci-Fi float, " \
               "genre-Short float, genre-Thriller float, genre-War float, userID float, movieID float, " \
               "genre_Western float, rating float,PRIMARY KEY(userID)".replace('-', '_')

    else:
        return "genre-Action float, genre-Adventure float, genre-Animation float, genre-Children float, " \
               "genre-Comedy float, genre-Crime float, genre-Documentary float, genre-Drama float, " \
               "genre-Fantasy float, genre-Film-Noir float, genre-Horror float, genre-IMAX float, " \
               "genre-Musical float, genre-Mystery float, genre-Romance float, genre-Sci-Fi float, " \
               "genre-Short float, genre-Thriller float, genre-War float, userID float, " \
               "genre_Western float, PRIMARY KEY(userID)".replace('-', '_')


def prepare_db():
    global keyspace, cluster, session
    # utworzenia połączenia z klastrem
    cluster = Cluster(['127.0.0.1'], port=9042)
    session = cluster.connect()
    # utworzenie nowego keyspace
    create_keyspace(session, keyspace)
    # ustawienie używanego keyspace w sesji
    session.set_keyspace(keyspace)
    # użycie dict_factory pozwala na zwracanie słowników
    # znanych z języka Python przy zapytaniach do bazy danych
    session.row_factory = dict_factory
    # tworzenie tabeli
    create_table(session, keyspace, table_movies, True)
    create_table(session, keyspace, table_profiles, False)


if __name__ == "__main__":
    keyspace = "user_ratings"
    table = "user_avg_rating"
    # utworzenia połączenia z klastrem
    cluster = Cluster(['127.0.0.1'], port=9042)
    session = cluster.connect()
    # utworzenie nowego keyspace
    create_keyspace(session, keyspace)
    # ustawienie używanego keyspace w sesji
    session.set_keyspace(keyspace)
    # użycie dict_factory pozwala na zwracanie słowników
    # znanych z języka Python przy zapytaniach do bazy danych
    session.row_factory = dict_factory
    # tworzenie tabeli
    col_type = {'user_id': 'int', 'avg_movie_rating': 'float'}
    create_table(session, keyspace, table, False)
    # umieszczanie danych w tabeli
    push_data_table(session, keyspace, table, userId=1337, avgMovieRating=4.2)
    # pobieranie zawartości tabeli i wyświetlanie danych
    get_data_table(session, keyspace, table)
    # czyszczenie zawartości tabeli
    clear_table(session, keyspace, table)
    get_data_table(session, keyspace, table)
    # usuwanie tabeli
    delete_table(session, keyspace, table)
