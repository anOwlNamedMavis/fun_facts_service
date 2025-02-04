from flask import Flask
import random

app = Flask(__name__)

# Load fun facts from a file
def load_facts(filename="fun_facts.txt"):
    try:
        with open(filename, "r", encoding="utf-8") as file:
            facts = [line.strip() for line in file if line.strip()]
        return facts if facts else ["No facts available."]
    except FileNotFoundError:
        return ["Error: Facts file not found."]

fun_facts = load_facts()

@app.route('/')
def random_fact():
    return random.choice(fun_facts), 200, {'Content-Type': 'text/plain'}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
