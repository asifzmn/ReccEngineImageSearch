from flask import Flask, jsonify, request
from flask_cors import CORS

from image_search_module import get_similar_images

app = Flask(__name__)
CORS(app)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


@app.route('/is')
def image_search():
    resp = jsonify({'image_url': 'https://picsum.photos/200/300'})
    # print(type(resp))
    resp.headers['Access-Control-Allow-Origin'] = '*'
    return resp


@app.route('/upload1', methods=['POST'])
def upload1():
    file = request.files['file']
    file.save('uploaded_image.png')
    return {'message': 'Image uploaded successfully!'}


@app.route('/upload', methods=['POST'])
def upload():
    # Check if a file was included in the request
    if 'file' not in request.files:
        return 'No file uploaded', 400

    # Get the file data from the request body
    file = request.files['file']

    # print(file)
    # Do something with the file, such as saving it to disk

    filename = 'newplot.png'
    file.save(filename)
    image_list = get_similar_images(filename)
    image_list = {i + 1: v for i, v in zip(range(len(image_list)), image_list.values())}

    # image_list = {1: 'Image/boots_1.jpg', 2: 'Image/boots_3.jpg', 3: 'Image/chelsea_4.jpg', 4: 'Image/chelsea_3.jpg', 5: 'Image/chelsea_2.png'}
    print(image_list)

    # Return a response
    resp = jsonify({'msg': 'File uploaded successfully', 'images': image_list})
    # print(type(resp))
    resp.headers['Access-Control-Allow-Origin'] = '*'
    # resp.headers['Access-Control-Allow-Methods'] = 'POST'
    # resp.headers['Access-Control-Allow-Headers'] = 'Content-Type'
    return resp

    # return jsonify({'success': True})
    # return 'File uploaded successfully', 200


if __name__ == '__main__':
    app.run(debug=True)
