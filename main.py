from flask import Flask, redirect

#redirecting from testmypython.pythonanywhere.com Flask demo application
#to desired link and counting such visits to the server log on PythonAnywhere
TARGET = 'https://openai.com/'

app = Flask(__name__)

counter = 0

@app.route("/")
def hello_world():
    global counter

    counter +=1
    print("counter = ", counter)
    return redirect(TARGET)