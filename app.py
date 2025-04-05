from flask import Flask
# create a Flask app
app = Flask(__name__)
# register a route to the application
@app.route('/')
def hello():
  return "Hello World! baby"

# check if we are running this app.py file as script, as python app.py
if __name__ == "__main__":
  app.run(host="0.0.0.0", debug=True) # debug=True will auto restart the server when there are changes in the code
# "0.0.0.0" means it will run in local