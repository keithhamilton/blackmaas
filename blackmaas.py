from flask import Flask, url_for, request,Response, send_file, redirect
import ipsum
import placeholder_graphic.generator as image_generator
import json
import os

app = Flask(__name__,static_url_path='/static')

@app.route('/')
def default():
    return redirect(url_for('ipsum'))

@app.route('/ipsum/<path:static_type>/<path:path>')
def serve_js(static_type,path):
    return app.send_static_file(os.path.join(static_type, path))

@app.route('/ipsum/create')
def ipsum():
    return app.send_static_file('generate.html')

@app.route('/ipsum/generate', methods=['GET'])
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
        return_data['text'] = ipsum.generator.generate(p,s_variance,include_enochian,enochian_weight)
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