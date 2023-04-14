# from flask import Flask, render_template

# app = Flask(__name__)


# @app.route('/')
# def index():
    # return render_template('pcl_view_json.html')


# if __name__ == '__main__':
    # app.run(debug=True)

from flask import Flask, render_template, send_from_directory
import os

app = Flask(__name__)

# Disable caching for static files
@app.after_request
def add_header(response):
    if 'Cache-Control' not in response.headers:
        response.headers['Cache-Control'] = 'no-cache, no-store, must-revalidate'
    return response

@app.route('/')
def index():
    return render_template('pcl_view_json.html')
    #return render_template('voxel_pcl_viewer.html')
    
@app.route('/voxel')
def voxel():
    #return render_template('pcl_view_json.html')
    return render_template('voxel_pcl_viewer.html')

@app.route('/static/<path:path>')
def send_static(path):
    return send_from_directory(os.path.join(app.root_path, 'static'), path, cache_timeout=0)

if __name__ == '__main__':
    app.run(debug=True)
