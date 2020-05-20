import json
import unittest

import requests

post_payload = {"userID": 75.0, "movieID": 3.0, "rating": 1.0, "Action": 0.0, "Adventure": 1.0, "Animation": 0.0,
                "Children": 0.0, "Comedy": 0.0, "Crime": 1.0, "Documentary": 0.0, "Drama": 0.0, "Fantasy": 0.0,
                "Film-Noir": 0.0, "Horror": 0.0, "IMAX": 0.0, "Musical": 0.0, "Mystery": 0.0, "Romance": 0.0,
                "Sci-Fi": 0.0, "Short": 0.0, "Thriller": 0.0, "War": 0.0, "Western": 0.0}
server_address = 'http://localhost:5000'


class TestLab3(unittest.TestCase):

    def test_exc3_sequence(self):
        self.test_exc3_post_rating()
        self.test_exc3_get_ratings()
        self.test_exc3_delete_ratings()
        self.test_exc3_get_ratings()
        self.test_exc3_get_afg_genre_all_users()
        self.test_exc3_get_afg_genre_one_user()

    def test_exc3_post_rating(self):
        request_result = requests.post(url=server_address + '/rating', json=post_payload)
        assert request_result.status_code == 200
        print(request_result.content)

    def test_exc3_get_ratings(self):
        request_result = requests.get(url=server_address + '/ratings')
        assert request_result.status_code == 200
        print(json.loads(request_result.content))

    def test_exc3_delete_ratings(self):
        request_result = requests.delete(url=server_address + '/ratings', json=post_payload)
        assert request_result.status_code == 200
        print(request_result.content)

    def test_exc3_get_afg_genre_all_users(self):
        request_result = requests.get(url=server_address + '/avg-genre-ratings/all-users')
        assert request_result.status_code == 200
        print(json.loads(request_result.content))

    def test_exc3_get_afg_genre_one_user(self):
        request_result = requests.get(url=server_address + '/avg-genre-ratings/25')
        assert request_result.status_code == 200
        print(json.loads(request_result.content))


if __name__ == '__main__':
    unittest.main()
