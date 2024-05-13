from flask import Flask , request
app = Flask(__name__)
@app.route('/', methods =['GET'])
def index ():
return {
"result": "Some result ...",
}
app.run(host="0.0.0.0", port =8080 , debug=True)
