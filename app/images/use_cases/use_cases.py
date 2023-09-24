import calendar
import time
import json
from ..repository.repository import Save,Find
from flask import request,jsonify,current_app,send_file
from werkzeug.utils import secure_filename
import os


ALLOWED_EXTENSIONS={'webp','gif','png','jpg','jpeg','svg'}


def allowed_file(filename:str)->bool:
    return '.' in filename and filename.rsplit('.',1)[1].lower() in ALLOWED_EXTENSIONS

def save_file():
    try:
        if 'file' not in request.files:
            return jsonify({"error":"An error occurred proccessing the file!"})
        file=request.files['file']
        if len(file.filename) ==0:
            return jsonify({"error":"An error occurred proccessing the file!"})

        if file and allowed_file(file.filename):
            time_stamp=calendar.timegm(time.gmtime())
            file.filename=f'{time_stamp}-{file.filename}'
            filename=secure_filename(file.filename)
            
            path=os.path.join(current_app.config['UPLOAD_FOLDER'],filename)
            url=f'{current_app.config["API"]}/images/{filename}'
            file.save(path)
            save_image_db(url,time_stamp,filename,0)
            return jsonify({"ok":"file uploaded successfully","id_file":filename})
        return jsonify({"error":"Invalid file type!"})
    except:
        return jsonify({"error":"Internal server error!"})
    

def get_image_by_name(filename:str):
    try:
        if len(filename)>0:
            return send_file(os.path.join(current_app.config['UPLOAD_FOLDER'],filename))
        else:
            return jsonify({"error":"EO File not found on DB!"})
    except:
        return jsonify({"error":"Internal server error!"})

def find_image(filename:str):
    try:
       findImage=Find(filename=filename)
       findImage_obj=json.loads(findImage)
       return findImage_obj 
    except:
        return jsonify({"error":"Internal server error!"})

def save_image_db(path:str,createdAt:int,filename:str,size:int):
    try:
        fileInfo={
        "path":path,
        "createdAt":createdAt,
        "filename":filename,
        "size":size
        }
        return Save(fileInfo)
    except:
        return jsonify({"error":"DB server error or internal!"})
    

