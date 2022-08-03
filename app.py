from flask import (
     Flask,
     request,
     render_template)
from bat_create import *

MACOS_FOLDER= "/static/files/mac"
WINDOWS_FOLDER= "/static/files/windows"

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['GET', 'POST'])
def submit():
    if request.method == 'POST':
        select_os = request.form['select_os']
        file_name = request.form['file_name']
        input_data = request.form['extensions']
        path = return_path(select_os, file_name)
        exts, exts_n = get_extensions(input_data)
        body = create_body(select_os,exts, exts_n)
        create_file(path,body)
        return render_template('result.html',path=path,file_name=file_name,exts=exts)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port='80')
