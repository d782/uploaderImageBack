from flask import Flask
from flask_mongoengine import MongoEngine
from images.routes import images_routes
from flask_cors import CORS

def Application():
    app=Flask(__name__,instance_relative_config=True)

    CORS(app,resources={r"/*":{"origins":"*"}})

    app.config.from_object('config.Config')

    db=MongoEngine(app)

    app.register_blueprint(images_routes,url_prefix='/images')
    
    
    return app



if __name__ == '__main__':
    Application().run()