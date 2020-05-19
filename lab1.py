import redis


def create_queue(name: str):
    conn.rpush(name=name)


def push_queue(name: str, values: list):
    conn.rpush(name, *values)


def read_one_from_queue(name: str):
    return conn.lpop(name)


def read_all_from_queue(name: str):
    while conn.llen(name) != 0:
        print(conn.lpop(name))


def empty_queue():
    conn.flushdb("imiona")


conn = redis.StrictRedis(host="127.0.0.1", port="6381", decode_responses=True)

push_queue("imiona", ["bob"])
push_queue("imiona", ["jacek", "placek"])
read_all_from_queue("imiona")
# print(read_one_from_queue("imiona"))
# print(read_one_from_queue("imiona"))
# print(read_one_from_queue("imiona"))
