# BY Alon Galperin

import sys
from flask import Flask,request

# todo: add data field to responses

app = Flask(__name__)

# Add dictionary data structure to app for storing messages in RAM memory
app.config["messages"] = {}

# from routes import users_routes
# from routes import messages_routes

@app.route("/")
def hello():
    return "Hello World"

if __name__ == '__main__':
    if (len(sys.argv) > 1 and str(sys.argv[1])) == "debug":
        app.run(debug=True)
    app.run()