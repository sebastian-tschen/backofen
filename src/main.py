from flask import Flask, request

# creating the Flask application
app = Flask(__name__)


@app.route('/designs', methods=['POST'])
def add_design():
    """upload a design and get the corresponding id to later download the stl file"""
    data = request.get_data()

    print(data)

    // Wonderbolts EneMeneMiste1Kiste 10000

    return 121

@app.route('/designs')
def get_design():
    """upload a design and get the corresponding id to later download the stl file"""
    return "dfssdf"
