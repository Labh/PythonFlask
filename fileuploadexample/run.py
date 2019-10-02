from flask import Flask, render_template, request, redirect, flash
from config import ALLOWED_EXTENSION, UPLOAD_FOLDER, SECRET_KEY
from werkzeug import secure_filename
import os

app=Flask(__name__)

app.config['SECRET_KEY']=SECRET_KEY
app.config['UPLOAD_FOLDER']=UPLOAD_FOLDER

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/", methods=["POST"])
def upload_file():
    if request.method=="POST":
        upfile=request.files['file']
        if upfile:
            fname=secure_filename(upfile.filename)
            in_f_name=os.path.join(app.config['UPLOAD_FOLDER'], fname)
            upfile.save(in_f_name)
            flash("File saved")
    return render_template("index.html")

if __name__=='__main__':
    app.run()
