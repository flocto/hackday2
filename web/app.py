from flask import Flask, send_file, request, jsonify, Response
from base64 import b64decode, b64encode
import time

app = Flask(__name__)

@app.route('/')
def index():
    return "Visit a subdomain to attempt a challenge."

@app.route('/inspection', methods=['GET'])
def inspection():
    return send_file('inspect.html')

@app.route('/cookie', methods=['GET'])
def cookie():
    try:
        is_admin = request.cookies.get('admin')
        is_admin = b64decode(is_admin).decode()

        if is_admin == 'true':
            return "social{yum_yum_cookies}"
    except:
        pass

    cookie = b64encode(cookie.encode('utf-8')).decode('utf-8')
    response = Response('You are not an admin', 401)
    response.set_cookie('admin', cookie)
    return response

@app.route('/feedback', methods=['GET'])
def feedback():
    return send_file('feedback.html')

notes = {
    0: 'social{very_insecure_direct_object_references}',
}
id = 1
@app.route('/feedback', methods=['POST'])
def feedback_post():
    note = request.json['note']
    global id
    notes[id] = note
    
    ret = id
    id += 1
    if id > 200:
        id = 1
    time.sleep(0.3) # lol
    return {'id': ret + 100000}

@app.route('/feedback/<id>', methods=['GET'])
def feedback_get(id):
    if not id.isdigit():
        return 'invalid id', 400
    if len(id) != 6:
        return 'invalid id', 400
    
    id = int(id) - 100000
    return notes[id]


if __name__ == '__main__':
    app.run(host='localhost', port=5000)

