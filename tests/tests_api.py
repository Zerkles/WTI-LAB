import json
import unittest

import requests

post_payload = {"userID": 78.0, "movieID": 7.0, "rating": 2.8, "Action": 0.0, "Adventure": 1.0,
                "Animation": 0.0,
                "Children": 0.0, "Comedy": 0.0, "Crime": 0.0, "Documentary": 1.0,
                "Drama": 0.0, "Fantasy": 0.0,
                "Film-Noir": 0.0, "Horror": 0.0, "IMAX": 1.0, "Musical": 1.0,
                "Mystery": 0.0, "Romance": 0.0,
                "Sci-Fi": 0.0, "Short": 0.0, "Thriller": 0.0, "War": 0.0}


post_payload2 = {"userID": 78.0, "movieID": 7.0, "rating": 2.8, "genre-Action": 0.0, "genre-Adventure": 1.0,
                 "genre-Animation": 0.0,
                 "genre-Children": 0.0, "genre-Comedy": 0.0, "genre-Crime": 0.0, "genre-Documentary": 1.0,
                 "genre-Drama": 0.0, "genre-Fantasy": 0.0,
                 "genre-Film-Noir": 0.0, "genre-Horror": 0.0, "genre-IMAX": 1.0, "genre-Musical": 1.0,
                 "genre-Mystery": 0.0, "genre-Romance": 0.0,
                 "genre-Sci-Fi": 0.0, "genre-Short": 0.0, "genre-Thriller": 0.0, "genre-War": 0.0, "genre-Western": 0.0}
server_address = 'http://localhost:5000'


class TestAPI(unittest.TestCase):

    def test_sequence(self):
        self.test_post_rating()
        self.test_get_ratings()
        self.test_get_avg_genre_all_users()
        self.test_get_avg_genre_one_user()
        self.test_delete_ratings()

    def test_sequence_data_saving(self):
        self.test_get_ratings()
        self.test_post_rating()
        self.test_get_ratings()

    def test_post_rating(self):
        route = '/rating'
        print(route)
        request_result = requests.post(url=server_address + route, json=post_payload2)
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
        request_result = requests.delete(url=server_address + route, json=post_payload2)
        assert request_result.status_code == 200
        print(request_result.content)

    def test_get_avg_genre_all_users(self):
        route = '/avg-genre-ratings/all-users'
        print(route)
        request_result = requests.get(url=server_address + route)
        assert request_result.status_code == 200
        print(json.loads(request_result.content))

    def test_get_avg_genre_one_user(self):
        route = '/avg-genre-ratings/78'
        print(route)
        request_result = requests.get(url=server_address + route)
        assert request_result.status_code == 200
        print(json.loads(request_result.content))


if __name__ == '__main__':
    unittest.main()
