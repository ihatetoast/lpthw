#FLASK_APP=flask_play.py python -m flask run
from flask import Flask

app = Flask(__name__)

@app.route("/")
def add_ten(number):
	return number + 10

divider = '~' * 50

print "def add_ten(number)"

num = int(raw_input("Give me a number: "))

print "Your number is " + str(num)
print "your number plus 10 is: "
print add_ten(num)