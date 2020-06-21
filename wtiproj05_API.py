from flask import Flask, json, request, Response

import wtiproj05_api_logic as api
from wtiproj04_ETL_and_data_processing import exercise_1

app = Flask(__name__)


@app.route('/rating', methods=['POST'])
def post_rating_route():
    request_dict = dict(json.loads(request.get_data()))
    api.insert_rating(request_dict)
    return Response(status=201)


@app.route('/ratings', methods=['GET'])
def get_ratings_route():
    return Response(response=api.get_ratings(), status=200, content_type='application/json')


@app.route('/ratings', methods=['DELETE'])
def delete_ratings_route():
    api.delete_ratings()
    return Response(status=200)


@app.route('/avg-genre-ratings/all-users', methods=['GET'])
def avg_for_all_route():
    return Response(response=json.dumps(api.get_genre_avg_rating_all_users()), status=200,
                    content_type='application/json')


@app.route('/avg-genre-ratings/<userID>', methods=['GET'])
def avg_per_user_route(userID):
    return Response(response=json.dumps(api.get_genre_avg_rating_for_user(userID)), status=200,
                    content_type='application/json')


if __name__ == '__main__':
    api.df = exercise_1(api.user_ratedmovies_data, api.movie_genres_data)[0]
    app.run()  # flask app
