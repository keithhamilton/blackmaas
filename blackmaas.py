from flask import Flask, url_for, request,Response, send_file, redirect, current_app, make_response
import ipsum.generator as ipsum_generator
import placeholder_graphic.generator as image_generator
import json
import os
from datetime import timedelta
from functools import update_wrapper

app = Flask(__name__,static_url_path='/static')

def crossdomain(origin=None, methods=None, headers=None, max_age=21600, attach_to_all=True, automatic_options=True):  
    if methods is not None:
        methods = ', '.join(sorted(x.upper() for x in methods))
    if headers is not None and not isinstance(headers, basestring):
        headers = ', '.join(x.upper() for x in headers)
    if not isinstance(origin, basestring):
        origin = ', '.join(origin)
    if isinstance(max_age, timedelta):
        max_age = max_age.total_seconds()

    def get_methods():
        if methods is not None:
            return methods

        options_resp = current_app.make_default_options_response()
        return options_resp.headers['allow']

    def decorator(f):
        def wrapped_function(*args, **kwargs):
            if automatic_options and request.method == 'OPTIONS':
                resp = current_app.make_default_options_response()
            else:
                resp = make_response(f(*args, **kwargs))
            if not attach_to_all and request.method != 'OPTIONS':
                return resp

            h = resp.headers

            h['Access-Control-Allow-Origin'] = origin
            h['Access-Control-Allow-Methods'] = get_methods()
            h['Access-Control-Max-Age'] = str(max_age)
            if headers is not None:
                h['Access-Control-Allow-Headers'] = headers
            return resp

        f.provide_automatic_options = False
        return update_wrapper(wrapped_function, f)
    return decorator

@app.route('/')
def default():
    return redirect(url_for('ipsum'))
    
@app.route('/about')
def about():
    return app.send_static_file('about.html')

@app.route('/image')
def images():
    return app.send_static_file('images.html')
    
@app.route('/<path:static_type>/<path:path>')
def serve_js(static_type,path):
    return app.send_static_file(os.path.join(static_type, path))

@app.route('/ipsum')
def ipsum():
    return app.send_static_file('generate.html')

@app.route('/ipsum/generate', methods=['GET','OPTIONS'])
@crossdomain(origin='*',headers='*')
def generate_ipsum():
    # defaults
    p=4
    s_variance=0
    include_enochian=False
    enochian_weight=1
    return_data = { 'text': '', 'success': 'false', 'status':500 }

    if 'p' in request.args:
        p=int(request.args['p'])
    if 'sentence_variance' in request.args:
        s_variance = int(request.args['sentence_variance'])
    if 'include_enochian' in request.args:
        if request.args['include_enochian'] in ['true','True']:
            include_enochian = True
    if 'enochian_weight' in request.args:
        enochian_weight = int(request.args['enochian_weight'])

    try:
        return_data['text'] = ipsum_generator.generate(p,s_variance,include_enochian,enochian_weight)
        return_data['success'] = 'true'
        return_data['status'] = 200
    except Exception as e:
        print e

    resp = Response(json.dumps(return_data),status=return_data['status'],mimetype='application/json')
    return resp

@app.route('/image/create')
def image():
    pass

@app.route('/image/generate')
def generate_image():
    # defaults
    width=500
    height=350

    if 'width' in request.args:
        width=int(request.args['width'])
    if 'height' in request.args:
        height=int(request.args['height'])

    try:
        image = image_generator.generate(width,height)
        print image
        return send_file(image, mimetype='image/png')
    except Exception as e:
        print e
        return "{'success':'error'}"    

if __name__ == '__main__':
    app.debug = False
    if app.debug:
        app.run()
    else:
        app.run(host='0.0.0.0',port=80)
