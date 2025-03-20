from flask import Flask, render_template
import os 

app = Flask(__name__)

IMAGE_FOLDER = 'static/images'
app.config['IMAGE_FOLDER'] = IMAGE_FOLDER

@app.route('/')
def index():
    images = os.listdir(app.config['IMAGE_FOLDER'])
    images = [image for image in images if image.endswith(('jpg', 'jpeg', 'png', 'gif'))]
    return render_template('index.html', images=images)

if __name__ == "__main__":
    app.run(debug=True)
    