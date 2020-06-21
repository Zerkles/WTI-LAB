import json
import threading
import time
import pandas
import redis

conn = redis.StrictRedis(host="127.0.0.1", port="6381")


def empty_queue(queue_name: str):
    conn.flushdb(queue_name)


def producer(queue_name: str, rows_count: int):
    df = pandas.read_table("hetrec2011-movielens-2k-v2/user_ratedmovies.dat")

    for row in df[0:rows_count].iterrows():
        # print(row[1].to_json())
        conn.rpush(queue_name, row[1].to_json())
        time.sleep(0.01)


def consumer(queue_name: str):
    stop = time.time() + 10

    while time.time() < stop:
        read_all_messages(queue_name)
        time.sleep(0.25)


def read_all_messages(queue_name: str):
    while conn.llen(queue_name) > 0:
        print(json.loads(conn.lpop(queue_name)))
    print("\n")


if __name__ == "__main__":
    name = "user_ratedmovies"
    rows_to_be_sent_count = 200

    empty_queue(name)

    producer_thread1 = threading.Thread(target=producer, args=(name, rows_to_be_sent_count,))
    producer_thread2 = threading.Thread(target=producer, args=(name, rows_to_be_sent_count,))
    producer_thread3 = threading.Thread(target=producer, args=(name, rows_to_be_sent_count,))
    consumer_thread = threading.Thread(target=consumer, args=(name,))

    producer_thread1.start()
    producer_thread2.start()
    producer_thread3.start()

    consumer_thread.start()

    producer_thread1.join()
    producer_thread2.join()
    producer_thread3.join()
    consumer_thread.join()

# Komentarz do podpunktu 6
#    Konsument w "poszególnej sekwencji odczytuje tym więcej wiadaomości im krótsza jest częstotliwość ich wysyłania
#    przez producenta ponieważ więcej tych wiadomości maszansę dotrzeć do redisa pomiędzy kolejnymi odczytaniami bazy danych"
# Komentarz do podpunktu 7
#   Aplikacja konsumencka będzie odbierała różne ilości i często powtarzające się dane.
# Komentarz do podpunktu 8
#   Aplikacje konsumenckie będą odbierały niewiele lub nawet wcale wiadomości ponieważ te zostały już zkonsumowane przez
#   inne instancje konsumenta.
