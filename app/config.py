class Config(object):
    DEBUG=True
    DEVELOPMENT=True
    MONGODB_SETTINGS={
        "host":"mongodb+srv://user:password@cluster0.n9ajk.mongodb.net/images?retryWrites=true&w=majority"
    }
    UPLOAD_FOLDER='./uploads'
    API='http://localhost:5000'