from flask import Flask, jsonify
from iban import Iban
from namesgenerator import Person

app = Flask(__name__)

@app.route('/', methods=['GET'])
def mainPage():
    return """<a href="/getIban">Get IBAN webservice</a><br>
    <a href="/randomDude">Get random person webservice</a>
    """

@app.route('/getIban', methods=['GET'])
def get_iban():
    new_iban = Iban.generate_iban()
    return jsonify(new_iban.__dict__)

@app.route('/randomDude', methods=['GET'])
def get_dude():
    new_dude = Person.random_dude()
    return jsonify(new_dude.__dict__)

def run_app():
    app.run(host='localhost')

if __name__ == '__main__':
    run_app()