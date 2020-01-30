from flask import Flask, request

# creating the Flask application
app = Flask(__name__)

@app.route('/designs', methods=['POST'])
def add_design():
    """upload a design and get the corresponding id to later download the stl file"""
    request.get_json()
