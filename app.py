from flask import Flask
from datetime import datetime
app = Flask(__name__)

@app.route('/')
def hello():    
    return 'Hello World!'

@app.route('/time')
def time():    
    return str(datetime.now())

if __name__ == '__main__':
    app.run(debug=False , host='0.0.0.0', port=os.environ.get("PORT", 5000), threaded=True)