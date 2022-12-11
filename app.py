from flask import Flask
from config import config

app = Flask(__name__)

@app.route("/")
def index():
    return "holaa"

def page_not_found(error):
    return "Not found page", 404

if __name__ == '__main__':
    app.config.from_object(config['development'])
    app.register_error_handler(404, page_not_found)
    app.run()
