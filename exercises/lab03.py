import pandas as pd

def exercise_01():
    user_ratedmovies_data = pd.read_table('resources/user_ratedmovies.dat')
    movie_genres_data = pd.read_table('resources/movie_genres.dat')


    merge_inner = pd.merge(left=user_ratedmovies_data, right=movie_genres_data, left_on='movieID', right_on='movieID')

    print(merge_inner)


def main():
    exercise_01()


if __name__ == '__main__':
    main()