import cherrypy
import wtiproj04_ETL_and_data_processing
import wtiproj05_API
import wtiproj05_API_logic as api

cherrypy.tree.graft(wtiproj05_API.app.wsgi_app, '/')
cherrypy.config.update({'server.socket_host': '0.0.0.0',
                        'server.socket_port': 9898,
                        'engine.autoreload.on': False,
                        })

if __name__ == '__main__':
    # api.df = exercise_1(api.user_ratedmovies_data, api.movie_genres_data)[0] # uncomment for full data
    api.df = wtiproj04_ETL_and_data_processing.exercise_1(api.user_ratedmovies_data, api.movie_genres_data)[0][:0]
    cherrypy.engine.start()  # cherrypy app
