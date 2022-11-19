from flask import Flask, request, jsonify
from io import BytesIO

from flask_cors import cross_origin
from backend.parser import ast_parser
from backend.systrace import trace_call

app = Flask(__name__)

@app.route('/graph', methods=['POST'])
@cross_origin()
def respond():
    try:
        file = request.files['file']
        file_bytes = file.read()
        defs = ast_parser(file_bytes)
        trace_call(file_bytes)

    except Exception as e:
        print(f"Error found: {e}")

    response = {}
    response["defs"] = defs
    response = jsonify(response)
    return response

@app.route('/graph', methods=['GET'])
@cross_origin()
def otherRespond():

    response = {}
    
    response["response"] = "You have succeeded. Go on."
    # Return the response in json format
    response = jsonify(response)
    
    # Add headers
    # response.headers.add('Access-Control-Allow-Origin', '*')

    return response

@app.route('/')
def index():
    # A welcome message to test our server
    return "<h1>Welcome to our medium-greeting-api!</h1>"

if __name__ == '__main__':
    # Threaded option to enable multiple instances for multiple user access support
    app.run(threaded=True, port=8888)



# Add headers
    # response.headers.add('Access-Control-Allow-Origin', '*')
