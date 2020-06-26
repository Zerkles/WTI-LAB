import time

import wtiproj03_API_client as cli

if __name__ == '__main__':
    post_payload = {"userID": 75.0, "movieID": 7.0, "rating": 2.8, "genre-Action": 0.0, "genre-Adventure": 1.0,
                    "genre-Animation": 0.0,
                    "genre-Children": 0.0, "genre-Comedy": 0.0, "genre-Crime": 0.0, "genre-Documentary": 1.0,
                    "genre-Drama": 0.0, "genre-Fantasy": 0.0,
                    "genre-Film-Noir": 0.0, "genre-Horror": 0.0, "genre-IMAX": 1.0, "genre-Musical": 1.0,
                    "genre-Mystery": 0.0, "genre-Romance": 0.0,
                    "genre-Sci-Fi": 0.0, "genre-Short": 0.0, "genre-Thriller": 0.0, "genre-War": 0.0,
                    "genre-Western": 0.0}
    address_api = 'http://localhost:5000'
    address_api_server = 'http://localhost:9898'

    start = time.time()
    cli.run_sequence(address_api, post_payload)
    cli.multithreaded_run_sequence(address_api, post_payload)
    stop = time.time()
    time_flask = stop - start

    start = time.time()
    cli.run_sequence(address_api_server, post_payload)
    cli.multithreaded_run_sequence(address_api_server, post_payload)
    stop = time.time()
    time_cherrypy = stop - start

    print("flask: ", time_flask, "cherrypy:", time_cherrypy)
