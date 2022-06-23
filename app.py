from email.mime import image

from tkinter import Image
from typing import Set
from flask import Flask,jsonify,Blueprint,jsonify,Response,request,send_file
import os
from os import getcwd
from pymongo import MongoClient
from bson.json_util import dumps
import datetime
from PIL import Image


app = Flask(__name__)
client = MongoClient(os.environ.get('DB')) 
db = client.blog

routes_files = Blueprint("routes_files",__name__)

path_file = getcwd() + "/files/"
ALLOWED_EXTENSIONS = set(['jpg', 'png', 'jpeg', 'gif'])

def response_json(mensaje: str,status: int = 200)-> Response:
    response = jsonify({
        "message": mensaje
    })

    response.status_code = status
    return response

@app.route('/')
def home():
    num = app.config['UPLOAD_FOLDER'] = './files'
    return jsonify(num)


@app.route("/upload/<string:imagen_nom>", methods=['POST'])
def upload_file(imagen_nom):
        file = request.files['file']
        # Guardamos el archivo en el directorio "Archivos PDF"
        
        if file and allowed_file(file.filename):
            file.save(path_file+imagen_nom+file.filename)
            return response_json("succes")
    
@app.route('/imagen/<string:imagen_nombre>')
def get_imagen(imagen_nombre):
    if request.args.get('type') == '1':
       filename = 'ok.gif'
    else:
       filename = 'files/'+imagen_nombre
    return send_file(filename, mimetype=filename+imagen_nombre)

def allowed_file(filename):
    return "." in filename and filename.rsplit(".",1)[1] in ALLOWED_EXTENSIONS


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)




