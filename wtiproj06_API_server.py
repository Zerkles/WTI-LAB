import cherrypy
import wtiproj04_ETL_and_data_processing
import wtiproj05_API
import wtiproj06_API
import wtiproj06_API_logic as api
import wtiproj06_simple_cassandra_client

cherrypy.tree.graft(wtiproj06_API.app.wsgi_app, '/')
cherrypy.config.update({'server.socket_host': '0.0.0.0',
                        'server.socket_port': 9898,
                        'engine.autoreload.on': False,
                        })

if __name__ == '__main__':
    wtiproj06_simple_cassandra_client.prepare_db()
    api.prepare_keys()
    cherrypy.engine.start()  # cherrypy app
