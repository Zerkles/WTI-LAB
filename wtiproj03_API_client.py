import threading
import time

import requests

post_payload = {"userID": 75.0, "movieID": 3.0, "rating": 1.0, "Action": 0.0, "Adventure": 1.0, "Animation": 0.0,
                "Children": 0.0, "Comedy": 0.0, "Crime": 1.0, "Documentary": 0.0, "Drama": 0.0, "Fantasy": 0.0,
                "Film-Noir": 0.0, "Horror": 0.0, "IMAX": 0.0, "Musical": 0.0, "Mystery": 0.0, "Romance": 0.0,
                "Sci-Fi": 0.0, "Short": 0.0, "Thriller": 0.0, "War": 0.0, "Western": 0.0}
server_address = 'http://localhost:5000'


def multithreaded_run_sequence():
    clients = []

    for i in range(100):
        t = threading.Thread(target=run_sequence)
        clients.append(t)
        t.start()

    for c in clients:
        c.join()


def run_sequence():
    post_rating()
    time.sleep(0.01)
    get_ratings()
    time.sleep(0.01)
    delete_ratings()
    time.sleep(0.01)
    get_ratings()
    time.sleep(0.01)
    get_afg_genre_all_users()
    time.sleep(0.01)
    get_afg_genre_one_user()
    time.sleep(0.01)


def post_rating():
    request_result = requests.post(url=server_address + '/rating', json=post_payload)
    print_request_info(request_result)


def get_ratings():
    request_result = requests.get(url=server_address + '/ratings')
    print_request_info(request_result)


def delete_ratings():
    request_result = requests.delete(url=server_address + '/ratings', json=post_payload)
    print_request_info(request_result)


def get_afg_genre_all_users():
    request_result = requests.get(url=server_address + '/avg-genre-ratings/all-users')
    print_request_info(request_result)


def get_afg_genre_one_user():
    request_result = requests.get(url=server_address + '/avg-genre-ratings/25')
    print_request_info(request_result)


def print_request_info(request: requests):
    print("------------------------------------")
    print("request.url " + request.url)
    print("request.status_code " + str(request.status_code))
    print("request.headers " + str(request.headers))
    print("request.text " + request.text)
    print("request.request.body " + str(request.request.body))
    print("request.request.headers " + str(request.request.headers))
    print("------------------")


if __name__ == '__main__':
    run_sequence()
