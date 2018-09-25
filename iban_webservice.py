from flask import Flask, json, request, jsonify, Response
from iban import Iban

app = Flask(__name__)

@app.route('/getIban', methods=['GET'])
def getIban():
    newIban = Iban.generateIban()
    return jsonify(newIban.__dict__)

def runApp():
    app.run(host='localhost', port=5000)

if __name__ == '__main__':
    runApp()