import os
from flask import Flask, render_template, request
from flask_uploads import UploadSet, configure_uploads, IMAGES
from flask import send_file

app = Flask(__name__)

photos = UploadSet('photos', IMAGES)

app.config['UPLOADED_PHOTOS_DEST'] = 'static'
configure_uploads(app, photos)

@app.route('/', methods=['GET', 'POST'])
def upload():
	if request.method == 'POST' and 'photo' in request.files:
		filename = photos.save(request.files['photo'])
		cwd = os.getcwd()
		os.system("python model.py --image "+filename)
		op_file=cwd+'/Output/Descrip.txt'
		Description=""
		with open(op_file,'r') as f:
			Description = f.read()
		return render_template('output.html',result=Description,file_name=filename)
	return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',threaded=True)