from datetime import date
import os
from PIL.Image import Image
import time

import PIL
import os
import os.path
from PIL import Image

from flask import Flask, request,flash, redirect, sessions, url_for, jsonify, render_template,make_response
from werkzeug.utils import secure_filename
from flask import send_from_directory
from main import search_image,getImages_names, search_image_pertinance_down, search_image_pertinance_up

SAVED_FOLDER = './static/images/searched/'

app = Flask(__name__, static_url_path='/static')

app.config['UPLOAD_FOLDER'] = '/static/images/searched/'
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024
 
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])
 


@app.route('/')
def root():
    return app.send_static_file('index.html')
    #return render_template('index.html')


@app.route('/index', methods=['POST'])



def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS



@app.post('/upload-image')
#@app.route("/upload-image", methods=["GET", "POST"])
def upload_image():
    print(
    request.files['image']    
    )
    
    if request.method == 'POST':
        if 'image' not in request.files:
            return redirect(request.url)
        image = request.files['image']
        if image.filename == '':
            return redirect(request.url)
        if image and allowed_file(image.filename):
            filename = secure_filename(image.filename)
            # sessions["id"] = filename
            img = Image.open(image)
            img = img.resize((200,200))
            img.save(os.path.join(SAVED_FOLDER +filename)) 
            return redirect(request.url)



@app.route('/search/<path:image_src>') 
def search(image_src):
    try: 
        stats = search_image(image_src)
        return jsonify(stats[:16])  
    except IndexError as err: 
      print(f"Unexpected {err=}, {type(err)=}")
    

@app.route('/allImages') 
def getAll():
    try: 
        data = getImages_names()
        return jsonify(data)  
        
    except IndexError as err: 
      print(f"Unexpected {err=}, {type(err)=}")
    

@app.route('/search_pertinance_down/<path:image_src>') 
def search_pertinanc_down(image_src):
    try: 
        stats = search_image_pertinance_down(image_src)
        return jsonify(stats[:16])
    except IndexError as err: 
      print(f"Unexpected {err=}, {type(err)=}")

@app.route('/search_pertinance_up/<path:image_src>') 
def search_pertinance_up(image_src):
    try: 
        stats = search_image_pertinance_up(image_src)
        return jsonify(stats[:16])
    except IndexError as err: 
      print(f"Unexpected {err=}, {type(err)=}")

@app.route('/<filename>')
def display_image(filename):
    return redirect(url_for(filename), code=301)




# existance
@app.route('/images/<path:filename>')
def custom_static(filename):
    return send_from_directory('images', filename)



if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    # app.run(host='0.0.0.0', port=port)
    app.run( port=port)