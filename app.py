from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return (f' Cleriston Junior RA: 22201072 \n Joao Pedro RA:2201068 \n Mateus Pereira Jardim RA: 2201058 \n Guilherme Pereira RA:2201325')

if __name__ == "__main__":
    app.run(debug=True)



