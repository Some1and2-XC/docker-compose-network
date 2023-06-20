# Import flask module
from flask import Flask
 
app = Flask(__name__)
 
@app.route('/')
def index():
    return 'Working Webserver!!'

@app.route("/post", methods = [ "GET", "POST" ])
def post():
    if request.method == "POST":
        ...

# main driver function
if __name__ == "__main__":
    app.run()