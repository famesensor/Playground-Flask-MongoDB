from flask import Flask, render_template, request, send_from_directory
import os
import db as d

app = Flask(__name__)

APP_ROOT = os.path.dirname(os.path.abspath(__file__))

# def encode_img(img_fn):
#   with open(img_fn, "rb") as f:
#     encoded_string = base64.b64encode(f.read())
#     return encoded_string

@app.route('/')
def index():
    return render_template('upload.html')


@app.route('/upload', methods=['POST'])
def upload():
    target = os.path.join(APP_ROOT, 'images')  #folder path
    print("target : ",target)
    if not os.path.isdir(target):
        os.mkdir(target)     # create folder if not exits
    face_db_table = d.mongo.db.Image  # database table name
    print("R : ",request.files.getlist("face_image"))
    if request.method == 'POST':
        for upload in request.files.getlist("face_image"): #multiple image handel
            print("Upload : ",upload)
            filename = upload.filename
            print("filename : ",filename)
            destination = "/".join([target, filename])
            upload.save(destination)
            # str = encode_img(destination)
            # str = base64.b64encode(pic.read())
            # print(str)
            face_db_table.insert({'image': filename})   #insert into database mongo db
           
        # return 'Image Upload Successfully'
        return render_template('show.html', image_name=filename)

@app.route('/upload/<filename>')
def send_image(filename):
    return send_from_directory("images", filename)

if __name__ == '__main__' :
    app.run(host='localhost',port=8000,debug=True)