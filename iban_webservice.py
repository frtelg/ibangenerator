from flask import Flask, jsonify
from iban import Iban

app = Flask(__name__)

@app.route('/getIban', methods=['GET'])
def getIban():
    newIban = Iban.generateIban()
    return jsonify(newIban.__dict__)

def runApp():
    app.run(host='localhost')

if __name__ == '__main__':
    runApp()