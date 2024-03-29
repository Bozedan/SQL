from flask import Flask, make_response, jsonify
from flask_cors import CORS

def create_app():
    '''SWAGGER_URL = '/swagger'
    API_URL = '/static/swagger.json'
    SWAGGER_UI_BLUEPRINT = get_swaggerui_blueprint(
        SWAGGER_URL,
        API_URL,
        config={
            'app_name': "Cloud service"
        }
    )'''

    app = Flask(__name__)
    CORS(app, supports_credentials=True)
    #app.config['TESTING'] = testing
    #app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
    with app.app_context():
        #db = get_db_connection()
        #app.db = db

        from rest.routes import user

        app.register_blueprint(user.get_blueprint())
        #app.register_blueprint(admin.get_blueprint())
        #app.register_blueprint(SWAGGER_UI_BLUEPRINT, url_prefix=SWAGGER_URL)
        #db.create_all()
        #db.session.commit()

    '''@app.errorhandler(400)
    def handle_400_error(_error):
        """Return a http 400 error to client""" # pragma: no cover
        return make_response(jsonify({'error': 'Misunderstood'}), 400) # pragma: no cover

    @app.errorhandler(401)
    def handle_401_error(_error):
        """Return a http 401 error to client""" # pragma: no cover
        return make_response(jsonify({'error': 'Unauthorised'}), 401) # pragma: no cover

    @app.errorhandler(403)
    def handle_403_error(_error):
        """Return a http 403 error to client""" # pragma: no cover
        return make_response(jsonify({'error': 'Forbidden'}), 403) # pragma: no cover

    @app.errorhandler(404)
    def handle_404_error(_error):
        """Return a http 404 error to client""" # pragma: no cover
        return make_response(jsonify({'error': 'Not found'}), 404) # pragma: no cover

    @app.errorhandler(500)
    def handle_500_error(_error):
        """Return a http 500 error to client""" # pragma: no cover
        return make_response(jsonify({'error': 'Server error'}), 500) # pragma: no cover
'''
    return app

if __name__ == '__main__':
    app = create_app() 
    app.run()
