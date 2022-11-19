from flask import Flask, request, jsonify
from io import BytesIO
app = Flask(__name__)


@app.route('/graph', methods=['POST'])
def respond():
    try:
        file = request.files['file']
        file_bytes = file.read()
        file_content = BytesIO(file_bytes).readlines()
        print(file_content)

    except Exception as e:
        print(f"Couldn't upload file {e}")

    response = {}
    
    response["response"] = "You have succeeded. Go on."
    # Return the response in json format
    response = jsonify(response)
    
    # Add headers
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response


@app.route('/graph', methods=['GET'])
def otherRespond():

    response = {}
    
    response["response"] = "You have succeeded. Go on."
    # Return the response in json format
    response = jsonify(response)
    
    # Add headers
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response


@app.route('/')
def index():
    # A welcome message to test our server
    return "<h1>Welcome to our medium-greeting-api!</h1>"


if __name__ == '__main__':
    # Threaded option to enable multiple instances for multiple user access support
    app.run(threaded=True, port=5000)
