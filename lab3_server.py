import random

import cherrypy
import pandas as pd
from flask import Flask, request, json

import lab3

app = Flask(__name__)

df = lab3.get_prepared_df()[0:0]


@app.route('/rating', methods=['POST'])
def rating_route():
    request_dict = dict(json.loads(request.get_data()))
    series = pd.Series(request_dict)

    print(request_dict)

    global df
    df = df.append(series, ignore_index=True)

    return "OK"


@app.route('/ratings', methods=['GET'])
def get_ratings_route():
    global df
    return df.to_json()


@app.route('/ratings', methods=['DELETE'])
def delete_ratings_route():

    global df
    df = df[0:0]
    return "OK"


@app.route('/avg-genre-ratings/all-users', methods=['GET'])
def avg_for_all_route():
    global df

    dict_keys = df.keys().copy().drop(labels=['userID', 'movieID', 'rating'])
    genre_averages_dict = dict.fromkeys(dict_keys, random.random())

    return json.dumps(genre_averages_dict)


@app.route('/avg-genre-ratings/<userID>', methods=['GET'])
def avg_per_user_route(userID):
    global df

    dict_keys = df.keys().copy().drop(labels=['userID', 'movieID', 'rating'])
    genre_averages_dict = dict.fromkeys(dict_keys, random.random())
    genre_averages_dict.update({"userID": userID})

    return json.dumps(genre_averages_dict)


cherrypy.tree.graft(app.wsgi_app, '/')
cherrypy.config.update({'server.socket_host': '0.0.0.0',
                        'server.socket_port': 5000,
                        'engine.autoreload.on': False,
                        })

if __name__ == '__main__':
    app.run()  # flask app
    #cherrypy.engine.start()  # cherrypy app
