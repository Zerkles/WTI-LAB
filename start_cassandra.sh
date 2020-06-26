docker run --name main_cass -p 9042:9042 --rm cassandra:3

#DESCRIBE CLUSTER;
#CREATE KEYSPACE IF NOT EXISTS ratings_keyspace WITH replication = {'class': 'SimpleStrategy', 'replication_factor': 1};
#CREATE TABLE IF NOT EXISTS ratings_keyspace.user_profile(user_id int, avg_ratings_for_genre_horror float, avg_ratings_for_genre_war float, avg_ratings_for_genre_comedy float, PRIMARY KEY(user_id));
#SELECT table_name FROM system_schema.tables;
#DROP TABLE ratings_keyspace.user_profile;