import os
from factory import create_app

app = create_app(os.getenv('FLASK_ENV', default='dev'))

if __name__ == '__main__':
    app.secret_key = '342'
    app.config['SESSION_TYPE'] = 'filesystem'

    app.run(threaded=True)