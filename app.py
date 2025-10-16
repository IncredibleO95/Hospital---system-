from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Karibu kwenye mfumo wa hospitali!"

if __name__ == '__main__':
    app.run(debug=True)
