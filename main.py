
from flask import Flask
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

app = Flask(__name__)

@app.route('/')
def home():
    return 'Welcome to River!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
