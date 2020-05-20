import pandas as pd

pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)


def get_prepared_df():
    ratedmovies_df = pd.read_table("hetrec2011-movielens-2k-v2/user_ratedmovies.dat",
                                   usecols=['userID', 'movieID', 'rating'])
    genres_df = pd.read_table("hetrec2011-movielens-2k-v2/movie_genres.dat")

    genres_df["dummyCol"] = 1
    genres_pivoted_df = genres_df.pivot(index='movieID', columns='genre', values='dummyCol')

    return ratedmovies_df.join(genres_pivoted_df).fillna(0)


if __name__ == "__main__":
    # exc1
    prepared_df = get_prepared_df()
    print(prepared_df)

    # exc2
    for row in prepared_df[0:10].iterrows():
        print(row[1].to_json())

    # exc3
    # Kod znajduje się w pliku lab3_server.py

    # exc4
    # Zamiast wykonywania testowania ręcznego przy uzyciu POSTmana, napisano testy jednostkowe spełniające tę samą
    # funkcjonalność, testy te znajdują się w tests/lab3_tests. Każdy punky końcowy aplikacji można przetestować osobno
    # oraz została również przyogotwana specjalna sekwencja pokazująca prawidłowe współdziałanie całego API.

    # exc 5 oraz 6
    # Kod znajduje się w pliku lab3_client.py

    # exc 7
    # Aby uruchomić wielowątkowego klienta należy użyć funkcji multithreaded_run_sequence() z pliku lab3_client.py
    # Aby uruchomić flaskowy serwer w wielowątkowym cherrypy należy w sekcji main pliku lab3_server.py zakomentować
    # linię app.run() a odkomentować linię cherrypy.engine.start()
