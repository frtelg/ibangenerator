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
def getIban():
    newIban = Iban.generateIban()
    return jsonify(newIban.__dict__)

@app.route('/randomDude', methods=['GET'])
def getDude():
    newDude = Person.randomDude()
    return jsonify(newDude.__dict__)

def runApp():
    app.run(host='localhost')

if __name__ == '__main__':
    runApp()