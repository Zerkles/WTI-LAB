import json

import pandas as pd
import redis

conn = redis.StrictRedis(host="127.0.0.1", port="6381", decode_responses=True)


def set_user_profile(profile: dict):
    conn.sadd("user_profiles", json.dumps(profile))


def set_movie(movie: dict):
    conn.sadd("movies", json.dumps(movie))


def get_user_profiles():
    df = pd.DataFrame()
    for m in list(conn.smembers("user_profiles")):
        df = df.append(json.loads(m), ignore_index=True)
    return df


def get_movies():
    df = pd.DataFrame()
    for m in list(conn.smembers("movies")):
        df = df.append(json.loads(m), ignore_index=True)
    return df


def clear():
    conn.flushall()


if __name__ == "__main__":
    get_user_profiles()
