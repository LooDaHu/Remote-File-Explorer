from flask import Flask
from flask import render_template, session, redirect, request, url_for
from flask_bootstrap import Bootstrap
import drive
import time
from config import Config

temp_path = ''
# temp_path = ''
app = Flask(__name__)
bootstrap = Bootstrap(app)
app.secret_key = 'P02r31j/3yX R~XHH!nmN]LWX/,?XT'


@app.route('/')
def index():
    return render_template('index.html')


# @app.route('/loading')
@app.route('/loading/<file_type>/<path>', methods=['GET', 'POST'])
def loading(path, file_type):
# def loading():
    global temp_path
    temp_path = path
    # print(temp_path)
    # print(file_type)
    return render_template('loading.html', file_type=file_type)


@app.route('/netdrive/<path>', methods=['GET', 'POST'])
def net_drive(path):
    content = drive.win_nt(path)
    seg_path = drive.div_path(path)
    # for i in seg_path:
    #     print(i)
    if content is not None:
        return render_template('netdrive.html', u=content, u1=seg_path)
    else:
        return render_template('error.html')


@app.route('/netdrive')
def net_drive_main():
    content = drive.win_nt('')
    return render_template('netdrive.html', u=content)


@app.route('/video', methods=['GET', 'POST'])
def video():
    global temp_path
    file_name = drive.get_filename(temp_path)
    drive.copy_file_to_cache(temp_path)
    temp_path = ''
    return render_template('video.html', file_name=file_name)


@app.route('/audio', methods=['GET', 'POST'])
def audio():
    global temp_path
    file_name = drive.get_filename(temp_path)
    drive.copy_file_to_cache(temp_path)
    temp_path = ''
    return render_template('audio.html', file_name=file_name)


@app.route('/image', methods=['GET', 'POST'])
def image():
    global temp_path
    file_name = drive.get_filename(temp_path)
    drive.copy_file_to_cache(temp_path)
    temp_path = ''
    return render_template('image.html', file_name=file_name)


@app.route('/text', methods=['GET', 'POST'])
def text():
    global temp_path
    file_name = drive.get_filename(temp_path)
    drive.copy_file_to_cache(temp_path)
    temp_path = ''
    return render_template('text.html', file_name=file_name)


@app.route('/login', methods=['POST', 'GET'])
def login():
    conf = Config()
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username == conf.get_username() and password == conf.get_password():
            session['username'] = request.form['username']
            return redirect(url_for('index'))
        else:
            redirect(url_for('login'))
    return render_template('login.html')


@app.route('/logout')
def logout():
    # delete all files in cache
    drive.delete_cache()
    # remove the username from the session if it's there
    session.pop('username', None)
    return render_template('logout.html')


@app.before_request
def before_login():
    if 'username' not in session and request.endpoint != 'login':
        return redirect(url_for('login'))
    
    
@app.route('/file', methods=['GET', 'POST'])
def file():
    global temp_path
    file_name = drive.get_filename(temp_path)
    drive.copy_file_to_cache(temp_path)
    temp_path = ''
    return render_template('file.html', file_name=file_name)


@app.route('/test')
def test():
    return render_template('test.html')


@app.route('/upload')
def upload():
    return render_template('upload.html')


@app.route('/get-upload', methods=['POST'])
def get_upload():
    uploaded_file = request.files.get('file')
    if not uploaded_file:
        return 'need file'
    uploaded_file.save('static/uploaded_file/%s' % uploaded_file.filename)
    return  render_template('get-upload.html')


if __name__ == '__main__':
    app.run()
