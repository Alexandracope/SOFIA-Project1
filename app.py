from flask import Flask

if __name__ == '__main__':
     app.run(debug=True, host='0.0.0.0')

@app.route('/')
@app.route('/home')
def home():
    return "Hello Internet!"