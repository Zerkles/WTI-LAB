import json
import unittest

import requests

post_payload = {"userID": 75.0, "movieID": 4.0, "rating": 2.3, "genre-Action": 0.0, "genre-Adventure": 1.0, "genre-Animation": 0.0,
                "genre-Children": 0.0, "genre-Comedy": 0.0, "genre-Crime": 1.0, "genre-Documentary": 1.0, "genre-Drama": 0.0, "genre-Fantasy": 0.0,
                "genre-Film-Noir": 0.0, "genre-Horror": 0.0, "genre-IMAX": 0.0, "genre-Musical": 0.0, "genre-Mystery": 0.0, "genre-Romance": 0.0,
                "genre-Sci-Fi": 0.0, "genre-Short": 0.0, "genre-Thriller": 0.0, "genre-War": 0.0, "genre-Western": 0.0}
server_address = 'http://localhost:5000'


class TestLab3_5(unittest.TestCase):

    def test_sequence(self):
        self.test_post_rating()
        self.test_get_ratings()
        self.test_get_avg_genre_all_users()
        self.test_get_avg_genre_one_user()
        self.test_delete_ratings()

    def test_post_rating(self):
        route = '/rating'
        print(route)
        request_result = requests.post(url=server_address + route, json=post_payload)
        assert request_result.status_code == 201
        print(request_result.content)

    def test_get_ratings(self):
        route = '/ratings'
        print(route)
        request_result = requests.get(url=server_address + route)
        assert request_result.status_code == 200
        print(json.loads(request_result.content))

    def test_delete_ratings(self):
        route = '/ratings'
        print(route)
        request_result = requests.delete(url=server_address + route, json=post_payload)
        assert request_result.status_code == 200
        print(request_result.content)

    def test_get_avg_genre_all_users(self):
        route = '/avg-genre-ratings/all-users'
        print(route)
        request_result = requests.get(url=server_address + route)
        assert request_result.status_code == 200
        print(json.loads(request_result.content))

    def test_get_avg_genre_one_user(self):
        route = '/avg-genre-ratings/75'
        print(route)
        request_result = requests.get(url=server_address + route)
        assert request_result.status_code == 200
        print(json.loads(request_result.content))


if __name__ == '__main__':
    unittest.main()
