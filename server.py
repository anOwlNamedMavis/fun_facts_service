from flask import Flask
import random

app = Flask(__name__)

fun_facts = [
    "Bananas are berries, but strawberries are not.",
    "Honey never spoils. Archaeologists have found pots of honey in ancient Egyptian tombs that are over 3000 years old and still edible.",
    "A day on Venus is longer than a year on Venus.",
    "Octopuses have three hearts.",
    "Sharks existed before trees."
]

@app.route('/')
def random_fact():
    return random.choice(fun_facts), 200, {'Content-Type': 'text/plain'}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
