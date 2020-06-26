import wtiproj05_API_logic
import wtiproj06_simple_cassandra_client as cass_client
from wtiproj04_ETL_and_data_processing import calculate_mean_rating_for_genres, calculate_mean_rating_for_user, \
    calculate_user_profile_ratings

keys = wtiproj05_API_logic.keys


def prepare_keys():
    global keys
    k2 = []

    for k in keys:
        k2.append(k.lower().replace('-', '_'))
    k2.append('userID')
    keys = k2


def insert_rating(data: dict):
    cass_client.push_data_dict_table(cass_client.session, cass_client.keyspace, cass_client.table_movies, data)


def get_ratings():
    data=cass_client.get_data_table(cass_client.session, cass_client.keyspace, cass_client.table_movies)
    #print(data)
    return data


def delete_ratings():
    cass_client.clear_table(cass_client.session, cass_client.keyspace, cass_client.table_movies)


def get_genre_avg_rating_all_users():
    global keys

    data = get_ratings()
    data.rename(columns={'userid': 'userID'}, inplace=True)

    global_means = calculate_mean_rating_for_genres(data, keys)
    return global_means


def get_genre_avg_rating_for_user(user_id: float):
    global keys

    data = get_ratings()
    data.rename(columns={'userid': 'userID'}, inplace=True)

    global_means = get_genre_avg_rating_all_users()
    user_means = calculate_mean_rating_for_user(float(user_id), data, keys)
    user_profile = calculate_user_profile_ratings(user_means, global_means)

    cass_client.push_data_dict_table(cass_client.session, cass_client.keyspace, cass_client.table_profiles,
                                     user_profile)

    return user_profile
