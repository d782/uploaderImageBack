from flask import Blueprint
from .use_cases.use_cases import save_file,get_image_by_name,find_image
images_routes=Blueprint('upload',__name__)

@images_routes.route("/upload",methods=["POST"])
def upload_images():
    return save_file()

@images_routes.route("/<filename>",methods=["GET"])
def get_image(filename):
    return get_image_by_name(filename)

@images_routes.route("/getImage/<filename>",methods=["GET"])
def get_image_by_id(filename):
    return find_image(filename)
